
import pandas as pd
import numpy as np

df = pd.read_csv("datasets/shootings.csv")


#* 1- Display the first 10 records.
def ques_one(df:pd.DataFrame)->None:
    return df.head(10)
result = ques_one(df=df)

#* 2- How many rows and columns are in the dataset?
def ques_two(df:pd.DataFrame)->None:
    return [len(df.index),len(df.columns)]
result = ques_two(df=df)

#* 3- List all column names and their data types.
def ques_three(df:pd.DataFrame)->None:
    return df.dtypes
result = ques_three(df=df)

#* 4- In how many different cities have incidents occurred?
def ques_four(df:pd.DataFrame)->None:
    return df["city"].nunique()
result = ques_four(df=df)

#* 5- Which city has the highest number of incidents?
def ques_five(df:pd.DataFrame)->None:
    return df["city"].value_counts().index[0]
    # return df.value_counts(subset="city").index[0]
result = ques_five(df=df)

#* 6- Which state has the highest number of incidents?
def ques_six(df:pd.DataFrame)->None:
    return df["state"].value_counts().index[0]
    # return df.value_counts(subset="state").index[0]
result = ques_six(df=df)

#* 7- How many incidents occurred in each year?
def ques_seven(df:pd.DataFrame)->None:
    df["year"] = df["date"].str.split("-",expand=True)[0]
    return df["year"].value_counts()
    # return df.value_counts(subset="year")
result = ques_seven(df=df.iloc[::,::])

#* 8- Which race of people has been affected the most in these incidents?
def ques_eight(df:pd.DataFrame)->None:
    return df["race"].value_counts().index[0]
    # return df.value_counts(subset="race").index[0]
result = ques_eight(df=df)

#* 9- Display the values and counts in the “manner_of_death” column.
def ques_nine(df:pd.DataFrame)->None:
    return df["manner_of_death"].value_counts()
    # return df.value_counts(subset="manner_of_death")
result = ques_nine(df=df)

#* 10- Which type of weapon (armed) is involved in the most incidents?
def ques_ten(df:pd.DataFrame)->None:
    return df["armed"].value_counts().index[0]
    # return df.value_counts(subset="armed").index[0]
result = ques_ten(df=df)

#* 11- List the records where “manner_of_death” is “shot and Tasered”.
def ques_eleven(df:pd.DataFrame)->None:
    return df[df["manner_of_death"] == "shot and Tasered"]
    # return df.groupby("manner_of_death").get_group("shot and Tasered")
result = ques_eleven(df=df)

#* 12- Filter the people who are younger than 18 years old.
def ques_twelve(df:pd.DataFrame)->None:
    return df[df["age"] < 18]
result = ques_twelve(df=df)

#* 13- Find the average age of people whose race is “W”.
def ques_thirteen(df:pd.DataFrame)->None:
    return df[df["race"] == "White"]["age"].mean()
    # return df.groupby("race").get_group("White")["age"].mean()
    # return df.groupby("race").get_group("White").agg(Mean_age = ("age","mean"))
result = ques_thirteen(df=df)

#* 14- Find the total number of female individuals.
def ques_fourteen(df:pd.DataFrame)->None:
    return df["gender"].value_counts()["F"]
    # return len(df[df["gender"] == "F"].index)
result = ques_fourteen(df=df)

#* 15- Find the number of people who attempted to flee by car.
def ques_fiveteen(df:pd.DataFrame)->None:
    return len(df[df["flee"] == "Car"].index)
    # return df.value_counts(subset="flee")["Car"]
    # return len(df.groupby("flee").get_group("Car").index)
result = ques_fiveteen(df=df)

#* 16- Find the number of individuals with “signs_of_mental_illness” equal to True.
def ques_sixteen(df:pd.DataFrame)->None:
    return len(df[df["signs_of_mental_illness"]].index)
    # return df.value_counts(subset="signs_of_mental_illness")[True]
result = ques_sixteen(df=df)

