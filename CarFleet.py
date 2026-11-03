class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos, speed = sortByPosition(position, speed) # O(nlogn)
        timesRises = 0
        currMax = 0
        for i in range(len(speed)): # O(n)
            hours = (target - pos[i]) / speed[i]
            if hours > currMax:
                timesRises += 1
                currMax = hours
            
        return timesRises

def sortByPosition(pos: List[int], speed: List[int]):
    pairs = sorted(zip(pos, speed), reverse=True)
    return list(zip(*pairs)) 
            
'''
This one i did from the scratch all by myself and was a little bit pissed, that i dont understand how the monotonic stack works.
Have spend about 15' programming, then 30' debuging and after changing insertion sort to sorted(), got exactly the perfect solution XD

i am really really proud of myself!!!
'''


        