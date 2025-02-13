# Dead Frontier Build Tool - Windows Branch

This is the Windows-specific distribution branch of the Dead Frontier Build Tool. The source code and releases contained within are intended **ONLY** for use on Windows-based systems, and their functionality cannot be guaranteed elsewhere.

![Image showing the app](https://i.imgur.com/Uso7xYS.png)

## Build instructions
Honestly, I don't really know what I'm doing; figuring out how to build it myself took hours. But if you're the kind of person who builds git projects instead of downloading their releases, I'm sure you know more about it than I do.

If you wish to build it exactly the way I did, here's the simple steps:
- Download the source.
- Open your terminal of choice.
- Navigate to the folder you downloaded the source to.
 - Create a virtual environment (optional, if you know how to set up PATH variables within Windows).
 - Install the dependencies to the virtual environment (optional, if you know how to set up PATH variables within Windows).
- Run the command `pyinstall release.spec`, or `pyinstall release_debug.spec` to see which files are and are not being included in the packaged file, and for the packaged executable to have a console output (everything will be in the `dist` folder).

Once it's done compiling, you can find the executable in the `dist` folder. Simply copy the `images` folder to wherever you plan to run the executable from, and fire away!


If you're looking to build it your own way, the process is basically the same. You just need to construct your own `pyinstall` command or `.spec` file.

### Build dependencies
You're gonna need to have the following packages to build the project yourself:
- `pip install "kivy[full]"`
- `pip install "kivy[gstreamer]"`
- `pip install "kivy[sdl2]"`
- `pip install "kivy[glew]"`
- `pip install pyperclip`
- `pip install plyer`
- `pip install pyinstaller`

This is going to sound pretty bad, but I've spent so many hours trying to get the build working on my end, that I've forgotten if there were any other dependencies. Hopefully I haven't, but please let me know if I did.
