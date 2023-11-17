xa, ya, xb, yb, xc, yc = map(int,input().split())

result = 0.0

if xa == xb == xc or ya == yb == yc :
    result = -1.0
    
elif ya-yb != 0 and ya-yc != 0 and yb-yc != 0 \
    and (xa-xb) / (ya-yb) == (xb-xc) / (yb-yc) == (xa-xc) / (ya-yc):
    result = -1.0
else :
    dAB = ((xa-xb)**2 + (ya-yb)**2) ** (1/2)
    dBC = ((xb-xc)**2 + (yb-yc)**2) ** (1/2)
    dCA = ((xc-xa)**2 + (yc-ya)**2) ** (1/2)

    result = (max(dAB, dBC, dCA) - min(dAB, dBC, dCA)) * 2

print(result)