class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int length = nums.size();
        vector<int> ans(2 * length);
        for (int i = 0; i < length; i++) {
            ans[i] = nums[i];
        }
        for(int i = length; i < 2 * length; i++) {
            ans[i] = nums[i - length];
        }
        return ans;
    }
};