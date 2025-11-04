import random
import csv
from io import StringIO
from common import fname, MAX_PITS

with open(fname + ".csv", "r") as file:
    data = list(csv.DictReader(file))

driver_names = set()
for d in data:
    driver_names.add(d["driver_name"])

locations = set()
for d in data:
    d['location'] =  d['location'].replace(" ", "_").replace("-", "_").lower().encode('ascii', 'ignore').decode('ascii')
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



loc_dict = {}
for l in locations:
    loc_dict[l] = 0

final_data = []
for d in data:
    row = {}

    row["rain"]      = d["rain"]
    row["grid_pos"]  = d["grid_pos"]
    row["pit_count"] = d["pit_count"]
    row["final"]     = d["final"]


    compounds = parse_list(d["compounds"])
    laps      = parse_list(d["pit_laps"])

    if not len(laps) or laps[0] == '': continue
    if not len(compounds) or compounds[0] == '': continue

    laps      = [int(float(l)) for l in laps]
    
    assert(len(laps) <= MAX_PITS)

    for pit_i in range(0,MAX_PITS+1):
        row[f"compound_{pit_i}"] = "null"
        row[f"lap_{pit_i}"]      = "null"

    assert(len(compounds) == len(laps)) 

    for i, c in enumerate(compounds):
        row[f"compound_{i}"] = c

    for i, c in enumerate(laps):
        row[f"lap_{i}"] = c

    for n in driver_names:
        row[n] = 0 + random.random()/1000
    row[d["driver_name"]] = 1 + random.random()/1000

    for n in locations:
        row[n] = 0 + random.random()/1000
    row[d["location"]] = 1 + random.random()/1000
    loc_dict[d["location"]] += 1

    final_data.append(row)

random.shuffle(final_data)

cutoff = int(len(final_data) * 0.2)
testing_set_raw = final_data[:cutoff]
final_data = final_data[cutoff:]

testing_set = []
for t in testing_set_raw:
    try:
        if int(float(t["final"])) == 1:
            testing_set.append(t)
    except ValueError:
        pass


print(loc_dict)

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

print(loc_dict)

output = StringIO()
csv_writer = csv.DictWriter(output, fieldnames=testing_set[0].keys())
csv_writer.writeheader()
for row in testing_set:
    csv_writer.writerow(row)
csv_string = output.getvalue()
output.close()

with open(fname + "_test_encoded.csv", "w") as file:
    file.write(csv_string)

print("Generated " + fname + "_test_encoded.csv")


train_r_script = f"""
library(MASS)

data = read.csv("{fname}_encoded.csv")
"""

def add_training_data():
    global train_r_script
    train_r_script +=    "                         "
    for driver in driver_names:
        train_r_script += driver + " + "

    train_r_script +=  "\n                         "
    for loc in locations:
        train_r_script += loc + " + "

    train_r_script +=  "\n                         "
    train_r_script += "rain + final + grid_pos, data=data)\n\n"

for i in range(0, MAX_PITS):
    train_r_script += f"compound_{i}_model = lda(compound_{i} ~ \n"
    add_training_data()

for i in range(1, MAX_PITS):
    train_r_script += f"lap_{i}_model = lda(lap_{i} ~ \n"
    add_training_data()

for i in range(0, MAX_PITS):
    train_r_script += f'save(compound_{i}_model, file = "compound_{i}_lda_model.RData")\n'

train_r_script += "\n"

for i in range(1, MAX_PITS):
    train_r_script += f'save(lap_{i}_model, file = "lap_{i}_lda_model.RData")\n'

with open("train_generated.R", "w") as file:
    file.write(train_r_script)

print("Generated train_generated.R")



predict_r_script = """
library(MASS)

args = commandArgs(trailingOnly = TRUE)

con = textConnection(args)
    new_data = read.csv(con)
close(con)
"""

for i in range(0, MAX_PITS):
    predict_r_script += f'load("compound_{i}_lda_model.RData")\n'

predict_r_script += "\n"

for i in range(1, MAX_PITS):
    predict_r_script += f'load("lap_{i}_lda_model.RData")\n'

