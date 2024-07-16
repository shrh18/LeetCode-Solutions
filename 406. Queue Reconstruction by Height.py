class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        print("people - ", people)
        fin = [[-1, -1]]*len(people)
        while people:
            start = 0
            steps = people[0][1] 
            for num in fin:
                if num==[-1,-1] or num[0]==people[0][0]:
                    break
                start+=1
            
            st = 0
            j=start
            while st<steps:
                if fin[j+1]==[-1,-1] or fin[j+1][0]==people[0][0]:
                    st+=1
                j+=1
            fin[j] = people[0]
            del people[0]
            # print("fin - ", fin)


        print("fin - ", fin)
        return fin    