#include <vector>

class Solution {
    public: // Beats 100.00% in runtime :DDDDD
        std::vector<int> productExceptSelf(std::vector<int>& nums) {
            int n = nums.size();
            std::vector<int> left_arr(n);
            std::vector<int> right_arr(n);
            std::vector<int> final_arr(n);
    
            left_arr[0] = right_arr[n-1] = 1;
    
            for (int i = 1; i < n; i++) {
                left_arr[i] = nums[i-1] * left_arr[i-1];
                right_arr[n-i-1] = nums[n-i] * right_arr[n-i];
            }
    
            for (int i = 0; i < n; i++) {
                final_arr[i] = left_arr[i] * right_arr[i];
            }
    
            return final_arr;
    
    
        }
    };