
import pandas as pd
import numpy as np

df = pd.read_csv("datasets/Billionaires Statistics Dataset.csv")

#* 1- Show the top 15 rows of the dataset.
def ques_one(df:pd.DataFrame) ->pd.DataFrame:
    return df.head(15)
result = ques_one(df)

#* 2- Find the total number of records in the dataset.
def ques_two(df:pd.DataFrame) ->pd.DataFrame:
    return len(df.index)
result = ques_two(df)

#* 3- Calculate how many unique countries are present.
def ques_three(df:pd.DataFrame) ->pd.DataFrame:
    return df["country"].nunique()
    # return len(df["country"].value_counts().index)
result = ques_three(df)

#* 4- Find the age and name of the youngest billionaire.
def ques_four(df:pd.DataFrame) ->pd.DataFrame:
    return df[df["age"].min() == df["age"]][["age","personName"]]
    # return df.sort_values(by="age").iloc[0,::][["personName","age"]]
result = ques_four(df)

#* 5- Find the age and city of the oldest billionaire.
def ques_five(df:pd.DataFrame) ->pd.DataFrame:
    return df[df["age"].max() == df["age"]][["age","city"]]
    # return df.sort_values(by="age",ascending=False).iloc[0,::][["city","age"]]
result = ques_five(df)

#* 6- List the billionaires under the age of 50.
def ques_six(df:pd.DataFrame) ->pd.DataFrame:
    return df[df["age"] < 50]
result = ques_six(df)

#* 7- Filter those older than 60 with a net worth over 100,000.
def ques_seven(df:pd.DataFrame) ->pd.DataFrame:
    return df[(df["age"] > 60) & (df["finalWorth"] > 100000)]
result = ques_seven(df)

#* 8- Select the billionaires living in France.
def ques_eight(df:pd.DataFrame) ->pd.DataFrame:
    return df[df["country"] == "France"]
    # return df.groupby("country").get_group("France")
result = ques_eight(df)

#* 9- List those in the "Technology" category who live in the United States.
def ques_nine(df:pd.DataFrame) ->pd.DataFrame:
    return df[(df["category"] == "Technology") & (df["country"] == "United States")]
result = ques_nine(df)

#* 10- Select records where "selfMade" is True.
def ques_ten(df:pd.DataFrame) ->pd.DataFrame:
    return df[df["selfMade"]]
result = ques_ten(df)

#* 11- List the top 10 billionaires with the highest finalWorth.
def ques_eleven(df:pd.DataFrame) ->pd.DataFrame:
    return df.sort_values(by="finalWorth").tai(10)
    # return df.reindex(index=list(df["finalWorth"].sort_values(ascending=False).head(10).index))
result = ques_eleven(df)

#* 12- Show the 5 people with the lowest net worth along with their age.
def ques_twelve(df:pd.DataFrame) ->pd.DataFrame:
    return df.sort_values(by="finalWorth").head().reindex(columns=["age","personName"])
result = ques_twelve(df)

#* 13- List the 5 people with the oldest birth years.
def ques_thirteen(df:pd.DataFrame) ->pd.DataFrame:
    return df.sort_values(by="birthYear").head(5)
result = ques_thirteen(df)

#* 14- Sort the data alphabetically by the "country" column.
def ques_fourteen(df:pd.DataFrame) ->pd.DataFrame:
    return df.sort_values(by="country")
result = ques_fourteen(df)

#* 15- Show the records where the "city" information is missing (NaN).
def ques_fiveteen(df:pd.DataFrame) ->pd.DataFrame:
    return df[df["city"].isnull()]
result = ques_fiveteen(df)

#* 16- Count the number of billionaires per country.
def ques_sixteen(df:pd.DataFrame) ->pd.DataFrame:
    return df.value_counts(subset=["country"])
result = ques_sixteen(df)

#* 17- Find the average age grouped by gender.
def ques_seventeen(df:pd.DataFrame) ->pd.DataFrame:
    return df.groupby("gender")["age"].mean()
