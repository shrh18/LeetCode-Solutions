class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        meetings.sort()
        i = 1
        while i<len(meetings):
            if meetings[i][0] < meetings[i-1][1]:
                if meetings[i-1][1] < meetings[i][1]:
                    meetings[i] = [meetings[i-1][0], meetings[i][1]]
                else:
                    meetings[i] = [meetings[i-1][0], meetings[i-1][1]]
                del meetings[i-1]
            else:
                i += 1
        count = meetings[0][0] - 1
        for i in range(1, len(meetings)):
            if meetings[i-1][1] < meetings[i][0]:
                count += (meetings[i][0] - meetings[i-1][1] - 1)

        count += (days - meetings[-1][1])

        return count