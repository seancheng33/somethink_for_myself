#!/bin/bash

# for ((i=1;i<=9;i++))
# do
#     for ((j=1;j<=i;j++))
#     do
#         echo -ne "$i*$j="$[$i * $j]"\t"
#     done
#     echo
# done

# echo "    *"
# echo "   ***"
# echo "  *****"
# echo " *******"
# echo "*********"


level=$1
tmplevel=1
for ((i=$level;i>=0;i--))
do
    # tmplevel=1
    for j in `seq $i`
    do
        echo -n " "
    done
    for ((j=1;j<tmplevel*2;j++))
    do
        echo -n "*"
    done
    ((tmplevel++))
    echo
done