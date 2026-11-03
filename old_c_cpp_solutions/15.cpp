class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
    
    sort(nums.begin(), nums.end());
    int n = nums.size();
    int sum;
    vector<vector<int>> answer;

    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] > 0)
            break;

        if (i > 0 && nums[i] == nums[i-1])
            continue;

        int lo = i + 1;
        int hi = n - 1;
        while (lo < hi) {
            sum = nums[i] + nums[lo] + nums[hi];
            if (sum == 0) {
                answer.push_back({nums[i], nums[lo], nums[hi]});
                lo++;
                hi--;
                while (lo < hi && nums[lo] == nums[lo-1])
                    lo++;
                while (lo < hi && nums[hi] == nums[hi+1])
                    hi--;
            }
            else if (sum < 0)
                lo++;
            else
                hi--;
        }
    }

    return answer;
    }
};
