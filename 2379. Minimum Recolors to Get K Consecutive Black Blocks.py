class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        blocks = list(blocks)
        l, r = 1, k
        win = blocks[:k]
        print(win)
        c = Counter(win)
        print(c)
        count = c['W']
        while r<len(blocks):
            if blocks[l-1] == 'W':
                c['W'] -= 1
            else:
                c['B'] -= 1

            if blocks[r] == 'W':
                c['W'] += 1
            else:
                c['B'] += 1

            count = min(count, c['W'])
            l += 1
            r += 1

        return count