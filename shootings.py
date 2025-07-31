
import pandas as pd
import numpy as np

df = pd.read_csv("datasets/shootings.csv")


#* 1- İlk 10 kaydı görüntüleyiniz.
def ques_one(df:pd.DataFrame)->None:
    return df.head(10)
result = ques_one(df=df)

#* 2- Veri setinde kaç satır ve kaç sütun vardır?
def ques_two(df:pd.DataFrame)->None:
    return [len(df.columns),len(df.index)]
result = ques_two(df=df)

#* 3- Tüm sütun adlarını ve veri tiplerini listeleyiniz.
def ques_three(df:pd.DataFrame)->None:
    return df.dtypes
result = ques_three(df=df)

#* 4- Kaç farklı şehirde (city) olay yaşanmıştır?
def ques_four(df:pd.DataFrame)->None:
    return df["city"].nunique()
result = ques_four(df=df)

#* 5- En çok olay yaşanan şehir hangisidir?
def ques_five(df:pd.DataFrame)->None:
    return df["city"].value_counts().index[0]
    # return df.value_counts(subset="city").index[0]
result = ques_five(df=df)

#* 6- En çok olay yaşanan eyalet (state) hangisidir?
def ques_six(df:pd.DataFrame)->None:
    return df["state"].value_counts().index[0]
    # return df.value_counts(subset="state").index[0]
result = ques_six(df=df)

#* 7- Hangi yıllarda kaç olay gerçekleşmiştir?
def ques_seven(df:pd.DataFrame)->None:
    df["year"] = df["date"].str.split("-",expand=True)[0]
    return df["year"].value_counts()
    # return df.value_counts(subset="year")
result = ques_seven(df=df.iloc[::,::])

#* 8- Hangi ırktan (race) kişiler bu olaylara en fazla maruz kalmıştır?
def ques_eight(df:pd.DataFrame)->None:
    return df["race"].value_counts().index[0]
    # return df.value_counts(subset="race").index[0]
result = ques_eight(df=df)

#* 9- “manner_of_death” sütunundaki değerleri ve sayılarını görüntüleyiniz.
def ques_nine(df:pd.DataFrame)->None:
    return df["manner_of_death"].value_counts()
    # return df.value_counts(subset="manner_of_death")
result = ques_nine(df=df)

#* 10- Hangi silah (armed) türü en fazla olayda yer almıştır?
def ques_ten(df:pd.DataFrame)->None:
    return df["armed"].value_counts().index[0]
    # return df.value_counts(subset="armed").index[0]
result = ques_ten(df=df)

#* 11- “manner_of_death” değeri “shot and Tasered” olan kayıtları listeleyiniz.
def ques_eleven(df:pd.DataFrame)->None:
    return df[df["manner_of_death"] == "shot and Tasered"]
    # return df.groupby("manner_of_death").get_group("shot and Tasered")
result = ques_eleven(df=df)

#* 12- Yaşı 18’den küçük olan kişileri filtreleyiniz.
def ques_twelve(df:pd.DataFrame)->None:
    return df[df["age"] < 18]
result = ques_twelve(df=df)

#* 13- “race” değeri “W” olanların yaş ortalamasını bulunuz.
def ques_thirteen(df:pd.DataFrame)->None:
    return df[df["race"] == "White"]["age"].mean()
    # return df.groupby("race").get_group("White")["age"].mean()
    # return df.groupby("race").get_group("White").agg(Mean_age = ("age","mean"))
result = ques_thirteen(df=df)

#* 14- Kadın olan kişilerin toplam sayısını bulunuz.
def ques_fourteen(df:pd.DataFrame)->None:
    return df["gender"].value_counts()["F"]
    # return len(df[df["gender"] == "F"].index)
result = ques_fourteen(df=df)

#* 15- “flee” sütununda “Car” ile kaçma girişiminde bulunanların sayısını bulunuz.
def ques_fiveteen(df:pd.DataFrame)->None:
    return len(df[df["flee"] == "Car"].index)
    # return df.value_counts(subset="flee")["Car"]
    # return len(df.groupby("flee").get_group("Car").index)
result = ques_fiveteen(df=df)

#* 16- “signs_of_mental_illness” değeri True olan kişilerin sayısını bulunuz.

#* 17- Silahsız (“unarmed”) kişilerin yüzdesini hesaplayınız.

#* 18- “body_camera” kullanılan olay sayısını bulunuz.

#* 19- “armed” durumuna göre yaş ortalamalarını hesaplayınız.

#* 20- “gender” ve “race” kombinasyonuna göre olay sayılarını görüntüleyiniz.

#* 21- Hangi “flee” türü en yaygın olandır?

#* 22- En yaşlı kişinin bilgilerini (isim, yaş, şehir) görüntüleyiniz.

#* 23- “state” sütununa göre olay sayılarını büyükten küçüğe sıralayınız.

#* 24- “race” ve “manner_of_death” ilişkisini inceleyiniz.

#* 25- “age” sütununu yaş gruplarına ayırarak her gruptaki olay sayılarını hesaplayınız.

#* 26- Her yıl için silahsız (“unarmed”) olan kişi sayısını bulunuz.

#* 27- “date” kolonunu yıl, ay, gün formatında ayırarak yeni sütunlar oluşturunuz.

#* 28- “signs_of_mental_illness” ile “body_camera” arasında bir ilişki olup olmadığını inceleyiniz (metot ima edilir).

#* 29- “age” ve “flee” türü arasında bir ilişki olup olmadığını gözlemleyin (metot ima edilir).

#* 30- En çok olay yaşanan ilk 10 şehri sıralayınız.



print(df)
print(result)



