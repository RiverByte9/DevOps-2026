read -p "Enter your age: " age
if [[ ! "$age" =~ ^[0-9]+$ ]]; then
echo "Not a number"
elif (( age >=18 && age <= 65 )); then
echo "working age"
else
echo "Not typical working age"
fi