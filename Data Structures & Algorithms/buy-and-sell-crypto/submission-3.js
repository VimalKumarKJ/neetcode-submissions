class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        var left = 0;
        var right = 1;
        var maxProfit = 0;

        while (right < prices.length){
            if(prices[left] < prices[right]){
                let currProfit = prices[right] - prices[left];
                maxProfit = Math.max(maxProfit, currProfit);
            } else {
                left = right;
            }
            right++;
        }
        return maxProfit;
    }
}
