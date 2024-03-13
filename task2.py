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
    species = {"Total": [iris['sepal_square'], iris['petal_square']], "Setosa": [setosa['sepal_square'], setosa['petal_square']],
               "Versicolor": [versicolor['sepal_square'], versicolor['petal_square']], "Virginica": [virginica['sepal_square'], virginica['petal_square']]}
    
    for spec in species:
        sepal_square, petal_square = species[spec][0], species[spec][1]    
        sepal_sample_avg, petal_sample_avg = round(sample_average(sepal_square), 4), round(sample_average(petal_square), 4)
        sepal_sample_var, petal_sample_var = str(round(sample_variance(sepal_square, sepal_sample_avg), 4)), str(round(sample_variance(petal_square, petal_sample_avg), 4))
        sepal_sample_median, petal_sample_median = str(round(sample_median(sepal_square), 4)), str(round(sample_median(petal_square), 4))
        sepal_sample_quantile, petal_sample_quantile = str(round(numpy.quantile(sepal_square, 0.4), 4)), str(round(numpy.quantile(petal_square, 0.4), 4))
        data_map[spec] = [str(sepal_sample_avg), str(petal_sample_avg), sepal_sample_var, petal_sample_var, sepal_sample_median, petal_sample_median, sepal_sample_quantile, petal_sample_quantile]

    return data_map

def tables_output():
    values = calculations()
    species_count = {"Setosa": len(setosa), "Versicolor": len(versicolor), "Virginica": len(virginica)}
    data = [["SPECIES", "SEPAL AVERAGE", "PETAL AVERAGE", "SEPAL VARIANCE", "PETAL VARIANCE", "SEPAL MEDIAN", "PETAL MEDIAN", "SEPAL QUANTILE", "PETAL QUANTILE"]]
    min_max_data = [["SPECIES", "COUNT"]]
    
    for spec in values:
        data.append([spec] + values[spec])
        
    for spec in species_count:
        count = [str(species_count[spec])]
        min_max_data.append([spec] + count)
    
    print("\n")
    pretty_print.print_pretty_table(min_max_data)
    print("\n\n")
    pretty_print.print_pretty_table(data)
    print("\n")

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