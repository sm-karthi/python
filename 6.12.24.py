# tuples in python
tuple1 = (1, 2)
tuple2 = (3, 4)
print(tuple1 + tuple2)

print(tuple1 * 2)

print(2 in tuple1)


# Functions
def calculate(a, b):
    return a+b, a*b

print(calculate(5, 10))


# list=["karthik","santhosh","sheriff"]
# print(list)

# list.extend(["shriram"])
# print(list)

arr=[3,2,78,1,5]
arr.reverse()
print(arr)
arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)


array = [1, 2, 3, 4, 5]
odd = [i for i in array if i % 2 ==1]
print(",".join(map(str,odd)))
    