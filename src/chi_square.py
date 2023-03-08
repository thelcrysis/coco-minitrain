from scipy.stats import chisquare

sample = {'82_L': 18, '6_L': 36, '1_L': 764, '1_M': 685, '27_M': 48, '1_S': 631, '62_S': 90, '3_S': 241, '10_S': 85, '42_M': 24, '42_L': 22, '31_S': 56, '6_S': 11, '75_L': 7, '4_L': 33, '35_M': 15, '19_L': 35, '19_S': 7, '19_M': 12, '62_L': 76, '73_L': 30, '67_L': 104, '25_L': 25, '70_L': 36, '81_L': 20, '16_L': 21, '44_S': 106, '62_M': 140, '47_S': 81, '73_M': 8, '74_S': 7, '78_M': 9, '79_M': 9, '81_S': 7, '27_S': 33, '51_S': 36, '72_M': 19, '86_S': 15, '17_L': 35, '39_M': 15, '38_M': 11, '77_M': 28, '8_M': 33, '41_M': 13, '54_L': 18, '48_M': 23, '49_M': 23, '49_L': 22, '3_L': 65, '3_M': 129, '4_M': 25, '4_S': 13, '79_L': 21, '47_M': 53, '51_M': 46, '32_L': 16, '51_L': 34, '72_L': 22, '65_L': 43, '75_S': 22, '5_L': 28, '37_S': 45, '85_M': 26, '38_L': 9, '90_M': 8, '60_L': 22, '60_M': 23, '60_S': 26, '27_L': 19, '7_L': 26, '33_L': 25, '33_M': 33, '76_L': 14, '21_M': 37, '21_S': 22, '21_L': 31, '34_L': 3, '87_L': 5, '64_M': 18, '31_L': 15, '31_M': 40, '48_S': 16, '44_M': 112, '49_S': 27, '59_M': 19, '59_S': 8, '17_M': 2, '63_L': 42, '11_L': 14, '88_L': 21, '50_S': 26, '55_L': 12, '2_M': 24, '15_S': 11, '41_S': 4, '28_M': 38, '28_S': 50, '15_L': 35, '9_L': 29, '9_M': 31, '9_S': 49, '81_M': 28, '90_S': 11, '18_L': 36, '14_S': 5, '46_M': 31, '64_S': 10, '85_S': 14, '11_S': 5, '14_L': 4, '32_M': 15, '39_L': 3, '75_M': 25, '84_M': 42, '7_M': 7, '22_L': 24, '38_S': 33, '64_L': 22, '32_S': 18, '63_M': 2, '47_L': 28, '2_L': 10, '22_S': 6, '22_M': 14, '15_M': 41, '24_L': 26, '46_L': 9, '50_M': 23, '67_M': 25, '34_M': 9, '61_L': 30, '76_M': 8, '43_M': 19, '43_S': 7, '37_L': 2, '41_L': 10, '35_L': 9, '8_L': 25, '20_L': 15, '20_S': 13, '20_M': 21, '53_M': 33, '56_M': 43, '56_L': 22, '56_S': 10, '77_S': 29, '53_S': 15, '85_L': 7, '77_L': 11, '36_S': 9, '28_L': 19, '58_L': 15, '2_S': 9, '59_L': 31, '61_M': 27, '37_M': 10, '54_M': 6, '36_M': 7, '55_M': 7, '52_L': 16, '87_M': 1, '50_L': 9, '18_S': 3, '43_L': 4, '48_L': 19, '57_L': 8, '13_S': 4, '23_L': 7, '86_L': 16, '86_M': 9, '16_M': 22, '16_S': 64, '13_L': 4, '10_M': 27, '84_S': 96, '40_M': 9, '40_L': 2, '36_L': 3, '46_S': 28, '52_S': 31, '55_S': 19, '54_S': 3, '67_S': 16, '84_L': 9, '5_M': 19, '44_L': 23, '74_L': 6, '24_M': 21, '53_L': 5, '88_M': 21, '18_M': 4, '58_M': 4, '33_S': 21, '25_M': 5, '6_M': 10, '39_S': 4, '40_S': 22, '34_S': 8, '70_M': 11, '52_M': 31, '13_M': 3, '8_S': 15, '57_M': 20, '65_M': 2, '42_S': 9, '82_M': 1, '17_S': 1, '88_S': 6, '87_S': 8, '72_S': 1, '76_S': 3, '78_L': 4, '57_S': 16, '74_M': 5, '10_L': 6, '35_S': 5, '23_M': 1, '14_M': 3, '70_S': 3, '89_S': 1, '73_S': 1, '5_S': 1, '61_S': 2, '78_S': 1, '7_S': 2, '25_S': 1, '58_S': 1}

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