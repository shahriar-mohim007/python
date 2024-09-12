def getMedian(ar1,ar2,n1,n2):
    i = 0
    j = 0
    m1=m2=-1
    for _ in range((n1+n2)//2+1):
        m2 = m1
        if(i!=n1 and j!=n2):
            if ar1[i]>ar2[j]:
               m1 = ar2[j]
               j+=1
            else:
                m1 = ar1[i]
                i+=1
        elif(i<n1):
            m1 = ar1[i]
            i+=1
        else:
            m1 = ar1[j]
            j+=1
    return m1 if (n1+n2)%2 ==1 else (m1+m2)/2


        





ar1 = [1,2,3,900]
ar2 = [5, 8, 10, 20]

n1 = len(ar1)
n2 = len(ar2)
print(getMedian(ar1, ar2, n1, n2))

#median using binary search