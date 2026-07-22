### Generate mermaid diagrams

import json
from subprocess import run
from os import environ

input_files_to_regen = json.loads(environ["INPUT_FILES_TO_REGEN"])
output_files_to_regen = json.loads(environ["OUTPUT_FILES_TO_REGEN"])

mermaid_env = [
    "env",
    "PUPPETEER_CACHE_DIR=mermaid-maker-chrome-browser",
    "aa-exec",
    "--profile=chrome",
]

# generate mermaid diagram for each changed file
for i in range(len(input_files_to_regen)):
    mermaid_cmd = [
        "mmdc",
        "-i",
        input_files_to_regen[i],
        "-o",
        output_files_to_regen[i],
        "-b",
        "transparent",
    ]

    run(
        mermaid_env + [environ["RUN_CMD"]] + mermaid_cmd,
    )
