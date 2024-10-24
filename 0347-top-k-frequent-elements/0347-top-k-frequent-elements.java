import java.util.List;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        if(nums == null || nums.length == 0){
            return new int[]{};
        }
        
        int[] res = new int[k];
        int max = Integer.MIN_VALUE;
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for(int num: nums){
            map.put(num, map.getOrDefault(num, 0) + 1);
            max = Math.max(max, map.get(num));            
        }
        
        List [] bucketArr = new List[max + 1];
        

        for(int key: map.keySet()){
            int index = map.get(key);
            if(bucketArr[index] == null){
                bucketArr[index] = new ArrayList<>();
            }
                
            bucketArr[index].add(key);
            
    }   
    
        for(int i = max; i >= 0 && k > 0; i--){
            if(bucketArr[i] != null){
                List<Integer> list = bucketArr[i];
                for(int j=0; j< bucketArr[i].size() && k>0; j++){
                    res[k- 1] = list.get(j);
                    k--;
                }
            }
        }
        
        return res;
    }
}