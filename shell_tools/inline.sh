#!/bin/bash

var1=1
var2=2
var3=2
var4=2

var5=`bc <<EOF
scale=4
a1 = $var1 * $var2
b1 = $var3 * $var4
a1 + b1
EOF
`
echo The final answer for this mess is $var5
