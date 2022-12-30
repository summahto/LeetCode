class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        
        int i =0;
        List<Integer> missedNumbers = new ArrayList<>();
        while(i < nums.length){

            int correct = nums[i]-1;
            if (nums[i] != nums[correct]){
                swap(nums, i, correct);
            } else {
                i++;
            }

        }

        for (int j=0; j< nums.length; j++){
            if(j != nums[j] -1)
                missedNumbers.add(j+1);
        }

        return missedNumbers;
    
    }

    public static void swap(int[] nums, int i, int j) {

        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}