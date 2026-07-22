### Package manager setup
from subprocess import run

pkg_manager_run_cmd = ""
if "${{inputs.pkg_manager}}" == "npm":
  print("Nothing to setup")
elif "${{inputs.pkg_manager}}" == "pnpm":
  run(["pnpm", "config", "set", "--location=project", "strictDepBuilds", "false"])
elif "${{inputs.pkg_manager}}" == "yarn":
  print("Nothing to setup")
elif "${{inputs.pkg_manager}}" == "bun":
  print("Nothing to setup")
else:
    run(["exit", "1"])
