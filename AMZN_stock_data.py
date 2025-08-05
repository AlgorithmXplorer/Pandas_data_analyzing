
import pandas as pd
import numpy as np

df = pd.read_csv("datasets/AMZN_stock_data.csv")
df[["year","month","day"]] = df["Date"].str[:10].str.split("-",expand=True)


#* 1- Display the first 10 rows.
def ques_one(df:pd.DataFrame) ->None:
    return df.head(10)
result = ques_one(df=df)

#* 2- How many total records are there?
def ques_two(df:pd.DataFrame) ->None:
    return len(df.index)
result = ques_two(df=df)

#* 3- Print the column names and their data types.
def ques_three(df:pd.DataFrame) ->None:
    return df.dtypes
result = ques_three(df=df)

#* 4- Calculate the average of the 'Close' column.
def ques_four(df:pd.DataFrame) ->None:
    return df["Close"].mean()
result = ques_four(df=df)

#* 5- Find the maximum value in the 'Volume' column.
def ques_five(df:pd.DataFrame) ->None:
    return df["Volume"].max()
result = ques_five(df=df)

#* 6- Find the day with the highest value in the 'High' column.
def ques_six(df:pd.DataFrame) ->None:
    return df[df["High"] == df["High"].max()]["day"]
result = ques_six(df=df.loc[:,:])

#* 7- Print the start and end dates from the 'Date' column.
def ques_seven(df:pd.DataFrame) ->None:
    return [df["Date"].iloc[0], df["Date"].iloc[-1]]
result = ques_seven(df=df.loc[:,:])

#* 8- Which day has the lowest trading volume?
def ques_eight(df:pd.DataFrame) ->None:
    return df[df["Volume"] == df["Volume"].min()]["day"]
result = ques_eight(df=df.loc[:,:])

#* 9- What is the average difference between 'Open' and 'Close' values?
def ques_nine(df:pd.DataFrame) ->None:
    return df["Open"].mean() - df["Close"].mean()
result = ques_nine(df=df.loc[:,:])

#* 10- Is there any difference between the 'Adj Close' and 'Close' columns?
def ques_ten(df:pd.DataFrame) ->None:
    df["Adj_Close_Approx"] = (df["Close"] - df["Dividends"]) / (df["Stock Splits"].replace(0, 1))
    return df["Adj_Close_Approx"] - df["Close"]
result = ques_ten(df=df.loc[:,:])

#* 11- List the records where 'Close' value is above 3000.
def ques_eleven(df:pd.DataFrame) ->None:
    return df[df["Close"] > 3000]
result = ques_eleven(df=df.loc[:,:])

#* 12- Filter the data for the year 2021.
def ques_twelve(df:pd.DataFrame) ->None:
    return df[df["year"] == "2021"]
result = ques_twelve(df=df.loc[:,:])

#* 13- Get the closing prices for January 2020.
def ques_thirteen(df:pd.DataFrame) ->None:
    return df[(df["year"] == "2020") & (df["month"] == "01")]["Close"]
result = ques_thirteen(df=df.loc[:,:])

#* 14- List the dates and 'Close' prices for days with 'Volume' under 50 million.
def ques_fourteen(df:pd.DataFrame) ->None:
    return df[df["Volume"] < 50000000].reindex(columns=["year","month","day","Close"])
result = ques_fourteen(df=df.loc[:,:])

#* 15- On which day in 2022 did the highest closing price occur?
def ques_fiveteen(df:pd.DataFrame) ->None:
    year_2022 = df[df["year"] == "2022"]
    return year_2022[year_2022["Close"] == year_2022["Close"].max()]["day"]
result = ques_fiveteen(df=df.loc[:,:])

#* 16- Find the records where 'Volume' is greater than 500 million.
def ques_sixteen(df:pd.DataFrame) ->None:
    return df[df["Volume"] > 500000000]
result = ques_sixteen(df=df.loc[:,:])

