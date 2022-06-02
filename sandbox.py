"""
testing area
"""

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Kiwi.csv')
kiwi_weight = df['Weight(kg)']
plt.boxplot(kiwi_weight)
plt.show()
