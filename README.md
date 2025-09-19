![Banner](./GitHub%20Assets/GitHub%20Banner.png)

# __Project Resonator | *The* Open-Source IEM.__  
> A love letter to the IEM/CIEM hobby.

## 🔧 Technologies Used & Software Required

1. **VituixCAD**             — Tuning simulation (see install guide below)  
2. **KiCad**                 — Schematic and PCB design  
3. **Autodesk Fusion**       — Designing the IEM shell  
4. **FPGraphTracer**         — Tracking frequency and impedance responses from driver spec sheets  

## 📅 Development Timeline

- [x] Moved crossover simulation to the latest VituixCAD (old version archived under `/legacy`) | Crossover  
- [x] Updated driver setup to CI22955 + BK23824 + 2× SWFK 31736 | Drivers  
- [x] Removed PCB requirement in favor of direct SMD soldering (PCB file kept for reference) | Assembly  
- [x] Removed outdated SMD components list (will add new sourcing guide soon) | Documentation  
- [+] First physical prototype in progress thanks to preliminary funding | Prototyping

- [x] Modified PCB Shape To Wrap Entire Shell | PCB Design
- [x] Re-arranged Drivers To Fit Better       | Drivers
- [X] Created New IEM Colorways               | Design & Prototyping

- [+] [Modular, Node-based Tuning Software](https://github.com/DriftingOtter/EarCanvas)     | Software

- [x] Tools & Software                        | Wiki Entry  
- [x] Driver Selection                        | Wiki Entry  
- [+] Crossover Design                        | Wiki Entry  

...  
_More to come._

## 🎧 Philosophy & Reasoning

> I fell in love with IEMs, so I decided "why not, I'm bored."

## ❓ *Can I Use These Files To Build My Own IEM?*

Absolutely. I’ve set the license to be lenient for anyone who wants to use this as a base for their own commercial projects—while still keeping that open-source spirit that I’ve grown to love in the comp sci world.

I hope this gives you a head start—maybe even helps you dodge some of the mistakes I made.

*Reminder: I’m still human, and this design is far from perfect—but it should give you a solid look at what an IEM build process can look like.*

## Project Resonator 4 Way Passive Crossover Diagram [For 4BA Driver Configuration]

```mermaid
graph TD
    A["Input Signal<br/>100mV @ 0s"] --> B["10Ω"]
    
    B --> C["Junction Point"]
    
    %% High Frequency Path (Top Branch)
    C --> D["1kΩ"]
    D --> E["2kΩ"]
    D --> F["2.2µF"]
    F --> GND1["Ground"]
    E --> G["D1 CL22955<br/>Sub-Woofer Driver"]
    
    %% Mid-High Frequency Path (Second Branch)
    C --> H["470nF"]
    H --> I["3.3Ω"]
    H --> J["10µF"]
    J --> K["D2 BK 26824<br/>Bass-Mid Driver"]
    J --> GND2["Ground"]
    I --> GND3["Ground"]
    
    %% Mid-Low Frequency Path (Third Branch)
    C --> L["10Ω"]
    L --> M["4.7µF"]
    M --> N["D3 SWFK 31736<br/>Mid-High Driver"]
    
    %% Low Frequency Path (Fourth Branch)
    C --> O["3.3Ω"]
    O --> P["D4 SWFK 31736<br/>High-Air Driver"]

    
    classDef driver fill:#ffffff,stroke:#000000,stroke-width:3px,color:#000000
    classDef resistor fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    classDef capacitor fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    classDef input fill:#ffffff,stroke:#000000,stroke-width:3px,color:#000000
    classDef ground fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    classDef junction fill:#ffffff,stroke:#000000,stroke-width:3px,color:#000000
    
    class G,K,N,P driver
    class B,D,E,I,L,O resistor
    class F,H,J,M capacitor
    class A input
    class GND1,GND2,GND3,GND4,GND5,GND6,GND7 ground
    class C junction
```

## 🛠️ Installation Guide

### VituixCAD + Fixing Missing File Paths

1. Go to `https://kimmosaunisto.net/`
2. Find and download latest version
3. Install it and open the `.vxp` simulation file included in this project  

You’ll probably get a bunch of “missing file path” errors—don’t worry. That just means the project is still pointing to paths from my own system.

To fix:
- Click the folder icon next to the `.frd` or `.zma` file slot
- Navigate to the correct folder for each BA driver (inside the `BA Driver Spec Sheets` folder in this repo)
- Re-link the appropriate files

*(You only need to do this once.)*

### Downloading Fusion 360 IEM Shell Files

All IEM shell files are now hosted on **MEGA**. This includes both `.stl` files for direct printing and `.f3d` Fusion files for editing.

Since GitHub has upload limits, I’ve stored them externally here:

🔗 [Mega Link For IEM Shell Files](https://mega.nz/folder/2Z4WzYDR#g-NULd1YQFsHa81YXLZzIw)

Inside, you'll find:

- `Ready-To-Prints`     | Shell prototypes you can print right away  
- `Fusion-Shell-Models` | Editable Fusion files to tweak however you’d like

---

## 👨‍💻 Author

- **Daksh Kaul** (aka. *DriftingOtter*)

## 🙌 Credits & Citations

- Head-Fi DIY IEM forums & community  
- [Kozh](https://www.youtube.com/@kozh4013/videos)  
- [Kirby Meets Audio](https://youtu.be/QClvPIuW3zI?si=NcwjdGAZriBUcmHE)  
- [Crinacle](https://www.youtube.com/watch?v=tCqV3ZRcZ9g&t=1227s)  
- [Mr.T’s Design Graveyard](https://youtu.be/3FGNw28xBr0?si=LEpJtPCjVtikS_FK)  
- *And many more...*  

*If I forgot to credit you, shoot me a message—I’ll make sure you’re added.*

