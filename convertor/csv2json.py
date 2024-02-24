import re
import os
import json
import csv


def is_csv_file(file_path: str, /) -> bool:
    pattern = re.compile(r"\S+\.csv")
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
