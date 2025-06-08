x = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]
y = []; z = []

for xval in x:
    y.append(xval**2)
    z.append(xval**3)

print("The values squared from for loop are:{}".format(y))
