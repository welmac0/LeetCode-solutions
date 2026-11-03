class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::map<string, std::vector<std::string>> anagram_map;
        for (int i = 0; i < strs.size(); i++) {
            std::string s = strs.at(i);
            sort(s.begin(), s.end());

            if (anagram_map.find(s) != anagram_map.end()) {
                anagram_map[s].push_back(strs.at(i));
            } else {
                anagram_map[s] = {strs.at(i)};
            }
        }

        std::vector<std::vector<std::string>> result;
        for (const auto& pair : anagram_map) {
            result.push_back(pair.second);
        }

        return result;
    }
};