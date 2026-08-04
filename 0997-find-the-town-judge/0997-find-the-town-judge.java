class Solution {
    public int findJudge(int n, int[][] trust) {
        // if(trust.length == 0 || trust == null){
        //     return 1;
        // }
        int[] indegrees = new int[n + 1];

        for(int i = 0; i < trust.length; i++){
            int trustee = trust[i][0];
            int trusted = trust[i][1];

            indegrees[trustee] -= 1;
            indegrees[trusted] += 1;
        }

        for(int i = 1; i <= n; i++){
            if(indegrees[i] == n - 1){
                return i;
            }
        }
        // System.out.println(Arrays.toString(indegrees));

        return -1;
    }
}

// Time Complexity: O(n)
// Space Complexity: O(n)