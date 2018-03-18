import pandas, os

actualDir = os.getcwd()

print(actualDir)

df1 = pandas.read_csv("Pandas/Reference/supermarkets.csv")
df1 = df1.set_index("ID")
print(df1.loc["1":"3","City":"Country"])