class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        final = []
        idle = "idle"
        eachFreq = {}
        for each in tasks:
            if (each in eachFreq):
                eachFreq[each] += 1
            else:
                eachFreq[each] = 1
        
        eachFreq = sorted(eachFreq.items(), key=lambda x:x[1], reverse=True)
        eachFreq = dict(eachFreq)
        print(eachFreq)
        types = list(eachFreq.keys())
        print(types)
        
        # while(len(types)>0):
        #     cycle = n+1
        #     i=0
        #     k=0
        #     origlen=len(types)
        #     print("Origlen - ", origlen)
        #     while i<len(types):
        #         if(cycle==1 and origlen<i):
        #             maxKey = max(eachFreq, key = lambda x: eachFreq[x]) 
        #         else:
        #             maxKey = types[i]
        #         final.append(maxKey)
        #         print("appending - ", maxKey)
        #         eachFreq[maxKey] -= 1
        #         if(eachFreq[maxKey]==0):
        #             types.remove(maxKey)
        #             eachFreq.pop(maxKey)
        #         else:
        #             i+=1
        #         k+=1
        #         cycle -= 1
        #         if(k>=origlen):
        #             print("In k with ", k)
        #             while(cycle>0 and len(types)>0):
        #                 cycle -= 1
        #                 print("appending - idle")
        #                 final.append(idle)
        #         if(cycle==0):
        #             break

        # (n+1)*(f-1)+X
        # print("One line Code Key value: ", list(my_dict.keys())[list(my_dict.values()).index(100)])

        x=0
        for first,second in eachFreq.items():
            if second == eachFreq[types[0]]:
                x = x+1

        total = ((n+1)*(eachFreq[types[0]]-1)) + x
        fin = max(total, len(tasks))
        print(fin)
        return fin
        