class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        List<Integer> result = new ArrayList<>();
      
        // Binary search to find the closest position to x
        int left = 0, right = arr.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] < x) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        // Initialize two pointers around the closest position
        left = right - 1;
        
        // Expand around the closest position to find k elements
        while (k > 0) {
            if (left < 0) {
                right++;
            } else if (right >= arr.length || Math.abs(arr[left] - x) <= Math.abs(arr[right] - x)) {
                left--;
            } else {
                right++;
            }
            k--;
        }

        // Collect the elements between left and right pointers
        for (int i = left + 1; i < right; i++) {
            result.add(arr[i]);
        }
        
        return result;
    }
}
