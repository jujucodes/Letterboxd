cd ~/code
ls
cd springboard
cd data
ls
cd Capstone2Letterboxd/
ls
cd data
ls
import pandas as pd
pd.read_csv('Horror.csv')
who
df = pd.read_csv('Horror.csv')
df.head()
df.describe()
type(df)
df.info()
df.isna()
df.isna().sum
df.isna().sum()
df.isna((axis=1))
df.isna(axis=1)
df['title'][df['director'].isna()]
df['title'][df['year'].isna()]
df[df['year'].isna()]
history
history -o
history -o -p
history -o -p -f "EDA.ipy"
history -f "EDA.py"
history
pwd
ls
history -f EDA.py
