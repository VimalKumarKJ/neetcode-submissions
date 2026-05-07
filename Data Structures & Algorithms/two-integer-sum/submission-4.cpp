class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int>rec;

        for(int i = 0; i < nums.size(); i++){
            int reqNum = target - nums[i];
            if(rec.find(reqNum) != rec.end()){
                return {rec[reqNum], i};
            }
            rec.insert({nums[i], i});
        }
        return {};
    }
};
