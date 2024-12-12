fruits = ["apple", "banana", "apple", "orange", "banana", "apple",]


temp = 0
result = ""
for i in fruits:
    count = 0
    for j in fruits:  
        if i == j:
            count = count +1
            
    if count > temp:
        temp = count
        result = i
print(result)



for i in range(2, 11, 2):
    print(i)
