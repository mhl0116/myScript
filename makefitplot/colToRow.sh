txtname=$1
grep "0.0 0.9" ../../txtfiles/${txtname} | awk -F " " '{print $8}' | awk 'BEGIN { ORS = "," } { print }'
echo " "
grep "0.9 2.4" ../../txtfiles/${txtname} | awk -F " " '{print $8}' | awk 'BEGIN { ORS = "," } { print }'
echo " "
