import csv


def parse_csv(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        alphabet = {row["letter"]: row["code"] for row in reader}
        return alphabet


def parse_user_input(message):
    answer = input(message).strip().lower()
    return answer


def main():
    alphabet = parse_csv("phonetic_alphabet.csv")
    name = parse_user_input("What is your name?\n")
    result = [alphabet[letter].capitalize() for letter in name]
    print(result)


if __name__ == "__main__":
    main()
