### Set pkg_manager run commmand

from subprocess import run
from os import environ

pkg_manager_run_cmd = ""
if environ["PKG_MANAGER"] == "npm":
    pkg_manager_run_cmd = "npx"
elif environ["PKG_MANAGER"] == "pnpm":
    pkg_manager_run_cmd = "pnpm"
elif environ["PKG_MANAGER"] == "yarn":
    pkg_manager_run_cmd = "yarn dlx"
elif environ["PKG_MANAGER"] == "bun":
    pkg_manager_run_cmd = "bunx"
else:
    run(["exit", "1"])

with open(environ["GITHUB_OUTPUT"], "a") as file:
    print("pkg_manager_run_cmd=" + pkg_manager_run_cmd, file=file)
