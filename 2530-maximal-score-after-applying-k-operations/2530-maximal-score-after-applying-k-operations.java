class Solution {
    public long maxKelements(int[] nums, int k) {
        long result = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        // PriorityQueue
        for(int i : nums){
            pq.add(i);
        }
        
        while(k > 0){
            int curr = pq.poll();
            result += curr;
            k -= 1;
            pq.add((int) Math.ceil(curr/3.0));
        }
        
        return result;
    }
}

//Time Complexity: O(klogn + nlogn)
//Space Complexity: O(n)