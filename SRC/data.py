import pandas as pd
from datetime import datetime

df = pd.read_csv("data.csv", sep=";")

df['timestamp'] = df['timestamp'].apply(lambda x: datetime.fromtimestamp(x))


print(df)


def group_weekly(df, startDate, endDate):

    df_filtered = df[(df.index < endDate) & (df.index > startDate)]

    df
