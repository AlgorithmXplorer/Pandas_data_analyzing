

import pandas as pd
import numpy as np

df = pd.read_csv("datasets/CO2 Emissions_Canada.csv")

#*1- İlk 10 satırı görüntüleyiniz.
def ques_one(df:pd.DataFrame):
    return df.head(10)
result = ques_one(df) 

#*2- Kaç satır ve kaç sütun vardır?
def ques_two(df:pd.DataFrame):
    return f"row count:{df.shape[0]}  ///  column count:{df.shape[1]}"
result = ques_two(df) 

#*3- Sütun adlarını ve veri türlerini listeleyiniz.
def ques_three(df:pd.DataFrame):
    return df.dtypes
result = ques_three(df) 

#*4- "CO2 Emissions(g/km)" ortalamasını bulunuz.
def ques_four(df:pd.DataFrame):
    return df["CO2 Emissions(g/km)"].mean()
    # return df.agg(mean = ("CO2 Emissions(g/km)","mean"))
result = ques_four(df) 

#*5- En yüksek karbon salımı yapan araç hangisidir?
def ques_five(df:pd.DataFrame):
    return df[df["CO2 Emissions(g/km)"] == df["CO2 Emissions(g/km)"].max()]
result = ques_five(df) 

#*6- "Make" (marka) sütunundaki eşsiz marka sayısını bulunuz.
def ques_six(df:pd.DataFrame):
    return df["Make"].nunique()
result = ques_six(df) 

#*7- En çok modele sahip olan marka nedir?
def ques_seven(df:pd.DataFrame):
    return df.groupby("Make")["Model"].value_counts(ascending=False).sort_values().index[-1]
result = ques_seven(df) 

#*8- "Fuel Type" bazında araç sayılarını bulunuz.
def ques_eight(df:pd.DataFrame):
    return df["Fuel Type"].value_counts()
result = ques_eight(df) 

#*9- "Transmission" değerinde en çok kullanılan tür hangisidir?
def ques_nine(df:pd.DataFrame):
    return df["Transmission"].value_counts(ascending=False).index[0]
result = ques_nine(df) 

#*10- Ortalama motor hacmini ("Engine Size(L)") hesaplayınız.
def ques_ten(df:pd.DataFrame):
    return df["Engine Size(L)"].mean()
result = ques_ten(df) 

#*11- "Fuel Type" = "D" (dizel) olan araçları listeleyiniz.
def ques_eleven(df:pd.DataFrame):
    return df[df["Fuel Type"] == "D"]
    # return df.groupby("Fuel Type").get_group("D")
result = ques_eleven(df) 

#*12- Karbon salımı 200 g/km’nin üzerinde olanları filtreleyiniz.
def ques_twelve(df:pd.DataFrame):
    return df[df["CO2 Emissions(g/km)"] > 200]
result = ques_twelve(df) 

#*13- "Cylinders" değeri 8 olan araçları seçiniz.
def ques_thirteen(df:pd.DataFrame):
    return df[df["Cylinders"] == 8]
    # return df.groupby("Cylinders").get_group(8)
result = ques_thirteen(df) 

#*14- "Transmission" sütununda geçen farklı şanzıman türlerini listeleyiniz 
#*    ve her bir türden kaç adet bulunduğunu sayınız.
def ques_fourteen(df:pd.DataFrame):
    return df["Transmission"].value_counts()
result = ques_fourteen(df) 

#*15- "Fuel Consumption City (L/100 km)" değeri en yüksek olan ilk 5 aracı listeleyiniz.
def ques_fiveteen(df:pd.DataFrame):
    return df.sort_values(by="Fuel Consumption City (L/100 km)").tail()
    # return df.reindex(index=list(df["Fuel Consumption City (L/100 km)"].sort_values().tail().index))
result = ques_fiveteen(df) 

#*16- Motor hacmi 2.5L’den büyük olan araçları seçiniz.

#*17- "Fuel Type" ve "CO2 Emissions" ilişkisini analiz ediniz.

#*18- Ortalama "Fuel Consumption Hwy" değerine göre sıralayınız.

#*19- Tüm "Make" değerleri için ortalama karbon salımını hesaplayınız.

#*20- 4 silindirli araçların ortalama motor hacmi nedir?

#*21- "Make" ve "Fuel Type" bazında gruplama yaparak CO2 ortalamasını çıkarınız.

#*22- Her "Transmission" türü için ortalama yakıt tüketimini hesaplayınız.

#*23- En verimli araçları bulmak için nasıl bir metrik kullanılabilir? (metot ima edilir)

#*24- CO2 değeri en düşük 10 aracı sıralayınız.

#*25- "CO2 Emissions" değerini normalize ediniz.

#*26- Eksik veri olup olmadığını kontrol ediniz.

#*27- "Fuel Type" bazında en yüksek karbon salan 3 aracı bulunuz.

#*28- "Engine Size" ve "Fuel Consumption" arasındaki ilişkiyi nasıl incelersiniz? (metot ima edilir)

#*29- "Cylinders" sütununu histogram gibi bir dağılımla temsil etmek isterseniz hangi analiz uygundur? (metot ima edilir)

#*30- Tüm araçlardan şehirde en verimli olanları (en az tüketen) filtreleyiniz.


print(df)
print(result)

