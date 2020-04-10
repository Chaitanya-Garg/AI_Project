def TOH(n,a,b,c): 
    if n == 0:return
    TOH(n-1, a, c, b)
    print ("Move disk from rod",a,"to rod",c)
    TOH(n-1, b, a, c)

n = 3
TOH(n, 'A', 'B', 'C')