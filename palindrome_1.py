#palindrome_1 exercise : 
result1= ""
for i in range (0, 26):
    result1 += chr(ord('a')+i)
    
result2= ""
for i in range (0, 25):
    result2 += chr(ord('y')-i)

print(result1+result2)
