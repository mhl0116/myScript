counter=0
while [ $counter -le 8 ]
do
  python makePlot.py -t "mc_DY15_16_muPtErr_"${counter} 
  counter=`expr $counter + 1`
done
