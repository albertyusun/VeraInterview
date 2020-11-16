import numpy as np
import pandas as pd

# Read Datafile
pd.set_option('display.max_columns', None)
a = pd.read_csv("rawJailDataIntern.csv")
print(a.head())

# Compare admissions and discharge on year level; drop weekly/daily

