class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0;
        int j = height.size() - 1;
        int V = 0;
        int curr_v, width;

        curr_v = 0;

        while (i < j) {
            width = j-i;
            curr_v = min(height[i], height[j]) * width;

            V = curr_v > V ? curr_v : V;
            if (height[j] < height[i]) j--;
            else i++;
        }

        return V;
    }
};