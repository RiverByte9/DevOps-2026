 Rules:- 
 No spaces around =- Quote values with spaces: name="John Doe"- Use $variable or
 ${variable} to access

Testing Your Scripts
Always test scripts before deploying:
1. Syntax check

bash-n script.sh
# Check for syntax errors
2. Dry run with debug
bash-x script.sh
# Show each command before execution
3. Test with various inputs
./script.sh test1.txt
./script.sh /path/to/file
./script.sh ""
# Empty input
4. Check exit codes
./script.sh
echo $?
# 0 = success, non-zero = error