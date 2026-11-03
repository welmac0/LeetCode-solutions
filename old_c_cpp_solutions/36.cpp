class Solution {
    public:
        bool isValidSudoku(vector<vector<char>>& board) {
            for (int i = 0; i < 9; i++) {
                vector<int> count_col(10, 0);
                vector<int> count_row(10, 0);
                for (int j = 0; j < 9; j++) {
                    // kolumny i wiersze
                    if (board[j][i] != '.') {
                        count_col[board[j][i] - '0'] += 1;
                        if (count_col[board[j][i]  - '0'] > 1)
                            return false;
                    }
                    
                    if (board[i][j] != '.') {
                        count_row[board[i][j]  - '0'] += 1;
                        if (count_row[board[i][j]  - '0'] > 1)
                            return false;
                    }
                }
            }
            // 3x3
            for (int i = 0; i < 9; i += 3) {
                for (int j = 0; j < 9; j += 3) {
                    vector<int> count(10, 0);
    
                    for (int k = i; k < i + 3; k++) {
                        for (int l = j; l < j + 3; l++) {
                            
                            if (board[k][l] != '.') {
                                count[board[k][l]  - '0'] += 1;
                                if (count[board[k][l] - '0'] > 1)
                                    return false;
                            }
                        }
                    }
                }
            }
    
            return true;
        }
    };