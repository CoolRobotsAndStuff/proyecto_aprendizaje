import fastf1

min_year = 2020
max_year = 2025


table = []

for year in range(min_year, max_year):
    try:
        for index, event in fastf1.get_event_schedule(year).iterrows():
            try:
                print("YEAR ", year)
                location = event["Location"]
                session = fastf1.get_session(event["EventDate"].year, event["EventName"], 5, backend="fastf1")
                session.load(laps=True, telemetry=False, weather=True, messages=False)

                out = []
                for driver_abreviation in session.drivers:
                    driver      = session.get_driver(driver_abreviation)
                    driver_laps = session.laps.pick_driver(driver["Abbreviation"])

                    row = {
                        "lap_n": 0,
                        "stint_n": 0,
                        "compounds": [],
                        "pit_laps": [],
                        "team": "UNKNOWN",
                        "rain": 0,
                        "driver_name":"UNKNOWN",
                        "grid_pos": 0,
                        "pit_count": 0,
                        "final": 0,
                        "location": location
                    }
                    for index, lap in driver_laps.iterrows():
                        lap_n         = lap["LapNumber"]
                        stint_n       = lap["Stint"]
                        compound      = lap["Compound"]
                        team          = lap["Team"]
                        rain          = session.weather_data["Rainfall"]
                        driver_name   = lap["Driver"]
                        grid_pos      = driver["GridPosition"]
                        row["lap_n"] = max(row["lap_n"], lap_n)
                        row["stint_n"] = max(row["stint_n"], stint_n)
                        if not len(row["compounds"]) or compound != row["compounds"][-1]:
                            row["compounds"].append(compound)
                            row["pit_laps"].append(lap_n);
                        row["team"] = team;
                        row["driver_name"] = driver_name;
                        row["rain"] = int(bool(rain[0]));
                        row["grid_pos"] = int(grid_pos);
                        row["final"] = lap["Position"]  

                        # print("lap_n      ", lap_n     )
                        # print("stint_n    ", stint_n   )
                        # print("compound   ", compound  )
                        # print("team       ", team      )
                        # print("rain       ", rain      )
                        # print("driver_name", driver_name)
                        # print("grid_pos   ", grid_pos  )
                    row["pit_count"] = len(row["compounds"]);
                    table.append(row)
                    #print(row)
                    #print("-----------")
            except Exception as e:
                print("ERROR:", e)

    except Exception as e:
        print("ERROR: ", e)


import csv
from io import StringIO

output = StringIO()
csv_writer = csv.DictWriter(output, fieldnames=table[0].keys())
csv_writer.writeheader()
for row in table:
    csv_writer.writerow(row)
csv_string = output.getvalue()
output.close()

with open(f"f1data_{min_year}-{max_year}.csv", "w") as file:
    file.write(csv_string)


