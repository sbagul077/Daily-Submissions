class Solution {
    public int[] nextGreaterElements(int[] nums) {
        if(nums == null || nums.length == 0){
            return new int[-1];
        }

        int n = nums.length;
        Stack<Integer> st = new Stack<>();
        int[] result = new int[n];

        Arrays.fill(result, -1);

        for(int index = 0; index < (n * 2); index++){

            int currIndex = index % n;

            while(!st.isEmpty() && nums[currIndex] > nums[st.peek()]){
                int top = st.pop();
                result[top] = nums[currIndex];
            }

            if(index < n){
                st.add(currIndex);
            }
        }
        return result;
    }
}

// #monotonic stack
// #Time Complexity: O(n)
// #Space Complexity:O(n)