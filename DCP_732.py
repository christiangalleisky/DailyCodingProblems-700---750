def bin_packing_problem(people, limit):

	people.sort()
	
	if people[-1] > limit :
		return -1
		
	head = 0
	tail = len(people) - 1
	boats = 0
	
	while head < tail:
		
		if (people[head] + people[tail]) <= limit:
			head += 1; tail -= 1; boats += 1
		else:
			tail -= 1; boats += 1
	 
	return boats
	 
people = [12, 54, 33, 76, 27, 32]
limit = 90

print(bin_packing_problem(people, limit))
