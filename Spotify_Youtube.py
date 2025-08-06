
import pandas as pd
import numpy as np

df = pd.read_csv("datasets/Spotify_Youtube.csv")


#* 1- Display the first 10 rows.
def ques_one(df:pd.DataFrame) -> None:
    return df.head(10)
result = ques_one(df.loc[:,:])

#* 2- How many rows and columns are in the dataset?
def ques_two(df:pd.DataFrame) -> None:
    return [len(df.index),len(df.columns)]
result = ques_two(df.loc[:,:])

#* 3- List the column names and their data types.
def ques_three(df:pd.DataFrame) -> None:
    return df.dtypes
result = ques_three(df.loc[:,:])

#* 4- Find the most frequently repeated track name.
def ques_four(df:pd.DataFrame) -> None:
    return df["Track"].value_counts().index[0]
result = ques_four(df.loc[:,:])

#* 5- Display the name and duration of the longest track.
def ques_five(df:pd.DataFrame) -> None:
    return df[df["Duration_ms"].max() == df["Duration_ms"]][["Album","Duration_ms"]]
result = ques_five(df.loc[:,:])

#* 6- Find the artist with the most tracks.
def ques_six(df:pd.DataFrame) -> None:
    return df.value_counts(subset=["Artist"]).index[0]
result = ques_six(df.loc[:,:])

#* 7- Which artist has the most works in the 'Album' type?
def ques_seven(df:pd.DataFrame) -> None:
    album_rows = df[df["Album_type"] == "album"]
    return album_rows["Artist"].value_counts().index[0]
result = ques_seven(df.loc[:,:])

#* 8- How many unique artists are there?
def ques_eight(df:pd.DataFrame) -> None:
    return df["Artist"].nunique()
result = ques_eight(df.loc[:,:])

#* 9- How many different album types are there?
def ques_nine(df:pd.DataFrame) -> None:
    return df["Album_type"].nunique()
result = ques_nine(df.loc[:,:])

#* 10- Print the name of the album with the most tracks.
def ques_ten(df:pd.DataFrame) -> None:
    return df["Album"].value_counts().index[0]
result = ques_ten(df.loc[:,:])

#* 11- What is the average value of 'Danceability?
def ques_eleven(df:pd.DataFrame) -> None:
    return df["Danceability"].mean()
result = ques_eleven(df.loc[:,:])

#* 12- Print the song and artist with the highest 'Speechiness' value.
def ques_twelve(df:pd.DataFrame) -> None:
    return df[df["Speechiness"].max() == df["Speechiness"]][["Artist","Album"]]
result = ques_twelve(df.loc[:,:])

#* 13- What is the average value of 'Acousticness'?
def ques_thirteen(df:pd.DataFrame) -> None:
    return df["Acousticness"].mean()
result = ques_thirteen(df.loc[:,:])

#* 14- Print the name of the song with the lowest 'Loudness' value.
def ques_fourteen(df:pd.DataFrame) -> None:
    return df[df["Loudness"].min() == df["Loudness"]]["Album"] 
result = ques_fourteen(df.loc[:,:])

#* 15- Count the number of songs with 'Instrumentalness' greater than 0.8.
def ques_fiveteen(df:pd.DataFrame) -> None:
    return len(df[df["Instrumentalness"] > 0.8 ].index) 
result = ques_fiveteen(df.loc[:,:])

#* 16- Print the name and channel of the most viewed song on YouTube.
def ques_sixteen(df:pd.DataFrame) -> None:
    return df[df["Views"].max() == df["Views"]][["Title","Channel"]]
result = ques_sixteen(df.loc[:,:])

#* 17- What is the average number of likes?
def ques_seventeen(df:pd.DataFrame) -> None:
    return df["Likes"].mean()
result = ques_seventeen(df.loc[:,:])

#* 18- What is the average number of views for songs where 'official_video' is True?
def ques_eighteen(df:pd.DataFrame) -> None:
    videos = df[df["official_video"].notnull()]
    result = videos[videos["official_video"]]
    return result["Views"].mean()
result = ques_eighteen(df.loc[:,:])

#* 19- Find the average number of comments for videos that are not licensed.
def ques_nineteen(df:pd.DataFrame) -> None:
    videos = df[df["Licensed"].notnull()]
    result = videos[videos["Licensed"] == False]
    return result["Comments"].mean()
result = ques_nineteen(df.loc[:,:])

#* 20- List the names of songs with more than 1 million likes.
def ques_twenty(df:pd.DataFrame) -> None:
    return df[df["Likes"] > 1000000]["Title"] 
result = ques_twenty(df.loc[:,:])

#* 21- Which channel has published the most videos?
def ques_twenty_one(df:pd.DataFrame) -> None:
    return df["Channel"].value_counts().index[0]
result = ques_twenty_one(df.loc[:,:])

#* 22- Calculate the average 'Valence' values for each 'Album_type'.
def ques_twenty_two(df:pd.DataFrame) -> None:
    return df.groupby("Album_type")["Valence"].mean()
result = ques_twenty_two(df.loc[:,:])

#* 23- Calculate the average 'Energy' values by artist.
def ques_twenty_three(df:pd.DataFrame) -> None:
    return df.groupby("Artist")["Energy"].mean()
result = ques_twenty_three(df.loc[:,:])

#* 24- Sort the average 'Tempo' values for each 'Key'.
def ques_twenty_four(df:pd.DataFrame) -> None:
    return df.groupby("Key")["Tempo"].mean()
result = ques_twenty_four(df.loc[:,:])

#* 25- List total 'Views' by YouTube channel in descending order.
def ques_twenty_five(df:pd.DataFrame) -> None:
    return df.groupby("Channel")["Views"].sum()
result = ques_twenty_five(df.loc[:,:])

# * 26- Which channel has the highest like-to-view ratio? (Ratio: Likes / Views)
def ques_twenty_six(df:pd.DataFrame) -> None:
    df["Mean_of_like_view"] = df["Likes"] / df["Views"]
    return df[df["Mean_of_like_view"].max() == df["Mean_of_like_view"]]
result = ques_twenty_six(df.loc[:,:])

#* 27- Filter the songs among the first 100 that have “Stream” values higher than the overall average. Sort the results.
def ques_twenty_seven(df:pd.DataFrame) -> None:
    not_null = df[df["Stream"].notnull()].head(100)
    mean = not_null["Stream"].mean()
    return not_null[not_null["Stream"] > mean]
result = ques_twenty_seven(df.loc[:,:])

#* 28-List the top 5 most frequent values in the “Stream” column along with the names of the songs that have these values.
def ques_twenty_eight(df:pd.DataFrame) -> None:
    most_agained = df.sort_values(by="Stream",ascending=False).head()
    return most_agained["Title"]
result = ques_twenty_eight(df.loc[:,:])

#* 29- List the columns that contain missing (NaN) values.
def ques_twenty_nine(df:pd.DataFrame) -> None:
    columns = list(df.columns)
    null_inculde = []
    for column in columns:
        null_data = len(df[df[column].isnull()].index)
        if null_data != 0:
            null_inculde.append(column)
    return null_inculde
result = ques_twenty_nine(df.loc[:,:])

#* 30- Convert the values in the 'Duration_ms' column to minutes and create a new column.
def ques_thirty(df:pd.DataFrame) -> None:
    return pd.to_timedelta(df["Duration_ms"],unit="ms").apply(func=lambda date: str(date)[10:15])
result = ques_thirty(df.loc[:,:])


print(df)
print(result)


