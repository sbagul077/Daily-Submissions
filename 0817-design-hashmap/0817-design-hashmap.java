
class MyHashMap {
    class Node {
        int key;
        Node next;
        int val;

        public Node(int key, int val) {
            this.key = key;
            this.val = val;

        }
    }

    Node[] nodesArr;
    int arrLen;

    public MyHashMap() {
        arrLen = 10000;
        nodesArr = new Node[arrLen];
    }

    //returns hashIndex
    private int getHashValue(int key) {
        return Integer.hashCode(key) % arrLen;
    }

    private Node find(Node head, int key) {
        // int hashValue = getHashValue(key);
        Node prev = null; // dummy node
        Node curr = head;

        while (curr != null && curr.key != key) {
            prev = curr;
            curr = curr.next;
        }
        return prev;

    }

    public void put(int key, int value) {
        int index = getHashValue(key);
        if (nodesArr[index] == null) {
            nodesArr[index] = new Node(-1, -1);
        }

        Node prev = find(nodesArr[index], key);
        if (prev.next == null) {
            prev.next = new Node(key, value);
        } else {
            prev.next.val = value;
        }
    }

    public int get(int key) {
        int index = getHashValue(key);
        if(nodesArr[index] == null){
            return -1;
        }
        Node prev = find(nodesArr[index], key);
        if (prev.next == null) {
            return -1;
        }else{
            return prev.next.val;
        }
    }

    public void remove(int key) {
        int index = getHashValue(key);
        if (nodesArr[index] == null) {
            return;
        }
        Node prev = find(nodesArr[index], key);
        if(prev.next == null){
            return;
        }
        else{
            
            prev.next = prev.next.next;
        }

    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */