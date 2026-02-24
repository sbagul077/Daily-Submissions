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

        for(Employee emp : employees){
            map.put(emp.id, emp);
        }

        Queue<Integer> q = new LinkedList<>();
        q.add(id);

        while(!q.isEmpty()){
            int curr = q.poll();
            Employee emp = map.get(curr);

            result += emp.importance;

            for(int sub : emp.subordinates){
                q.add(sub);
            }
        }

        return result;
    }
}