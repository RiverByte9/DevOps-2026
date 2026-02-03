#!/bin/bash
# pathparser.sh - Parse file paths and manipulate strings
# Test file path
path="/home/user/documents/report_2024.txt"
echo "=== Original Path ==="
echo "$path"
echo ""
# Extract components
filename="${path##*/}" # Get filename only
dirname="${path%/*}" # Get directory only
basename="${filename%.*}" # Filename without extension
extension="${filename##*.}" # Extension only
echo "=== Components ==="
echo "Directory: $dirname"
echo "Filename: $filename"
echo "Base name: $basename"
echo "Extension: $extension"
echo ""
# Transform filename
uppercase="${filename^^}"
lowercase="${filename,,}"
renamed="${filename/report/summary}"
echo "=== Transformations ==="
echo "Uppercase: $uppercase"
echo "Lowercase: $lowercase"
echo "Renamed: $renamed"
echo ""
# Build new path

new_path="${dirname}/${renamed}"
echo "New path: $new_path"
echo ""
# Extract year from filename
if [[ $filename =~ ([0-9]{4}) ]]; then
year="${BASH_REMATCH[1]}"
echo "Found year: $year"
fi