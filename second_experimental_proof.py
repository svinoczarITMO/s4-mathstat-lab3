import numpy
import matplotlib.pyplot as plt
from scipy.stats import gamma

shape = 2
scale = 1

samples_size = 30

count_of_samples = 10000
samples_statistics = numpy.zeros(count_of_samples)

for i in range(count_of_samples):
    sample = numpy.random.normal(0, 0.01, samples_size)
    sample = numpy.sort(sample)
    samples_statistics[i] = samples_size * (1 - sample[len(sample)-1])
    
plt.hist(samples_statistics, bins=30, density=True, color='blue', label='n(1 - F(X_(2)))')

x = numpy.linspace(0, 10, 1000)

plt.plot(x, gamma.pdf(x, 1, scale=1), 'r-', lw=2, label='Exp(1)')

plt.title('Асимптотическая нормальность для n(1 - F(X_(2)))')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.legend()
plt.grid()
plt.show()