# This simulates the chance of drawing a blackjack on the first hand
# It should equal 4.8% with one deck and 4.7% for 8 decks, with some variation
hands.to.simulate <- 10000
number.of.decks <- 8

suit <- c("H" ,"C" ,"D", "S")
rank <- c(2:9, "T", "J", "Q", "K", "A")
deck <- NULL #create the deck
for(r in rank){ 
  deck <- c(deck, paste(r, suit)) 
}

# Assign values to cards
deck <- data.frame(deck)
deck$value <- ifelse(substr(deck$deck, 1,1) == "A", 11, 
                     ifelse(substr(deck$deck, 1,1) == "T", 10,
                            ifelse(substr(deck$deck, 1,1) == "J", 10,
                                   ifelse(substr(deck$deck, 1,1) == "Q", 10, 
                                          ifelse(substr(deck$deck, 1,1) == "K", 10, 
                                                 (substr(deck$deck, 1,1)
                                                 ))))))
deck$value <- as.numeric(deck$value) #Make it numeric

deck <- deck[rep(seq_len(nrow(deck)), number.of.decks), ] # Duplicate the deck

games <- function(n){
  draw <- deck[sample(nrow(deck), 2), ]
  result <- sum(draw$value)
  cards <- paste(draw$deck[1], " and ", draw$deck[2])
  output <- list(cards, result)
  return(output)
}

# Repeat the function x number of times and turn the results into a df
library("plyr") 
l <- alply(cbind(rep(hands.to.simulate,hands.to.simulate),rep(20,10)),1,games)
result <- data.frame(matrix(unlist(l), nrow=hands.to.simulate, byrow=T))
colnames(result) <- c("cards", "result")
result$blackjack <- ifelse(result$result == 21, "blackjack", "no")
result$tab <- ifelse(result$blackjack == "blackjack", 1, 0)

total <- sum(result$tab)
ratio <- sum(result$tab)/hands.to.simulate

print(paste0("I got ", total, " blackjacks out of ", hands.to.simulate, " simulations of the first hand, for a ratio of %", ratio * 100))