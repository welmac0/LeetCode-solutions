class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::map<int, int> num_map;
        for (int i = 0; i < nums.size(); i++) {
            num_map[nums.at(i)]++;
        }

        std::vector<std::pair<int, int>> vec(num_map.begin(), num_map.end());
        std::sort(vec.begin(), vec.end(), [](const std::pair<int, int>& a, const    std::pair<int, int>& b) {
            if (a.second != b.second) {
                return a.second > b.second;
            }
            return a.first > b.first;
        });

        std::vector<int> final_nums;
        for (int j = 0; j < k; j++) {
            final_nums.push_back(vec[j].first);
        }

        return final_nums;
    }
};