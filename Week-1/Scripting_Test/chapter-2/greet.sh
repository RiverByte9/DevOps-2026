#!/bin/bash

# name=$1
# age=$2

# echo "Hello, $name"
# echo "you are $age years old"

# Providing Default Values

# name=${1:-"Guest"}
# age=${2:-"unknown"}

# echo "Hello, $name!"
# echo "You are $age years old"

# Validating Arguments

if [ $# -eq 0 ]; then
echo "Usage: $0 <name> [age]"
exit 1
fi

name=$1
age=${2:-"unknown"}

echo "hello, $name! Age: $age"

