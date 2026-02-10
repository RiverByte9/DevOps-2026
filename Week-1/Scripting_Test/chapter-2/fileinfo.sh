#!/bin/bash
# fileinfo.sh- Display file information with validation

# Validate argument
if [ $# -eq 0 ]; then
echo "Usage: $0 <filename>"
exit 1

fi
file=$1

# Check if file exists
if [ ! -f "$file" ]; then
echo "Error: File '$file' not found"
exit 2
fi

# Display information
echo "=== File Information ==="
echo "Name: $(basename "$file")"
echo "Path: $(realpath "$file")"
echo "Size: $(wc -c < "$file") bytes"
echo "Lines: $(wc -l < "$file")"
echo "Words: $(wc -w < "$file")"


# Check permissions
echo ""
echo "=== Permissions ==="
[ -r "$file" ] && echo " Readable" || echo " Not readable"
[ -w "$file" ] && echo " Writable" || echo " Not writable"
[ -x "$file" ] && echo " Executable" || echo " Not executable"


echo ""
echo "Last modified: $(date -r "$file")"