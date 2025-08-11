class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int minPrice = Integer.MAX_VALUE;

        for(int price : prices){
            minPrice = Math.min(price, minPrice);

            if(price > minPrice){
                maxProfit += price - minPrice;
                minPrice = price;
            }
        }

        return maxProfit;
    }
}

//Time Complexity: O(n)
//Space Complexity: O(1)