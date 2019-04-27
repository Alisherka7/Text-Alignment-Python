import math
width = 20
b = 1
dl = int(input())
# dl = 9# dlina bukvi
ss = dl*dl
mmm = math.ceil(dl/2) # vidayet srednyee kol stolbikov
b1 = dl*2-1

for i in range(dl):
    h = '*'*b
    print(h.center(dl*2))
    b = b+2

for i in range(dl+1):
    C = '*'*dl
    print(C.center(dl*2),''.center(dl*2-2),C.center(dl*2))

for i in range(mmm):
    C = '*'*(dl*5)
    print(C.center(dl*6))
for i in range(dl+1):
    C = '*'*dl
    print(C.center(dl*2),''.center(dl*2-2),C.center(dl*2))

#Bottom Cone
for i in range(dl):
    h1 = '*'*b1
    print(''.ljust(dl*4-1),h1.center(dl*2))
    b1 = b1-2

#################################################################################################    
#thickness = int(input()) #This must be an odd number
#c = 'G'

#Top Cone
#for i in range(thickness):
#    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
#for i in range(thickness+1):
#    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
#for i in range((thickness+1)//2):
#   print((c*thickness*5).center(thickness*6))

#Bottom Pillars
#for i in range(thickness+1):
#    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
#for i in range(thickness):
#    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
###############################################################################################################
