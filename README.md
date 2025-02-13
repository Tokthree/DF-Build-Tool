# Dead Frontier Build Tool

Here it is, a build tool you can use without needing to launch a browser, go to DF Profiler, or navigate your 200+ tab deathstack! Do all of your build theorycrafting from the comfort of your desktop with this *bespoke* app!

### Blurb over

Real talk, this is a project I've wanted to work on for a long time. However, I have always been lacking the necessary skills to make it happen. First and foremost: This project is for myself, to say that I can do it; if anyone else finds it useful, then hot dang I simply cannot stop winning.

![Image showing the app](https://i.imgur.com/Uso7xYS.png)

## Features
- Supports entry of profession, level, stats, proficiencies, and equipment bonuses.
- Provides a live updating level requirement based on the points you've allocated.
  - Color coded if you exceed the maximum possible level!
- Provides a live updating display of the points you've allocated vs the points you have from your entered level.
  - Color coded if you're above, below or equal to the points granted by your entered level!
- Provides the ability to reset your stats, your equipment bonuses, or everything via handy buttons in the top right corner of each panel!
- Found in the header bar are three buttons:
  - Copy to your clipboard a rundown of your entered stats!
  - Open a saved build!
  - Save your current build as a JSON file!

That's basically it, a tool like this can only have so many features. Hopefully someone finds this useful, besides myself.

## Installation
Just grab the latest file from the releases section, unzip it while preserving the folder structure (all the files must be inside the `DF Build Tool` folder) and you should be good to go!

## Build instructions
This branch is intended to be run as-is on a Linux system. Please either download one of the pre-packaged releases, or navigate to one of the platform-specific branches for adjusted source code and platform-appropriate build instructions!

### Dependencies
You're gonna need to have the following packages to build the project yourself:
- `pip install "kivy[full]"`
- `pip install "kivy[gstreamer]"`
- `pip install "kivy[sdl2]"`
- `pip install "kivy[glew]"`
- `pip install pyperclip`
- `pip install plyer`
- `pip install pyinstaller`

This is going to sound pretty bad, but I've spent so many hours trying to get the build working on my end, that I've forgotten if there were any other dependencies. Hopefully I haven't, but please let me know if I did.
