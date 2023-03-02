def ratarata(n1,n2,n3,n4,n5,n6,n7,n8):
    
    nilai=[n1,n2,n3,n4,n5,n6,n7,n8]
    nilai.sort()
    
    a=min(nilai)
    nilai.remove(a)
    b=min(nilai)
    nilai.remove(b)
    totalnilai=sum(nilai)
    rata_rata=totalnilai/6
    print(round(rata_rata))
    
n1 = int(input('n1:'))
n2 = int(input('n2:'))
n3 = int(input('n3:'))
n4 = int(input('n4:'))
n5 = int(input('n5:'))
n6 = int(input('n6:'))
n7 = int(input('n7:'))
n8 = int(input('n8:'))
ratarata(n1,n2,n3,n4,n5,n6,n7,n8)