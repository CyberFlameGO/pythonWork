"""
testing area
"""

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv(r'./91264 _-_2022_-_Cricket_ODI_Dataset.csv')
weight, gender = df['Span'], df['Gender']

plt.boxplot(wg := [weight, gender])
plt.show()
