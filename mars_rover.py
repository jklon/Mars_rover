#This is the soltion to the mars rover problem
from sys import exit


def main(input):
	result = []

	xmax, ymax, number, rover_actions = string_parser(input)
	
	for rover in range(0, number):
		within_bounds = True
		move_count = 0
		position = rover_actions[rover][0]
		x = position[0]
		y = position[1]
		d = position[2]

		for action in rover_actions[rover][1]:
			if within_bounds == True:
				x,y,d = operator(action,x,y,d)
				if x > xmax or x < 0 or y > ymax or y < 0:
					within_bounds = False
				else:
					move_count += 1



		if within_bounds:
			result.append('rover %d is at %d, %d, %s' %(rover + 1, x, y, resolve_direction(d)))
		else:
			result.append('The rover %d goes out of bound at the move %d ' %( rover +1, move_count + 1))

	return result

#The operator function provides the navigation logic to the rover
def operator(action, x,y,d):
	if action == 'M':
		if d%4 == 1:
			return x, y+1, d
		elif d%4 == 3:
			return x, y-1, d
		elif d%4 == 0:
			return x+1, y, d
		elif d%4 == 2:
			return x-1, y, d

	if action == 'R':
		return x, y, d - 1
	if action == 'L':
		return x, y, d + 1

#in the navigation logic, I have used direction as numbers as specified in the dict below
#The navigation logic becomes easier like this when we have to turn the rover around
def resolve_direction(d):
	L2N = {'N':1, 'E':0, 'W':2, 'S':3}
	N2L = {1:'N', 2:'W', 3:'S', 0:'E'}
	try:
		d = d%4
	except TypeError:
		pass

	if d in L2N:
		return L2N[d]
	elif d in N2L:
		return N2L[d]



#This function takes input as the text file in appropriate format
#I have tried to do some error handling here
def string_parser(input):
	number = 0
	f_end = False
	rover_actions = []

	f = open(input)
	pleatue_size = f.readline().split()
	xmax = int(pleatue_size[0])
	ymax = int(pleatue_size[1])


	while not f_end:
		position = f.readline().split()
		if len(position) > 0:
			try:
				x = int(position[0])
				y = int(position[1])
			except ValueError:
				print "Input not a valid string containing x and y coordinates in numbers"
				exit()
			d = resolve_direction(position[2].upper().rstrip())

			moves = f.readline().rstrip().upper()
			rover_actions.append(([x,y,d], moves))
			number += 1
		else:
			f_end = True
		

	return xmax, ymax, number, rover_actions
 
#drover_actions contain tuples of the starting location and
#the following action for all rovers in a list

print main('input.txt')