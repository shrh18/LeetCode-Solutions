# class Solution:
#     def letterCasePermutation(self, s: str) -> List[str]:
#         def permut(nums, ans, s, k, arr):
#                 if k<len(arr) and arr[k] not in nums:
#                     arr1 = copy.deepcopy(arr)
#                     arr1[k] = arr1[k].lower()
#                     if "".join(arr1) not in ans:
#                         ans.append("".join(arr1))
#                     permut(nums, ans, s, k+1, arr1)
#                     arr2 = copy.deepcopy(arr)
#                     arr2[k] = arr2[k].upper()
#                     if "".join(arr2) not in ans:
#                         ans.append("".join(arr2))
#                     permut(nums, ans, s, k+1, arr2)
#                 else:
#                     if k<len(arr):
#                         permut(nums, ans, s, k+1, arr)
#                     else:
#                         return
                        
#         nums = ['0','1','2','3','4','5','6','7','8','9']
#         ans = []
#         ans.append(s)
#         for k in range(len(s)):
#             permut(nums, ans, s, k, list(s))        
#         print(ans)
#         return ans

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(sub: str, i: int):
            if i == len(s):
                ans.append(sub)
                return
            if s[i].isalpha():
                backtrack(sub + s[i].lower(), i + 1)
                backtrack(sub + s[i].upper(), i + 1)
            else:
                backtrack(sub + s[i], i + 1)
                
        ans = []
        backtrack("", 0)
        return ans