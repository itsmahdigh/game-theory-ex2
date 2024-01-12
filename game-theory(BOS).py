expay = {                    
    'y1':[
        [[2,1],[0,0]],
        [[0,0],[1,2]],
        ],
    'n1':[
        [[2,0],[0,2]],
        [[0,1],[1,0]],
        ],

    'y2':[
        [[0,1],[2,0]],
        [[1,0],[0,2]]
    ],
    'n2':[
        [[0 , 0] , [2 , 2]] ,
        [[1 , 1] , [0 , 0]] ,
        ]

}

yy = [       
    [(2,1), (0,0)],
    [(0,0), (1,2)]
]
yn = [
    [(2,0), (0,2)],
    [(0,1), (1,0)]
]
ny = [
    [(0,1), (2,0)],
    [(1,0), (0,2)]
]
nn = [
    [(0,0), (2,2)],
    [(1,1), (0,0)]
]



p = 0.5    
q = 1/3

for i in [0,1]:   
    for row in [0,1]:
        for col in [0,1]:
            expay['y1'][i][row][col] = round(p*yy[i][row][0] + (1-p)*yn[i][col][0],3)
            expay['n1'][i][row][col] = round(p*ny[i][row][0] + (1-p)*nn[i][col][0],3)
            expay['y2'][i][col][row] = round(q*yy[row][i][1] + (1-q)*ny[col][i][1],3)
            expay['n2'][i][col][row] = round(q*yn[row][i][1] + (1-q)*nn[col][i][1],3)


br1 = [[-1,-1],[-1,-1]]     

if yy[0][0][0] > yy[1][0][0]:
    br1[0][0] = 0 
else: 1
if ny[0][0][0] > ny[1][0][0]:
    br1[1][0] = 0
else: 1

if yy[0][1][0] > yy[1][1][0]:
    br1[0][1] = 0 
else: 1
if ny[0][1][0] > ny[1][1][0]:
    br1[1][1] = 0  
else: 1


br2 = [[-1,-1],[-1,-1]]     

if yy[0][0][1] > yy[0][1][1]:
    br2[0][0] = 0 
else: 1
if yn[0][0][1] > yn[0][1][1]:
    br2[0][1] = 0 
else: 1

if yy[1][0][1] > yy[1][1][1]:
    br2[1][0] = 0  
else: 1
if yn[1][0][1] > yn[1][1][1]:
    br2[1][1] = 0 
else: 1

ne1 = [-1,-1] 
ne2 = [-1,-1]


for ac in [0,1]:
     resp = br2[ac]
     if not (expay['y1'][ac][resp[0]][resp[1]] < expay['y1'][(ac+1)%2][resp[0]][resp[1]]):
         ne1[0] = ac

for ac in [0,1]:
     resp = br2[ac]
     if not (expay['n1'][ac][resp[0]][resp[1]] < expay['n1'][(ac+1)%2][resp[0]][resp[1]]):
         ne1[1] = ac

if br2[ne1[0]] == br2[ne1[1]]:
    print(f"Nash Equilibrium for player 1: ({ne1}, {br2[ne1[0]]})")
else:
    print(f"NO Nash Equilibrium for player 1 !")

for ac in [0,1]:
     resp = br1[ac]
     if not (expay['y2'][ac][resp[0]][resp[1]] < expay['y2'][(ac+1)%2][resp[0]][resp[1]]):
         ne2[0] = ac

for ac in [0,1]:
     resp = br1[ac]
     if not (expay['n2'][ac][resp[0]][resp[1]] < expay['n2'][(ac+1)%2][resp[0]][resp[1]]):
         ne2[1] = ac

if br1[ne2[0]] == br1[ne2[1]]:
    print (f"Nash Equilibrium for player 2: ({ne2}, {br1[ne2[0]]})")
else:
    print(f"NO Nash Equilibrium for player 2 !")