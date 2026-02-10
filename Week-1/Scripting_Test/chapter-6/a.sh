file="report.txt"

if [[ -f "$file" && -r "$file" && -s "$file" ]]; then
 echo "Good: regular file, readable, and has content"
 else
 echo "problem with the file"
 exit 1
 fi