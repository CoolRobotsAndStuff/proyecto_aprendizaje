library(nnet)
args <- commandArgs(trailingOnly = TRUE)

#cat("Hacer 2 paradas en las vueltas 11, 32. Utilizar los neumáticos HARD y MEDIUM.\n")

con = textConnection(args)
    input_data = read.csv(con)
close(con)


new_data <- data.frame(
    lap_n=c(20),
    team=c(input_data$equipo),
    rain=c(input_data$lluvia),
    driver_name=c(input_data$corredor),
    grid_pos=c(input_data$posicion),
    final=(1)
)

load("compounds_model.RData")
load("pit_laps_model.RData")

new_data$team        = as.factor(new_data$team)
new_data$driver_name = as.factor(new_data$driver_name)

compound_probs = predict(compounds_model, type = "prob")
compound_max_probabilities = colSums(compound_probs)
best_compound_index        = which.max(compound_max_probabilities)
best_compound              = colnames(compound_probs)[best_compound_index]

pit_laps_probs = predict(pit_laps_model, type = "prob")
pit_laps_max_probabilities = colSums(pit_laps_probs)
best_pit_laps_index        = which.max(pit_laps_max_probabilities)
best_pit_laps              = colnames(pit_laps_probs)[best_pit_laps_index]

cat("{\n    \"compounds\": ")
cat(gsub("'", "\"", best_compound))
cat(",\n    \"pit_laps\": ")
cat(best_pit_laps)
cat("\n}\n")


