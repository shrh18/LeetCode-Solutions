class Solution {
    public void sortColors(int[] nums) {
        // red = 0
        // white = 1
        // blue = 2
        // int z=0,o=0,t = 0;
        Arrays.sort(nums);

        // for(int i=0; i<nums.length; i++){
        //     if(nums[i] == 0){
        //         z++;
        //     }
        //     else if(nums[i] == 1){
        //         o++;
        //     }
        //     else{
        //         t++;
        //     }
        // }
        // System.out.println("z = "+z);
        // System.out.println("o = "+o);
        // System.out.println("t = "+t);

        // for(int i=0; i<z; i++){
        //     nums[i] = 0;
        // }
        // for(int i=z; i<z+o; i++){
        //     nums[i] = 1;
        // }
        // for(int i=z+o; i<z+o+t; i++){
        //     nums[i] = 2;
        // }

    }
}