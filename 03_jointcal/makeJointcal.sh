#!/bin/bash

label="WIDE"
mkdir  $label-scripts
cat FilterTractVisits_$label  | while read line
do
    tract=`echo $line | awk '{print $2}'`
    filter=`echo $line | awk '{print $1}'`
    visit=`echo $line | awk '{print $3}'`
    sed "s|@TRACT@|$tract|g ; s|@VISIT@|$visit|g ; s|@WEEK@|$label|g ; s|@FILTER@|$filter|g " jointcal_template_$label.sh > $label-scripts/$label-jointcal-$tract-$filter.sl
    echo "sbatch $label-jointcal-$tract-$filter.sl" >> $label-jointcal-submit.sh
done

chmod +x $label-jointcal-submit.sh
mv -i $label-jointcal-submit.sh $label-scripts
