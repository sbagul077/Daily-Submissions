class Solution {
    public int maxEqualRowsAfterFlips(int[][] matrix) {
        Map<String, Integer> map = new HashMap<>();
        
        for(int[] curr : matrix){
            StringBuilder patternBuilder = new StringBuilder("");
            
            for(int col = 0; col < curr.length; col++){
                if(curr[0] == curr[col]){
                    patternBuilder.append("T");
                }else{
                    patternBuilder.append("F");
                }
            }
            
            String rowPattern = patternBuilder.toString();
            map.put(rowPattern, map.getOrDefault(rowPattern, 0) + 1);
        }
        
        int maxFreq = 0;
        
        for(int freq : map.values()){
            maxFreq = Math.max(freq, maxFreq);
        }
        
        return maxFreq;
    }
}