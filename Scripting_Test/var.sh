
name="Devops"
count=56

echo "hello, $name"
echo "count: $count"

current_user=$(whoami)
file_count=$(ls | wc -l)

# $ ./var.sh
# hello, Devops
# count: 56
