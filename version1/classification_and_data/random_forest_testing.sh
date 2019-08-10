#!/bin/bash

echo initialized.

#for sample_count in 100 250 500 1000 3000 6000 10000
for sample_count in 50000 100000 500000 1000000
do
  python3 header.py $sample_count
  for j in {1..10}
  do
    #python3 DataGenerator.py $sample_count
    python3 NormalDistributionGenerator.py $sample_count
    python3 RandomForestClassifierTraining.py
  done
  #sample_count=$sample_count*10
  echo done with $sample_count
done

python3 footer.py
