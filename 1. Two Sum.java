class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];
        int[] def = {0,1};
        if(nums.length==2){
            return def;
        }
        else{
            for(int i=0; i<nums.length-1; i++){
                for(int j=i+1; j<nums.length; j++){
                    if(nums[i]+nums[j]==target){
                        ans[0]=i; ans[1]=j;
                    }
                }
            }
        }
        return ans;
    }
}