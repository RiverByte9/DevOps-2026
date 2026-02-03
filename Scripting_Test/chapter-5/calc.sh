#!/bin/bash
# calc.sh - Simple calculator with integer and decimal support
echo "=== Simple Calculator ==="
echo ""
# Get input
read -p "Enter first number: " num1
read -p "Enter operator (+, -, *, /): " op
read -p "Enter second number: " num2
# Integer calculation
case $op in
+) result=$((num1 + num2));;
-) result=$((num1 - num2));;
*) result=$((num1 * num2));;
/) result=$((num1 / num2));;
*) echo "Invalid operator"; exit 1;;
esac
echo ""
echo "=== Integer Result ==="
echo "$num1 $op $num2 = $result"
# Decimal calculation using bc
if [ "$op" = "/" ]; then
decimal=$(echo "scale=2; $num1 / $num2" | bc)
echo ""
echo "=== Decimal Result ==="
echo "$num1 $op $num2 = $decimal"
fi
# Additional calculations
echo ""
echo "=== Additional Info ==="
echo "Sum: $((num1 + num2))"
echo "Difference: $((num1 - num2))"
echo "Product: $((num1 * num2))"
if [ $num2 -ne 0 ]; then
echo "Quotient: $((num1 / num2))"
echo "Remainder: $((num1 % num2))"
fi