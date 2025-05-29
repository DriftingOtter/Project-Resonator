import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import serial
import serial.tools.list_ports
import threading
import queue
import time

# --- Configuration Constants ---
DEFAULT_BAUD_RATE = 115200
CMD_READ_TIMEOUT = 1.0  # Seconds to wait for a response line
CONNECT_TIMEOUT = 2.0   # Seconds to wait for port to open

class ATCommandGUI:
    def __init__(self, root_window):
        self.root = root_window
        self.root.title("FSC-BT6038 AT Command Programmer")
        self.root.geometry("700x650")

        self.serial_connection = None
        self.serial_thread = None
        self.running = False
        self.command_queue = queue.Queue()
        self.response_queue = queue.Queue()

        style = ttk.Style()
        style.configure("TButton", padding=5, font=('Helvetica', 10))
        style.configure("TLabel", padding=5, font=('Helvetica', 10))
        style.configure("TEntry", padding=5, font=('Helvetica', 10))

        connection_frame = ttk.LabelFrame(self.root, text="Connection", padding=10)
        connection_frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(connection_frame, text="Serial Port:").grid(row=0, column=0, sticky="w")
        self.port_var = tk.StringVar()
        self.port_combobox = ttk.Combobox(connection_frame, textvariable=self.port_var, width=20)
        self.port_combobox.grid(row=0, column=1, padx=5, sticky="ew")
        self.populate_serial_ports()

        ttk.Label(connection_frame, text="Baud Rate:").grid(row=0, column=2, sticky="w", padx=(10,0))
        self.baud_var = tk.StringVar(value=str(DEFAULT_BAUD_RATE))
        self.baud_entry = ttk.Entry(connection_frame, textvariable=self.baud_var, width=10)
        self.baud_entry.grid(row=0, column=3, padx=5, sticky="w")

        self.connect_button = ttk.Button(connection_frame, text="Connect", command=self.toggle_connection)
        self.connect_button.grid(row=0, column=4, padx=5)
        self.refresh_ports_button = ttk.Button(connection_frame, text="Refresh Ports", command=self.populate_serial_ports)
        self.refresh_ports_button.grid(row=0, column=5, padx=5)

        self.connection_status_var = tk.StringVar(value="Status: Disconnected")
        self.connection_status_label = ttk.Label(connection_frame, textvariable=self.connection_status_var, foreground="red")
        self.connection_status_label.grid(row=1, column=0, columnspan=6, sticky="w", pady=(5,0))

        connection_frame.columnconfigure(1, weight=1)

        commands_frame = ttk.LabelFrame(self.root, text="Quick Commands", padding=10)
        commands_frame.pack(padx=10, pady=5, fill="x")
        buttons = [
            ("Restore Factory",            self.confirm_restore_factory),
            ("Get Version",        lambda: self.queue_at_command("AT+VER")),
            ("Reboot",             lambda: self.queue_at_command("AT+REBOOT", delay_after=2.0)),
            ("Set Pairable",       lambda: self.queue_at_command("AT+PAIR=1")),
            ("Set Auto-Connect",   lambda: self.queue_at_command("AT+AUTOCONN=1")),
            ("Set Name (MyIEM)",   lambda: self.set_bt_name("MyIEM")),
            ("Set COD (Headset)",  lambda: self.queue_at_command("AT+COD=0x240404")),
            ("Set Profile (Sink)", lambda: self.queue_at_command("AT+PROFILE=A2DP-SINK")),
        ]

        for idx, (text, cmd) in enumerate(buttons):
            row, col = divmod(idx, 4)
            ttk.Button(commands_frame, text=text, command=cmd).grid(row=row, column=col, padx=2, pady=2, sticky="ew")
            commands_frame.columnconfigure(col, weight=1)

        i2s_frame = ttk.LabelFrame(self.root, text="I2S Configuration (AT+I2SCFG)", padding=10)
        i2s_frame.pack(padx=10, pady=5, fill="x")
        self.i2s_params = {}
        labels = ["Mode(0:S/1:M)", "Format", "BCLK_Div", "LRCLK_Div", "MCLK_Out(0:D/1:E)", "MCLK_kHz"]
        defaults = ["1","0","4","64","1","12288"]

        for i, lbl in enumerate(labels):
            ttk.Label(i2s_frame, text=lbl+":").grid(row=0, column=i*2, sticky="w", padx=2)
            var = tk.StringVar(value=defaults[i])
            self.i2s_params[lbl] = var
            entry = ttk.Entry(i2s_frame, textvariable=var, width=7)
            entry.grid(row=0, column=i*2+1, padx=2, sticky="ew")
            i2s_frame.columnconfigure(i*2+1, weight=1)

        ttk.Button(i2s_frame, text="Send I2S Config", command=self.send_i2s_config).grid(row=1, column=0, columnspan=len(labels)*2, pady=5, sticky="ew")

        manual_frame = ttk.LabelFrame(self.root, text="Manual AT Command", padding=10)
        manual_frame.pack(padx=10, pady=5, fill="x")
        self.manual_cmd_var = tk.StringVar()
        entry = ttk.Entry(manual_frame, textvariable=self.manual_cmd_var, width=60)
        entry.pack(side="left", fill="x", expand=True, padx=(0,5))
        entry.bind("<Return>", lambda e: self.send_manual_command())
        ttk.Button(manual_frame, text="Send", command=self.send_manual_command).pack(side="left")

        term_frame = ttk.LabelFrame(self.root, text="Output Terminal", padding=10)
        term_frame.pack(padx=10, pady=10, fill="both", expand=True)
        self.terminal_output = scrolledtext.ScrolledText(term_frame, wrap=tk.WORD, font=("Courier New",9))

        self.terminal_output.pack(fill="both", expand=True)
        self.terminal_output.configure(state='disabled')

        self.root.after(100, self.process_response_queue)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.disconnect_serial()
        self.root.destroy()

    def populate_serial_ports(self):
        try:
            ports = [p.device for p in serial.tools.list_ports.comports()]
        except Exception:
            ports = []
        self.port_combobox['values'] = ports
        self.port_var.set(ports[0] if ports else "")

    def toggle_connection(self):
        if self.serial_connection:
            self.disconnect_serial()
        else:
            try:
                port = self.port_var.get()
                baud = int(self.baud_var.get())
                self.serial_connection = serial.Serial(port, baud, timeout=CONNECT_TIMEOUT)
                self.serial_connection.reset_input_buffer()
                self.serial_connection.reset_output_buffer()
                self.running = True
                self.serial_thread = threading.Thread(target=self.read_serial_thread, daemon=True)
                self.serial_thread.start()
                self.connection_status_var.set(f"Status: Connected to {port}")
                self.connection_status_label.configure(foreground="green")
                self.connect_button.config(text="Disconnect")
            except Exception as e:
                messagebox.showerror("Connection Error", str(e))
                self.serial_connection = None

    def disconnect_serial(self):
        self.running = False
        if self.serial_connection:
            try:
                self.serial_connection.close()
            except:
                pass
        self.serial_connection = None
        self.connect_button.config(text="Connect")
        self.connection_status_var.set("Status: Disconnected")
        self.connection_status_label.configure(foreground="red")

    def read_serial_thread(self):
        while self.running and self.serial_connection:
            try:
                if self.serial_connection.in_waiting:
                    line = self.serial_connection.readline().decode(errors='replace').strip()
                    self.response_queue.put(line)
            except Exception as e:
                self.response_queue.put(f"[Error reading serial]: {e}")
                break

    def process_response_queue(self):
        while not self.response_queue.empty():
            line = self.response_queue.get()
            self.terminal_output.configure(state='normal')
            self.terminal_output.insert(tk.END, line + "\n")
            self.terminal_output.configure(state='disabled')
            self.terminal_output.see(tk.END)
        self.root.after(100, self.process_response_queue)

    def send_manual_command(self):
        cmd = self.manual_cmd_var.get().strip()
        if cmd:
            self.queue_at_command(cmd)

    def queue_at_command(self, command, delay_after=0.5):
        if not self.serial_connection:
            messagebox.showwarning("Not Connected", "Please connect to a serial port first.")
            return
        def send():
            try:
                self.serial_connection.write((command + "\r\n").encode())
                time.sleep(delay_after)
            except Exception as e:
                self.response_queue.put(f"[Error sending command]: {e}")
        threading.Thread(target=send, daemon=True).start()

    def confirm_restore_factory(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to restore factory settings?"):
            self.queue_at_command("AT+RESTORE", delay_after=5.0)

    def set_bt_name(self, name):
        self.queue_at_command(f"AT+NAME={name}")

    def send_i2s_config(self):
        parts = [self.i2s_params[k].get() for k in self.i2s_params]
        if all(parts):
            cmd = f"AT+I2SCFG={','.join(parts)}"
            self.queue_at_command(cmd)

if __name__ == "__main__":
    root = tk.Tk()
    app = ATCommandGUI(root)
    root.mainloop()

