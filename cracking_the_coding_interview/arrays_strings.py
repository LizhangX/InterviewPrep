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

def URLify(s):
	