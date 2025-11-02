library(MASS)

data = read.csv("f1data_2000-2025_encoded.csv")

compound_0_model <- lda(compound_0 ~
                            Spielberg + Baku + Barcelona + Monaco + Melbourne + Budapest + Imola + Shanghai + Jeddah + Monza + Austin + Silverstone + Zandvoort + Sakhir + Suzuka
                            + BEA + HAD + PIA + ALB + COL + LEC + RUS + STR + TSU
                            + BOR + OCO + HUL + GAS + LAW + HAM + VER + DOO + NOR + SAI + ALO + ANT
                            + rain + final + grid_pos, data=data)

compound_1_model <- lda(compound_1 ~
                            Spielberg + Baku + Barcelona + Monaco + Melbourne + Budapest + Imola + Shanghai + Jeddah + Monza + Austin + Silverstone + Zandvoort + Sakhir + Suzuka
                            + BEA + HAD + PIA + ALB + COL + LEC + RUS + STR + TSU
                            + BOR + OCO + HUL + GAS + LAW + HAM + VER + DOO + NOR + SAI + ALO + ANT
                            + rain + final + grid_pos, data=data)

compound_2_model <- lda(compound_2 ~
                            Spielberg + Baku + Barcelona + Monaco + Melbourne + Budapest + Imola + Shanghai + Jeddah + Monza + Austin + Silverstone + Zandvoort + Sakhir + Suzuka
                            + BEA + HAD + PIA + ALB + COL + LEC + RUS + STR + TSU
                            + BOR + OCO + HUL + GAS + LAW + HAM + VER + DOO + NOR + SAI + ALO + ANT
                            + rain + final + grid_pos, data=data)

compound_3_model <- lda(compound_3 ~
                            Spielberg + Baku + Barcelona + Monaco + Melbourne + Budapest + Imola + Shanghai + Jeddah + Monza + Austin + Silverstone + Zandvoort + Sakhir + Suzuka
                            + BEA + HAD + PIA + ALB + COL + LEC + RUS + STR + TSU
                            + BOR + OCO + HUL + GAS + LAW + HAM + VER + DOO + NOR + SAI + ALO + ANT
                            + rain + final + grid_pos, data=data)

lap_1_model <- lda(lap_1 ~
                            Spielberg + Baku + Barcelona + Monaco + Melbourne + Budapest + Imola + Shanghai + Jeddah + Monza + Austin + Silverstone + Zandvoort + Sakhir + Suzuka
                            + BEA + HAD + PIA + ALB + COL + LEC + RUS + STR + TSU
                            + BOR + OCO + HUL + GAS + LAW + HAM + VER + DOO + NOR + SAI + ALO + ANT
                            + rain + final + grid_pos, data=data)

lap_2_model <- lda(lap_2 ~
                            Spielberg + Baku + Barcelona + Monaco + Melbourne + Budapest + Imola + Shanghai + Jeddah + Monza + Austin + Silverstone + Zandvoort + Sakhir + Suzuka
                            + BEA + HAD + PIA + ALB + COL + LEC + RUS + STR + TSU
                            + BOR + OCO + HUL + GAS + LAW + HAM + VER + DOO + NOR + SAI + ALO + ANT
                            + rain + final + grid_pos, data=data)

lap_3_model <- lda(lap_3 ~
                            Spielberg + Baku + Barcelona + Monaco + Melbourne + Budapest + Imola + Shanghai + Jeddah + Monza + Austin + Silverstone + Zandvoort + Sakhir + Suzuka
                            + BEA + HAD + PIA + ALB + COL + LEC + RUS + STR + TSU
                            + BOR + OCO + HUL + GAS + LAW + HAM + VER + DOO + NOR + SAI + ALO + ANT
                            + rain + final + grid_pos, data=data)


save(compound_0_model, file = "compound_0_lda_model.RData")
save(compound_1_model, file = "compound_1_lda_model.RData")
save(compound_2_model, file = "compound_2_lda_model.RData")
save(compound_3_model, file = "compound_3_lda_model.RData")

save(lap_1_model, file = "lap_1_lda_model.RData")
save(lap_2_model, file = "lap_2_lda_model.RData")
save(lap_3_model, file = "lap_3_lda_model.RData")


new_data <- data.frame(
    rain      = c(0),
    grid_pos  = c(1),
    pit_count = c(2),
    final     = c(1.0),
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




