class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for(int num : nums){
            pq.add(-num);
        }
        int result = 0;

        while(k > 0){
            result = pq.poll();
            k--;
        }

        return -result;

    }
}