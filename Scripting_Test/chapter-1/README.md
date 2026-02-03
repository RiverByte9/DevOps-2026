View a specific variable:
echo $HOME
echo $USER
echo $PATH
The $ tells the shell to substitute the variable’s value. $HOME becomes /home/username.
View all variables:
env            # All environment variables

printenv HOME   # Specific variable

For current shell only:
MY_VAR="hello"
echo $MY_VAR

Export to child processes:
export MY_VAR="hello"
./my_script.sh           # Script can access MY_VAR
Without export, child processes don’t see the variable. Use export when you want programs you
run to access the variable

Temporary variable for one command:
DEBUG=true ./script.sh
This sets DEBUG only for that one command execution.