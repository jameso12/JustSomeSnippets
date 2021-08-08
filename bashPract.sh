#!/usr/bin/bash
echo "Hello World"
# this is a comment
# > redirects stdout
# 2>          stderr
# &>          both
# data sink /dev/null
# man null to find more
# variables are made:
a=4
echo $a
#{varName_exp} places output in between, before or after 
# strings or values
#[process] 
#(output) executes and outputs
#stdin :
# this takes input(keystrokes are the most usual input)
# to < from
#until crt+D is pressed is used when using cat command

# functions:
function myFync {
echo "love";echo "life"
}
myFync
# inputs can also be recived using \$ appended by a number(1+)
# $# number of arguments given is displayed
# $* displays all arguments
# -z verifies if arg has value
# ! is still negator
# exit terminates execution can be given 1 or 0 args
# 1, meaning false, means an it terminated with an error



# man bash
# man find 
# man wc
# man echo
 

#comparisions
#string:
# less than <
# greater  >
# equal =
#not equal !=
# numeric:
#-lt
# -gt
# -eq
# -ne
# -le less than or equal
# -ge greater than or equal

#echo $? returns the reurn val of previously executed 
#expression
# 0 is true 1 is false
if [ 0 ]
then
echo "yes"
fi