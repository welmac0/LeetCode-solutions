class Solution {
    public:
    
        string encode(vector<string>& strs) {
            string new_string;
            for (const string& str : strs)
                new_string += to_string(str.length()) + "#" + str;
    
            return new_string;
        }
    
        vector<string> decode(string s) {
            vector<string> strs;
            int i = 0;
    
            while (i < s.length()) {
                int sep = s.find("#", i);
                int len = stoi(s.substr(i, sep-i));
                i = sep + 1;
                strs.push_back(s.substr(i, len));
                i += len;
    
            }
    
            return strs;
        }
    };
    