class Solution:
    '''
    I had no idea how to approach it with stacks. This solution is done in 30 minuts, but writing it itself was about 10.
    '''
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures.copy()
        result = [0] * len(temps)
        for i_t in range(len(temps)):
            following_colder = 1
            i_temp = temps[i_t]
            for j_t in range(i_t + 1, len(temps)):
                if temps[j_t] < i_temp:
                    following_colder += 1
                else:
                    result[i_t] = following_colder
                    break

        return result
    
'''
First time i had to watch solution to get know how to solve this. anyway, comes in handy.
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # chcemy zrobic monotonic stack order
        stack = [] # [ [t, i], ... ]
        result = len(temperatures) * [0]
        for i in range(len(temperatures)):
            t = temperatures[i]
            i = i
            while stack and stack[-1][0] < t:
                # usuwany
                i_popped = stack[-1][1]
                stack.pop()
                result[i_popped] = i - i_popped
            stack.append([t, i])
        return result




    
    
    