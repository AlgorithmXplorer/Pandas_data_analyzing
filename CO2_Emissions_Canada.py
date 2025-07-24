

import pandas as pd
import numpy as np

df = pd.read_csv("datasets/CO2 Emissions_Canada.csv")

#*1- Display the first 10 rows.
def ques_one(df:pd.DataFrame):
    return df.head(10)
result = ques_one(df) 

#*2- How many rows and columns are there?
def ques_two(df:pd.DataFrame):
    return f"row count:{df.shape[0]}  ///  column count:{df.shape[1]}"
result = ques_two(df) 

#*3- List the column names and their data types.
def ques_three(df:pd.DataFrame):
    return df.dtypes
result = ques_three(df) 

#*4- "Calculate the average of "CO2 Emissions (g/km)".
def ques_four(df:pd.DataFrame):
    return df["CO2 Emissions(g/km)"].mean()
    # return df.agg(mean = ("CO2 Emissions(g/km)","mean"))
result = ques_four(df) 

#*5- Which vehicle has the highest CO2 emissions?
def ques_five(df:pd.DataFrame):
    return df[df["CO2 Emissions(g/km)"] == df["CO2 Emissions(g/km)"].max()]
result = ques_five(df) 

#*6- "Find the number of unique brands in the "Make" column..
def ques_six(df:pd.DataFrame):
    return df["Make"].nunique()
result = ques_six(df) 

#*7- Which brand has the most models?
def ques_seven(df:pd.DataFrame):
    return df.groupby("Make")["Model"].value_counts(ascending=False).sort_values().index[-1]
result = ques_seven(df) 

#*8- Count the number of vehicles by "Fuel Type".
def ques_eight(df:pd.DataFrame):
    return df["Fuel Type"].value_counts()
result = ques_eight(df) 

#*9- What is the most common "Transmission" type
def ques_nine(df:pd.DataFrame):
    return df["Transmission"].value_counts(ascending=False).index[0]
result = ques_nine(df) 

#*10- Calculate the average engine size ("Engine Size (L)")..
def ques_ten(df:pd.DataFrame):
    return df["Engine Size(L)"].mean()
result = ques_ten(df) 

#*11- List the vehicles where "Fuel Type" equals "D" (diesel).
def ques_eleven(df:pd.DataFrame):
    return df[df["Fuel Type"] == "D"]
    # return df.groupby("Fuel Type").get_group("D")
result = ques_eleven(df) 

#*12- Filter vehicles with CO2 emissions over 200 g/km..
def ques_twelve(df:pd.DataFrame):
    return df[df["CO2 Emissions(g/km)"] > 200]
result = ques_twelve(df) 

#*13- Select the vehicles with "Cylinders" equal to 8.
def ques_thirteen(df:pd.DataFrame):
    return df[df["Cylinders"] == 8]
    # return df.groupby("Cylinders").get_group(8)
result = ques_thirteen(df) 

#*14- "List all unique transmission types and count how many of each exist
def ques_fourteen(df:pd.DataFrame):
    return df["Transmission"].value_counts()
result = ques_fourteen(df) 

#*15- List the top 5 vehicles with the highest "Fuel Consumption City (L/100 km)".
def ques_fiveteen(df:pd.DataFrame):
    return df.sort_values(by="Fuel Consumption City (L/100 km)").tail()
    # return df.reindex(index=list(df["Fuel Consumption City (L/100 km)"].sort_values().tail().index))
result = ques_fiveteen(df) 

#*16-  Select vehicles with engine size greater than 2.5L.
def ques_sixteen(df:pd.DataFrame):
    return df[df["Engine Size(L)"] > 2.5]
result = ques_sixteen(df) 

#*17- "Analyze the relationship between "Fuel Type" and "CO2 Emissions".
def ques_seventeen(df:pd.DataFrame):
    return df.groupby("Fuel Type")["CO2 Emissions(g/km)"].mean()
result = ques_seventeen(df) 

