from io import BytesIO
import statistics
import matplotlib.pyplot as plt


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


def create_histogram(growth_times):
    plt.figure()

    n, bins, patches = plt.hist(growth_times, density=True, alpha=0.75, edgecolor='black')

    plt.title('Poke Berries Growth Times')
    plt.xlabel('Growth Time')
    plt.ylabel('Frequency')

    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    plt.close()

    return buffer.getvalue()
