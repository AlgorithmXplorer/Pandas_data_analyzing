
import pandas as pd
import numpy as np

df = pd.read_csv("datasets/Billionaires Statistics Dataset.csv")

#* 1- Veri kümesindeki ilk 15 kaydı görüntüleyiniz.
def ques_one(df:pd.DataFrame) ->pd.DataFrame:
    return df.head(15)
result = ques_one(df)

#* 2- Veri kümesinde toplam kaç kayıt olduğunu bulunuz.
def ques_two(df:pd.DataFrame) ->pd.DataFrame:
    return len(df.index)
result = ques_two(df)

#* 3- Kaç farklı ülke (country) olduğunu hesaplayınız.
def ques_three(df:pd.DataFrame) ->pd.DataFrame:
    return df["country"].nunique()
    # return len(df["country"].value_counts().index)
result = ques_three(df)

#* 4- En genç milyarderin yaşını ve ismini bulunuz.
def ques_four(df:pd.DataFrame) ->pd.DataFrame:
    return df[df["age"].min() == df["age"]][["age","personName"]]
    # return df.sort_values(by="age").iloc[0,::][["personName","age"]]
result = ques_four(df)

#* 5- En yaşlı milyarderin yaşını ve yaşadığı şehri bulunuz.
def ques_five(df:pd.DataFrame) ->pd.DataFrame:
    return df[df["age"].max() == df["age"]][["age","city"]]
    # return df.sort_values(by="age",ascending=False).iloc[0,::][["city","age"]]
result = ques_five(df)

#* 6- Yaşı 50’den küçük olan milyarderleri listeleyiniz.
def ques_six(df:pd.DataFrame) ->pd.DataFrame:
    return df[df["age"] < 50]
result = ques_six(df)

#* 7- Yaşı 60’tan büyük ve net serveti (finalWorth) 100000’den fazla olanları filtreleyiniz.
def ques_seven(df:pd.DataFrame) ->pd.DataFrame:
    return df[(df["age"] > 60) & (df["finalWorth"] > 100000)]
result = ques_five(df)

#* 8- “France” ülkesinde yaşayan milyarderleri seçiniz.
def ques_eight(df:pd.DataFrame) ->pd.DataFrame:
    return df[df["country"] == "France"]
    # return df.groupby("country").get_group("France")
result = ques_eight(df)

#* 9- “Technology” kategorisinde olup “United States” ülkesinde yaşayanları listeleyiniz.
def ques_nine(df:pd.DataFrame) ->pd.DataFrame:
    return df[(df["category"] == "Technology") & (df["country"] == "United States")]
result = ques_nine(df)

#* 10- “selfMade” değeri True olan kayıtları seçiniz.
def ques_ten(df:pd.DataFrame) ->pd.DataFrame:
    return df[df["selfMade"]]
result = ques_ten(df)

#* 11- Serveti (finalWorth) en yüksek 10 milyarderi sıralayınız.

#* 12- En düşük net servete sahip 5 kişiyi yaşlarıyla birlikte getiriniz.

#* 13- Doğum yılı en eski olan 5 kişiyi sıralayınız.

#* 14- “country” bilgisine göre alfabetik sıralama yapınız.

#* 15- “city” bilgisinde eksik olan (NaN) kayıtları sıralayarak gösteriniz.

#* 16- Ülkelere göre milyarder sayısını hesaplayınız.

#* 17- Cinsiyete (gender) göre yaş ortalamasını bulunuz.

#* 18- category bilgisine göre ortalama finalWorth değerini hesaplayınız.

#* 19- Ülkelere göre toplam servetleri (finalWorth) toplayınız ve azalan şekilde sıralayınız.

#* 20- “Technology” kategorisindeki kişileri ülkeye göre gruplayarak her ülkede kaç kişi olduğunu gösteriniz.

#* 21- category sütununda “Finance” kelimesi geçen kayıtları listeleyiniz.

#* 22- source kolonunda “Amazon” ifadesi geçen milyarderleri bulunuz.

#* 23- personName değeri içinde “Bill” geçen kişileri filtreleyiniz.

#* 24- city bilgisi str tipinde olup uzunluğu 6 harften fazla olanları seçiniz.

#* 25- organization kolonu boş olan kayıtların sayısını bulunuz.

#* 26- birthYear bilgisi ile kişinin şu anki yaşını hesaplayarak yeni bir kolon oluşturunuz.

#* 27- finalWorth değerini milyar dolar cinsinden gösteren yeni bir kolon ekleyiniz.

#* 28- finalWorth değerine göre “Yüksek”, “Orta”, “Düşük” şeklinde kategorik bir etiket üretiniz.

#* 29- country sütunundaki her değerin yalnızca ilk 3 harfini içeren yeni bir sütun üretiniz.

#* 30- Her bireyin yaşadığı ülkenin nüfusu (population_country) ile finalWorth çarpımını gösteren bir kolon oluşturunuz.



print(df)
print(result)
