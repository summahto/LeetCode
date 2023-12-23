class Solution {
    public boolean isPathCrossing(String path) {

        Set<String> pts = new HashSet<>();

        pts.add("0:0");
        int x = 0, y = 0;
        for(char c : path.toCharArray()){
            if(c == 'N')
                x++;
            else if(c == 'S')
                x--;
            else if(c == 'E')
                y++;
            else
                y--;

            if(!pts.add(String.valueOf(x) + ":" + String.valueOf(y)))
                return true;

        }

        // System.out.println(pts);

        return false;
    }
}