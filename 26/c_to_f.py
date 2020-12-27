def main():
    weather_c = {
        "Monday": 12,
        "Tuesday": 14,
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24,
    }
    temp_f = {day: (c * 9/5) + 32 for day, c in weather_c.items()}
    print(temp_f)


if __name__ == "__main__":
    main()