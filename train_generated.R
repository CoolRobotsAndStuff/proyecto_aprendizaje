
library(MASS)

data = read.csv("f1data_2019-2025_encoded.csv")
compound_0_model = lda(compound_0 ~ 
                         VER + TSU + ZHO + FIT + GAS + GRO + PER + MSC + NOR + SAI + LAT + MAZ + DEV + RUS + UNKNOWN + HUL + ALB + KUB + KVY + GIO + BOT + RAI + VET + OCO + MAG + LEC + HAM + ALO + RIC + AIT + STR + 
                         silverstone + bahrain + spa_francorchamps + zandvoort + istanbul + le_castellet + so_paulo + nrburgring + spielberg + montral + imola + suzuka + barcelona + mugello + portimo + mexico_city + melbourne + baku + marina_bay + lusail + yas_island + monza + hockenheim + singapore + austin + monaco + sochi + miami + jeddah + shanghai + sakhir + budapest + spain + monte_carlo + 
                         rain + final + grid_pos, data=data)

compound_1_model = lda(compound_1 ~ 
                         VER + TSU + ZHO + FIT + GAS + GRO + PER + MSC + NOR + SAI + LAT + MAZ + DEV + RUS + UNKNOWN + HUL + ALB + KUB + KVY + GIO + BOT + RAI + VET + OCO + MAG + LEC + HAM + ALO + RIC + AIT + STR + 
                         silverstone + bahrain + spa_francorchamps + zandvoort + istanbul + le_castellet + so_paulo + nrburgring + spielberg + montral + imola + suzuka + barcelona + mugello + portimo + mexico_city + melbourne + baku + marina_bay + lusail + yas_island + monza + hockenheim + singapore + austin + monaco + sochi + miami + jeddah + shanghai + sakhir + budapest + spain + monte_carlo + 
                         rain + final + grid_pos, data=data)

compound_2_model = lda(compound_2 ~ 
                         VER + TSU + ZHO + FIT + GAS + GRO + PER + MSC + NOR + SAI + LAT + MAZ + DEV + RUS + UNKNOWN + HUL + ALB + KUB + KVY + GIO + BOT + RAI + VET + OCO + MAG + LEC + HAM + ALO + RIC + AIT + STR + 
                         silverstone + bahrain + spa_francorchamps + zandvoort + istanbul + le_castellet + so_paulo + nrburgring + spielberg + montral + imola + suzuka + barcelona + mugello + portimo + mexico_city + melbourne + baku + marina_bay + lusail + yas_island + monza + hockenheim + singapore + austin + monaco + sochi + miami + jeddah + shanghai + sakhir + budapest + spain + monte_carlo + 
                         rain + final + grid_pos, data=data)

compound_3_model = lda(compound_3 ~ 
                         VER + TSU + ZHO + FIT + GAS + GRO + PER + MSC + NOR + SAI + LAT + MAZ + DEV + RUS + UNKNOWN + HUL + ALB + KUB + KVY + GIO + BOT + RAI + VET + OCO + MAG + LEC + HAM + ALO + RIC + AIT + STR + 
                         silverstone + bahrain + spa_francorchamps + zandvoort + istanbul + le_castellet + so_paulo + nrburgring + spielberg + montral + imola + suzuka + barcelona + mugello + portimo + mexico_city + melbourne + baku + marina_bay + lusail + yas_island + monza + hockenheim + singapore + austin + monaco + sochi + miami + jeddah + shanghai + sakhir + budapest + spain + monte_carlo + 
                         rain + final + grid_pos, data=data)

compound_4_model = lda(compound_4 ~ 
                         VER + TSU + ZHO + FIT + GAS + GRO + PER + MSC + NOR + SAI + LAT + MAZ + DEV + RUS + UNKNOWN + HUL + ALB + KUB + KVY + GIO + BOT + RAI + VET + OCO + MAG + LEC + HAM + ALO + RIC + AIT + STR + 
                         silverstone + bahrain + spa_francorchamps + zandvoort + istanbul + le_castellet + so_paulo + nrburgring + spielberg + montral + imola + suzuka + barcelona + mugello + portimo + mexico_city + melbourne + baku + marina_bay + lusail + yas_island + monza + hockenheim + singapore + austin + monaco + sochi + miami + jeddah + shanghai + sakhir + budapest + spain + monte_carlo + 
                         rain + final + grid_pos, data=data)

