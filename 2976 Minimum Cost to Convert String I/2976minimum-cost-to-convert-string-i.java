class Solution {
    public long minimumCost(String source, String target, char[] original, char[] changed, int[] cost) {
        
        Map<Character, List<Pair<Character, Integer>>> adjList = new HashMap<>();
        Set<Character> uniq = new HashSet<>();

        for(int i=0 ; i< original.length; i++){
            
            adjList.computeIfAbsent(original[i], k -> new ArrayList<>()).add(new Pair<>(changed[i], cost[i]));
            uniq.add(original[i]);
            uniq.add(changed[i]);
        }

        // System.out.println(adjList);
        Map<Pair<Character, Character>, Integer> memo = new HashMap<>();

        Map<Character, Integer> distMap = new HashMap<>();
        PriorityQueue<Pair<Integer, Character>> pq = new PriorityQueue<>((a, b) -> a.getKey() - b.getKey());
        long totalCost = 0;

        for(int i=0 ; i< source.length() ; i++){
            
            if(source.charAt(i) == target.charAt(i))
                continue;

            else{
                Pair<Character, Character> p = new Pair<>(source.charAt(i), target.charAt(i));

                if(memo.containsKey(p)){
                    totalCost += memo.get(p);
                    continue;
                }


                for(Character key: uniq){
                    distMap.put(key, Integer.MAX_VALUE);
                }

                distMap.put(source.charAt(i), 0);
                pq.add(new Pair<>(0, source.charAt(i)));
                boolean pathFound = false;

                Set<Character> seen = new HashSet<>();

                while(!pq.isEmpty()){
                    // System.out.println(i + " : " + totalCost +  " : " + pq);
                    
                    Pair<Integer, Character> curr = pq.poll();
                    int currD = curr.getKey();
                    Character currCh = curr.getValue();

                    if(currD > distMap.get(currCh))
                        continue;

                    if(currCh == target.charAt(i)){
                        totalCost += distMap.get(currCh);
                        memo.put(p, distMap.get(currCh));
                        pathFound = true;
                        break;
                    }

                    if(!adjList.containsKey(currCh)){
                        continue;
                    }

                    if(!seen.contains(currCh)){
                        seen.add(currCh);
                        for(var neighbour : adjList.get(currCh)){
                            int neighCost = neighbour.getValue();
                            Character neighCh = neighbour.getKey();

                            if(currD + neighCost < distMap.get(neighCh)){
                                distMap.put(neighCh, currD + neighCost);
                                pq.add(new Pair<>(currD + neighCost, neighCh));
                            }
                        }
                    }
                        
                }

                if (!pathFound)
                    return -1;

                pq.clear();
                seen.clear();
            }
        }

        return totalCost;
    }
}