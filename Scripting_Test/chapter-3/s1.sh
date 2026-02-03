text="Hello World"
echo ${#text}
# → 11

greeting="Hi there" #8
filename="photo_2025_vacation.jpg" #23
echo ${#greeting}
echo ${#filename}


text="Hello World"

echo ${text:0:5}     # Hello
echo ${text:6}       # World
echo ${text:6:3}     # Wor
echo ${text:-5}      # World   (last 5 characters)
echo ${text: -5:2}   # Wo     (notice space before -5)



file="/home/user/docs/report.txt"

echo ${file#*/}      # home/user/docs/report.txt     (shortest match)
echo ${file##*/}     # report.txt                    (longest match → everything until last /)

echo ${file#/}       # home/user/docs/report.txt     (removes just leading /)
echo ${file#*user/}  # docs/report.txt





file="/home/user/report.txt"

echo ${file%.txt}       # /home/user/report
echo ${file%.*}         # /home/user/report          (removes shortest = .txt)
echo ${file%%.*}        # /home/user/report          (still removes .txt — no longer match)

file="image-backup-v3.tar.gz"

echo ${file%.gz}        # image-backup-v3.tar
echo ${file%%.*}        # image-backup-v3            (longest → removes everything from first .)

text="hello world hello everyone"

echo ${text/hello/hi}       # hi world hello everyone
echo ${text//hello/hi}      # hi world hi everyone

echo ${text//o/O}           # hellO wOrld hellO everyOne


text="Hello World 2025!"

echo ${text^^}     # HELLO WORLD 2025!
echo ${text,,}     # hello world 2025!

echo ${text^}      # Hello World 2025!  (only first letter)
echo ${text,,[A-Z]}   # hello world 2025!  (lowers only A–Z, not numbers)