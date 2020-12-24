import csv
import pandas


def temp_calc_csv():
    """
        Implemented with csv module
    """
    filename = "./weather_data.csv"
    temperature = []
    average_temp = 0
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            temperature.append(int(row["temp"]))
    average_temp = sum(temperature) / len(temperature)
    average_temp = round(average_temp, 1)
    max_temp = max(temperature)
    print(average_temp)


def temp_calc_pandas():
    """
        Implemented with Pandas module
    """
    filename = "./weather_data.csv"
    data_frame = pandas.read_csv(filename)
    mean_temp = data_frame["temp"].mean()
    max_temp = data_frame["temp"].max()
    max_temp_row = data_frame[data_frame.temp == max_temp]
    print(max_temp_row["day"])


def write_to_csv():
    """
        Implemented with Pandas module
    """
    data =  {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }
    data_frame = pandas.DataFrame(data)
    data_frame.to_csv("scores.csv")


def parse_squirrel_data():
    """
        Count the number of squirrel based on primary fur color
        Write the data into a new csv file
    """
    filename = "central_park_squirrel_sensus_2018.csv"
    df = pandas.read_csv(filename)
    pfc = df["Primary Fur Color"]
    pfc = pfc.dropna()
    # counts = {}
    # for row in pfc:
    #     if type(row) == str:
    #         if row not in counts:
    #             counts[row] = 0
    #         counts[row] += 1
    counts = pfc.value_counts()
    fur_color = pfc.unique()
    output = pandas.DataFrame({
        "Fur Color": list(fur_color),
        "Count": list(counts)
    })
    output.to_csv("squirrel_count_by_fur_color.csv")


def main():
    parse_squirrel_data()


if __name__ == "__main__":
    main()
