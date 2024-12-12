# n = int(input("Enter your number: "))
# if n % 2 ==0:
#     print("Even")
# else:
#     print("Odd")
  
  
# Prime number  
a = 7
isPrime = True

if a <= 1:
    isPrime = False
    
for i in range(2, a-1):
    if a % i == 0:
        isPrime = False
        break
    
if isPrime:
    print(f"{a} Prime number")
else:
    print(f"{a} Not prime number")
    
    
""" Write a function to check if a given string is a palindrome. Ignore case and spaces.
Input: "Madam"
Output: True """

name = "Madam"
reverseString = ""
check = True
for i in name:
    reverseString = i + reverseString
    
print(reverseString)

if name.lower() == reverseString.lower():
    print("True")
else:
    print("False")
    
    
    
#  Write a function to find the character that appears the most in a given string.
# Input:
# "hello world"
# Output:
# "l"

string = "hello world"
temp = 0
result = ""
for i in string:
    count = string.count(i)
    if count > temp:
        temp = count
        result = i

print(result)


""" 3. Write a function to replace all occurrences of a substring in a string with another substring.
Input:
String: "apples are red, apples are sweet"
Substring to replace: "apples"
Replacement: "oranges"
Output:
"oranges are red, oranges are sweet" """

string = "apples are red, apples are sweet"
replace = string.replace("apples", "oranges")
print(replace)

""" Write a program to count how many words in a string are palindromic. A palindromic word is a word that reads the same forwards and backwards.
Input:
"madam level hello racecar world" """

string = "madam level hello racecar world"
cal = string.split(" ")
reverse = ""
for i in cal:
    for j in i:
        reverse = j + reverse
    
print(reverse)