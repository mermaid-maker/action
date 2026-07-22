### Package manager teardown
from subprocess import run

pkg_manager_run_cmd = ""
if "${{inputs.pkg_manager}}" == "npm":
  print("Nothing to teardown")
elif "${{inputs.pkg_manager}}" == "pnpm":
  run(["pnpm", "config", "set", "--location=project", "strictDepBuilds", "true"])
elif "${{inputs.pkg_manager}}" == "yarn":
  print("Nothing to teardown")
elif "${{inputs.pkg_manager}}" == "bun":
  print("Nothing to teardown")
else:
    run(["exit", "1"])