lap_1_model = lda(lap_1 ~ 
                         VER + TSU + ZHO + FIT + GAS + GRO + PER + MSC + NOR + SAI + LAT + MAZ + DEV + RUS + UNKNOWN + HUL + ALB + KUB + KVY + GIO + BOT + RAI + VET + OCO + MAG + LEC + HAM + ALO + RIC + AIT + STR + 
                         silverstone + bahrain + spa_francorchamps + zandvoort + istanbul + le_castellet + so_paulo + nrburgring + spielberg + montral + imola + suzuka + barcelona + mugello + portimo + mexico_city + melbourne + baku + marina_bay + lusail + yas_island + monza + hockenheim + singapore + austin + monaco + sochi + miami + jeddah + shanghai + sakhir + budapest + spain + monte_carlo + 
                         rain + final + grid_pos, data=data)

lap_2_model = lda(lap_2 ~ 
                         VER + TSU + ZHO + FIT + GAS + GRO + PER + MSC + NOR + SAI + LAT + MAZ + DEV + RUS + UNKNOWN + HUL + ALB + KUB + KVY + GIO + BOT + RAI + VET + OCO + MAG + LEC + HAM + ALO + RIC + AIT + STR + 
                         silverstone + bahrain + spa_francorchamps + zandvoort + istanbul + le_castellet + so_paulo + nrburgring + spielberg + montral + imola + suzuka + barcelona + mugello + portimo + mexico_city + melbourne + baku + marina_bay + lusail + yas_island + monza + hockenheim + singapore + austin + monaco + sochi + miami + jeddah + shanghai + sakhir + budapest + spain + monte_carlo + 
                         rain + final + grid_pos, data=data)

lap_3_model = lda(lap_3 ~ 
                         VER + TSU + ZHO + FIT + GAS + GRO + PER + MSC + NOR + SAI + LAT + MAZ + DEV + RUS + UNKNOWN + HUL + ALB + KUB + KVY + GIO + BOT + RAI + VET + OCO + MAG + LEC + HAM + ALO + RIC + AIT + STR + 
                         silverstone + bahrain + spa_francorchamps + zandvoort + istanbul + le_castellet + so_paulo + nrburgring + spielberg + montral + imola + suzuka + barcelona + mugello + portimo + mexico_city + melbourne + baku + marina_bay + lusail + yas_island + monza + hockenheim + singapore + austin + monaco + sochi + miami + jeddah + shanghai + sakhir + budapest + spain + monte_carlo + 
                         rain + final + grid_pos, data=data)

lap_4_model = lda(lap_4 ~ 
                         VER + TSU + ZHO + FIT + GAS + GRO + PER + MSC + NOR + SAI + LAT + MAZ + DEV + RUS + UNKNOWN + HUL + ALB + KUB + KVY + GIO + BOT + RAI + VET + OCO + MAG + LEC + HAM + ALO + RIC + AIT + STR + 
                         silverstone + bahrain + spa_francorchamps + zandvoort + istanbul + le_castellet + so_paulo + nrburgring + spielberg + montral + imola + suzuka + barcelona + mugello + portimo + mexico_city + melbourne + baku + marina_bay + lusail + yas_island + monza + hockenheim + singapore + austin + monaco + sochi + miami + jeddah + shanghai + sakhir + budapest + spain + monte_carlo + 
                         rain + final + grid_pos, data=data)

save(compound_0_model, file = "compound_0_lda_model.RData")
save(compound_1_model, file = "compound_1_lda_model.RData")
save(compound_2_model, file = "compound_2_lda_model.RData")
save(compound_3_model, file = "compound_3_lda_model.RData")
save(compound_4_model, file = "compound_4_lda_model.RData")

save(lap_1_model, file = "lap_1_lda_model.RData")
save(lap_2_model, file = "lap_2_lda_model.RData")
save(lap_3_model, file = "lap_3_lda_model.RData")
save(lap_4_model, file = "lap_4_lda_model.RData")
