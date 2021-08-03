import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("datasrc.csv")
figure = ff.create_distplot([df["Avg_Rating"].tolist()], ["Rating"], show_hist=False)
figure.show()