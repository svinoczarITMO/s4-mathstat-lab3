import numpy as np
from scipy.stats import norm

mu_1 = 2
mu_2 = 1
sigma_1_squared = 1
sigma_2_squared = 0.5
n = 25
m = 25
alpha = 0.05
repetitions = 1000

def confidence_interval(X, Y, alpha):
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)
    
    std_diff = np.sqrt(sigma_1_squared/n + sigma_2_squared/m)
    
    standardized_diff = (mean_X - mean_Y - (mu_1 - mu_2)) / std_diff
    
    z_alpha = norm.ppf(1 - alpha / 2)
    
    lower_bound = standardized_diff - z_alpha * std_diff
    upper_bound = standardized_diff + z_alpha * std_diff
    
    return lower_bound, upper_bound

def check_coverage(lower_bound, upper_bound):
    return 0 >= lower_bound and 0 <= upper_bound

covered_count_25 = 0
for _ in range(repetitions):
    X = np.random.normal(mu_1, np.sqrt(sigma_1_squared), n)
    Y = np.random.normal(mu_2, np.sqrt(sigma_2_squared), m)
    lower_bound, upper_bound = confidence_interval(X, Y, alpha)
    if check_coverage(lower_bound, upper_bound):
        covered_count_25 += 1

print("Для выборок объема 25:")
print(f"Количество покрывающих интервалов: {covered_count_25}/{repetitions}")
print(f"Процент покрытия: {covered_count_25 / repetitions * 100:.2f}%")

n = 10000
m = 10000
covered_count_10000 = 0
for _ in range(repetitions):
    X = np.random.normal(mu_1, np.sqrt(sigma_1_squared), n)
    Y = np.random.normal(mu_2, np.sqrt(sigma_2_squared), m)
    lower_bound, upper_bound = confidence_interval(X, Y, alpha)
    if check_coverage(lower_bound, upper_bound):
        covered_count_10000 += 1

print("\nДля выборок объема 10000:")
print(f"Количество покрывающих интервалов: {covered_count_10000}/{repetitions}")
print(f"Процент покрытия: {covered_count_10000 / repetitions * 100:.2f}%")
