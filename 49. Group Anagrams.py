class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ls = defaultdict(list)
        for word in strs:
            gg = ''.join(sorted(word))
            ls[gg].append(word)
        ret = []
        for k, v in ls.items():
            ret.append(v)
        print(ret)
        return ret
