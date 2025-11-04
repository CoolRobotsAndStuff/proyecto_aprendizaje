import common
import io
import subprocess
import csv
import json
import time

def calc_efficiency(comps_ganador, comps_prediccion, 
                    vueltas_ganador, vueltas_predichas, time_taken):
    def kendall_tau(comps_ganador: list, comps_prediccion: list) -> float:
        cgs_i = []
        for cg in comps_ganador:
            if cg in comps_prediccion:
                cgs_i.append(cg)

        cps_i = []
        for cg in comps_prediccion:
            if cg in comps_ganador:
                cgs_i.append(cg)

        n = len(cgs_i)
        concordantes = 0
        discordantes = 0
        for i in range(n):
            for j in range(n):
                pass
        
        # TODO
        return 0.5

    o = 0.5

    print("time taken: ", time_taken)
    t = 1 - (min(time_taken, 5*60)/(5*60))
    print("t:", t)
    
    normalization = 10
    d = 0
    for vuelta_g in vueltas_ganador:
        d_parcial = max(vueltas_ganador)
        for vuelta_p in vueltas_predichas:
            d_parcial = min(abs(vuelta_g - vuelta_p), d_parcial)

        d += min(max(d_parcial/normalization, 0), 1)

    d = d / (len(vueltas_ganador) if len(vueltas_ganador) != 0 else 0.0000001)
    d = 1.0-d

    print("d: ", d)


    G = set(comps_ganador)
    P = set(comps_prediccion)

    # print("G:", comps_ganador)
    # print("P:", comps_prediccion)

    c = len((G.intersection(P)))/max(len(G), len(P))

    print("c: ", c)

    ng = len(vueltas_ganador)   #nro de paradas ganador
    np = len(vueltas_predichas) #nro de paradas predichas
    n = 1 - min(abs(ng - np), 4)/4

    print("n: ", n)

    efficiency =  0.2 * n + 0.3 * d + 0.2 * c + 0.2 * o + 0.1 * t

    return efficiency

with open(f"{common.fname}_test_encoded.csv", "r") as file:
    test_data = file.readlines()

header = test_data.pop(0)

efficiencies = []
for line in test_data:
    start_time = time.time()

    line = header + line

    winner_data = list(csv.DictReader(io.StringIO(line)))[0]

    comps_ganador = []
    vueltas_ganador = []
    for key, value in winner_data.items():
        if key.startswith('compound'):
            comps_ganador.append(value)

        if key.startswith('lap'):
            vueltas_ganador.append(value)

    max_laps      = vueltas_ganador.index('null') if 'null' in vueltas_ganador else len(vueltas_ganador)
    max_compounds = comps_ganador.index('null')   if 'null' in comps_ganador else len(comps_ganador)
    max_stops = min(max_laps, max_compounds)

    vueltas_ganador = vueltas_ganador[:max_stops]
    comps_ganador   = comps_ganador[:max_stops]


    vueltas_ganador = [int(float(v)) for v in vueltas_ganador]



    command = ["Rscript", "predict_generated.R", line]

    result = subprocess.run(command, capture_output=True, text=True, check=False)
    try:
        result.check_returncode()
        #print("Trying to parse this:\n", result.stdout)
        data = json.loads(result.stdout)

        laps = data["laps"]
        compounds = [c.strip() for c in data["compounds"]]

        max_laps = laps.index(None) if None in laps else len(laps)
        max_compounds = compounds.index('null') if 'null' in compounds else len(compounds)

        max_stops = min(max_laps, max_compounds)

        vueltas_predichas = laps[:max_stops]
        comps_prediccion = compounds[:max_stops]


        vueltas_predichas = vueltas_predichas[1:]
        vueltas_ganador = vueltas_ganador[1:]

        print("--------------------------------")

        print("comps_ganador:   ", comps_ganador)
        print("comps_prediccion:", comps_prediccion)

        print("vueltas_ganador:  ", vueltas_ganador)
        print("vueltas_predichas:", vueltas_predichas)

        efficiency = calc_efficiency(comps_ganador, comps_prediccion, vueltas_ganador, vueltas_predichas, time_taken = time.time()-start_time)


        print("Efficiency: ", efficiency)
        efficiencies.append(efficiency)


    except subprocess.CalledProcessError:
        print("Error:", result.stderr)
        exit()

avg_efficiency = sum(efficiencies) / len(efficiencies)
print("------------------------------------")
print("Average Efficiency:", avg_efficiency)
print("------------------------------------")

