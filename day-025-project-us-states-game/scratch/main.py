import pandas

original_df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231113.csv")
gray_squirrels_count = len(original_df[original_df["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(original_df[original_df["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(original_df[original_df["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
print(df)

df.to_csv("squirrel_count.csv")
