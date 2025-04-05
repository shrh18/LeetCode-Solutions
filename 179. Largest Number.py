class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums = list(map(str, nums))
        print(nums)

        def compare(a, b):
            return (b+a) > (a+b)

        nums.sort(key=cmp_to_key(lambda a,b: 1 if compare(a, b) else -1))

        return "0" if nums[0] == "0" else "".join(nums)