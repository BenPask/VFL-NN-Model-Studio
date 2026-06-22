import pandas
import numpy

df = pandas.read_csv("Unsorted Data In\Copy of VFL Stat Dungeon Post-London - ELO Rating.csv", header=None)

df1 = df.iloc[6:54, numpy.r_[1, 11:14]]
print(df1)