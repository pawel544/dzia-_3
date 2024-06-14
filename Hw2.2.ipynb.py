import pandas as pd

file= pd.read_csv("C:\Users\pawel\Downloads\2017_jun_final - 2017_jun_final.csv")
filee=pd.DataFrame(file)
file_read=filee.head()
print(filee.shape)
print(filee.dtypes)
th=filee.replace(" ",pd.nan)
sum=th.isnull().sum()/ len(th)
column=[filee for fil in filee.columns if " " and fil in fil!="Język programowania"]
filee.drop(columns=column, inplace=True)
ht= filee.replace(" ", pd.nan)
su=ht.isnull().sum()/ len(ht)
filee.dropna(inplace=True)
print(filee.shape)
python_data= filee[filee["Język programowania"]=="Python"]
print(python_data.shape)
grupy=python_data.groupby["Stanowisko"].mean()
price=grupy.agg({"Wynagrodzenie.za.miesiąc":["min", "max"]})
python_data["avg"]=python_data["Wynagrodzenie.za.miesiąc"].apply(fill_avg_salary)
status=python_data.describe()
python_data.to_csv()
