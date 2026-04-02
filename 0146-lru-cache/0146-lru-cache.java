class Node{
    int key;
    int val;
    Node next;
    Node prev;

    public Node(int key, int val){
        this.key = key;
        this.val = val;
        // this.next = null;
        // this.prev = null;
    }
}

class LRUCache {
    int capacity;
    HashMap<Integer, Node> map;
    Node head;
    Node tail;

    public LRUCache(int capacity) {
        map = new HashMap<>();
        this.capacity = capacity;
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head.next = tail;
        tail.prev = head;
        
    }
    
    private void removeNode(Node node){
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void addNode(Node node){
        node.next = head.next;
        node.prev = head;
        head.next.prev = node;        
        head.next = node;

        // node.next = head.next;
        // node.prev = head;
        // head.next.prev = node;  // ✅ fix: move this BEFORE changing head.next
        // head.next = node;
    }

    public int get(int key) {
        if(!map.containsKey(key)){
            return -1;
        }
        
        Node currNode = map.get(key);
        // System.out.println(currNode.val);
        removeNode(currNode);
        addNode(currNode);
        return currNode.val;
    }
    
    public void put(int key, int value) {
        // System.out.println(value);
        if(map.containsKey(key)){
            Node node = map.get(key);
            node.val = value;
            removeNode(node);
            addNode(node);
        }else{
            if(map.size() == capacity){
                Node tailPrevNode = tail.prev;
                System.out.println(tailPrevNode.val);
                removeNode(tailPrevNode);
                map.remove(tailPrevNode.key);
            }
            System.out.println(value);
            System.out.println(map.size()+ "Size");
            Node newNode = new Node(key, value);
            addNode(newNode);
            map.put(key, newNode); 
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */