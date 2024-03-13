import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('iris.csv')

setosa = iris[iris['Species'] == 'setosa']
versicolor = iris[iris['Species'] == 'versicolor']
virginica = iris[iris['Species'] == 'virginica']

iris_sepal_square = iris['Sepal.Length']*iris['Sepal.Width']
iris_petal_square = iris['Petal.Length']*iris['Petal.Width']


def sample_average(square):
    return sum(square)/square.count()

def sample_variance(square, avg):
    avg_square = avg * avg
    return sum(square ** 2) / square.count() - avg_square

def sample_median(square):
    sorted_square = square.sort_values()
    count = sorted_square.count()
    if count % 2 == 0:
        return (sorted_square[count/2 - 1] + sorted_square[count/2])/2
    else:
        return sorted_square[count/2 - 1] 

# TOTAL
#  Sample Average for:
#   `Sepal`
total_sepal_sample_avg = (sample_average(iris_sepal_square))
#   `Petal`
total_petal_sample_avg = (sample_average(iris_petal_square))
#  Sample Variance for:
#   `Sepal`
total_sepal_sample_variance = (sample_variance(iris_sepal_square, total_sepal_sample_avg))
#   `Petal`
total_petal_sample_variance = (sample_variance(iris_petal_square, total_petal_sample_avg))
#  Sample Median for:
#   `Sepal`
total_sepal_sample_median = (sample_median(iris_sepal_square))
#   `Petal`
total_petal_sample_median = (sample_median(iris_petal_square))

print(total_sepal_sample_avg, total_petal_sample_avg)
print(total_sepal_sample_variance, total_petal_sample_variance)
print(total_sepal_sample_median, total_petal_sample_median)