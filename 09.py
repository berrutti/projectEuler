for c in range(3,997):
    for b in range(2,c):
        for a in range(1,b):
            if (a+b+c==1000):
                sumOfSquares = a**2+b**2
                cSquared = c**2
                if (sumOfSquares==cSquared):
                    print('a: '+str(a))
                    print('b: '+str(b))
                    print('c: '+str(c))
                    print('Sum of squares: '+str(sumOfSquares))
                    print('c squared: '+str(cSquared))
                    print('a*b*c: '+str(a*b*c))
                    break