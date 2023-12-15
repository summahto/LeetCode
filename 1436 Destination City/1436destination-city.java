class Solution {
    public String destCity(List<List<String>> paths) {
        
        Map<String, String> pathMap = new HashMap<>();
        
        for(List<String> path : paths){
            pathMap.put(path.get(0), path.get(1));
        }

        for(List<String> path: paths){
            if(!pathMap.containsKey(path.get(1)))
                return path.get(1);
        }

        return null;
    }
}