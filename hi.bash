        arr=()
        for file in ${ALL_CHANGED_FILES}; do
          file_base=$(basename -s ".${{inputs.input_file_extension}}" "${file}")
          original_file_dir=$(dirname "${file}")
          if [[ "${{inputs.output_dir}}" == "same" ]]; then
            output_file="${original_file_dir}/${file_base}.${{inputs.output_file_extension}}"
            arr+=("$output_file")
            PUPPETEER_CACHE_DIR=mermaid-maker-chrome-browser aa-exec --profile=chrome mmdc -i "$file" -o "$output_file" -b transparent
          else
            output_file="${{inputs.output_dir}}/${file_base}.${{inputs.output_file_extension}}"
            arr+=("$output_file")
            PUPPETEER_CACHE_DIR=mermaid-maker-chrome-browser aa-exec --profile=chrome mmdc -i "$file" -o "$output_file" -b transparent
          fi
        done


        # Source - https://stackoverflow.com/a/67489301
        # Posted by Weeble, modified by community. See post 'Timeline' for change history
        # Retrieved 2026-07-09, License - CC BY-SA 4.0

        echo "OUTPUTTED_FILES=$(jq --compact-output --null-input '$ARGS.positional' --args -- "${arr[@]}")" >> "$GITHUB_OUTPUT"
