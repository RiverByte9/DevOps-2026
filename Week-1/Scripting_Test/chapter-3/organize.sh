#!/bin/bash
# organize.sh- Organize files by type into directories

echo "=== File Organizer ==="
# Create test files
echo "Creating test files..."
touch document{1..3}.txt
touch photo{1..3}.jpg
touch data{1..3}.csv
touch script{1..3}.sh

# Create directories
mkdir-p documents images data scripts

# Count and move files
txt_count=$(ls *.txt 2>/dev/null | wc -l)
jpg_count=$(la *.jpg 2>/dev/null | wc -l)
csv_count=$(ls *.csv 2>/dev/null | wc-l)
sh_count=$(ls *.sh 2>/dev/null | wc-l)

echo ""
echo "Found files:"
echo " Text files: $txt_count"
echo " Images: $jpg_count"
echo " CSV files: $csv_count"
echo " Scripts: $sh_count"

[ $text_count -gt 0 ] && mv *.txt documents/
[ $jpg_count -gt 0 ]  && mv *. jpg images/
[ $csv_count-gt 0 ] && mv *.csv data/
[ $sh_count-gt 0 ] && mv *.sh scripts/

echo ""
echo "files organized"
ls -R documents/ images/ data/ scripts/

#cleanup

echo ""
read -p "Remove organized directories? (y/n) " answer
if [ "$answwer" = "y"]; then
rm -rf documents/ images/ data/ scripts/
echo "cleaned up"
fi