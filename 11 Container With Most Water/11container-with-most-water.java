class Solution {
    public int maxArea(int[] height) {
        int i = 0, j = height.length -1, maxArea = 0, currArea = 0;

        while(i < j){

            if(height[i] > height[j]){

                currArea = height[j] * (j-i);
                maxArea = Math.max(currArea, maxArea);
                j--;

            } else if( height[j] > height[i]){

                currArea = height[i] * (j-i);
                maxArea = Math.max(currArea, maxArea);
                i++;

            } else {

                currArea = height[i] * (j-i);
                maxArea = Math.max(currArea, maxArea);

                if(height[i+1] > height[j-1]){
                    i++;
                } else if (height[i+1] < height[j-1]) {
                    j--;
                } else i++;
            }
        }

        return maxArea;
    }
}