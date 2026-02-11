class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] indegrees = new int[numCourses];
        HashMap<Integer, List<Integer>> map = new HashMap<>();

        int count = 0;

        for(int [] course: prerequisites){
            indegrees[course[0]]++;

            if(!map.containsKey(course[1])){
                map.put(course[1], new ArrayList<>());
            }

            map.get(course[1]).add(course[0]);
        }

        Queue<Integer> q = new LinkedList<>();

        for(int i = 0; i < indegrees.length; i++){
            if(indegrees[i] == 0){
                q.add(i);
                count++;
            }
        }

        if(q.isEmpty()){
            return false;
        }

        while(!q.isEmpty()){
            int curr = q.poll();
            List<Integer> currList = map.get(curr);

            if(currList != null){
                for(int child : currList){
                    indegrees[child]--;

                    if(indegrees[child] == 0){
                        q.add(child);
                        count++;
                    }
                }
            }
        }


        return count == numCourses;
    }
}

//Graph
// Time Complexity: O(V+E)
// Space Complexity: O(V+E)