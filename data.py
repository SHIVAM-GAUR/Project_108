import pandas as pd
import csv
import plotly.express as px
import plotly.figure_factory as ff

df  = pd.read_csv("data.csv")
mobileBrand = df["Mobile Brand"].tolist()
#print(mobileBrand)
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"],show_hist = False)
fig.show()