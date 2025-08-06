import pandas as pd
import numpy as np 

df = pd.read_csv("datasets/global_air_quality_data_10000.csv")

#* 1- Display the first 10 rows."
def ques_one(df:pd.DataFrame) -> None:
    return df.head(10)
    # return df.iloc[:10,::]
result = ques_one(df=df)

#* 2- How many rows (records) are there in the dataset?
def ques_two(df:pd.DataFrame) -> None:
    return len(df.index)
result = ques_two(df=df)

#* 3- How many columns are there in the dataset?
def ques_three(df:pd.DataFrame) -> None:
    return len(df.columns)
result = ques_three(df=df)

#* 4- List all column names
def ques_four(df:pd.DataFrame) -> None:
    return list(df.columns)
result = ques_four(df=df)

#* 5- Which city has the highest PM2.5 value?
def ques_five(df:pd.DataFrame) -> None:
    return df[df["PM2.5"] == df["PM2.5"].max()]["City"]
    # return df.sort_values(by="PM2.5").iloc[-1]["City"]
result = ques_five(df=df)

#* 6- What is the average PM10 value?
def ques_six(df:pd.DataFrame) -> None:
    return df["PM10"].mean()
    # return df.agg(mean_of_PM10 = ("PM10","mean"))
result = ques_six(df=df)

#* 7- Which city has the lowest NO2 value?
def ques_seven(df:pd.DataFrame) -> None:
    return df[df["NO2"] == df["NO2"].min()]["City"]
    # return df.sort_values(by="NO2").iloc[-1]["City"]
result = ques_seven(df=df)

#* 8- What is the average CO value?
def ques_eight(df:pd.DataFrame) -> None:
    return df["CO"].mean()
    # return df.agg(mean_of_CO = ("CO","mean"))
result = ques_eight(df=df)

#* 9- What is the average temperature?
def ques_nine(df:pd.DataFrame) -> None:
    return df["Temperature"].mean()
    # return df.agg(mean_of_Temperature = ("Temperature","mean"))
result = ques_nine(df=df)

#* 10- Which country has the highest temperature?
def ques_ten(df:pd.DataFrame) -> None:
    return df[df["Temperature"] == df["Temperature"].max()]["Country"]
    # return df.sort_values(by="Temperature").iloc[-1]["Country"]
result = ques_ten(df=df)

#* 11- List the cities with a PM2.5 value greater than 100.
def ques_eleven(df:pd.DataFrame) -> None:
    return df[df["PM2.5"] > 100]["City"]
result = ques_eleven(df=df)

#* 12- How many rows have a CO value greater than 5?
def ques_twelve(df:pd.DataFrame) -> None:
    return len(df[df["CO"] > 5].index)
result = ques_twelve(df=df)

#* 13- List the names and dates of cities with an O3 value above 100.
def ques_thirteen(df:pd.DataFrame) -> None:
    return df[df["O3"] > 100].reindex(columns=["City","Date"])
result = ques_thirteen(df=df)

#* 14- Filter all records related to the city 'Istanbul'
def ques_fourteen(df:pd.DataFrame) -> None:
    return df[df["City"] == "Istanbul"]
result = ques_fourteen(df=df)

#* 15- List the cities with a temperature below 15°C and humidity above 60
def ques_fiveteen(df:pd.DataFrame) -> None:
    return df[(df["Temperature"] < 15) & (df["Humidity"] > 60)]["City"]
result = ques_fiveteen(df=df)

#* 16- Calculate the average PM2.5 value for each country.
def ques_sixteen(df:pd.DataFrame) -> None:
    return df.groupby("Country")["PM2.5"].mean()
result = ques_sixteen(df=df)

#* 17- Find the maximum SO2 value for each country.
def ques_seventeen(df:pd.DataFrame) -> None:
    return df.groupby("Country")["SO2"].max()
result = ques_seventeen(df=df)

#* 18- List the average temperature for each city.
def ques_eightteen(df:pd.DataFrame) -> None:
    return df.groupby("City")["Temperature"].mean()
result = ques_eightteen(df=df)

#* 19- How many different cities have been measured in each country?
def ques_nineteen(df:pd.DataFrame) -> None:
    return df.groupby("Country")["City"].nunique()
result = ques_nineteen(df=df)

#* 20- Sort the average humidity values for each country.
def ques_twenty(df:pd.DataFrame) -> None:
    return df.groupby("Country")["Humidity"].mean()
result = ques_twenty(df=df)

#* 21- List the records of cities that contain the word 'new' in their names.
def ques_twenty_one(df:pd.DataFrame) -> None:
    return df[df["City"].str.lower().str.contains("new")]
result = ques_twenty_one(df=df)

#* 22- Display the CO and NO2 values for cities starting with 'Rio'.
def ques_twenty_two(df:pd.DataFrame) -> None:
    return df[df["City"].str.lower().str.startswith("rio")].reindex(columns=["CO","NO2"])
result = ques_twenty_two(df=df)

#* 23- List cities with names longer than 7 letters.
def ques_twenty_three(df:pd.DataFrame) -> None:
    return df[df["City"].str.len() > 7 ]
result = ques_twenty_three(df=df)

#* 24- On which date was the highest average PM10 measured?
def ques_twenty_four(df:pd.DataFrame) -> None:
    return df.groupby("Date")["PM10"].mean().sort_values().index[-1]
result = ques_twenty_four(df=df)

#* 25- Find the average temperature of all cities measured in March 2023.
def ques_twenty_five(df:pd.DataFrame) -> None:
    return df[df["Date"].str.contains("2023-03")].groupby("City")["Temperature"].mean() 
result = ques_twenty_five(df=df.loc[::,::])

#* 26- How many unique cities were measured in 2023?
def ques_twenty_six(df:pd.DataFrame) -> None:
    return df["City"].nunique()
result = ques_twenty_six(df=df.loc[::,::])

#* 27- How many rows contain missing (NaN) values in the dataset?
def ques_twenty_seven(df:pd.DataFrame) -> None:
    all_rows = len(df.index)
    without_nan = len(df.dropna(axis = "index",how="any").index)
    return all_rows - without_nan
result = ques_twenty_seven(df=df.loc[::,::])

#* 28- Which columns contain missing (NaN) values?
def ques_twenty_eight(df:pd.DataFrame) -> None:
    columns = []
    for i in list(df.columns):
        if len(df[df[i].isnull()]) !=0:
            columns.append(i)
        else:
            print(i)
    return columns
result = ques_twenty_eight(df=df.loc[::,::])

#* 29- List the data types of all numeric columns.
def ques_twenty_nine(df:pd.DataFrame) -> None:
    return df.dtypes[df.dtypes == "float64"]
result = ques_twenty_nine(df=df.loc[::,::])

#* 30- Fill in the missing values in the 'Wind Speed' column with the average. (implied special method)
def ques_thirty(df:pd.DataFrame) -> None:
    return df["Wind Speed"].fillna(df["Wind Speed"].mean())
result = ques_thirty(df=df.loc[::,::])


print(df)
print(result)
