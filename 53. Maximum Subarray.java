class Solution {
    public int maxSubArray(int[] nums) {
        // Brute force method
        // int max = nums[0], sum = 0;
        // for(int i=0; i<nums.length; i++){
        //     for(int j=i; j<nums.length; j++){
        //         for(int k=i; k<=j; k++){
        //             sum = sum + nums[k];  
        //         }
        //         // System.out.println("sum = "+sum);
        //         if(sum > max){
        //             max = sum;
        //         }
        //         sum = 0;        
        //     }
        //     // System.out.println();
        //     sum = 0;
        // }
        // System.out.println(max);
        // return max;

        // Solving it with Kadane's Algo
        int currMax = nums[0], glMax = nums[0];
        for(int i=1; i<nums.length; i++){
            currMax = Math.max(nums[i], currMax + nums[i]);
            if(currMax > glMax){
                glMax = currMax;
            }
        }
        return glMax;

    }
}