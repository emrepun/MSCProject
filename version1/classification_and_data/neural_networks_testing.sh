#!/bin/bash

echo initialized.

for sample_count in 500 1000 5000 10000 50000 100000 250000 500000 1000000 2500000 5000000
#for sample_count in 500 1000
do
  python3 header_neural_networks.py $sample_count
  for i in {1..10}
  do
    python3 DataGenerator.py $sample_count
    python3 TensorflowKerasClassifier.py
  done

  echo done with $sample_count
done

python3 footer_neural_networks.py
