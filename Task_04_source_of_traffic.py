def bayes_source(prior_probs, conversion_rates):     # Tasks 4.3 & 4.4
    """
    prior_probs: list[float]  -> P(H_i)
    conversion_rates: list[float] -> P(A|H_i)
    returns: list[float] -> P(H_i|A)
    """
    if len(prior_probs) != len(conversion_rates):
        raise ValueError("Списки повинні мати однакову довжину.")

    if not prior_probs:
        raise ValueError("Списки мають бути непорожніми.")

    # Ваги: P(H_i) * P(A|H_i)
    weights = [p * r for p, r in zip(prior_probs, conversion_rates)]
    total = sum(weights)

    if total == 0:
        raise ValueError("Total probability of purchase is zero (all conversions are 0).")

    posteriors = [w / total for w in weights]
    return posteriors


# Приклад зі значеннями з умови
priors = [0.50, 0.30, 0.20]
rates  = [0.04, 0.02, 0.08]
print(bayes_source(priors, rates))

# -> [0.47619047619047616, 0.14285714285714285, 0.38095238095238093]
