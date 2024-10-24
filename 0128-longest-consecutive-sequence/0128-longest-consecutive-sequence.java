class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums == null || nums.length == 0){
            return 0;
        }
        
        int longest = 0;
        HashSet<Integer> set = new HashSet<>();
        
        for(int num: nums){
            set.add(num);
        }
        
        // System.out.println(set);
        
        for(int num : nums){
            if(!set.contains(num - 1)){
                
                int length = 0;
                while(set.contains(num + length)){
                    length += 1;
                }
                longest = Math.max(longest, length);
            }
        }
        
        return longest;
    }
}