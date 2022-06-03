import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }


# df = pd.DataFrame(mydataset)
# # print(df)

# print(pd.__version__)

#series

# a =[1,7,2]
# myvar = pd.Series(a,index=["x","y","z"])
# print(myvar["y"])


# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories,index = ["day1", "day2","day3"])
# print(myvar)

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# print(df)
# print(df.loc["day2"])

# df = pd.read_csv("data.csv")

# pd.options.display.max_rows =9999
# # print(pd.options.display.max_rows)
# print(df.head(10))
# print("-----------------")
# print(df.tail())
url = 'https://raw.githubusercontent.com/werowe/logisticRegressionBestModel/master/KidCreative.csv'
df = pd.read_csv(url, delimiter=',')
print(df)
print(df.info()) 
# new_df = df.dropna()
# print("---------------")
# print(df.info()) 



# import pandas as pd

# df = pd.read_csv('data.csv')

# df.dropna(inplace = True)

# print(df.to_string())



# Replace Empty Values
# import pandas as pd

# df = pd.read_csv('data.csv')

# df.fillna(130, inplace = True)


# Replace Only For Specified Columns

# import pandas as pd

# df = pd.read_csv('data.csv')

# df["Calories"].fillna(130, inplace = True)