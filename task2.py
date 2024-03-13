import pandas as pd
import matplotlib.pyplot as plt
import numpy
import pretty_print

iris = pd.read_csv('iris.csv')

setosa = iris[iris['Species'] == 'setosa']
versicolor = iris[iris['Species'] == 'versicolor']
virginica = iris[iris['Species'] == 'virginica']

sepal_length = 'Sepal.Length'
sepal_width = 'Sepal.Width'
petal_length = 'Petal.Length'
petal_width = 'Petal.Width'

iris_sepal_square = iris[sepal_length]*iris[sepal_width]
iris_petal_square = iris[petal_length]*iris[petal_width]
setosa_sepal_square = setosa[sepal_length]*setosa[sepal_width]
setosa_petal_square = setosa[petal_length]*setosa[petal_width]
versicolor_sepal_square = versicolor[sepal_length]*versicolor[sepal_width]
versicolor_petal_square = versicolor[petal_length]*versicolor[petal_width]
virginica_sepal_square = virginica[sepal_length]*virginica[sepal_width]
virginica_petal_square = virginica[petal_length]*virginica[petal_width]

def sample_average(square):
    return sum(square)/square.count()

def sample_variance(square, avg):
    avg_square = avg * avg
    return sum(square ** 2) / square.count() - avg_square

def sample_median(square):
    sorted_square = square.sort_values()
    count = len(sorted_square)
    if count % 2 == 0:
        return (sorted_square.iloc[count//2 - 1] + sorted_square.iloc[count//2])/2
    else:
        return sorted_square.iloc[count//2 - 1]
    
def calculations():
    data_map = {}
    species = {"Total": [iris_sepal_square, iris_petal_square], "Setosa": [setosa_sepal_square, setosa_petal_square],
               "Versicolor": [versicolor_sepal_square, versicolor_petal_square], "Virginica": [virginica_sepal_square, virginica_petal_square]}

    for spec in species:
        sepal_square, petal_square = species[spec][0], species[spec][1]    
        sepal_sample_avg, petal_sample_avg = round(sample_average(sepal_square), 4), round(sample_average(petal_square), 4)
        sepal_sample_var, petal_sample_var = str(round(sample_variance(sepal_square, sepal_sample_avg), 4)), str(round(sample_variance(petal_square, petal_sample_avg), 4))
        sepal_sample_median, petal_sample_median = str(round(sample_median(sepal_square), 4)), str(round(sample_median(petal_square), 4))
        sepal_sample_quantile, petal_sample_quantile = str(round(numpy.quantile(sepal_square, 0.4), 4)), str(round(numpy.quantile(petal_square, 0.4), 4))
        data_map[spec] = [str(sepal_sample_avg), str(petal_sample_avg), sepal_sample_var, petal_sample_var, sepal_sample_median, petal_sample_median, sepal_sample_quantile, petal_sample_quantile]

    return data_map
4
def output():
    values = calculations()
    data = [["SPECIES", "SEPAL AVERAGE", "PETAL AVERAGE", "SEPAL VARIANCE", "PETAL VARIANCE", "SEPAL MEDIAN", "PETAL MEDIAN", "SEPAL QUANTILE", "PETAL QUANTILE"]]
    for spec in values:
        data.append([spec] + values[spec])
    pretty_print.print_pretty_table(data)

output()