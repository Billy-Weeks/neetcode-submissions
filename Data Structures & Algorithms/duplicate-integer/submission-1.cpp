class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int length = nums.size();
        int target = 0;
        while (target < length) {
            int checker = target + 1;
            while (checker < length) {
                if (nums[target] == nums[checker]) {
                    return true;
                }
                else {
                    checker++;
                }
            }
            target++;
        }
        return false;
    }
};