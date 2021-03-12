
b_String_True = "(){[]}()"
b_String_False = "()){(])"
print(b_String_True)
print(b_String_False)

def analyze_mirror(s):
	y = len(s) - 1
	for x in range(len(s) // 2):
		if s[x] == '(' and s[y-x] != ')':
			return False
		if s[x] == ')' and s[y-x] != '(':
			return False
		if s[x] == '{' and s[y-x] != '}':
			return False
		if s[x] == '}' and s[y-x] != '{':
			return False
		if s[x] == '[' and s[y-x] != ']':
			return False
		if s[x] == ']' and s[y-x] != '[':
			return False
	return True
	
def bracket_balance(s):
	#open to the left = -1
	#open to the right = +1
	square_bracket_count = 0
	curly_bracket_count = 0
	circular_bracket_count = 0
	if(len(s) % 2 != 0):
		print("Not Even Length")
		return False
	for x in s:
		if x == '(':
			circular_bracket_count += 1
		elif x == ')':
			circular_bracket_count -= 1
		elif x == '{':
			curly_bracket_count += 1
		elif x == '}':
			curly_bracket_count -= 1
		elif x == '[':
			square_bracket_count += 1
		elif x == ']':
			square_bracket_count -= 1
		#check in each iteration to see if
		#there is a negative number of brackets
		#ie: unrecoverable amount of leftness
		if (square_bracket_count < 0 or curly_bracket_count < 0 or circular_bracket_count < 0):
			return False
	#final state, balance, ie: 0 for all counts
	if (square_bracket_count != 0 and curly_bracket_count != 0 and circular_bracket_count != 0):
		return False
	else:
		return True


ex_s0 = "[}]" 
ex_s1 = "((()))"
ex_s2 = "([]{)}"
ex_s3 = "blah"

print(bracket_balance(ex_s0))
print(bracket_balance(ex_s1))
print(bracket_balance(ex_s2))
print(bracket_balance(ex_s3))
