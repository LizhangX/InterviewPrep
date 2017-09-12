import sys

class Solution:
    def __init__(self):
        self.q = []
        self.s = []
    
    def pushCharacter(self, c):
        self.q.append(c)
    def popCharacter(self):
        return self.q.pop(0)
    def enqueueCharacter(self, c):
        self.s.append(c)
    def dequeueCharacter(self):
        return self.s.pop()

# read the string s
s=raw_input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l / 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    sys.stdout.write ("The word, "+s+", is a palindrome.")
else:
    sys.stdout.write ("The word, "+s+", is not a palindrome.")    