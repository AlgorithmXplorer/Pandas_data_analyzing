import pandas as pd
import numpy as np 

df = pd.read_csv("datasets/global_air_quality_data_10000.csv")

#* 1- İlk 10 satırı görüntüleyiniz.
def ques_one(df:pd.DataFrame) -> None:
    return df.head(10)
    # return df.iloc[:10,::]
result = ques_one(df=df)

#* 2- Veri kümesinde toplam kaç satır (kayıt) vardır?
def ques_two(df:pd.DataFrame) -> None:
    return len(df.index)
result = ques_two(df=df)

#* 3- Veri kümesinde kaç sütun bulunmaktadır?
def ques_three(df:pd.DataFrame) -> None:
    return len(df.columns)
result = ques_three(df=df)

#* 4- Tüm sütun isimlerini listeleyiniz.
def ques_four(df:pd.DataFrame) -> None:
    return list(df.columns)
result = ques_four(df=df)

#* 5- En yüksek PM2.5 değerine sahip şehir hangisidir?
def ques_five(df:pd.DataFrame) -> None:
    return df[df["PM2.5"] == df["PM2.5"].max()]["City"]
    # return df.sort_values(by="PM2.5").iloc[-1]["City"]
result = ques_five(df=df)

#* 6- Ortalama PM10 değeri kaçtır?
def ques_six(df:pd.DataFrame) -> None:
    return df["PM10"].mean()
    # return df.agg(mean_of_PM10 = ("PM10","mean"))
result = ques_six(df=df)

#* 7- En düşük NO2 değerine sahip şehir hangisidir?
def ques_seven(df:pd.DataFrame) -> None:
    return df[df["NO2"] == df["NO2"].min()]["City"]
    # return df.sort_values(by="NO2").iloc[-1]["City"]
result = ques_seven(df=df)

#* 8- Ortalama CO değeri kaçtır?
def ques_eight(df:pd.DataFrame) -> None:
    return df["CO"].mean()
    # return df.agg(mean_of_CO = ("CO","mean"))
result = ques_eight(df=df)

#* 9- Ortalama sıcaklık (Temperature) kaçtır?
def ques_nine(df:pd.DataFrame) -> None:
    return df["Temperature"].mean()
    # return df.agg(mean_of_Temperature = ("Temperature","mean"))
result = ques_nine(df=df)

#* 10- En yüksek sıcaklığa sahip ülke hangisidir?
def ques_ten(df:pd.DataFrame) -> None:
    return df[df["Temperature"] == df["Temperature"].max()]["Country"]
    # return df.sort_values(by="Temperature").iloc[-1]["Country"]
result = ques_ten(df=df)

#* 11- PM2.5 değeri 100’den büyük olan şehirleri listeleyiniz.
def ques_eleven(df:pd.DataFrame) -> None:
    return df[df["PM2.5"] > 100]["Country"].index
result = ques_eleven(df=df)

#* 12- CO değeri 5’ten büyük olan kaç satır vardır?
def ques_twelve(df:pd.DataFrame) -> None:
    return len(df[df["CO"] > 5].index)
result = ques_twelve(df=df)

#* 13- O3 değeri 100’ün üzerinde olan şehirlerin isimlerini ve tarihlerini listeleyiniz.
def ques_thirteen(df:pd.DataFrame) -> None:
    return df[df["O3"] > 100].reindex(columns=["City","Date"])
result = ques_thirteen(df=df)

#* 14- “Istanbul” şehrine ait tüm kayıtları filtreleyiniz.
def ques_fourteen(df:pd.DataFrame) -> None:
    return df[df["City"] == "Istanbul"]
result = ques_fourteen(df=df)

#* 15- Sıcaklığı 15°C’nin altında ve nemi 60’ın üzerinde olan şehirleri listeleyiniz.
def ques_fiveteen(df:pd.DataFrame) -> None:
    return df[(df["Temperature"] < 15) & (df["Humidity"] > 60)]["City"]
result = ques_fiveteen(df=df)

#* 16- Her ülkenin ortalama PM2.5 değerini hesaplayınız.
def ques_sixteen(df:pd.DataFrame) -> None:
    return df.groupby("Country")["PM2.5"].mean()
result = ques_sixteen(df=df)

#* 17- Her ülke için en yüksek SO2 değerini bulunuz.
def ques_seventeen(df:pd.DataFrame) -> None:
    return df.groupby("Country")["SO2"].max()
result = ques_seventeen(df=df)

#* 18- Her şehir için ortalama sıcaklık değerini listeleyiniz.
def ques_eightteen(df:pd.DataFrame) -> None:
    return df.groupby("City")["Temperature"].mean()
result = ques_eightteen(df=df)

#* 19- Her ülke için kaç farklı şehir ölçüm yapılmıştır?
def ques_nineteen(df:pd.DataFrame) -> None:
    return df.groupby("Country")["City"].nunique()
result = ques_nineteen(df=df)

#* 20- Her ülke için ortalama nem (Humidity) değerini sıralayınız.
def ques_nineteen(df:pd.DataFrame) -> None:
    return df.groupby("Country")["City"].nunique()
result = ques_nineteen(df=df)

#* 21- Şehir adında “new” kelimesi geçen kayıtları listeleyiniz.

#* 22- “Rio” ile başlayan şehirlerin CO ve NO2 değerlerini görüntüleyiniz.

#* 23- Şehir adının uzunluğu 7 harften fazla olanları listeleyiniz.

#* 24- Hangi tarihte ölçülen PM10 ortalaması en yüksektir?

#* 25- 2023 yılı Mart ayında ölçülen tüm şehirlerin ortalama sıcaklık değerini bulunuz.

#* 26- 2023 yılına ait ölçüm verilerinde toplam kaç farklı şehir bulunmaktadır?

#* 27- Veri kümesinde eksik (NaN) değer içeren kaç satır vardır?

#* 28- Hangi sütunlarda eksik veri (NaN) bulunmaktadır?

#* 29- Tüm numerik sütunların veri tiplerini listeleyiniz.

#* 30- “Wind Speed” sütunundaki boş değerleri ortalama değer ile doldurunuz. (imalı özel metot içeriyor)


print(df)
print(result)
