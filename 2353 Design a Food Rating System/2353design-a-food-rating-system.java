class FoodRatings {

    class Food implements Comparable<Food>{
        int foodRating;
        String foodName;

        public Food(int foodRating, String foodName){
            this.foodRating = foodRating;
            this.foodName = foodName;
        }

        @Override
        public int compareTo(Food other){

            if(this.foodRating == other.foodRating)
                return this.foodName.compareTo(other.foodName);

            return other.foodRating - this.foodRating;
        }
    }

    Map<String, Integer> foodRatingMap = new HashMap<>();
    Map<String, String> foodCuisineMap = new HashMap<>();
    Map<String, PriorityQueue<Food>> cuisineFoodMap= new HashMap<>();

    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        
        for(int i=0; i< foods.length; i++){
            foodRatingMap.put(foods[i], ratings[i]);
            foodCuisineMap.put(foods[i], cuisines[i]);
            cuisineFoodMap.computeIfAbsent(cuisines[i], k -> new PriorityQueue<>()).add(new Food(ratings[i], foods[i]));
        }
        
    }
    
    public void changeRating(String food, int newRating) {
        foodRatingMap.put(food, newRating);
        String cuisine = foodCuisineMap.get(food);
        cuisineFoodMap.get(cuisine).add(new Food(newRating, food));
        
    }
    
    public String highestRated(String cuisine) {
        PriorityQueue<Food> pq = cuisineFoodMap.get(cuisine);
        
        while(foodRatingMap.get(pq.peek().foodName) != pq.peek().foodRating ){
            pq.poll();
        }
        
        return pq.peek().foodName;
        
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings obj = new FoodRatings(foods, cuisines, ratings);
 * obj.changeRating(food,newRating);
 * String param_2 = obj.highestRated(cuisine);
 */