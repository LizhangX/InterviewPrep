### This is the interview questions from the book "Cracking the Coding Interview"
### Chapter: Arrays and Strings

## 1.1 Is Unique: 
## Implement an algorithm to determine if a sting has all unique characters. 
## What if you cannot use additional data structures?
## Hints: 44, 117, 132

def isUnique(string):
	for i in range(len(string)):
		for j in range(i+1,len(string)):
			if string[i] == string[j]:
				return "not all unique"
	return "all unique"

# s1 = "lol"
# s2 = "load"
# print isUnique(s1)
# print isUnique(s2)


## 1.2 Check Permutation:
## Given two strings, write a method to decide if one is a permutation of the other.
## Hints: 1, 84, 122, 131

def isPermutation(s1, s2):
	a = list(s1)
	b = list(s2)
	a.sort()
	b.sort()
	if a == b:
		return "is permutaion"
	return "not permutation"

# print isPermutation("lol","llo")
# print isPermutation("lol","ll")

## 1.3 URLify:
## Write a method to replace all spaces in a string with '%20', You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)
## Example
## Input: "Mr John Smith     ", 13
## Output: "Mr%20John%20Smith"
## Hints: 53, 118

def URLify(s, l):
	arr = []
	for i in range(l):
		if s[i] == " ":
			arr.append("%20")
		else:
			arr.append(s[i])
	return ''.join(arr)

# print URLify("Mr John Smith     ", 13)


## 1.4 Palindrome Permutation:
## Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
## Example
## Input: Tact Coa
## Output: True(permutations:"taco cat","atco cta", etc.)

def palindromePermutation(s):
	s = s.lower().replace(" ","")
	d = {}
	for i in s:
		if i not in d:
			d[i] = 1
		else:
			d[i] += 1
	midpoint = False
	for j in d:
		if d[j] % 2 == 1:
			if midpoint == True:
				return False
			else:
				midpoint = True
	return True
			
print palindromePermutation("Tact Coa")
			
			
