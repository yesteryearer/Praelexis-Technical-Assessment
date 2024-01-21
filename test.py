import pymc as pm
import arviz as az

# Define a simple Bayesian model
with pm.Model() as model:
    # Prior Distribution for unknown mean of a normal distribution
    mu = pm.Normal('mu', mu=0, sigma=1)

    # Likelihood (sampling distribution) of observations
    Y_obs = pm.Normal('Y_obs', mu=mu, sigma=1, observed=[-1, 0, 1])

    # Draw samples from the posterior
    trace = pm.sample(1000, return_inferencedata=True)

# Print summary statistics using ArviZ
print(az.summary(trace))

