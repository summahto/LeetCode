class Solution {
    public int totalMoney(int n) {
        
        int numOfWeeks = n/7;
        int rem = n%7;
        int monday = 1;
        double money = 0;
        
        while(monday <= numOfWeeks) {
            money += (7.0/2) * (monday + (monday + 6));
            monday = monday+1;             
        }
        // System.out.println(money + " :" + monday);

        money += (rem/2d)*(monday + monday + rem -1);

        // System.out.println(money);

        return (int)money;
    }
}