#include <unordered_map>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;

        for (auto &s : strs) {
            string copy = s;
            sort(copy.begin(), copy.end());
            groups[copy].push_back(s);

            // not needed c++ automatically creates a default vector
            // if (groups.find(copy) != groups.end()) {
            //     groups[copy].push_back(s);
            //     continue;
            // }

            // groups[copy] = {s};
        }
        vector<vector<string>> ret;
        for (const auto &p: groups) {
            ret.push_back(p.second);
        }
        return ret;
    }
};
