# General Notes

## 0x03 Shell, init files, variables and expansions
- If we place text inside double quotes, all the special characters used by the shell lose their special meaning and are treated as ordinary characters. The exceptions are “$”, “\” (backslash), and “`” (back- quote)
- When we need to suppress all expansions, we use single quotes
```shell
[me@linuxbox me]$ echo text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER
text /home/me/ls-output.txt a b foo 4 me
[me@linuxbox me]$ echo "text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER"
text ~/*.txt {a,b} foo 4 me
[me@linuxbox me]$ echo 'text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER'
text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER
```
- We can use a backslash (\\) to get the shell to ignore a newline character like this:
```shell
ls -l \
   --reverse \
   --human-readable \
   --full-time
```
- To set a variable **in the shell**, use
`VARNAME="value"`
- To set a **global variable**, use `export VARNAME="value"`

- The positional parameters are the words following the name of a shell script. They are put into the variables \$1, \$2, \$3 and so on. As long as needed, variables are added to an internal array. \$# holds the total number of parameters, as is demonstrated with this simple script:
```bash
#!/bin/bash

# positional.sh
# This script reads 3 positional parameters and prints them out.

POSPAR1="$1"
POSPAR2="$2"
POSPAR3="$3"

echo "$1 is the first positional parameter, \$1."
echo "$2 is the second positional parameter, \$2."
echo "$3 is the third positional parameter, \$3."
echo
echo "The total number of positional parameters is $#."
```
``` shell
youssef ~> positional.sh one two three four five
one is the first positional parameter, $1.
two is the second positional parameter, $2.
three is the third positional parameter, $3.

The total number of positional parameters is 5.

youssef ~> positional.sh one two
one is the first positional parameter, $1.
two is the second positional parameter, $2.
 is the third positional parameter, $3.

The total number of positional parameters is 2.
```
