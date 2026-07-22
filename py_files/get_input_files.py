### Get all the input mermaid files

from glob import glob
from os import environ
import json

if environ["INPUT_DIR"] == "all":
    input_files_glob_pattern = f"**/*.{environ['INPUT_FILE_EXTENSION']}"
else:
    input_files_glob_pattern = (
        f"{environ['INPUT_DIR']}/*.{environ['INPUT_FILE_EXTENSION']}"
    )

input_files = []
for file in glob(input_files_glob_pattern, recursive=True):
    input_files.append(file)

with open(environ["GITHUB_OUTPUT"], "a") as file:
    print("input_files=" + json.dumps(input_files), file=file)
