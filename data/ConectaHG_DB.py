import json

a_file = open("./data/database.json", "r")

json_object = json.load(a_file)

a_file.close()

print(json_object)

json_object["d"] = 100


a_file = open("./data/database.json", "w")

json.dump(json_object, a_file)

a_file.close()