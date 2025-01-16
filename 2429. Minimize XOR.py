class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        b1, b2 = format(num1, '032b'), format(num2, '032b')
        cc1, cc2 = Counter(b1), Counter(b2)

        if cc1['1'] == cc2['1']:
            return num1
        
        app = cc2['1']
        ret = ['0']*len(b1)

        if cc1['1']>cc2['1']:
            for i in range(len(ret)):
                if app == 0:
                    break
                if b1[i] == '1':
                    ret[i] = '1'
                    app -= 1
        else:
            for i in range(len(ret)-1, -1, -1):
                if app == 0:
                    break
                if b1[i] == '1':
                    ret[i] = '1'
                    app -= 1
            if app>0:
                for i in range(len(ret)-1, -1, -1):
                    if app == 0:
                        break
                    if b1[i] == '0':
                        ret[i] = '1'
                        app -= 1
        ret = "".join(ret) 
        return int(ret, 2)
            