import csv
from io import StringIO
fname = "f1data_2000-2025"

with open(fname + ".csv", "r") as file:
    data = list(csv.DictReader(file))

driver_names = set()
for d in data:
    driver_names.add(d["driver_name"])

locations = set()
for d in data:
    locations.add(d["location"])


with open(fname + "_driver_names.txt", "w") as file:
    for n in driver_names:
        file.write(n)
        file.write("\n")
print("Generated " + fname + "_driver_names.txt")

with open(fname + "_locations.txt", "w") as file:
    for n in locations:
        file.write(n)
        file.write("\n")

print("Generated " + fname + "_locations.txt")

def parse_list(s):
    return (s.replace('"', '')
            .replace("'", "")
            .replace("[", "")
            .replace("]", "")
            .replace(" ", "")
            .split(","))



final_data = []
for d in data:
    row = {}
    
    row["rain"]      = d["rain"]
    row["grid_pos"]  = d["grid_pos"]
    row["pit_count"] = d["pit_count"]
    row["final"]     = d["final"]
    #row["location"]     = d["location"]


    for pit_i in range(0,5):
        row[f"compound_{pit_i}"] = "NONE"
        row[f"lap_{pit_i}"]      = "NONE"

    compounds = parse_list(d["compounds"])
    laps      = parse_list(d["pit_laps"])
    laps      = [int(float(l)) for l in laps]

    #print(compounds)
    #print(laps)

    assert(len(compounds) == len(laps) and len(laps) < 5) 

    for i, c in enumerate(compounds):
        row[f"compound_{i}"] = c

    for i, c in enumerate(laps):
        row[f"lap_{i}"] = c

    for n in driver_names:
        row[n] = 0
    row[d["driver_name"]] = 1

    for n in locations:
        row[n] = 0
    row[d["location"]] = 1

    final_data.append(row)


output = StringIO()
csv_writer = csv.DictWriter(output, fieldnames=final_data[0].keys())
csv_writer.writeheader()
for row in final_data:
    csv_writer.writerow(row)
csv_string = output.getvalue()
output.close()

with open(fname + "_encoded.csv", "w") as file:
    file.write(csv_string)

print("Generated " + fname + "_encoded.csv")







