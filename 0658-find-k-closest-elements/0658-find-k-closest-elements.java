class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        List<Integer> result = new ArrayList<>();
        if(arr == null || arr.length == 0){
            return result;
        }

        int low = 0;
        int high = arr.length - 1;

        while(high - low + 1 != k){
            if(Math.abs(arr[high] - x) >= Math.abs(arr[low] - x)){
                high--;
            }else{
                low++;
            }
        }

        for(int i = low; i<= high; i++){
            result.add(arr[i]);
        }
        return result;


    }
}