#* 17- Calculate the percentage of unarmed individuals.
def ques_seventeen(df:pd.DataFrame)->None:
    return (len(df[df["armed"] == "unarmed"])  / len(df.index)) * 100 
result = ques_seventeen(df=df)

#* 18- Find the number of incidents where a body camera was used.
def ques_eighteen(df:pd.DataFrame)->None:
    return len(df[df["body_camera"]].index)
    # return len(df.groupby("body_camera").get_group(True))
result = ques_eighteen(df=df)

#* 19- Calculate the average age by “armed” status.
def ques_nineteen(df:pd.DataFrame)->None:
    return df.groupby("armed")["age"].mean()
    # return df.groupby("armed").agg(Mean_of_age = ("age","mean"))
result = ques_nineteen(df=df)

#* 20- Display the number of incidents by “gender” and “race” combinations.
def ques_twenty(df:pd.DataFrame)->None:
    return df.groupby(["gender","race"]).value_counts()
result = ques_twenty(df=df)

#* 21- Which “flee” type is the most common?
def ques_twenty_one(df:pd.DataFrame)->None:
    return df["flee"].value_counts().index[0]
result = ques_twenty_one(df=df)

#* 22- Display the name, age, and city of the oldest person.
def ques_twenty_two(df:pd.DataFrame)->None:
    return df[df["age"] == df["age"].max()][["name","age","city"]]
    # return df.reindex(index = [df["age"].sort_values().index[-1]] , columns= ["name","age","city"] )
result = ques_twenty_two(df=df)

#* 23- Sort the number of incidents by “state” in descending order.
def ques_twenty_three(df:pd.DataFrame)->None:
    return df["state"].value_counts()
result = ques_twenty_three(df=df)

#* 24- Analyze the relationship between “race” and “manner_of_death”.
def ques_twenty_four(df:pd.DataFrame)->None:
    return df.groupby("race")["manner_of_death"].value_counts()
result = ques_twenty_four(df=df)

#* 25- Divide the “age” column into age groups and count the number of incidents in each group.
def ques_twenty_five(df:pd.DataFrame)->None:
    bins = np.arange(10,110,10)
    labels = ["10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","90-100"]
    age_groups:pd.Series = pd.cut(x=df["age"], bins=bins,labels=labels)
    return age_groups.value_counts()
result = ques_twenty_five(df=df)

#* 26- Find the number of unarmed individuals for each year.
def ques_twenty_six(df:pd.DataFrame)->None:
    df["years"] = df["date"].str.split("-",expand=True)[0]
    groups = df.groupby("years")
    counts = {}
    for year,group in groups:
        count = group["arms_category"].value_counts()["Unarmed"]
        counts.update({year:int(count)})
    return counts
result = ques_twenty_six(df=df.loc[::,::])

#* 27- Split the “date” column into year, month, and day columns.
def ques_twenty_seven(df:pd.DataFrame)->None:
    df[["year","month","day"]] = df["date"].str.split("-",expand=True)

    # year,month,day = df["date"].str.split("-",expand=True).loc[::,0],df["date"].str.split("-",expand=True).loc[::,1],df["date"].str.split("-",expand=True).loc[::,2]
    # df["year"] = year
    # df["month"] = month
    # df["day"] = day
    return df
result = ques_twenty_seven(df=df.loc[::,::])

#* 28-Investigate whether there is a relationship between “signs_of_mental_illness” and “body_camera”.
def ques_twenty_eight(df:pd.DataFrame)->None:
    return df.groupby("signs_of_mental_illness")["body_camera"].value_counts()
result = ques_twenty_eight(df=df)

#* 29- Find the average age based on types of "flee" (method is implied).
def ques_twenty_nine(df:pd.DataFrame)->None:
    return df.groupby("flee")["age"].mean()
result = ques_twenty_nine(df=df)

#* 30- List the top 10 cities with the highest number of incidents.
def ques_thirty(df:pd.DataFrame)->None:
    return df["city"].value_counts().head(10)
    # return df.value_counts(subset=["city"]).head(10)
result = ques_thirty(df=df)


print(df)
print(result)