# predict_r_script += """
# new_data <- data.frame(
#     rain      = c(0),
#     grid_pos  = c(1),
#     pit_count = c(2),
#     final     = c(1.0),
# """
#
# driver_names = list(driver_names)
# locations = list(locations)
#
# for driver in driver_names[:-1]:
#     predict_r_script += "    " + driver + " = c(0),\n"
#
# predict_r_script += "    " + driver_names[-1] + " = c(1),\n"
#
# predict_r_script +=  "\n"
# for loc in locations[:-1]:
#     predict_r_script += "    " + loc + " = c(0),\n"
#
# predict_r_script += "    " + locations[-1] + " = c(1)\n"
#
# predict_r_script += ")\n\n"
#
for i in range(0, MAX_PITS):
    predict_r_script += f'compound_{i}_prediction = predict(compound_{i}_model, new_data)\n'

predict_r_script +=  "\n"

for i in range(1, MAX_PITS):
    predict_r_script += f'lap_{i}_prediction = predict(lap_{i}_model, new_data)\n'

predict_r_script += 'cat("{\\n")\n'
predict_r_script += 'cat("    \\"laps\\": [ 0, ")\n'
for i in range(1, MAX_PITS-1):
    predict_r_script += f'cat(as.character(lap_{i}_prediction$class), ", ")\n'

predict_r_script += f'cat(as.character(lap_{MAX_PITS-1}_prediction$class), " ],\\n")\n'

predict_r_script += 'cat("    \\"compounds\\": [ ")\n'

for i in range(0, MAX_PITS-1):
    predict_r_script += f'cat("\\"", as.character(compound_{i}_prediction$class), "\\"", ", ")\n'

predict_r_script += f'cat("\\"", as.character(compound_{MAX_PITS-1}_prediction$class), "\\"", " ]\\n")\n'

predict_r_script += 'cat("}\\n")\n'

# predict_r_script += 'cat(as.character(compound_0_prediction$class), " to start\\n")\n'
# for i in range(1, MAX_PITS):
#     predict_r_script += f'cat(as.character(compound_{i}_prediction$class), " at lap ",  as.character(lap_{i}_prediction$class), "\\n")\n'

with open("predict_generated.R", "w") as file:
    file.write(predict_r_script)

print("Generated predict_generated.R")

"""
    location  = c("Sakhir"),

    STR       = c(0),
    NOR       = c(0),
    HAD       = c(0),
    TSU       = c(0),
    HUL       = c(0),
    LAW       = c(0),
    ALB       = c(0),
    LEC       = c(0),
    ANT       = c(0),
    PIA       = c(0),
    BEA       = c(0),
    COL       = c(0),
    BOR       = c(0),
    OCO       = c(0),
    HAM       = c(0),
    GAS       = c(0),
    ALO       = c(0),
    SAI       = c(0),
    DOO       = c(1),
    RUS       = c(0),
    VER       = c(0),

    Spielberg = c(0),
    Baku      = c(0),
    Barcelona = c(0),
    Monaco    = c(0),
    Melbourne = c(0),
    Budapest  = c(0),
    Imola     = c(0),
    Shanghai  = c(0),
    Jeddah    = c(0),
    Monza     = c(0),
    Austin    = c(0),
    Silverstone = c(0),
    Zandvoort = c(0),
    Sakhir    = c(1),
    Suzuka    = c(0)
)

compound_0_prediction = predict(compound_0_model, new_data)
compound_1_prediction = predict(compound_1_model, new_data)
compound_2_prediction = predict(compound_2_model, new_data)
compound_3_prediction = predict(compound_3_model, new_data)

lap_1_prediction = predict(lap_1_model, new_data)
lap_2_prediction = predict(lap_2_model, new_data)
lap_3_prediction = predict(lap_3_model, new_data)

cat(as.character(compound_0_prediction$class), " to start\n")
cat(as.character(compound_1_prediction$class), " at lap ",  as.character(lap_1_prediction$class), "\n")
cat(as.character(compound_2_prediction$class), " at lap ",  as.character(lap_2_prediction$class), "\n")
cat(as.character(compound_3_prediction$class), " at lap ",  as.character(lap_3_prediction$class), "\n")

"""







