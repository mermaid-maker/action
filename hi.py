import os
import json
from subprocess import run
from pathlib import Path

output_file_arr = []
mermaid_env = [
    "aa-exec",
    "--profile=chrome",
]

# generate mermaid diagram for each changed file
for file in "${{env.ALL_CHANGED_FILES}}".split("\n"):
    if "${{inputs.output_dir}}" == "same":
        output_file = file + ".${{inputs.output_file_extension}}"
        output_file_arr.append(output_file)

        # use env variable to specify custom browser location
        # use aa-exec --profile chrome to sandbox puppeteer's chrome executoin
        # generate output files with transparent background
        mermaid_cmd = [
            "mmdc",
            "-i",
            file + ".${{inputs.input_file_extension}}",
            "-o",
            output_file,
            "-b",
            "transparent",
        ]

        run(
            mermaid_env + ["${{env.RUN_CMD}}"] + mermaid_cmd,
            env=os.environ.copy()
            | {"PUPPETEER_CACHE_DIR": "mermaid-maker-chrome-browser"},
        )

    else:
        # use user specified output dir
        output_file = (Path("${{inputs.output_dir}}") / file).with_suffix(
            "${{inputs.output_file_extension}}"
        )
        output_file_arr.append(output_file)

        mermaid_cmd = [
            "mmdc",
            "-i",
            file + ".${{inputs.input_file_extension}}",
            "-o",
            output_file,
            "-b",
            "transparent",
        ]

        run(
            mermaid_env + ["${{env.RUN_CMD}}"] + mermaid_cmd,
            env=os.environ.copy()
            | {"PUPPETEER_CACHE_DIR": "mermaid-maker-chrome-browser"},
        )

with open(os.environ["GITHUB_OUTPUT"]) as file:
    print(f"OUTPUTTED_FILES={json.dumps(output_file_arr)}", file=file)
