import numpy as np
from scipy.stats import norm

mu_1 = 2
mu_2 = 1
sigma_1_squared = 1
sigma_2_squared = 0.5
alpha = 0.05
repetitions = 1000

real_tau = mu_1 - mu_2
sample_sizes = [25, 10000]

def confidence_interval(X, Y, alpha):
    n1 = len(X)
    n2 = len(Y)

    std_diff = np.sqrt(sigma_1_squared / n1 + sigma_2_squared / n2)
    standardized_diff = (np.mean(X) - np.mean(Y) - real_tau) / std_diff
    z_alpha = norm.ppf(1 - alpha / 2)
    lower_bound = standardized_diff - z_alpha
    upper_bound = standardized_diff + z_alpha
    return lower_bound, upper_bound

def experiment(mu1, mu2, alpha, sample_size, experiments):
    covered = 0
    for _ in range(experiments):
        X = np.random.normal(mu1, np.sqrt(sigma_1_squared), sample_size)
        Y = np.random.normal(mu2, np.sqrt(sigma_2_squared), sample_size)
        interval = confidence_interval(X, Y, alpha)
        if interval[0] <= 0 <= interval[1]:
            covered += 1
    coverage_probability = covered / experiments
    return coverage_probability

for sample_size in sample_sizes:
    coverage_probability = experiment(mu_1, mu_2, alpha, sample_size, repetitions)
    print(f"Для выборки объемом {sample_size}:")
    print(f"Вероятность покрытия реального значения параметра: {coverage_probability}")
