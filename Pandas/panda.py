import pandas as pd
import matplotlib.pyplot as plt
s = pd.Series(data = [10, 5, 15, 20, 10], index = [1,2,3,4,5])
s.plot()
plt.show()