#* 17- Filter a specific date range (e.g., 2020-06-01 to 2020-12-31).
def ques_seventeen(df:pd.DataFrame) ->None:
    start_index = df[(df["year"] == "2020") & (df["month"] == "06") &(df["day"] == "01")].index[0]
    end_index = df[(df["year"] == "2020") & (df["month"] == "12") &(df["day"] == "31")].index[0]
    return df.loc[start_index:end_index , ::]
result = ques_seventeen(df=df.loc[:,:])

#* 18- List the day with the largest difference between 'Low' and 'Open'.
def ques_eighteen(df:pd.DataFrame) ->None:
    result = df["Low"] - df["Open"]
    result = result.sort_values().index[-1]
    return df.loc[result,::][["year","month","day"]]
result = ques_eighteen(df=df.loc[:,:])

#* 19- Calculate the correlation coefficient between 'Close' and 'Open'. (method implied))
def ques_nineteen(df:pd.DataFrame) ->None:
    return df[["Close","Open"]].corr()
result = ques_nineteen(df=df.loc[:,:])

#* 20- Show monthly average volume changes for the year 2021.
def ques_twenty(df:pd.DataFrame) ->None:
    return df[df["year"] == "2021"].groupby("month")["Volume"].mean()
result = ques_twenty(df=df.loc[:,:])

#* 21- List the average closing price for each year.
def ques_twenty_one(df:pd.DataFrame) ->None:
    return df.groupby("year")["Close"].mean()
result = ques_twenty_one(df=df.loc[:,:])

#* 22- Show the maximum 'High' values per month.
def ques_twenty_two(df:pd.DataFrame) ->None:
    return df.groupby(["year","month"])["High"].max()
result = ques_twenty_two(df=df.loc[:,:])

#* 23- Sort the yearly minimum closing prices.
def ques_twenty_three(df:pd.DataFrame) ->None:
    return df.groupby("year")["Close"].min()
result = ques_twenty_three(df=df.loc[:,:])

#* 24- Find the day with the highest trading volume for each year.
def ques_twenty_four(df:pd.DataFrame) ->None:
    group = df.groupby("year")
    days = []
    for name,grp in group:
        result = grp.sort_values(by="Volume").iloc[-1]
        date = result[["year","month","day"]]
        days.append({"year":date["year"],"month":date["month"],"day":date["day"]})
        print(days)
    return days
result = ques_twenty_four(df=df.loc[:,:])

#* 25- Normalize the volume values as percentages. (method implied)
def ques_twenty_five(df:pd.DataFrame) ->None:
    return (df["Volume"] - df["Volume"].min()) / (df["Volume"].max()- df["Volume"].min()) 
result = ques_twenty_five(df=df.loc[:,:])

#* 26- Check if there is any missing data.
def ques_twenty_six(df:pd.DataFrame) ->None:
    return  (len(df.index) - len(df.dropna().index)) != 0
result = ques_twenty_six(df=df.loc[:,:])

#* 27- Fill missing closing prices with the previous day’s value.
def ques_twenty_seven(df:pd.DataFrame) ->None:
    if len(df[df["Close"].isnull()].index) == 0:
        return "There is no null character in the 'Close' column"
    else:
        for index in df[df["Close"].isnull()].index:
            df.loc[index,"Close"] = df["Close"][index-1]
result = ques_twenty_seven(df=df.loc[:,:])

#* 28- Calculate the 5-day moving average for the first 30 days.
def ques_twenty_eight(df:pd.DataFrame) ->None:
    df["5_gunluk_ortalama"] = df["Close"].head(30).rolling(window=5).mean()
    return df.head(30)
result = ques_twenty_eight(df=df.loc[:,:])

#* 29- Write the difference between 'High' and 'Low' into a new column.
def ques_twenty_nine(df:pd.DataFrame) ->None:
    df["dif_of_high_low"] =df["High"] - df["Low"]
    return df
result = ques_twenty_nine(df=df.loc[:,:])

#* 30- What kind of analysis can be done to determine the most stable price period? (method implied).
def ques_thirty(df:pd.DataFrame) ->None:
    df["std_5"] = df["Close"].rolling(window=5).std()
    min_std_index = df["std_5"].idxmin()
    return df.loc[[min_std_index]]
result = ques_thirty(df=df.loc[:,:])


print(df)
print(result)

