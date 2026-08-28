class Solution {
    public int hIndex(int[] citations) {
        if(citations == null || citations.length == 0){
            return 0;
        }

        Arrays.sort(citations);

        int result = 0;
        int n = citations.length;

        for(int i = 0; i < n; i++){
            int diff = n - i;

            if(diff <= citations[i]){
                return diff;
            }
        }

        return 0;
        
    }
}



// # Sorting. Iterate until difference <= citations[i]
// # Time ComplexityL O(nlogn)
// # Space Complexity: O(1)