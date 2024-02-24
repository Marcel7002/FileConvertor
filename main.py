import os
import csv
import json
import re


def is_csv_file(file_path: str, /) -> bool:
    pattern = re.compile(r"\S+\.csv")
    result = pattern.fullmatch(file_path)
    if result is not None:
        return True
    return False


def is_json_file(file_path: str, /) -> bool:
    pattern = re.compile(r"\S+\.json")
    result = pattern.fullmatch(file_path)
    if result is not None:
        return True
    return False


def csv2json(file_path: str, /) -> None:
    csv_file_path = os.path.normpath(file_path)
    if (
        os.path.exists(csv_file_path)
        and os.path.isfile(csv_file_path)
        and is_csv_file(csv_file_path)
    ):
        with open(csv_file_path, mode="r", newline="") as file:
            csv_reader = csv.DictReader(file)
            data = {"data": [row for row in csv_reader]}
        json_file_path = csv_file_path.replace("csv", "json")
        json_file_path = os.path.normpath(json_file_path)
        os.remove(csv_file_path)
        with open(json_file_path, mode="w") as file:
            json.dump(data, file, indent=4)
    else:
        print("Invalid file path!")


def json2csv(file_path: str, /) -> None:
    json_file_path = os.path.normpath(file_path)
    if (
        os.path.exists(json_file_path)
        and os.path.isfile(json_file_path)
        and is_json_file(json_file_path)
    ):
        with open(json_file_path, mode="r") as file:
            data = json.load(file)
            key = [key for key in data.keys()][0]
            data = data[key]
        csv_file_path = json_file_path.replace("json", "csv")
        csv_file_path = os.path.normpath(csv_file_path)
        os.remove(json_file_path)
        with open(csv_file_path, mode="w", newline="") as file:
            csv_writer = csv.DictWriter(file, fieldnames=data[0].keys())
            csv_writer.writeheader()
            for row in data:
                csv_writer.writerow(row)
    else:
        print("Invalid file path!")


def run_program() -> None:
    file_path = input("Enter file path: ")
    print("1) csv -> json\n2) json -> csv")
    option_num = int(input("Option nr: "))
    if option_num == 1:
        csv2json(file_path)
    elif option_num == 2:
        json2csv(file_path)
    else:
        print("There is no such option!")


if __name__ == "__main__":
    run_program()
