class Solution {
public:

    int getIndex(char s){
        return (int(s) - int('a'));
    }

    bool isAnagram(string s, string t) {
        if (s.length() != t.length()){
            return false;
        }

        vector<int>checkAnagram(26, 0);

        for(int i = 0; i < s.length(); i++){
            int indexS = getIndex(s[i]);
            int indexT = getIndex(t[i]);
            checkAnagram[indexS] += 1;
            checkAnagram[indexT] -= 1;
        }

        for(int i = 0; i < checkAnagram.size(); i++){
            if (checkAnagram[i] != 0){
                return false;
            }
        }
        return true;
    }
};
