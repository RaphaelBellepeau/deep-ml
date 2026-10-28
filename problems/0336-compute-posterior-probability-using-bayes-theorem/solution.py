def bayes_theorem(priors: list[float], likelihoods: list[float]) -> list[float]:
	s = sum(x*y for x,y in zip(priors, likelihoods))
	return [x*y/s for x,y in zip(priors,likelihoods)]