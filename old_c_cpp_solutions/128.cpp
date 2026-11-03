class Solution {
    public:
        int longestConsecutive(vector<int>& nums) {
            unordered_set<int> ns(nums.begin(), nums.end());
    
            int longest = 0;
    
            for (int num : ns) {
                if (ns.find(num - 1) == ns.end()) {
                    int j = num;
                    int curr_len = 1;
    
                    while (ns.find(j+1) != ns.end()) {
                        j++;
                        curr_len++;  
                    }
                    longest = max(curr_len, longest);
                }
            }
    
            return longest;
        }
    };