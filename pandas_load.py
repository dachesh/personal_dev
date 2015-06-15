import pandas as pd
import numpy as np
import scipy as sp
import matplotlib as mpl

url = "<file location>"
ttData = pd.read_csv(url, header = 0, sep="\t")

print (ttData.head())