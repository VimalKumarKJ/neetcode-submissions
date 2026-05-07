class Solution {
public:
    bool isPalindrome(string s) {
        string required;
        for(int i = 0; i < s.length(); i++){
            if(isalnum(s[i])){
                required += tolower(s[i]);
            }
        }
        int start = 0, end = required.length() - 1;
        while(start < end){
            if(required[start] != required[end]){
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
};
