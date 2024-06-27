#include <algorithm>
#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        // counter based approach
        if (s.length() != t.length()) return false;

        unordered_map<char, int> counts;

        for (auto c: s) {
            counts[c]++;
        }

        for (auto c: t) {
            if (!counts[c]) return false;
            counts[c]--;
        }

        // sorting approach
        // sort(s.begin(), s.end());
        // sort(t.begin(), t.end());

        // for (int x = 0; x < s.size(); x++) {
        //     if (s[x] != t[x]) return false;
        // }

        return true;
    }
};
