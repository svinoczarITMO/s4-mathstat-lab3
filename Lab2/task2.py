import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Параметры априорного распределения
mu = 0
b = 1

# Параметры выборки
n_samples = 1000
sample_size = 10
delta = 1

# Генерация выборок и вычисление байесовских оценок
bayesian_estimates = []
for _ in range(n_samples):
    # Генерация выборки
    sample = np.random.normal(loc=mu, scale=delta, size=sample_size)
    
    # Вычисление параметров апостериорного распределения
    posterior_mu = (mu / (b ** 2) + np.mean(sample) / (delta ** 2)) / (1 / (b ** 2) + sample_size / (delta ** 2))
    posterior_sigma = np.sqrt(1 / (1 / (b ** 2) + sample_size / (delta ** 2)))
    
    # Вычисление байесовской оценки (моды апостериорного распределения)
    bayesian_estimate = posterior_mu
    bayesian_estimates.append(bayesian_estimate)

# Визуализация распределения байесовских оценок
plt.figure(figsize=(10, 6))
plt.hist(bayesian_estimates, bins=30, density=True, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Распределение байесовских оценок параметра $\\theta$')
plt.xlabel('Значение параметра $\\theta$')
plt.ylabel('Плотность вероятности')
plt.grid(True)
plt.show()
