class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> record;
        for (int num : nums) {
            record[num]++;
        }

        vector<pair<int, int>> freqVec;
        for (const auto& pair : record) {
            freqVec.push_back({pair.second, pair.first});
        }

        sort(freqVec.begin(), freqVec.end(), greater<pair<int, int>>());

        vector<int> result;
        for (int i = 0; i < k; ++i) {
            result.push_back(freqVec[i].second);
        }

        return result;
    }

};
