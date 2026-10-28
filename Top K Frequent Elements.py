class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_f = {}
        spotted_nums = set()
        for n in nums: # O(n)
            dict_f[n] = dict_f.get(n, 0) + 1
            spotted_nums.add(n)

        k_i = 0
        chosen_s = set()
        while k_i < k: # O(k)
            max_f = -1
            max_v = -9999
            for n in spotted_nums: # O(n)
                if n in chosen_s: 
                    continue

                f = dict_f.get(n, 0)
                if f > max_f:
                    max_f = f
                    max_v = n
            if max_v != -9999:
                chosen_s.add(max_v)
                
            k_i += 1
                
        return list(chosen_s)
    
print(Solution.topKFrequent(Solution, nums=[1,2,2,3,3,3], k=2))

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_f = {} # On
        for n in nums:
            dict_f[n] = dict_f.get(n, 0) + 1

        max_freq = -1
        bucket_s = {}
        for n in dict_f: # On
            freq = dict_f[n]
            if freq > max_freq:
                max_freq = freq

            if freq in bucket_s:
                bucket_s[freq].append(n)
            else:
                bucket_s[freq] = [n]

        ret_list = [] 
        for f in range(max_freq, 0, -1): # On, bo petla sie rozklada
            if f in bucket_s:
                ret_list.extend(bucket_s[f])

        return ret_list[:k]