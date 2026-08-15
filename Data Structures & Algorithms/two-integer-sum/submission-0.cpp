class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        

        unordered_map<int, int> mapped;
        int searched;
        for (int i = 0; i < nums.size(); i++) {
            
            searched = target - nums[i];
            if (mapped.find(searched) != mapped.end()) {
                return {mapped[searched], i};
            }
            mapped[nums[i]] = i; // stores the current i value as a key and i as the value
        }
        
    }
};