result = ques_seventeen(df)

#* 18- Calculate the average finalWorth by category.
def ques_eighteen(df:pd.DataFrame) ->pd.DataFrame:
    return df.groupby("category")["finalWorth"].mean()
result = ques_eighteen(df)

#* 19- Sum the finalWorth by country and sort in descending order.
def ques_nineteen(df:pd.DataFrame) ->pd.DataFrame:
    return df.groupby("country")["finalWorth"].sum().sort_values()
result = ques_nineteen(df)

#* 20- For the "Technology" category, group by country and show how many people are in each.
def ques_twenty(df:pd.DataFrame) ->pd.DataFrame:
    return df[df["category"] == "Technology"].value_counts("country")
result = ques_twenty(df)

#* 21- List records where the category column contains the word “Finance”.
def ques_twenty_one(df:pd.DataFrame) ->pd.DataFrame:
    return df[df["category"] == "Finance & Investments"]
    # return df.groupby("category").get_group("Finance & Investments")
result = ques_twenty_one(df)

#* 22- Find billionaires whose source contains “Amazon”.
def ques_twenty_two(df:pd.DataFrame) ->pd.DataFrame:
    return df[df["source"] == "Amazon"]
    # return df.groupby("source").get_group("Amazon")
result = ques_twenty_two(df)

#* 23- Filter for people whose personName includes "Bill".
def ques_twenty_three(df:pd.DataFrame) ->pd.DataFrame:
    return df["personName"].str.contains("Bill")
    # return df[df["personName"].apply(func=lambda str_data: "Bill" in str_data)]
result = ques_twenty_three(df)

#* 24- Select cities that are strings and have more than 6 characters.
def ques_twenty_four(df:pd.DataFrame) ->pd.DataFrame:
    return df[(df["city"].agg(func=type) == str) & (df["city"].str.len() > 6)]
    # return df[(df["city"].agg(func=type) == str) & (df[df["city"].notnull()]["city"].agg(func=lambda data: len(data)) > 6)]
result = ques_twenty_four(df)

#* 25- Count the number of records with an empty "organization" column.
def ques_twenty_five(df:pd.DataFrame) ->pd.DataFrame:
    return len(df[df["organization"].isnull()].index)
result = ques_twenty_five(df)

#* 26- Create a new column by calculating current age using birthYear.
def ques_twenty_six(df:pd.DataFrame) ->pd.DataFrame:
    df["AGE"] = 2025 - df["birthYear"]
    return df 
result = ques_twenty_six(df.loc[::,::])

#* 27- Add a new column showing finalWorth in billions of dollars.
def ques_twenty_seven(df:pd.DataFrame) ->pd.DataFrame:
    df["FİNAL_WORTH"] = df["finalWorth"]  / 1000000
    return df
result = ques_twenty_seven(df.loc[::,::])

#* 28- Create a categorical label as "High", "Medium", or "Low" based on finalWorth.
def ques_twenty_eight(df:pd.DataFrame) ->pd.DataFrame:
    def categoryzing(value:int) -> str:
        if value < 50000:
            return "LOW"
        elif value >= 50000 and value < 100000:
            return "MEDİUM"
        elif value >= 10000:
            return "HİGH"
    df["finalWorth_CATEGORYS"] = df["finalWorth"].apply(func=categoryzing)
    return df
result = ques_twenty_eight(df.loc[::,::])

#* 29- Create a new column containing only the first 3 letters of each country name.
def ques_twenty_nine(df:pd.DataFrame) ->pd.DataFrame:
    df["country_code"] = df["country"].str[:3]
    return df
result = ques_twenty_nine(df.loc[::,::])

#* 30- Create a column showing the product of finalWorth and the population of the person's country (population_country).
def ques_thirty(df:pd.DataFrame) ->pd.DataFrame:
    df["new_column"] = df["population_country"] * df["finalWorth"]
    return df
result = ques_thirty(df.loc[::,::])



print(df)
print(result)
