class Graph {

    List<List<Pair<Integer, Integer>>> adjList;

    public Graph(int n, int[][] edges) {
        adjList = new ArrayList<>();
        for(int i=0; i< n ; i++){
            adjList.add(new ArrayList<>());
        }
        
        for(int [] edge : edges){
            adjList.get(edge[0]).add(new Pair<>(edge[1], edge[2]));
        }

        // System.out.println(adjList);
        // System.out.println(neighMap);
    }
    
    public void addEdge(int[] edge) {
        adjList.get(edge[0]).add(new Pair<>(edge[1], edge[2]));
        // matrix[edge[0]] [edge[1]] = edge[2];
        
    }
    
    public int shortestPath(int node1, int node2) {
        int [] dist = new int [adjList.size()];
        PriorityQueue<List<Integer>> p = new PriorityQueue<>((a, b) -> a.get(0) - b.get(0));
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[node1] = 0;
        p.offer(Arrays.asList(0,  node1));
        
        while(!p.isEmpty()){
            var curr = p.poll();
            int currDist = curr.get(0);
            int currNode = curr.get(1);

            if(currDist > dist[currNode]) 
                continue;
            
            if(currNode == node2)
                return dist[currNode];



            for(var neighbour : adjList.get(currNode)){
                int neighNode = neighbour.getKey();
                int cost = neighbour.getValue();

                if(dist[currNode] + cost < dist[neighNode]){
                    dist[neighNode] = dist[currNode] + cost;
                    p.offer(Arrays.asList(dist[neighNode], neighNode));
                }


            }
        }

        return -1;
    }


    
}

/**
 * Your Graph object will be instantiated and called as such:
 * Graph obj = new Graph(n, edges);
 * obj.addEdge(edge);
 * int param_2 = obj.shortestPath(node1,node2);
 */