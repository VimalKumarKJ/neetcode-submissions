class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        var left = 0;
        const charSet = new Set();
        var result = 0;
        for(let right = 0; right < s.length; right++){
            while(charSet.has(s[right])){
                charSet.delete(s[left]);
                left++;
            }
            charSet.add(s[right]);
            result = Math.max(result, right - left + 1);
        }
        return result
    }
}
