class Solution {
    public List<String> letterCombinations(String digits) {
        // System.out.println(numMap.toString());
        List<String> ans = new ArrayList<>();
        
        if(digits == null || digits.length() == 0)
            return ans;
        
        char [][] map = new char [][]{ {}, {}, {'a', 'b', 'c'}, {'d', 'e', 'f'}, {'g', 'h', 'i'}, {'j', 'k', 'l'}, {'m', 'n', 'o'}, {'p', 'q', 'r', 's'}, {'t', 'u', 'v'}, {'w', 'x', 'y','z'}};

        backtrack(digits, ans, map, new StringBuilder(), 0);
        return ans;
    }


    public void backtrack(String digits, List<String> ans, char[][]map, StringBuilder sb, int start){

            if(start == digits.length()){
                ans.add(new String(sb));
                return;
            }

            int num = digits.charAt(start)  - '0';
            for(int i= 0; i<map[num].length ; i++){

                sb.append(map[num][i]);
                backtrack(digits, ans, map, sb, start + 1);
                sb.deleteCharAt(sb.length() - 1);
            }

        } 
}