from convertor import *


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
