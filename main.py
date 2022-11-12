from datetime import datetime

import json

parsed_file_save = None

with open("data.json", "r+", encoding="utf-8") as file:
    try:
        parsed_file = json.load(file)
    except:
        parsed_file = {}

parsed_file_save = parsed_file

with open("data.json", "w+", encoding="utf-8") as file:
    while True:

        console_data = input("input command -> ")

        if console_data == "quit":
            break

        elif console_data == "backup":
            with open("data_save.json", "w", encoding="utf-8") as saver_file:
                saver_file.write(str(parsed_file).replace("'", '"'))

        elif console_data == "help":
            print(f"quit\n"
                  f"print\n"
                  f"add\n"
                  f"del\n"
                  f"change\n")

        elif console_data == "clear":
            parsed_file = parsed_file_save

        elif console_data == "print":
            print(json.dumps(parsed_file, indent=4))

        elif console_data == "add":
            name, count = str.split(input(f"print book name and count with '/' before name ant count-> "), "/")
            try:
                print(f"already added !!! at {parsed_file[name]['date']}")
                continue
            except KeyError:
                parsed_file[name] = \
                    {
                        "count": int(count),
                        "date": f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year}"
                    }

        elif console_data == "del":
            name = input(f"print book name-> ")
            try:
                del parsed_file[name]
            except:
                print("not searched")

        elif console_data == "change":
            name, count = str.split(input(f"print book name and count with '/' before name ant count-> "), "/")
            try:
                del parsed_file[name]
            except:
                print("not searched")
            parsed_file[name] = \
                {
                    "count": count,
                    "date": f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year}"
                }

    file.write(str(parsed_file).replace("'", '"'))
