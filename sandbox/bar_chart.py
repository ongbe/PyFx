import numpy as np
from matplotlib import pyplot as plt
import data_aggregation.ticks_csv_parser as tcp
import data_structuring.frame_class as fc
x = fc.only_working_days(tcp.parse_csv_metatrader("EURUSD1.csv"))

#OY = np.array(fc.cut_by_OC_point(x, threshold=x.get_average_range()*0.5).get_HL_distribution())
#OY = np.array(x.get_HL_distribution())
#print(OY)
OY = x.get_minutely_distribution()
OX = range(len(OY))
fig = plt.figure()

width = 0.35
ind = np.arange(len(OY))
print(OY)
plt.bar(ind, OY)
plt.xticks(ind + width / 2, OX)
plt.grid()
fig.autofmt_xdate()

plt.show()

