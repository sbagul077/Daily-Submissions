class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int minShare = Integer.MAX_VALUE;

        for(int price : prices){
            minShare = Math.min(price, minShare);

            if(price > minShare){
                maxProfit = Math.max(maxProfit, price - minShare);
            }
        }
        
        return maxProfit;
    }
}

// Time Complexity :O(n)
// Space Complexity: O(1)