class Solution {
    public int leastInterval(char[] tasks, int n) {
        if(tasks == null || tasks.length == 0){
            return 0;
        }

        if(n==0){
            return tasks.length;
        }

        HashMap<Character, Integer> map = new HashMap<>();
        int maxFreq = Integer.MIN_VALUE;

        for(int i = 0; i < tasks.length; i++){
            char chr = tasks[i];
            if(!map.containsKey(chr)){
                map.put(chr, 0);
            }

            map.put(chr, map.get(chr) + 1);

            maxFreq = Math.max(maxFreq, map.get(chr));
        }

        int maxCount = 0;
        for(Character chr: map.keySet()){
            if(map.get(chr) == maxFreq){
                maxCount += 1;
            }
        }


        int partitions = maxFreq - 1;
        int empty = partitions * (n - (maxCount - 1));
        int pending = tasks.length - (maxFreq * maxCount);
        int idle = Math.max(0, empty - pending);


        return tasks.length + idle;
    }
}