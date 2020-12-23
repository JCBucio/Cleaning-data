import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

files = glob.glob('states*.csv')

df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)

us_census = pd.concat(df_list)

us_census.Income = us_census['Income'].replace('[\$,]', '', regex=True)
us_census.Income = pd.to_numeric(us_census.Income)

gender_split = us_census.GenderPop.str.split('_')
us_census['Men'] = gender_split.str.get(0)
us_census['Women'] = gender_split.str.get(1)

us_census['Men'] = us_census.Men.str[:-1]
us_census['Women'] = us_census.Women.str[:-1]

us_census.Men = pd.to_numeric(us_census.Men)
us_census.Women = pd.to_numeric(us_census.Women)

us_census = us_census.fillna(value={
'Women': us_census.TotalPop - us_census.Men})

duplicates = us_census.duplicated(subset=['State'])
us_census = us_census.drop_duplicates()

plt.scatter(us_census['Women'], us_census['Income'], color=['blue', 'red'])
plt.xlabel('Women')
plt.ylabel('Income')
plt.show()
plt.cla()

us_census['Hispanic'] = us_census.Hispanic.str[:-1]
us_census['Hispanic'] = pd.to_numeric(us_census.Hispanic)
us_census['White'] = us_census.White.str[:-1]
us_census['White'] = pd.to_numeric(us_census.White)
us_census['Black'] = us_census.Black.str[:-1]
us_census['Black'] = pd.to_numeric(us_census.Black)
us_census['Native'] = us_census.Native.str[:-1]
us_census['Native'] = pd.to_numeric(us_census.Native)
us_census['Asian'] = us_census.Asian.str[:-1]
us_census['Asian'] = pd.to_numeric(us_census.Asian)
us_census['Pacific'] = us_census.Pacific.str[:-1]
us_census['Pacific'] = pd.to_numeric(us_census.Pacific)

us_census = us_census.fillna(value={
'Hispanic': us_census.Hispanic.mean(),
'White': us_census.White.mean(),
'Black': us_census.Black.mean(),
'Native': us_census.Native.mean(),
'Asian': us_census.Asian.mean(),
'Pacific': us_census.Pacific.mean(),
})

plt.hist(us_census['Hispanic'])
plt.title('Hispanic')
plt.show()
plt.cla()

plt.hist(us_census['White'])
plt.title('White')
plt.show()
plt.cla()

plt.hist(us_census['Black'])
plt.title('Black')
plt.show()
plt.cla()

plt.hist(us_census['Native'])
plt.title('Native')
plt.show()
plt.cla()

plt.hist(us_census['Pacific'])
plt.title('Pacific')
plt.show()
plt.cla()

plt.hist(us_census['Asian'])
plt.title('Asian')
plt.show()

print(us_census.head())
print(us_census.columns)
print(us_census.dtypes)
