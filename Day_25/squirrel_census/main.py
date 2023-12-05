import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrel_cout = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_cout = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_cout = len(data[data["Primary Fur Color"] == "Black"])

data_dic = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_cout, red_squirrel_cout, black_squirrel_cout]
}

squirrel_data_frame = pandas.DataFrame(data_dic)
squirrel_data_frame.to_csv("Squirrel_color.csv")