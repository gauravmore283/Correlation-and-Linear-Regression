#Gaurav More
#PRN: 10303320181124510065

import math

x = [15 ,12 ,8 ,8 ,7 ,7 ,7 ,6 ,5 ,3]
y = [10 ,25 ,17 ,11 ,13 ,17 ,20 ,13 ,9 ,15]
n=10
xsum =0
ysum =0

for i in range (0,n):
    xsum=xsum+x[i]
    ysum=ysum+y[i]

x_mean = float((xsum)/n)
y_mean = float((ysum)/n)

y_sq=0
x_sq=0
product=0

for i in range (0,n):
  x_sq+=(x[i]-x_mean)**2
  y_sq+=(y[i]-y_mean)**2
  product+=(x[i]-x_mean)*(y[i]-y_mean)
res=float(product)/math.sqrt(x_sq*y_sq)
print (res)  
