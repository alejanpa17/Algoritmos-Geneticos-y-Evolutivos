#!/bin/bash

#num_pop - num_gen - prob_t - lambda - num_fam - cicles

#Ejemplo de ejecucion
#python3 main.py 100 4 0.05 40 3 100

mkdir solutions

#Porcentaje de lambda
echo "Porcentaje de lambda"
# python3 main.py 100 4 0.05 20 3 150 > solutions/lambda_20.txt
# python3 main.py 100 4 0.05 30 3 150 > solutions/lambda_30.txt
# python3 main.py 100 4 0.05 40 3 150 > solutions/lambda_40.txt
# python3 main.py 100 4 0.05 50 3 150 > solutions/lambda_50.txt
# python3 main.py 100 4 0.05 60 3 150 > solutions/lambda_60.txt
# python3 main.py 100 4 0.05 70 3 150 > solutions/lambda_70.txt
# python3 main.py 100 4 0.05 80 3 150 > solutions/lambda_80.txt

#Tamano de la poblacion
echo "Tamano de la poblacion"
python3 main.py 50 4 0.05 30 3 150 > solutions/pop_50.txt
python3 main.py 100 4 0.05 60 3 150 > solutions/pop_100.txt
python3 main.py 150 4 0.05 90 3 150 > solutions/pop_150.txt
python3 main.py 200 4 0.05 120 3 150 > solutions/pop_200.txt
python3 main.py 250 4 0.05 150 3 150 > solutions/pop_250.txt
python3 main.py 300 4 0.05 180 3 150 > solutions/pop_300.txt
python3 main.py 500 4 0.05 300 3 150 > solutions/pop_500.txt
