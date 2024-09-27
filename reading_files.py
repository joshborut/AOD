import csv
import json
# with open("favorite_colors.csv", "r") as f:
#     print(f)
#
# with open("favorite_colors.csv", "r") as f:
#     data = csv.reader(f)
#     for row in data:
#         print(row)
#
# with open("favorite_colors.csv", "r") as f:
#     data = csv.DictReader(f)
#     for row in data:
#         print(row)
#
# with open("2022-02-24-conti-logs.json", "r") as f:
#     data = json.load(f)
#     print(data["messages"][174]["u"]["name"])
#     print(data["messages"][174]["msg"])

# Application
with open("favorite_colors.csv", "r") as f:
    data = csv.DictReader(f)
    answer_dict = {}
    for data_point in data:
        if data_point["grade"] == "9" and data_point["favorite_color"] == "blue":
                answer_dict["Question 1"] = answer_dict.get("Question 1", 0) + 1
        if data_point["favorite_color"] == "yellow":
            answer_dict["Question 2"] = answer_dict.get("Question 2", 0) + 1
    print(answer_dict)


with open("2022-02-24-conti-logs.json", "r") as read_file:
    json_data = json.load(read_file)
    msgs = []
    for msg in json_data["messages"]:
        msgs.append(msg["msg"])
    with open("2022-02-24-conti-logs.txt", "w") as write_file:
        for msg in msgs:
            write_file.write(msg + "\n")


