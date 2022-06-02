"""
testing area
"""

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Kiwi.csv')
kiwi_weight, kiwi_gender = df['Weight(kg)'], df['Gender']

plt.boxplot(kiwi_wg := [kiwi_weight, kiwi_gender])
plt.show()
