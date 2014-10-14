# Monty Hall Simulation
games.to.simulate <- 5000

stick <- function(n){
  door <- data.frame(sample(1:3))
  colnames(door) <- c("prize")
  # Chose door one and stay with it
  result <- ifelse(door$prize[1] == 1, "win", "lose")
  return(result)
}

# Repeat the function x number of times and turn the results into a df
games <- data.frame(replicate(games.to.simulate, stick()))
colnames(games) <- c("result")
games$result <- ifelse(games$result == "win", 1, 0)
ratio.stick <- (sum(games$result))/games.to.simulate


switch <- function(n){
  door <- data.frame(sample(1:3))
  colnames(door) <- c("prize")
  # Chose door one and switch to the unrevealed
  first.guess <- door$prize[1]
  reveal <- ifelse(door$prize[2] != 1, door$prize[2], door$prize[3])
  final.guess <- ifelse(reveal == door$prize[2], door$prize[3], door$prize[2])
  result <- ifelse(final.guess == 1, "win", "lose")
  return(result)
}

# Repeat the function x number of times and turn the results into a df
games <- data.frame(replicate(games.to.simulate, switch()))
colnames(games) <- c("result")
games$result <- ifelse(games$result == "win", 1, 0)
ratio.switch <- (sum(games$result))/games.to.simulate


print (paste("Tactic 1: ", ratio.stick*100, " % winning chance"))
print (paste("Tactic 2: ", ratio.switch*100, " % winning chance"))

            