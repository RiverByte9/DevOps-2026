#command line arg and exit

#!/bin/bash

echo "script running is $0"
echo "first argument -> $1 second -> $2 third ->$3"
echo "list all arguments-> $@"
echo "count of arguments-> $#"

exit 1

#ecn
#echo $1 $2

# r -> read (4) w -> (2)  -> x (1)
# -rwxrwxrwx
# ---(user) ---(group)---(other)