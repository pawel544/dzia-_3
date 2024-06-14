import pandas as pd
import matplotlib.pyplot as plt

file=pd.read_csv("C:\Users\pawel\Downloads\bestsellers with categories.csv")
filee=pd.DataFrame(file)
print(filee.head()[0:6])
print(filee.shape)

missing=filee.isnull().sum(axis=1)/ len(filee)

if missing==True:
    print("tak")
else:
    print("Nie")

unique_value=filee["genre"].unique()
print(unique_value)
filee["Price"].plot( kind='hist')
min_price= filee["Price"].min()
max_price=filee["Price"].max()
mean_price=filee["Price"].mean()
median_price=filee["Price"].median()

max_rating=filee["Rating"].max()
book_with_rating= filee[filee["Rating"].max==max_rating].shape[0]
filee.loc[file["Reviews"].idxmax()]
top_50=filee[filee['data']==2015]
top_50[top_50['Price'].idxmax()]
filee[(filee["Data"]==2010& filee["Genre"]=="Fiction")].shape[0]
filee[(filee['Rating']=="4.9")& (filee["Data"].isin[2010,2011])].shape[0]
top_50[top_50["Price"<8]].sort_values(by="Price")
fikcjon=file[file["Genre"]=="Fiction"]
max_cena=fikcjon["Price"].max()
fikcjon[fikcjon['Price']==max_cena]
min_price=fikcjon["Price"].min()
fikcjon[fikcjon["Price"]==min_price]
non_fiction=filee[filee["Genre"]=="Non Fiction"]
max_non=non_fiction["Price"].max()
min_non=non_fiction["Price"].min()
non_fiction[non_fiction["Price"]==max_non]
non_fiction[non_fiction["Price"]==min_non]
n_value=filee[["Author"]]
n_column=n_value.groupby['Author'].agg({"Author":"count"}).reset_index()
n_column=["Author","Book"]
print(n_column.shape)
max_author=n_column.loc[n_column["Book"]].idmax()
print(max_author["Book"])
print(max_author["Author"])
new_value=filee[["Author","Rating"]]
new_column=new_value.groupby['Author'].agg({"Rating":"mean"}).reset_index()
new_min_rating=new_column.loc[new_value["Rating"].idxmin()]
print(new_min_rating["Author"])
print(new_min_rating["Rating"])
ne_tabel=pd.concat([max_author,new_column], axis=1)
sortowane=ne_tabel.sort_values(by="Author")
print(sortowane["Author"].head(1))
