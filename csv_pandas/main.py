import pandas as pd


def temp_fahrenheit(temp_celsius):
    return round(temp_celsius * 9 / 5 + 32)


if __name__ == "__main__":
    file = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
    data = pd.read_csv(file)
    df = pd.DataFrame(data['Primary Fur Color'].value_counts()).reset_index()
    df.to_csv("squirrel_count.csv")

    print(df)
