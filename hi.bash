shopt -s globstar nullglob
echo "VAR=$(
    for file in **/*.mmd; do
        if [[ "$(dirname "$file")/$(basename -s ".mmd" "$file").svg" -ot "$file" ]]; then
            echo "$file"
        fi
    done
)" >> "$GITHUB_OUTPUT"
shopt -u globstar nullglob

shopt -s globstar nullglob
VAR=$(
    for file in **/*.mmd; do
        if [[ "$(dirname "$file")/$(basename -s ".mmd" "$file").svg" -ot "$file" ]]; then
            echo "$file"
        fi
    done
)
shopt -u globstar nullglob

        shopt -s globstar nullglob

        echo CHANGED_FILES="$(

            for file in ${{env.FILES_TO_CHECK}}; do

                FILE_DIRNAME=$(dirname "$file")
                FILE_BASENAME=$(basename -s ".${{inputs.input_file_extension}}" "$file")

                if [[ "${FILE_DIRNAME}/${FILE_BASENAME}.${{inputs.output_file_extension}}" -ot "$file" ]]; then
                
                    echo "${FILE_BASENAME}"

                fi

            done
        )" >> "$GITHUB_OUTPUT"

        shopt -u globstar nullglob
