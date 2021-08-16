from mean import get_mean
from median import get_median
from mode import get_mode

mean = get_mean("SOCR-HeightWeight.csv")
median = get_median("SOCR-HeightWeight.csv")
mode = get_mode("SOCR-HeightWeight.csv")

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode:2f}")
