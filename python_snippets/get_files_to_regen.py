### Get all the input/ouput files that must be (re)generated

from os.path import getmtime
from os import environ
from pathlib import Path
import json

input_files = json.loads(environ["INPUT_FILES"])
output_files = json.loads(environ["OUTPUT_FILES"])

input_files_to_regen = []
output_files_to_regen = []

for i in range(len(input_files)):
    output_file_exists = Path(output_files[i]).exists()

    if not output_file_exists or (getmtime(input_files[i]) > getmtime(output_files[i])):
        input_files_to_regen.append(input_files[i])
        output_files_to_regen.append(output_files[i])

with open(environ["GITHUB_OUTPUT"], "a") as file:
    print("input_files_to_regen=" + json.dumps(input_files_to_regen), file=file)
    print("output_files_to_regen=" + json.dumps(output_files_to_regen), file=file)
