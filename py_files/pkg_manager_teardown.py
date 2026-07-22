### Package manager teardown

from subprocess import run
from os import environ

pkg_manager_run_cmd = ""

if environ["PKG_MANAGER"] == "npm":
    print("Nothing to teardown")
elif environ["PKG_MANAGER"] == "pnpm":
    run(["pnpm", "config", "set", "--location=project", "strictDepBuilds", "true"])
elif environ["PKG_MANAGER"] == "yarn":
    print("Nothing to teardown")
elif environ["PKG_MANAGER"] == "bun":
    print("Nothing to teardown")
else:
    run(["exit", "1"])
