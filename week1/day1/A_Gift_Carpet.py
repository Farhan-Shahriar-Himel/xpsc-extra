def __():
        
        [n, m] = list(map(int, input().split()))

        s = []
        for _ in range(n):
            wrd = input()
            s.append(wrd)

        v = I = k = a = False

        for i in range(m):               
               for j in range(n):                      
                      if s[j][i] == 'v' and not v:
                             v = True
                             break
                      elif s[j][i] == 'i' and v and not I:
                             I = True
                             break
                      elif s[j][i] == 'k' and v and I and not k:
                             k = True
                             break
                      elif s[j][i] == 'a' and v and I and k:
                             return "YES"
                      
        return "NO"


for _ in range(int(input())):
        print(__())
