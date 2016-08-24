# Number of throws needed to ensure all phases of a die has occurred at least once? With 99% certainty.
# https://www.reddit.com/r/statistics/comments/4z8oud/number_of_throws_needed_to_ensure_all_phases_of_a/

import random
import numpy as np
 
di = range(1,7)
 

def find_rolls_until_all_six():
	rolls = [ ]
	while len(set(rolls)) < 6:
		new_roll = random.choice(di)
		rolls.append(new_roll)
	return rolls


def get_distribution(n_sims):
	distribution = [ ]
	for i in range(0,n_sims):
		i = len(find_rolls_until_all_six())
		distribution.append(i)
	return distribution


a = np.array(get_distribution(10000))
p = np.percentile(a, 99)

print(p)