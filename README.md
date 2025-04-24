![Banner](./GitHub%20Assets/GitHub%20Banner.png)

# __Project Resonator | *The* Open-Source IEM.__  
> A love letter to the IEM/CIEM hobby.

## 🔧 Technologies Used & Software Required

1. **VituixCAD**             — Tuning simulation (see install guide below)  
2. **KiCad**                 — Schematic and PCB design  
3. **Autodesk Fusion**       — Designing the IEM shell  
4. **FPGraphTracer**         — Tracking frequency and impedance responses from driver spec sheets  

## 📅 Development Timeline

- [x] Tools & Software                        | Wiki Entry  
- [x] Driver Selection                        | Wiki Entry  
- [+] Crossover Design                        | Wiki Entry  
- [ ] Setup Access To `.f3d` IEM Shell Models | File Acquisition & User Support  
- [ ] Create Crossover Diagrams For RSNTR IEM | Product Development  

...  
_More to come._

## 🎧 Philosophy & Reasoning

> I fell in love with IEMs, so I decided "why not, I'm bored."

## ❓ *Can I Use These Files To Build My Own IEM?*

Absolutely. I’ve set the license to be lenient for anyone who wants to use this as a base for their own commercial projects—while still keeping that open-source spirit that I’ve grown to love in the comp sci world.

I hope this gives you a head start—maybe even helps you dodge some of the mistakes I made.

*Reminder: I’m still human, and this design is far from perfect—but it should give you a solid look at what an IEM build process can look like.*

## 🛠️ Installation Guide

### VituixCAD (Archived Version) + Fixing Missing File Paths

1. Go to [Internet Archive's Wayback Machine](https://archive.org/)  
2. Paste: `https://kimmosaunisto.net/`  
3. Find and download any version before **2018-04-25**  
4. Install it and open the `.vxp` simulation file included in this project  

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
