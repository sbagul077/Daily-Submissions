class Logger {
    HashMap<String, Integer> map;
    public Logger() {
        this.map = new HashMap<>();
    }
    
    public boolean shouldPrintMessage(int timestamp, String message) {
        if(!this.map.containsKey(message)){
            map.put(message, timestamp);
            return true;
        }

        if((timestamp - map.get(message)) >= 10){
            map.put(message, timestamp);
            return true;
        }
        return false;
    }
}

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * boolean param_1 = obj.shouldPrintMessage(timestamp,message);
 */