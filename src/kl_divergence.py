from scipy.stats import entropy


def calculate_kl_div(
    pop: dict,
    sample: dict,
):
    """
    Calculates Kullback-Leibler divergence.

    Args:
        pop: population represented by dictionary where key is name
            of the category and value is number of occurances in population
        sample: sample from population represented in the same way as
            the population

    Returns:
        chi-squared test statistic and p-value
    """
    # Laplace smoothing
    for key in pop.keys():
        pop[key] += 1
        if key not in sample:
            sample[key] = 0
        sample[key] += 1

    pop_size = sum(
        list(
            map(
                lambda x: x[1],
                pop.items(),
            )
        )
    )

    sample_size = sum(
        list(
            map(
                lambda x: x[1],
                sample.items(),
            )
        )
    )
    scaled_pop = {}
    complete_sample = {}
    for cat, n in pop.items():
        scaled_pop[cat] = n / pop_size * sample_size
        if cat not in sample.keys():
            complete_sample[cat] = 0
        else:
            complete_sample[cat] = sample[cat]

    keys = sorted(scaled_pop.keys())
    values_pop = list(map(lambda x: scaled_pop[x], keys))
    values_sample = list(map(lambda x: complete_sample[x], keys))
    # usually pk is the true distribution while values sample,
    # while qk is sample/approximation distribution
    return entropy(pk=values_pop, qk=values_sample)
