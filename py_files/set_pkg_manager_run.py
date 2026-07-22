### Set pkg_manager run commmand
from subprocess import run
import os

pkg_manager_run_cmd = ""
if "${{inputs.pkg_manager}}" == "npm":
    pkg_manager_run_cmd = "npx"
elif "${{inputs.pkg_manager}}" == "pnpm":
    pkg_manager_run_cmd = "pnpm"
elif "${{inputs.pkg_manager}}" == "yarn":
    pkg_manager_run_cmd = "yarn dlx"
elif "${{inputs.pkg_manager}}" == "bun":
    pkg_manager_run_cmd = "bunx"
else:
    run(["exit", "1"])

with open(os.environ["GITHUB_OUTPUT"], "a") as file:
    print("pkg_manager_run_cmd=" + pkg_manager_run_cmd, file=file)
