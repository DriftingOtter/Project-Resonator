# __Project Resonator | *The* Open-Source IEM.__

> A love letter to the IEM/CIEM hobby.

## Technologies Used & Software required

1. VituixCAD        (For tuning simulation)
2. KiCad            (For Schematic and PCB deisgn)
3. AutoDesk Fusion  (For designing the IEM shell)
5. OpenCTM          (For .stl 3D file compression)
6. FPGraphTracer    (For tracking frequnecy responses and impedence responses from spec sheets of BA drivers)

## Philosophy & Reasoning

> I fell in love with IEMS, so I decied "why not, I'm bored".

## *Can I Use These Files To Build My Own IEM ?*

For sure! I have set the liscense to be lenient with future project that would like to use my project as a basis for their own commerical products, whilst trying to maintain a 'semi' Open-source ideology I have loved and grown accustomed too in my own comp sci sphere.

I hope you all can use this as a springboard to learn more about IEMs yourself and maybe even skip some of the mistakes I made along the way and quickly get started on making your own!

*Remember I am still human so my design is not perfect, (far from it) but I hope it gives some what of an example of what a IEM build process kind of looks like).*

## How to compress Autodesk Fusion 360 IEM Shell Files

```Bash
for file in *.ctm; do
    ctmconv "$file" "${file%.ctm}.stl"
done
```

```Powershell
Get-ChildItem -Filter "*.ctm" | ForEach-Object {
    $output = $_.FullName -replace "\.ctm$", ".stl"
    & ctmconv $_.FullName $output
}
```

## Authors

- Daksh Kaul (aka. DriftingOtter)
- Head-Fi's DIY IEM forms and community
- [Kozh](https://www.youtube.com/@kozh4013/videos)
- [Kirby Meets Audio](https://youtu.be/QClvPIuW3zI?si=NcwjdGAZriBUcmHE)
- [Crinacle](https://www.youtube.com/watch?v=tCqV3ZRcZ9g&t=1227s)
- [Mr.T's Design Graveyard](https://youtu.be/3FGNw28xBr0?si=LEpJtPCjVtikS_FK)
- Any many more..

*if there is anyone I didn't mention, please let me know so I can add you to the list!*
