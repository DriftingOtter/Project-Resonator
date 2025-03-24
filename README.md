![Banner](./GitHub%20Assets/GitHub%20Banner.png)
# __Project Resonator | *The* Open-Source IEM.__

> A love letter to the IEM/CIEM hobby.

## Technologies Used & Software required

1. VituixCAD Ver < 2.0       (For tuning simulation) (Read below for install guide)
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

## How to install archived version of vituixCAD + Missing file paths issue [FIXED]

1. Go to [Internet Archive's Wayback machine](https://archive.org/)
2. Paste "https://kimmosaunisto.net/"
3. Find any version of the software before < 2018-04-25, then download + install
4. Then open the simulation ```.vxp``` file from the project

Most likely when you open the files it will give you a buch of errors of missing file path(s). Don't Worry! Its just because they still are using the paths on my system for finding the ```.frd``` and ```.zma``` files for the drivers.

To update the paths for the ```.frd``` (frequency response) and ```.zma``` (impedance response) files, click the folder icon next to the file upload section. Then, navigate to the correct folder for each BA driver in the "BA Driver Spec Sheets" directory within the project files and select the corresponding ```.frd``` or ```.zma``` file(s). This should resolve any missing path issues.

*(you only have to do this once)*

## How to de-compress Autodesk Fusion 360 IEM Shell Files

Since the IEM Shell files are too big to upload to GitHub, I have added them to the dropbox link below, go to the site and download the folder/file(s) and de-compress them via the respective commands below w/ OpenCTM.

[Dropbox Link For IEM Shell Files](https://www.dropbox.com/scl/fo/7igmpw1ufs74wjp9bscd1/APTIkM8Hd0Q5tOlSX6-9Vis?rlkey=q3dak7tetpvdot7d4ondi776o&st=a5fo64j4&dl=0)

### Linux
```Bash
for file in *.ctm; do
    ctmconv "$file" "${file%.ctm}.stl"
done
```

### Windows Powershell
```Powershell
Get-ChildItem -Filter "*.ctm" | ForEach-Object {
    $output = $_.FullName -replace "\.ctm$", ".stl"
    & ctmconv $_.FullName $output
}
```

## Authors

- Daksh Kaul (aka. DriftingOtter)

## Credits & Citations
- Head-Fi's DIY IEM forms and community
- [Kozh](https://www.youtube.com/@kozh4013/videos)
- [Kirby Meets Audio](https://youtu.be/QClvPIuW3zI?si=NcwjdGAZriBUcmHE)
- [Crinacle](https://www.youtube.com/watch?v=tCqV3ZRcZ9g&t=1227s)
- [Mr.T's Design Graveyard](https://youtu.be/3FGNw28xBr0?si=LEpJtPCjVtikS_FK)
- *Any many more...*


*if there is anyone I didn't mention, please let me know so I can add you to the list!*
