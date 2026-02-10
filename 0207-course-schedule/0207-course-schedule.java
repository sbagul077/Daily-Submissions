class Solution {

   HashMap<Integer, List<Integer>> map;

   boolean [] visited;    boolean [] path; //this path is curr path that we are making starting from a node

   public boolean canFinish(int numCourses, int[][] prerequisites) {

       visited = new boolean [numCourses];

       path = new boolean [numCourses];

       map = new HashMap<>();

       for(int [] edge : prerequisites){

           if(!map.containsKey(edge[1])){

               map.put(edge[1], new ArrayList<>());

           }

           map.get(edge[1]).add(edge[0]);

       }

       for (int i = 0; i < numCourses; i++) {

           if (!visited[i] && dfs(i)) {

               return false;

           }

       }

       return true;

   }

   //dfs is done for detecting cycle;

   private boolean dfs(int i){

       // base

       if(path[i]) return true;

       if(visited[i]) return false;        //logic

       visited[i] = true;        //action add to current path

       path[i] = true;        //recurse on all neigbours

       if(map.get(i) != null){

           for (int n : map.get(i)) {

               if (dfs(n)) return true;

           }

       }

       //backtrack

       path[i] = false;

       return false;

   }
}