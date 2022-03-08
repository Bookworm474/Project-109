import pandas as pd
import statistics as st

df = pd.read_csv("data.csv")
data = df["reading score"].tolist()

mean = st.mean(data)
median = st.median(data)
mode = st.mode(data)
sd = st.stdev(data)
print(mean, median, mode, sd)

sd1_start, sd1_end = mean - sd, mean + sd
sd2_start, sd2_end = mean - (2 * sd), mean + (2 * sd)
sd3_start, sd3_end = mean - (3 * sd), mean + (3 * sd)

sd1 = [result for result in data if result > sd1_start and result < sd1_end]
sd2 = [result for result in data if result > sd2_start and result < sd2_end]
sd3 = [result for result in data if result > sd3_start and result < sd3_end]

print("{}% of data lies within SD1".format(len(sd1) * 100.0 / len(data)))
print("{}% of data lies within SD2".format(len(sd2) * 100.0 / len(data)))
print("{}% of data lies within SD3".format(len(sd3) * 100.0 / len(data)))