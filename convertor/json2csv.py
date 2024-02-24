import os
import csv
import json
import re


def is_json_file(file_path: str, /) -> bool:
    pattern = re.compile(r"\S+\.json")
    result = pattern.fullmatch(file_path)
    if result is not None:
        return True
    return False


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
