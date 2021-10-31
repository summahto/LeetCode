class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0)
            return false;
        int o= x, rev = 0;
        
        while(x > 0){
            rev = rev*10 + x % 10;
            x = x/10;
        }
        
        if(o == rev)
            return true;
        
        return false;
    }
}