from scipy.stats import chisquare


def calculate_chi_sqr(
    pop: dict,
    sample: dict,
) -> tuple[int, int]:
    """
    Calculates Pearson's chi-squared test.

    Args:
        pop: population represented by dictionary where key is name
            of the category and value is number of occurances in population
        sample: sample from population represented in the same way as
            the population

    Returns:
        chi-squared test statistic and p-value
    """
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
    return chisquare(values_sample, values_pop)
