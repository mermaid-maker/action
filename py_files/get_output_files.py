### Get all the existing, generated mermaid files (if they exist)

from pathlib import Path
from os.path import basename
from os import environ
import json

input_files = json.loads(environ["INPUT_FILES"])
output_files = []

if environ["OUTPUT_DIR"] == "same":
    for file in input_files:
        output_files.append(
            Path(file).with_suffix(f".{environ['OUTPUT_FILE_EXTENSION']}").as_posix()
        )
else:
    for file in input_files:
        output_files.append(
            (Path(environ["OUTPUT_DIR"]) / basename(file))
            .with_suffix(f".{environ['OUTPUT_FILE_EXTENSION']}")
            .as_posix()
        )

with open(environ["GITHUB_OUTPUT"], "a") as file:
    print(f"output_files={json.dumps(output_files)}", file=file)
