#include <set>
#include <algorithm>

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {

        sort(nums.begin(), nums.end());
        for (int x = 1; x < nums.size(); x++) {
            if (nums[x] == nums[x - 1]) {
                return true;
            }
        }

        // set<int> seen;
        // for (auto &x: nums) {
        //     if (seen.find(x) != seen.end()) {
        //         return true;
        //     }
        //     seen.insert(x);
        // }        

        return false;
    }
};
