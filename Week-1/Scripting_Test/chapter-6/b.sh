filename="$1"

if [[ -z "$filename" ]]; then
    echo "No filename given"
    exit 1
fi

if [[ "$filename" =~ \.(jpe?g|JPE?G)$ ]]; then
    echo "Looks like a JPEG"
else
    echo "Not a JPEG filename"
fi