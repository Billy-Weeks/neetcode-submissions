//#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
       if (s.size() != t.size()) {
        return false; // can't be an anagram if not same size
       }

       unordered_map<char, int> track;

       for (char c : s) {
        track[c]++;
       }

       for (char c : t) {
        if (track.count(c) == 0) {
            return false; // t has a char NOT in s
        }
        track[c]--;
        if (track[c] < 0) return false; // t has MORE of that char than s
       }

       return true; 
    }
};
