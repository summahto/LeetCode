class Solution {

    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        boolean [][] visited = new boolean [image.length][image[0].length]; 
        dfs(image, sr, sc, color, image[sr][sc], visited);
        return image;

    
    }

    public void dfs(int[][] image, int sr, int sc, int newColor, int baseColor, boolean [][] visited ){

        int lr = image.length;
        int lc = image[0].length;

//        System.out.println("--" + sr);
//        System.out.println("++" + sc);

        if(sr < 0 || sr >= lr || sc < 0 || sc >= lc || image[sr][sc] != baseColor || visited [sr][sc] == true)
            return;

        visited[sr][sc] = true;

        image[sr][sc] = newColor;
        dfs(image, sr+1, sc, newColor, baseColor, visited);
        dfs(image, sr-1, sc, newColor, baseColor, visited);
        dfs(image, sr, sc+1, newColor, baseColor, visited);
        dfs(image, sr, sc-1, newColor, baseColor, visited);
    }
}