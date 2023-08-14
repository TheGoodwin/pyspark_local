# PySpark local

## Prerequisites

- Install Java 8
- Install Spark ([Windows guide](https://sparkbyexamples.com/spark/apache-spark-installation-on-windows/))
- Install Python 3
- Install poetry

## Fetch open datas

### 2019 births in France

https://www.insee.fr/fr/statistiques/4768335?sommaire=4768339

Download as CSV and extract the FD file into `data/inputs/births`

### 2019 deaths in France

https://www.insee.fr/fr/statistiques/4801913?sommaire=4768339

Download as CSV and extract the FD file into `data/inputs/deaths`

## Run the project

`poetry run spark-submit --master local pyspark_local\main.py`