class Solution { // beats 100.00%!!!! :D
    public:
        bool isPalindrome(string s) {
            string asc;
            for (auto& x : s) {
                if (isalnum(x))
                    asc += tolower(x);
            }
    
            string reversed = asc;
            std::reverse(reversed.begin(), reversed.end());
    
            if (reversed == asc) {
                return true;
            }
    
            return false;
        }
    };