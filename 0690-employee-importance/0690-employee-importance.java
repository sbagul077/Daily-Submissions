/*
// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
};
*/

class Solution {
    public int getImportance(List<Employee> employees, int id) {
        int result = 0;

        HashMap<Integer, Employee> map = new HashMap<>();

        for(Employee emp: employees){
            map.put(emp.id, emp);
        }

        Queue<Integer> q = new LinkedList<>();
        q.add(id);


        while(!q.isEmpty()){
            Employee currEmp = map.get(q.poll());

            result += currEmp.importance;

            for(int i = 0; i< currEmp.subordinates.size(); i++){
                q.add(currEmp.subordinates.get(i));
            }
        }

        return result;
    }
}

//BFS
// Time Complexity: O(N)
// Space Complexity: O(N)