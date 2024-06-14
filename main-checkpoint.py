import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as pyl



url="https://en.wikipedia.org/wiki/Demographics_of_Ukraine"
response= requests.get(url)
soup=BeautifulSoup(response.text, 'lxml')
wiki=soup.find_all('table', class_="wikitable sortable")
for trol in wiki:
    thl=[]
    gnom=trol.find_all('tr')
    for gnol in gnom[0].find_all('th'):
        thl.append(gnol.text.strip())
        tabele={tehel:[]  for tehel in thl}


    for angel in gnom[1:]:
        tp=angel.find_all('td')
        if len(tp)==len(thl):
            for th, tpl in zip(thl,tp ):
                tabele[th].append(tpl.text.strip())


wiersze= pd.DataFrame(tabele)
wiersz=pd.concat([wiersze, wiersze], ignore_index=True)
wp=wiersz.replace("-",pd.NA, inplace=True)
tlc=wiersz.head()[0:1]

wiersz.fillna(0, inplace=True)
print(wiersz.dtypes)
value=wiersz.isnull().sum()
new_wiersz=wiersz.drop([6])
print(new_wiersz)
wiersz.fillna(wiersz.mean(), inplace=True)
print(wiersz)

age=wiersz['Birth rate 2019'].mean()
age_Ukrain=wiersz[wiersz['Birth rate 2019']>[age]]
max20024=wiersz.loc[wiersz['Birth rate 2019'].idxmax()]
plt.ylabel('Birth rate 2019',fontdict="small",)
