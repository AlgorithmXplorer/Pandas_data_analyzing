
import pandas as pd
import numpy as np

df = pd.read_csv("datasets/AMZN_stock_data.csv")



#* 1- İlk 10 satırı görüntüleyiniz.
def ques_one(df:pd.DataFrame) ->None:
    return df.head(10)
result = ques_one(df=df)

#* 2- Toplam kaç kayıt bulunmaktadır?
def ques_two(df:pd.DataFrame) ->None:
    return len(df.index)
result = ques_two(df=df)

#* 3- Sütun isimlerini ve türlerini yazdırınız.
def ques_three(df:pd.DataFrame) ->None:
    return df.dtypes
result = ques_three(df=df)

#* 4- "Close" sütununun ortalamasını hesaplayınız.
def ques_four(df:pd.DataFrame) ->None:
    return df["Close"].mean()
result = ques_four(df=df)

#* 5- "Volume" sütunundaki maksimum değeri bulunuz.
def ques_five(df:pd.DataFrame) ->None:
    return df["Volume"].max()
result = ques_five(df=df)

#* 6- "High" sütunu en yüksek olan günü bulunuz.
def ques_six(df:pd.DataFrame) ->None:
    return df[df["High"] == df["High"].max()]["Date"].str[8:10]

    # df["Date"] = df["Date"].str.split(" ")
    # df["Date"] = df["Date"].str[0]
    # df["Date"] = df["Date"].str.split("-")
    # return df[df["High"] == df["High"].max()]["Date"].str[2]
result = ques_six(df=df.loc[:,:])

#* 7- "Date" kolonundaki başlangıç ve bitiş tarihini yazınız.
def ques_seven(df:pd.DataFrame) ->None:
    return [df["Date"].iloc[0], df["Date"].iloc[-1]]
result = ques_seven(df=df.loc[:,:])

#* 8- Hangi gün işlem hacmi (volume) en düşüktür?
def ques_eight(df:pd.DataFrame) ->None:
    # df["Date"] = df["Date"].str.split(" ")
    # df["Date"] = df["Date"].str[0]
    # df["Date"] = df["Date"].str.split("-")

    return df[df["Volume"] == df["Volume"].min()]["Date"].str[2]
result = ques_eight(df=df.loc[:,:])

#* 9- Ortalama "Open" ve "Close" değerleri arasındaki fark nedir?
def ques_nine(df:pd.DataFrame) ->None:
    return df["Open"].mean() - df["Close"].mean()
result = ques_nine(df=df.loc[:,:])

#* 10- "Adj Close" sütunu ile "Close" arasında fark var mı?
def ques_ten(df:pd.DataFrame) ->None:
    df["Adj_Close_Approx"] = (df["Close"] - df["Dividends"]) / (df["Stock Splits"].replace(0, 1))
    return df["Adj_Close_Approx"] - df["Close"]
result = ques_ten(df=df.loc[:,:])

#* 11- "Close" değeri 3000'in üzerinde olan kayıtları listeleyiniz.
def ques_eleven(df:pd.DataFrame) ->None:
    return df[df["Close"] > 3000]
result = ques_eleven(df=df.loc[:,:])

#* 12- 2021 yılına ait verileri filtreleyiniz.
def ques_twelve(df:pd.DataFrame) ->None:
    df["Year"] = df["Date"].str[:4]
    return df[df["Year"] == "2021"]
result = ques_twelve(df=df.loc[:,:])

#* 13- 2020 yılının ocak ayına ait kapanış fiyatlarını getiriniz.
def ques_thirteen(df:pd.DataFrame) ->None:
    return df[df["Date"].str[:7] == "2020-01"]["Close"]
result = ques_thirteen(df=df.loc[:,:])

#* 14- Volume’ değeri 50 milyonun altında olan günlerin tarihlerini ve o günkü ‘Close’ fiyatlarını listeleyiniz
def ques_fourteen(df:pd.DataFrame) ->None:
    return df[df["Volume"] < 50000000].reindex(columns=["Date","Close"])
result = ques_fourteen(df=df.loc[:,:])

#* 15- 2022 yılında en yüksek kapanış fiyatı hangi gün gerçekleşmiştir?


#* 16- "Volume" değeri 5 milyondan büyük olanları bulunuz.

#* 17- Belirli bir tarih aralığını (örneğin: 2020-06-01 - 2020-12-31) filtreleyiniz.

#* 18- "Low" değeri ile "Open" arasındaki farkın en fazla olduğu günü listeleyiniz.

#* 19- "Close" ve "Open" korelasyon katsayısını hesaplayınız. (metot ima edilir)

#* 20- 2021 yılında ay bazında ortalama hacim değişimini gösteriniz.

#* 21- Her yıl için ortalama kapanış değerini listeleyiniz.

#* 22- Ay bazında "High" değerlerinin maksimumunu gösteriniz.

#* 23- Yıllık minimum kapanış değerlerini sıralayınız.

#* 24- Her yılın en yüksek hacimli gününü bulunuz.

#* 25- Hacim değerini yüzdesel olarak normalize ediniz. (metot ima edilir)

#* 26- Eksik veri olup olmadığını tespit ediniz.

#* 27- Kapanış fiyatı eksik olan varsa önceki günle doldurunuz.

#* 28- İlk 30 günün 5 günlük hareketli ortalamasını hesaplayınız.

#* 29- "High" ve "Low" arasındaki farkı yeni bir sütuna yazınız.

#* 30- En istikrarlı fiyat dönemini belirlemek için nasıl bir analiz yapılabilir? (metot ima edilir)



print(df)
print(result)

