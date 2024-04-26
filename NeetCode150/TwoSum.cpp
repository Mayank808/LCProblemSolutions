#import <unordered_map> 

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // two pointer approach also possible by sorting the array but unnecissary
        
        unordered_map<int, int> seen;

        for (int x = 0; x < nums.size(); x++) {
            int val = nums[x];
            if (seen.find(target - val) != seen.end()) {
                return {seen[target - val], x};
            }
            seen[val] = x;
        }

        return {-1, -1};        
    }
};
