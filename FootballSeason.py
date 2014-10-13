# # Simulate a season of football

# Sports betting is now largely the domain of computer algorithms. For this challenge we will model a simplified season of American football. Take a list of six teams, e.g., '49ers', 'Broncos', 'Seahawks', 'Pats', 'Jets', 'Giants'. Now, have the teams play each other in random combinations for five games (no teams are eliminated from play). To simplify things, assume each team has a 50/50 shot of winning each game they play. Finally, model the season to find out how likely it is that at least one team will have an undefeated season. Express that as a percent, e.g., "there is a X% chance that..." Bonus: find the probability that exactly two teams will go undefeated. Double bonus: change the odds that certain teams will win in matches against other ones.

# http://www.reddit.com/r/dailyprogrammer_ideas/comments/2iwyqb/easy_model_an_undefeated_football_season/


import random

def week_one():
	winners = random.sample(set(['49ers', 'Broncos', 'Seahwaks', 'Pats', 'Jets', 'Giants']),3)
	return winners


weeks = range(1,6)

def season():
	winners = []
	for w in weeks:
		winners += week_one()
	return winners


def undefeated():
	outcome = season()
	undefeated_teams = set([x for x in outcome if outcome.count(x) >= 5])
	count = len(undefeated_teams)
	return count


def model(numSims):
	count_zero_undefeated = 0
	count_one_undefeated = 0
	count_two_undefeated = 0
	count_three_undefeated = 0

	for i in range(0,numSims):
		success = undefeated()
		if success == 0:
			count_zero_undefeated += 1
		if success == 1:
			count_one_undefeated += 1
		if success == 2:
			count_two_undefeated += 1
		if success == 3:
			count_three_undefeated += 1
	return (count_one_undefeated + count_two_undefeated + count_three_undefeated)


print("There is an {0:.0f}% chance that at least one team will go undefeated".format((model(10000))/100))

