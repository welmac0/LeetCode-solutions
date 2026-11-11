print(-3 // 2)  # -2
print(int(-3 // 2))  # -1

float("inf")
float("-inf")

arr = [1, 2, 3]
arr.append(5)  # O(1)
arr.pop()  # O(1)
arr.insert(1, 7)  # O(n)
arr[3] = 0  # O(1)
n = 5
arr = [1] * n
print(arr[-1])
print(arr[1:3])  # [arr[1], arr[2]]

a, b, c = [1, 2, 3]  # unpacking

nums = [4, 5, 6]
for i, n in enumerate(nums):
    print(i, n)

for n1, n2 in zip(arr, nums):
    print(n1, n2)

nums.sort(reverse=True)
nums.reverse()

names = ["Maciej", "Konrad", "Wełpa"]
arr.sort(key=lambda x: len(x))

arr = [i for i in range(5)]
arr = [2 * i for i in range(5)]
arr2d = [[0] * 4 for _ in range(4)]

# [[0] *4] * 4 <- THIS DOESN'T WORK
s = "abc"
# s[0] = c doesnt work

# ascii value of a character:
print(ord("a"))
print(" ".join(f"{names}"))

# list act as stack

from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()

mySet = {i for i in range(5)}
myMap = {i: 2 * i for i in range(3)}

for key in myMap:
    print(key)

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)

tup = (1, 2, 3)  # can be used as key in hashmap

import heapq

minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

heapq.heappop(minHeap)  # usuwa od elementu min

# max heap -> push -[int] and return pop as -1[.pop()]


class MyClass:
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)

    def getLen(self):
        return self.size

    def getDoubleLen(self):
        return 2 * self.getLen()

    def getOnePrivate():
        return 1

    @staticmethod
    def staticGetLen(nums):
        return len(nums)
