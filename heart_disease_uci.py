

import pandas as pd
import numpy as np

df = pd.read_csv("datasets/heart_disease_uci.csv")


#* 1 -Show the first 10 records.
def ques_one(df:pd.DataFrame):
    return df.head(10)
result = ques_one(df)


#* 2 -What is the total number of records in the dataset?
def ques_two(df:pd.DataFrame):
    return len(df.index)
    # return df.shape[0]
result = ques_two(df)

#* 3 -List the column names.
def ques_three(df:pd.DataFrame):
    return list(df.columns)
result = ques_three(df)


#* 4 -Calculate the average age in the "age" column.
def ques_four(df:pd.DataFrame):
    return df["age"].mean()
    # return df["age"].agg("mean")
result = ques_four(df)

#* 5 -Show the information of the youngest person.
def ques_five(df:pd.DataFrame):
    return df[df["age"] == df["age"].min()]
    # return df.sort_values(by="age").iloc[0]
result = ques_five(df)

#* 6 -Find the unique values in the "sex" column.
def ques_six(df:pd.DataFrame):
    return df[~ ( (df["sex"] == "Male") | (df["sex"] == "Female") ) ]
result = ques_six(df)

#* 7 -How many records have a "target" value of 1?
def ques_seven(df:pd.DataFrame):
    return df["num"].value_counts()[1]
result = ques_seven(df)

#* 8 -Count the number of females and males separately.
def ques_eight(df:pd.DataFrame):
    return df["sex"].value_counts()
result = ques_eight(df)

#* 9 -Who has the highest "chol" (cholesterol) value?
def ques_nine(df:pd.DataFrame):
    return df[df["chol"] == df["chol"].max()]
    # return df.sort_values(by="chol",ascending=False).iloc[0]
result = ques_nine(df)

#* 10- Find the average age of those with heart disease.
def ques_ten(df:pd.DataFrame):
    return df[~(df["num"] == 0)]["age"].mean()
    # return df[df["num"] != 0]["age"].mean()
result = ques_ten(df)

#* 11- List the records where age is greater than 50.
def ques_eleven(df:pd.DataFrame):
    return df[df["age"] > 50]
    # return df[df["age"].apply(func=lambda num: num > 50)]
result = ques_eleven(df)

#* 12- List age, sex, and thalach information of people with chest pain type "non-anginal"
def ques_twelve(df:pd.DataFrame):
    return df[df["cp"] == "non-anginal"].reindex(columns=["age","sex","thalch"])
result = ques_twelve(df)

#* 13- Filter records where "thalach" is greater than 150.
def ques_thirteen(df:pd.DataFrame):
    return df[df["thalch"] >150]
    # return df[df["thalch"].apply(func= lambda num: num > 150 )]
result = ques_thirteen(df)

#* 14- List only the first 5 people with an "fbs" value of 1.
def ques_fourteen(df:pd.DataFrame):
    return df[df["fbs"] == True].head()
result = ques_fourteen(df)

#* 15- Find the average "chol" of people without heart disease.
def ques_fiveteen(df:pd.DataFrame):
    return df[df["num"] == 0]["chol"].mean()
    # return df[df["num"] == 0].agg(Mean_of_chol = ("chol","mean"))
result = ques_fiveteen(df)

#* 16- Find people where "exang" is 1 and "oldpeak" is greater than 2.
def ques_sixteen(df:pd.DataFrame):
    return df[(df["exang"] == True) & (df["oldpeak"] > 2)]
result = ques_sixteen(df)

#* 17- Group the data by "sex" and "target".
def ques_seventeen(df:pd.DataFrame):
    return df.groupby(["sex","num"]).groups
result = ques_seventeen(df)

#* 18-Group by "thal" and find the average of "age".
def ques_eighteen(df:pd.DataFrame):
    return df.groupby("thal")["age"].agg("mean")
    # return df.groupby("thal").agg(Mean_of_age = ("age","mean"))
result = ques_eighteen(df)

#* 19- Detect missing values in the "ca" column.
def ques_nineteen(df:pd.DataFrame):
    return df[df["ca"].isnull()] 
    # return df[~(df["ca"].notnull())] 
result = ques_nineteen(df)

#* 20- What is the most frequent value in the "cp" column?
def ques_twenty(df:pd.DataFrame):
    return df["cp"].value_counts().index[0]
    # return df.value_counts(subset=["cp"]).index[0]
result = ques_twenty(df)

#* 21- Compare the average "thalach" values of people with and without heart disease
def ques_twenty_one(df:pd.DataFrame):
    return df[df["num"] == 0]["thalch"].mean() - df[~(df["num"] == 0)]["thalch"].mean() 
result = ques_twenty_one(df)

#* 22-Find the highest "oldpeak" value for records with target = 1
def ques_twenty_two(df:pd.DataFrame):
    target_1 = df[df["num"] == 1]
    return target_1[target_1["oldpeak"].max() == target_1["oldpeak"] ]
result = ques_twenty_two(df)

#* 23-Consider the correlation between the "chol" and "age" columns
def ques_twenty_three(df:pd.DataFrame):
    return df.reindex(columns=["age","chol"]).corr()
result = ques_twenty_three(df)

#* 24-Group the "age" column into 10-year intervals.
def ques_twenty_four(df:pd.DataFrame):
    ranges = np.arange(start=0,stop=110,step=10)
    df["age_range"] = pd.cut(df["age"],bins=ranges)
    return df.groupby("age_range").groups
result = ques_twenty_four(df)

#* 25- Calculate the average "thalach" for each "cp" value.
def ques_twenty_five(df:pd.DataFrame):
    return df.groupby("cp").agg(Thalch_mean = ("thalch","mean"))
result = ques_twenty_five(df)

#* 26- How can we group the data to evaluate the relationship between heart disease risk and sex?
def ques_twenty_six(df:pd.DataFrame):
    return df.groupby("sex")["num"].value_counts()
result = ques_twenty_six(df)

#* 27- Fill missing values with the mean.
def ques_twenty_seven(df:pd.DataFrame):
    df["age"] = df["age"].fillna(df["age"].mean())
    df["trestbps"] = df["trestbps"].fillna(df["trestbps"].mean())
    df["chol"] = df["chol"].fillna(df["chol"].mean())
    df["thalch"] = df["thalch"].fillna(df["thalch"].mean())
    df["oldpeak"] = df["oldpeak"].fillna(df["oldpeak"].mean())
    df["ca"] = df["ca"].fillna(df["ca"].mean())
    df["num"] = df["num"].fillna(df["num"].mean())
    return df
result = ques_twenty_seven(df)

#* 28-Sort the "thal" column by the most frequent value.
def ques_twenty_eight(df:pd.DataFrame):
    return df["thal"].value_counts().sort_values(ascending=False)
    
result = ques_twenty_eight(df)

#* 29-Suggest a method to normalize the "age" values
def ques_twenty_nine(df:pd.DataFrame):
    return (df["age"] - df["age"].min()) / (df["age"].max() - df["age"].min())
result = ques_twenty_nine(df)

#* 30- List the top 5 oldest people.
def ques_thirty(df:pd.DataFrame):
    return df.sort_values(by="age",ascending=False).head()
    # return df.reindex(index=list(df["age"].sort_values(ascending=False).head().index))
result = ques_thirty(df)



print(df)
print(result)

