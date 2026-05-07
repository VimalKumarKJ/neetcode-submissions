class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        map<int, int>record;
        for(int i = 0; i < n; i++){
            int req_num = target - nums[i];
            if(record.find(req_num) != record.end()){
                return {record[req_num], i};
            }
            record.insert({nums[i], i});
        }
        return {};
    }
};
