class Solution {
    boolean[] path;
    boolean[] visited;
    HashMap<Integer, List<Integer>> map;
    
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        
        path = new boolean[numCourses];
        visited = new boolean[numCourses];
        map = new HashMap<>();
        
        for(int[] edge: prerequisites){
            if(!map.containsKey(edge[1])){
                map.put(edge[1], new ArrayList<>());
            }
            
            map.get(edge[1]).add(edge[0]);
        }
        
        
        for(int i = 0; i < numCourses; i++){
            if(!visited[i] && dfs(i)){
                return false;
            }
        }
        
        return true;
    }
    
    private boolean dfs(int course){
        if(path[course]) return true;
        
        if(visited[course]) return false;
        
        visited[course] = true;
        path[course] = true;
        
        if(map.get(course) != null){
            for(int n: map.get(course)){
                if( dfs(n)) return true;
            }
        }
        // backtrack
        path[course] = false;
        return false;
    }
}