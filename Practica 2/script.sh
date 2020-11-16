#!/bin/bash

#num_pop - num_gen - prob_t - lambda - num_fam - cicles

#Ejemplo de ejecucion
#python3 main.py 100 4 0.05 40 3 100

mkdir solutions

#Porcentaje de lambda
echo "Porcentaje de lambda"
python3 main.py 100 4 0.05 20 3 150 > solutions/lambda_20.txt
python3 main.py 100 4 0.05 30 3 150 > solutions/lambda_30.txt
python3 main.py 100 4 0.05 40 3 150 > solutions/lambda_40.txt
python3 main.py 100 4 0.05 50 3 150 > solutions/lambda_50.txt
python3 main.py 100 4 0.05 60 3 150 > solutions/lambda_60.txt
python3 main.py 100 4 0.05 70 3 150 > solutions/lambda_70.txt
python3 main.py 100 4 0.05 80 3 150 > solutions/lambda_80.txt
