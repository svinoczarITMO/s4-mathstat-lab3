import numpy as np
import matplotlib.pyplot as plt

def plot_theta_distribution(thetas, n):
    plt.figure(figsize=(10, 6))
    plt.hist(thetas, bins=20, density=True, alpha=0.6)
    plt.xlabel('Значение параметра $\\theta$')
    plt.ylabel('Плотность вероятности')
    plt.title(f'Распределение оценок параметра $\\theta$ при выборках размера {n}')
    plt.grid(True)
    plt.show()

def grade(samples, n):
    thetas, bias, vars, mses = [0] * n, [0] * n, [0] * n, [0] * n
    for i in range(n):
        thetas[i] = (np.sqrt(3*np.var(samples[i])))
        bias[i] = abs(thetas[i] - 10)
        vars[i] = np.var(thetas)
        mses[i] = np.mean((thetas[i]-10)**2)
    return thetas, bias, vars, mses


for n in range(100, 1001, 100):
    samples = np.random.uniform(low=-10, high=10, size=(n, 100))
    thetas, bias, vars, mses = grade(samples, n)
    out_of_range = []    
    for i in thetas:
        if np.abs(np.abs(i) - 10)>0.88:
            out_of_range.append(i)
    print("За границей:")
    print (out_of_range[:10])
    print("Сдвиги:")
    print (bias[:10])
    print("Дисперсии:")
    print (vars[:10])
    print("Среднеквадратичная ошибка:")
    print (mses[:10])    
    plot_theta_distribution(thetas, n)
    
