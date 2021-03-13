import random

def make_starting_four():
	nums = []
	for _ in range(0, 4):
		x = random.randint(1, 9)
		nums.append(x)
	return nums

def play_24(n):
	print("24")
	
def apply_ops(a, b):
    return [a + b, a - b, a * b, a / b]

def play(nums):
    if len(nums) == 1:
        return nums[0] == 24
    elif len(nums) == 2:
        return any(play([x]) for x in apply_ops(*nums))
    else:
        for i in range(len(nums) - 2):
            for x in apply_ops(*nums[i : i + 2]):
                if play(nums[:i] + [x] + nums[i + 2:]):
                    return True
        return False	
	


print(play_24(make_starting_four()))
	
print(play(make_starting_four()))
