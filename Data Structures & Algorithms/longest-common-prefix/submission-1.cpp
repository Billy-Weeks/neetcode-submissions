class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = "";
        if (strs[0] == "") {
            return prefix;
        }
        string firstString = strs[0];
        int arrayLength = strs.size();
        int length = strs[0].size();

        for (int i = 0; i < length; i++) {
            char character = firstString[i];
            for (int j = 1; j < arrayLength; j++) {
                if (i >= strs[j].size() || strs[j][i] != character) {
                    return prefix;
                }
            }
            prefix.push_back(character);
        }
        return prefix;
    }
};