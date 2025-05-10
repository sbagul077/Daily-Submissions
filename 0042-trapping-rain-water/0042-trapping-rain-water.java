class Solution {
    public int trap(int[] height) {
        if(height == null || height.length == 0){
            return 0;
        }

        int left = 0;
        int right = height.length - 1;
        int lw = 0;
        int rw = 0;
        int result = 0;

        while(left <= right){
            if(lw <= rw){
                if(lw > height[left]){
                    result += lw - height[left];
                    left += 1;
                }
                else{
                    lw = height[left];
                    left++;
                }
            }

            else{
                if(rw > height[right]){
                    result += rw - height[right];
                    right -= 1;
                }
                else{
                    rw = height[right];
                    right -= 1;
                }
            }
        }

        return result;
    }
}


// 2 pointers
//Time Complexity: O(n)
//Space Complexity: O(1)