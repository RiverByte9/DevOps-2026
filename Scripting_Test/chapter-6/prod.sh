file="$1"
env="$2"

if [[ "$env" == "prod" && ! -f "$file" ]]; then
echo "Error: production deployment needs an existing file"
exit 2

fi

if [[ "$env" == "prod" ]] && ! grep -q "Release" "$file"; then
echo "prod builds must contain the world release"
exit 3

fi

echo "looks ok for $env"