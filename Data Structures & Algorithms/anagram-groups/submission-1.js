class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const anagram_map = {};

        for(let word of strs){
            var sortedWord = word.split('').sort().join('');

            if(!anagram_map[sortedWord]){
                anagram_map[sortedWord] = [];
            }
            anagram_map[sortedWord].push(word);
        }

        const result = Object.values(anagram_map);
        return result;
    }
}
