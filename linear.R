library(ggplot2)
library(nnet)

data(mtcars)
#View(mtcars)
#model <- lm(dependent_variable ~ independent_variable1 + independent_variable2, data = your_data)

data = read.csv("f1data_2000-2025.csv")


data$driver_name = as.factor(data$driver_name)
data$pit_laps    = as.factor(data$pit_laps)
data$team        = as.factor(data$team)
data$compounds   = as.factor(data$compounds)

compounds_model  = multinom(compounds ~ grid_pos + driver_name + team + rain + final, data=data, MaxNWts =10000000)
pit_laps_model   = multinom(pit_laps  ~ grid_pos + driver_name + team + rain + final, data=data, MaxNWts =10000000)


print(data)
#summary(pit_count_model)

#save(pit_count_model, file = "pit_count_model.RData")
save(compounds_model, file = "compounds_model.RData")
save(pit_laps_model , file = "pit_laps_model.RData")

#results$predicted_stint_laps <- factor(results$predicted_stint_laps, labels=levels(data$predicted_stint_laps))


# ggplot(data, aes(x = driver, y = final)) + 
#   geom_point() +
#   geom_smooth(method = "lm", se = FALSE, color = "blue") +
#   labs(title = "Regression of driver on Pit Count",
#        x = "driver",
#        y = "Final Place")
