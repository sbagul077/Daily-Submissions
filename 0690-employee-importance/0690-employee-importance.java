/*
// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
};
*/

class Solution {
    int result;
    HashMap<Integer, Employee> map;
    public int getImportance(List<Employee> employees, int id) {
        result = 0;
        map = new HashMap<>();

        for(Employee emp: employees){
            map.put(emp.id, emp);
        }

        dfs(id);
        return result;
    }

    private void dfs(int eid){
        
        Employee e = map.get(eid);
        result += e.importance;

        for(int subid: e.subordinates){
            dfs(subid);
        }
    }
}

 //DFS
// Time Complexity: O(N)
// Space Complexity: O(N)