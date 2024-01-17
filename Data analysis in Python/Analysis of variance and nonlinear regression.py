import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns


dane=pd.read_csv("http://theta.edu.pl/wp-content/uploads/2020/10/genomes.csv", sep=';')

dane.head()

dane.rename(columns={'temp.group':"temp_group"}, inplace=True)
dane['GC'] = dane["GC"].replace(0, np.nan)
dane['size'] = dane['size'].replace('.', np.nan)

dane=dane.dropna()
dane.head()
dane.dtypes
dane["size"]=dane["size"].astype("float")
dane.loc[:, dane.dtypes == "object"] = \
dane.select_dtypes(["object"]).apply(lambda x: x.astype('category'))

dane.dtypes 

plt.figure(figsize=(10, 6))
sns.boxplot(x='GC', y='habitat', data=dane)
plt.title('Różnice w rozkładzie zmiennej GC w zależności od miejsca bytowania')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='GC', y='temp_group', data=dane)
plt.title('Różnice w rozkładzie zmiennej GC w zależności od zakresu temperatury')
plt.show()

model=sm.formula.ols("GC~habitat+temp_group", data=dane).fit()
anova.table = sm.stats.anova_lm(model)
print(anova.table)

from statsmodels.stats.multpicomp import pairwise_tukeyhsd
tukey=pairwise_tukeyhsd(dane['GC'], dane["habitat"])
print(tukey)

dane2=pd.read_csv("http://theta.edu.pl/wp-content/uploads/2023/11/diabetes.csv", sep=',')
dane2.head()
dane2=dane2.dropna()
dane2.head()
dane2['diabetes']=dane2['diabetes'].replace('neg',0)
dane2['diabetes']=dane2['diabetes'].replace('pos',1)
dane2.head()

from sklearn.model_selection import train_test_split

train, test = train_test_split(dane2, train_size=0.75)

liczba_obserwacji_uczacy = len(train)
liczba_obserwacji_testowy = len(test)

print("Liczba obserwacji w zbiorze uczącym:", liczba_obserwacji_uczacy)
print("Liczba obserwacji w zbiorze testowym:", liczba_obserwacji_testowy)

x=np.array(train[['pregnant',	'glucose',	'pressure',	'triceps',	'insulin',	'mass',	'age']])

y=np.array(train["diabetes"])

x=sm.add_constant(x)

model1=sm.GLM(y,x, family=sm.families.Binomial())
wynik1=model1.fit()
wynik1.summary()

x=np.array(train[['pregnant',	'glucose','triceps',	'insulin',	'mass',	'age']])

y=np.array(train["diabetes"])

x=sm.add_constant(x)

model2=sm.GLM(y,x, family=sm.families.Binomial())
wynik2=model2.fit()
wynik2.summary()

x=np.array(train[['glucose','triceps',	'insulin',	'mass',	'age']])

y=np.array(train["diabetes"])

x=sm.add_constant(x)

model3=sm.GLM(y,x, family=sm.families.Binomial())
wynik3=model3.fit()
wynik3.summary()

x=np.array(train[['glucose','triceps','mass',	'age']])

y=np.array(train["diabetes"])

x=sm.add_constant(x)

model4=sm.GLM(y,x, family=sm.families.Binomial())
wynik4=model4.fit()
wynik4.summary()

x=np.array(train[['glucose','mass',	'age']])

y=np.array(train["diabetes"])

x=sm.add_constant(x)

model5=sm.GLM(y,x, family=sm.families.Binomial())
wynik5=model5.fit()
wynik5.summary()

xp=np.array(test[['glucose','mass',	'age']])
xp=sm.add_constant(xp)
y=wynik5.predict(xp)

y[1:10]

pred_class=np.where(y>0.5,1,0)
np.mean(pred_class==test['diabetes'])