class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        
        Map<Integer, Integer> pos = new HashMap<>();
        // int [] ngr2 = new int [nums2.length];

        // for(int i=0 ; i< nums2.length; i++){
        //     pos.put(nums2[i], i);
        // }

        int i=nums2.length -1;
        Stack<Integer> s = new Stack<>();

        while(i >= 0){

            while(!s.isEmpty() && nums2[i] > s.peek()){
                s.pop();
            }

            if(!s.isEmpty()){

                if(nums2[i] < s.peek()){
                    // ngr2[j--] = s.peek();
                    pos.put(nums2[i], s.peek());
                }
                
            } 
            s.push(nums2[i--]);
        }

        // System.out.println(Arrays.toString(ngr2));
        // System.out.println(pos);

        // int [] ngr1 = new int [nums1.length];
        // int m =0;

        for(int k=0 ; k< nums1.length; k++){
            // int index = pos.get(nums1[k]);
            // ngr1[m++] = ngr2[index];

            nums1[k] = pos.getOrDefault(nums1[k], -1);
        }

        return nums1;

    }
}