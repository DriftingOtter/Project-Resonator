![Banner](./GitHub%20Assets/GitHub%20Banner.png)

# __Project Resonator | *The* Open-Source IEM.__  
> A love letter to the IEM/CIEM hobby.

## 🔧 Technologies Used & Software Required

1. **VituixCAD**             — Tuning simulation (see install guide below)  
2. **KiCad**                 — Schematic and PCB design  
3. **Autodesk Fusion**       — Designing the IEM shell  
4. **FPGraphTracer**         — Tracking frequency and impedance responses from driver spec sheets  

[Youtube Playlist For Addional IEM Building Resources](https://youtube.com/playlist?list=PL4ahDGGN5zBFhmGqVUoBdOnjuF_9HXV5L&si=1wQDmEUnnXoC1L7I)

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
    %% Input + L-pad
    A["AC Source
    1V, 1Ω"] --> Rseries["22Ω"]
    Rseries --> Rshunt["6.8Ω"]
    Rshunt --> GND1["Ground"]

    %% CI 22955 Branch 
    Rseries --> R3["910Ω"]
    R3 --> R4["910Ω"]
    R3 --> C3["10µF"]
    C3 --> GND3["Ground"]
    R4 --> D1["CI 22955 
    (Sub-Bass)"]

    %% BK 26824 Branch
    Rseries --> C1["470nF"]
    C1 --> Rbk_shunt["6.8Ω"]
    Rbk_shunt --> GND2["Ground"]
    C1 --> C2["10µF"]
    C2 --> D2["BK 26824
    (Mid) 
    (Inversed Polarity)"]

    %% SWFK 31736 Pair 
    Rseries --> C4["10µF"]
    C4 --> D3["SWFK 31736 
    (Mid-High)"]
    Rseries --> C5["4.7µF"]
    C5 --> D4["SWFK 31736 
    (High-Air) 
    (Inversed Polarity)"]

    classDef driver fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    classDef resistor fill:#ffffff,stroke:#000000,stroke-width:1.5px,color:#000000
    classDef capacitor fill:#ffffff,stroke:#000000,stroke-width:1.5px,color:#000000
    classDef input fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    classDef junction fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    classDef ground fill:#ffffff,stroke:#000000,stroke-width:1.5px,color:#000000

    class A input
    class D1,D2,D3,D4 driver
    class Rseries,Rshunt,Rbk_shunt,R3,R4 resistor
    class C1,C2,C3,C4,C5 capacitor
    class GND1,GND2,GND3 ground
    class J1 junction
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

