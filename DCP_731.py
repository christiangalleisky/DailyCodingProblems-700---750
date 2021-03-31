'''
while accending keep count of height
log every accentions magnitude
take a running max of those magnitudes
'''

def profitMaximizer(values):
	
	#setup vars
	min_val = 9999999999
	max_val = -999999999
	profits = [("index", "value")]

	for i, x in enumerate(values):
		
		#do all checks before updating min and max
		if i > 0 and min(x, min_val) == x:
			pp = 0
			min_val = min(x, min_val)
			max_val = min_val
		else:
			#keep running absolute max and min
			min_val = min(x, min_val)
			max_val = max(x, max_val)
			pp = max_val - min_val
		profits.append((i, pp))
	return profits


nums = [5,7,12,3,1]
obj = profitMaximizer(nums)
print(obj)
