import pandas as pd
import numpy
import matplotlib.pyplot as plt
import seaborn as sns
import pretty_print


iris = pd.read_csv('iris.csv')

sepal_length = 'Sepal.Length'
sepal_width = 'Sepal.Width'
petal_length = 'Petal.Length'
petal_width = 'Petal.Width'

iris['sepal_square'] = iris[sepal_length] * iris[sepal_width]
iris['petal_square'] = iris[petal_length] * iris[petal_width]
iris['total_square'] = iris['sepal_square'] + iris['petal_square']

setosa = iris[iris['Species'] == 'setosa']
versicolor = iris[iris['Species'] == 'versicolor']
virginica = iris[iris['Species'] == 'virginica']

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
    species = {"Total": [iris['total_square']], "Setosa": [setosa['total_square']],
               "Versicolor": [versicolor['total_square']], "Virginica": [virginica['total_square']]}
    
    for spec in species:
        square = species[spec][0]
        average = sample_average(square)
        variance = sample_variance(square, average)
        median = sample_median(square)
        quantile = str(numpy.quantile(square, 0.4))
        data_map[spec] = [str(average), str(variance), str(median), str(quantile)]
        
    return data_map

def tables_output():
    values = calculations()
    species_count = {"Setosa": len(setosa), "Versicolor": len(versicolor), "Virginica": len(virginica)}
    data = [["SPECIES", "AVERAGE", "VARIANCE", "MEDIAN", "QUANTILE (0.4)"]]
    min_max_data = [["SPECIES", "COUNT"]]
    
    for spec in values:
        data.append([spec] + values[spec])
        
    for spec in species_count:
        count = [str(species_count[spec])]
        min_max_data.append([spec] + count)
    
    print()
    pretty_print.print_pretty_table(min_max_data)
    print()
    pretty_print.print_pretty_table(data)
    print()

def plot_all():
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
    total_square = 'Total Square (Sepal + Petal)'

    # ECDF
    sns.ecdfplot(iris['total_square'], label='Total', color='black', ax=axes[0])
    sns.ecdfplot(setosa['total_square'], label='Setosa', color='blue', ax=axes[0])
    sns.ecdfplot(versicolor['total_square'], label='Versicolor', color='red', ax=axes[0])
    sns.ecdfplot(virginica['total_square'], label='Virginica', color='purple', ax=axes[0])
    axes[0].set_title('Empirical Cumulative Distribution Function (ECDF)')
    axes[0].set_xlabel(total_square)
    axes[0].set_ylabel('Cumulative Probability')
    axes[0].legend()
    axes[0].grid()

    # Histogram
    sns.histplot(iris['total_square'], kde=False, color='black', label='Total', ax=axes[1])
    sns.histplot(setosa['total_square'], kde=False, label='Setosa', color='blue', ax=axes[1])
    sns.histplot(versicolor['total_square'], kde=False, label='Versicolor', color='red', ax=axes[1])
    sns.histplot(virginica['total_square'], kde=False, label='Virginica', color='purple', ax=axes[1])
    axes[1].set_title('Histogram of Total Square (Sepal + Petal)')
    axes[1].set_xlabel(total_square)
    axes[1].set_ylabel('Frequency')
    axes[1].legend()
    axes[1].grid()

    # Box-plot
    sns.boxplot(x='Species', y='total_square', data=iris, hue='Species', palette=['blue', 'red', 'purple'], legend=False, ax=axes[2])
    axes[2].set_title('Box-plot of Total Square (Sepal + Petal)')
    axes[2].set_xlabel('Species')
    axes[2].set_ylabel(total_square)
    axes[2].grid()

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    tables_output()
    plot_all()