#*18- Sort by the average "Fuel Consumption Hwy (L/100 km)".
def ques_eighteen(df:pd.DataFrame):
    return df.sort_values(by="Fuel Consumption Hwy (L/100 km)",ascending=False)
result = ques_eighteen(df) 

#*19- Calculate the average CO2 emissions for each "Make".
def ques_nineteen(df:pd.DataFrame):
    return df.groupby("Make")["CO2 Emissions(g/km)"].mean()
    # return df.groupby("Make").agg(Mean_Cao2 = ("CO2 Emissions(g/km)","mean"))
result = ques_nineteen(df) 

#*20- What is the average engine size of 4-cylinder vehicles?
def ques_twenty(df:pd.DataFrame):
    return df[df["Cylinders"]==4]["Engine Size(L)"].mean()
    # return df.groupby("Cylinders").get_group(4)["Engine Size(L)"].mean()
result = ques_twenty(df) 

#*21- Group by "Make" and "Fuel Type" and calculate the average CO2 emissions.
def ques_twenty_one(df:pd.DataFrame):
    return df.groupby(by=["Make","Fuel Type"])["CO2 Emissions(g/km)"].mean()
result = ques_twenty_one(df) 

#*22- Calculate the average fuel consumption for each transmission type.
def ques_twenty_two(df:pd.DataFrame):
    return df.groupby("Transmission")["Fuel Consumption City (L/100 km)"].mean()
result = ques_twenty_two(df) 

#*23- What metric could be used to find the most fuel-efficient vehicles
def ques_twenty_three(df:pd.DataFrame):
    return df.sort_values(by="Fuel Consumption City (L/100 km)").head()
result = ques_twenty_three(df) 

#*24- List the 10 vehicles with the lowest CO2 emissions.
def ques_twenty_four(df:pd.DataFrame):
    return df.sort_values(by="CO2 Emissions(g/km)").head(10)
result = ques_twenty_four(df) 

#*25- Normalize the "CO2 Emissions" values.
def ques_twenty_five(df:pd.DataFrame):
    return (df["CO2 Emissions(g/km)"] - df["CO2 Emissions(g/km)"].min()) / (df["CO2 Emissions(g/km)"].max() - df["CO2 Emissions(g/km)"].min())
result = ques_twenty_five(df) 

#*26- Check for missing values.
def ques_twenty_six(df:pd.DataFrame):
    columns = list(df.columns)
    for index in columns:
        null_datas = list(df[index][df[index].isnull()])
        if len(null_datas) != 0:
            return "there are null datas"
    
    return "there are no null datas"

result = ques_twenty_six(df) 

#*27- Find the top 3 highest CO2 emitting vehicles for each "Fuel Type".
def ques_twenty_seven(df:pd.DataFrame):
    return df.sort_values(by="CO2 Emissions(g/km)").groupby("Fuel Type").max().sort_values(by="CO2 Emissions(g/km)",ascending=False).iloc[:3,::]
result = ques_twenty_seven(df) 

#*28-How would you examine the relationship between "Engine Size" and "Fuel Consumption"
def ques_twenty_eight(df:pd.DataFrame):
    return df.reindex(columns=["Engine Size(L)","Fuel Consumption Comb (L/100 km)"]).corr()
result = ques_twenty_eight(df) 

#*29- What kind of analysis is suitable to represent the "Cylinders" column as a histogram?
def ques_twenty_nine(df:pd.DataFrame):
    df["Cylinders"].hist()
    # df["Cylinders"].plot(kind="hist")
ques_twenty_nine(df) 

#*30- Filter the 10 vehicles with the lowest "Fuel Consumption City (L/100 km)".
def ques_thirty(df:pd.DataFrame):
    return df.sort_values(by="Fuel Consumption City (L/100 km)").head(10)
    # return df.reindex(index=list(df["Fuel Consumption City (L/100 km)"].sort_values().head(10).index))
result = ques_thirty(df) 


print(df)
print(result)

