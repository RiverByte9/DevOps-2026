#conditional
#!/bin/bash

if [ ! -f "$1" ]; then
    echo "File doesn't exist..."
    exit 1
fi

# echo "Zipping the log file $1"
# zip "$1.zip" "$1" >/dev/null 2>$1
# cat /dev/null $1
# touch "$1"

echo " zipping the log file $1"
zip "$1.$(date +%s).zip" "$1" >/dev/null 2>&1
cat /dev/null > "$1"
touch "$1"


# output
#  chmod u+x 2.sh
#  ./2.sh dummy.log
# Zipping the log file dummy.log
#   adding: dummy.log (deflated 3%)
