class Solution {
    public int candy(int[] ratings) {

        int[] candies= new int[ratings.length];
        int n = ratings.length;

        Arrays.fill(candies, 1);


        // left to right pass
        for(int i = 1; i < n; i++){
            if(ratings[i] > ratings[i - 1]){
                candies[i] = candies[i- 1] + 1;
            }
        }
        
        int result = candies[n - 1];
        //right to left pass
        for(int i = n - 2; i >= 0; i--){
            if(ratings[i] > ratings[i + 1]){
                candies[i] = Math.max(candies[i], candies[i + 1] + 1);
            }
            result += candies[i];
        }

        return result;
    }
}

// two pass
// Time Complexity: O(n)
// Space Complexity: O(n)