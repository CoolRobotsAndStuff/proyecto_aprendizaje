library(ggplot2)
library(nnet)

data(mtcars)
#View(mtcars)
#model <- lm(dependent_variable ~ independent_variable1 + independent_variable2, data = your_data)

data = read.csv("f1data_2020-2021.csv")

#lap_n,stint_n,compounds,pit_laps,team,rain,driver_name,grid_pos

data$driver_name = as.factor(data$driver_name)
data$pit_laps    = as.factor(data$pit_laps)
data$team        = as.factor(data$team)
data$compounds   = as.factor(data$compounds)

head(data)

pit_count_model  = lm(pit_count       ~ grid + driver_name + team + rain + final, data=data)
compounds_model  = multinom(compounds ~ grid + driver_name + team + rain + final, data=data)
pit_laps_model   = multinom(pit_laps  ~ grid + driver_name + team + rain + final, data=data)


print(data)
summary(pit_count_model)

new_data = read.csv("f1data_2021-2022.csv")

new_data$team        = as.factor(new_data$team)
new_data$driver_name = as.factor(new_data$driver_name)

pit_predictions       = predict(pit_count_model, new_data)
compounds_predictions = predict(compounds_model, new_data, type = "prob")
pit_laps_predictions  = predict(pit_laps_model,  new_data, type = "prob")

results <- data.frame( new_data, 
    predicted_pit_count = pit_predictions,
    predicted_compounds = compounds_predictions,
    predicted_pit_laps = pit_laps_predictions
)

results$predicted_compounds <- factor(results$predicted_compounds, labels=levels(data$compounds))
results$predicted_pit_laps  <- factor(results$predicted_pit_laps,  labels=levels(data$pit_laps))

print(results)

#results$predicted_stint_laps <- factor(results$predicted_stint_laps, labels=levels(data$predicted_stint_laps))


# ggplot(data, aes(x = driver, y = final)) + 
#   geom_point() +
#   geom_smooth(method = "lm", se = FALSE, color = "blue") +
#   labs(title = "Regression of driver on Pit Count",
#        x = "driver",
#        y = "Final Place")
