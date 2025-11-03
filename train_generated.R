
library(MASS)

data = read.csv("f1data_2000-2025_encoded.csv")
compound_0_model = lda(compound_0 ~ 
                         LEC + ALO + STR + SAI + ALB + NOR + OCO + BEA + DOO + HUL + LAW + GAS + RUS + BOR + PIA + TSU + HAM + HAD + ANT + COL + VER + 
                         budapest + shanghai + zandvoort + spielberg + jeddah + baku + silverstone + imola + austin + suzuka + montral + monza + monaco + melbourne + mexico_city + barcelona + sakhir + marina_bay + miami_gardens + spa_francorchamps + 
                         rain + final + grid_pos, data=data)

compound_1_model = lda(compound_1 ~ 
                         LEC + ALO + STR + SAI + ALB + NOR + OCO + BEA + DOO + HUL + LAW + GAS + RUS + BOR + PIA + TSU + HAM + HAD + ANT + COL + VER + 
                         budapest + shanghai + zandvoort + spielberg + jeddah + baku + silverstone + imola + austin + suzuka + montral + monza + monaco + melbourne + mexico_city + barcelona + sakhir + marina_bay + miami_gardens + spa_francorchamps + 
                         rain + final + grid_pos, data=data)

compound_2_model = lda(compound_2 ~ 
                         LEC + ALO + STR + SAI + ALB + NOR + OCO + BEA + DOO + HUL + LAW + GAS + RUS + BOR + PIA + TSU + HAM + HAD + ANT + COL + VER + 
                         budapest + shanghai + zandvoort + spielberg + jeddah + baku + silverstone + imola + austin + suzuka + montral + monza + monaco + melbourne + mexico_city + barcelona + sakhir + marina_bay + miami_gardens + spa_francorchamps + 
                         rain + final + grid_pos, data=data)

compound_3_model = lda(compound_3 ~ 
                         LEC + ALO + STR + SAI + ALB + NOR + OCO + BEA + DOO + HUL + LAW + GAS + RUS + BOR + PIA + TSU + HAM + HAD + ANT + COL + VER + 
                         budapest + shanghai + zandvoort + spielberg + jeddah + baku + silverstone + imola + austin + suzuka + montral + monza + monaco + melbourne + mexico_city + barcelona + sakhir + marina_bay + miami_gardens + spa_francorchamps + 
                         rain + final + grid_pos, data=data)

lap_1_model = lda(lap_1 ~ 
                         LEC + ALO + STR + SAI + ALB + NOR + OCO + BEA + DOO + HUL + LAW + GAS + RUS + BOR + PIA + TSU + HAM + HAD + ANT + COL + VER + 
                         budapest + shanghai + zandvoort + spielberg + jeddah + baku + silverstone + imola + austin + suzuka + montral + monza + monaco + melbourne + mexico_city + barcelona + sakhir + marina_bay + miami_gardens + spa_francorchamps + 
                         rain + final + grid_pos, data=data)

lap_2_model = lda(lap_2 ~ 
                         LEC + ALO + STR + SAI + ALB + NOR + OCO + BEA + DOO + HUL + LAW + GAS + RUS + BOR + PIA + TSU + HAM + HAD + ANT + COL + VER + 
                         budapest + shanghai + zandvoort + spielberg + jeddah + baku + silverstone + imola + austin + suzuka + montral + monza + monaco + melbourne + mexico_city + barcelona + sakhir + marina_bay + miami_gardens + spa_francorchamps + 
                         rain + final + grid_pos, data=data)

lap_3_model = lda(lap_3 ~ 
                         LEC + ALO + STR + SAI + ALB + NOR + OCO + BEA + DOO + HUL + LAW + GAS + RUS + BOR + PIA + TSU + HAM + HAD + ANT + COL + VER + 
                         budapest + shanghai + zandvoort + spielberg + jeddah + baku + silverstone + imola + austin + suzuka + montral + monza + monaco + melbourne + mexico_city + barcelona + sakhir + marina_bay + miami_gardens + spa_francorchamps + 
                         rain + final + grid_pos, data=data)

save(compound_0_model, file = "compound_0_lda_model.RData")
save(compound_1_model, file = "compound_1_lda_model.RData")
save(compound_2_model, file = "compound_2_lda_model.RData")
save(compound_3_model, file = "compound_3_lda_model.RData")

save(lap_1_model, file = "lap_1_lda_model.RData")
save(lap_2_model, file = "lap_2_lda_model.RData")
save(lap_3_model, file = "lap_3_lda_model.RData")
