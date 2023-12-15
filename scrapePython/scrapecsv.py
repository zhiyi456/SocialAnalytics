import pandas as pd
# Scraped by me
df2 = pd.read_csv("./oldtweet.csv")
# if $ in tweet, save to new df 
df = df2[df2['Tweet'].astype(str).str.contains("prize|intern")]
df.to_csv('prize.csv')
# save tweets with $ to new df
# df = df2[df2['text'].astype(str).str.contains("$")]
# print(df2.head())
