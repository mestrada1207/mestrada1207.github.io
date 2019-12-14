import pandas as pd

df = pd.read_csv("Resources/cities.csv")

htmlTable = df.to_html()

f = open("cities.html", "w")
f.write(htmlTable)
f.close()
