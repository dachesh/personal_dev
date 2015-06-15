import pandas as pd
import numpy as np
import scipy as sp
import matplotlib as mpl

url = "http://ipsdatasciencemetrics-1a-i-3fb2431f.us-east-1.amazon.com:1080/ips_tt_metrics_data"
ttData = pd.read_csv(url, header = 0, sep="\t")

print (ttData.head())