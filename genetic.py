import random
import numpy as np 

TARGET = []
DNA_SIZE = 15
POPULATION_SIZE = 20
GENERATION_SIZE = 50

def mutation(item):

	mutate_r = random.randint(0,DNA_SIZE-1)

	if item[ mutate_r ] == 0:
		item[ mutate_r ] = 1
	else:
		item[ mutate_r ] = 0

	return item

def crossover(item1 , item2):

	split_r = random.randint(0,DNA_SIZE-1)

	item1 = np.append( item1[:split_r] , item2[split_r:] , axis = 0)
	item2 = np.append( item1[split_r:] , item2[:split_r] , axis = 0)

	return item1 , item2


def weight_choice( items ):

	top_r = random.randint(0,POPULATION_SIZE/2-1)

	return items[top_r]['population']

def random_target():

	target_r = np.random.randint(0,2,DNA_SIZE)
	return target_r

def random_population():

	population_r = np.zeros((POPULATION_SIZE,DNA_SIZE))

	for i in xrange(POPULATION_SIZE):
		population_r[i] = np.random.randint(0,2,DNA_SIZE)

	return population_r

def fitness( chromosome ):

	return np.sum( chromosome == TARGET )

if __name__ == "__main__":

	TARGET = random_target()
	population = random_population()

	for i in xrange(GENERATION_SIZE):

		print "====== Generation %s ======" %(i)
		print "Target : %s" %(TARGET)

		# Calculate each indiviadul chromsome's weight
		# Combine weight and population in one matrix , conveniently sort
		# reverse the matrix : higgest weight at the first
		weight = np.array([])
		for individual in population:
			weight = np.append( weight , fitness(individual))

		weighted_population = np.zeros((POPULATION_SIZE,) , dtype=[('population',np.int16,(DNA_SIZE)) , ('weight' , np.int16)])
		weighted_population['population'] = population
		weighted_population['weight'] = weight
		weighted_population.sort(order = 'weight')
		weighted_population[:] = weighted_population[::-1]

		population = np.zeros((POPULATION_SIZE,DNA_SIZE))

		for j in xrange(POPULATION_SIZE):

			# random choice two chromsomes which's weight ranking are more than helf
			ind1 = weight_choice( weighted_population )
			ind2 = weight_choice( weighted_population )

			# crossover two choosen chromsomes
			ind1 , ind2 = crossover(ind1,ind2)

			# mutatation rate is about 0.1
			if(random.randint(0,1000) > 900):
				mutation(ind1)
				mutation(ind2)

			population[j-1] = ind1
			population[j] = ind2

		weight = np.array([])
		for individual in population:
			weight = np.append( weight , fitness(individual))
		for i in xrange(POPULATION_SIZE):
			print "Sample'%s': '%s' , Weight '%s'" % ( i , population[i] , weight[i])


	exit()