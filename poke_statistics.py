import statistics


def calculate_statistics(growth_times):
    min_growth_time = min(growth_times)
    max_growth_time = max(growth_times)
    mean_growth_time = statistics.mean(growth_times)
    median_growth_time = statistics.median(growth_times)
    variance_growth_time = statistics.variance(growth_times)
    frequency_growth_time = {time: growth_times.count(time) for time in set(growth_times)}

    return {
        "min_growth_time": min_growth_time,
        "median_growth_time": median_growth_time,
        "max_growth_time": max_growth_time,
        "variance_growth_time": variance_growth_time,
        "mean_growth_time": mean_growth_time,
        "frequency_growth_time": frequency_growth_time
    }