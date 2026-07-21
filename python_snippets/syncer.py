from subprocess import run
from os import chdir
from pathlib import Path
from os.path import dirname

prompt = input(
    "=" * 120
    + "\n"
    + """How do you want to sync the python files with action.yml run commands?
  - Type "left" or "l" to sync left, i.e. copy *run* commands and paste them into individual python files.
  - Type "right" or "r" to sync right, i.e. copy python files and paste them into their respective *run* commands. 
  - Or... just type "quit" or "q" to quit."""
    + "\n"
    + "=" * 120
    + "\n"
)

left = ["l", "left"]
right = ["r", "right"]
if prompt.lower() in left + right:
    chdir(Path(dirname(__file__)) / ".." / "file_syncer")
    if prompt.lower() in left:
        print("Syncing left...")
        run(["pnpm", "sync_left"])
    else:
        print("Syncing right...")
        run(["pnpm", "sync_right"])
    print("Completed!")
elif prompt.lower() in ["q", "quit"]:
    print("Quitting...")
else:
    print(f"Sorry! But {prompt} is not a recognized command. Exiting...")
