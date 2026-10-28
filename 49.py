class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        w_dict = {}
        # O(mn)
        for w in strs: # O(m)
            c_count = [0] * 26 # 26 liter alfabetu <- lepsze
            for c in w:
                nof = ord(c) - ord('a') # number of letter in alphabet
                c_count[nof] += 1

            t_count = tuple(c_count)
            # w_sorted = ''.join(sorted(w)) # O(n log n) <- slabe
            if t_count in w_dict: # O(1)
                w_dict[t_count].append(w) # O1
            else:
                w_dict[t_count] = [w] # O1

        result_list = list()
        for k in w_dict:
            result_list.append(w_dict[k])

        return result_list