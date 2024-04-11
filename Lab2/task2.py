import numpy as np
from scipy.stats import norm

data_samples = np.random.normal(loc=0, scale=1, size=100)

def likelihood(theta, data):
    likelihoods = [norm.pdf(x, loc=theta, scale=1) for x in data]
    return np.prod(likelihoods)

def prior(theta):
    return norm.pdf(theta, loc=0, scale=1)

def posterior(theta, data):
    return likelihood(theta, data) * prior(theta)

def normalize_posterior(theta_range, data):
    unnormalized_posterior = [posterior(theta, data) for theta in theta_range]
    normalization_constant = np.trapz(unnormalized_posterior, theta_range)
    normalized_posterior = unnormalized_posterior / normalization_constant
    return normalized_posterior

def bayesian_estimate(theta_range, posterior):
    return np.trapz(theta_range * posterior, theta_range)

theta_range = np.linspace(-10, 10, 1000)

normalized_posterior = normalize_posterior(theta_range, data_samples)

bayesian_theta_estimate = bayesian_estimate(theta_range, normalized_posterior)
print("Байесовская оценка параметра theta:", bayesian_theta_estimate)
