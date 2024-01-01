class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        
        int i = 0; // pointer for g
        int j = 0; // pointer for s
        
        while(i < g.length){
            while(j < s.length && g[i] > s[j]){
                j++;
            }
            if(j < s.length){
                i++;
                j++;
            }
            else{
                break;
            }
        }
        
        return i;        
            
    }
}


// Sorting and Two Pointers
// Time Complexity: O(nlogn + mlogm)
// Space Complexity :O(1)
                