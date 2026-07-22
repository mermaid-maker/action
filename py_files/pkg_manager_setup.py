### Package manager setup

from subprocess import run
from os import environ

pkg_manager_run_cmd = ""

if environ["PKG_MANAGER"] == "npm":
    print("Nothing to setup")
elif environ["PKG_MANAGER"] == "pnpm":
    run(["pnpm", "config", "set", "--location=project", "strictDepBuilds", "false"])
elif environ["PKG_MANAGER"] == "yarn":
    print("Nothing to setup")
elif environ["PKG_MANAGER"] == "bun":
    print("Nothing to setup")
else:
    run(["exit", "1"])
