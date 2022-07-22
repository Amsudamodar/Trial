

def surfaceArea(A,H,W):
    area=0
    for i in range (H):
        for j in range(W):
            #number of unexposed faces of single cube
            r=min(A[i][j],A[i][j+1]) if ((j)<W-1) else 0
            l=min(A[i][j],A[i][j-1]) if ((j)>0) else 0
            u=min(A[i][j],A[i-1][j]) if ((i)>0) else 0
            d=min(A[i][j],A[i+1][j]) if ((i)<H-1) else 0    
            k=(A[i][j])*4+2-r-l-u-d # number of exposed faces=totalface - unexposed
            area=area+k
    print(area)        
    
   
if __name__ == '__main__':
 

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A,H,W)




