#!/bin/bash

# String length
text="Hello, World!"
echo "Length: ${#text}"

# Substring extraction
echo "First 5 chars: ${text:0:5}"
echo "From position 7: ${text:7}"

# String replacement
filename="document.txt"
echo "Replace txt with pdf: ${filename/txt/pdf}"

# Remove prefix/suffix
path="/home/user/file.txt"
echo "Filename: ${path##*/}"
echo "Directory: ${path%/*}"

# Case conversion (bash 4+)
name="John Doe"
echo "Uppercase: ${name^^}"
echo "Lowercase: ${name,,}"

# String comparison
str1="apple"
str2="Apple"
if [ "$str1" = "$str2" ]; then
    echo "Strings are equal"
else
    echo "Strings are different"
fi

# Pattern matching
if [[ "$filename" == *.txt ]]; then
    echo "It's a text file"
fi