import numpy as np
from scipy.stats import norm

# Заданный параметр
lambda_val = 1
alpha = 0.05
sample_size = 25
experiments = 1000

sample_mean = 1 / lambda_val
sample_std_mean = 1 / (lambda_val * np.sqrt(sample_size))

z_alpha_2 = norm.ppf(1 - alpha / 2)

covered_count = 0

for _ in range(experiments):
    sample = np.random.exponential(scale=1/lambda_val, size=sample_size)
    sample_mean = np.mean(sample)
    
    lower_bound = sample_mean - z_alpha_2 * sample_std_mean
    upper_bound = sample_mean + z_alpha_2 * sample_std_mean
    
    if lower_bound <= lambda_val <= upper_bound:
        covered_count += 1

coverage_probability = covered_count / experiments

print("Асимптотический доверительный интервал уровня", 1-alpha, "для параметра lambda:", (lower_bound, upper_bound))
print("Вероятность покрытия истинного значения параметра lambda: {:.2f}".format(coverage_probability))
