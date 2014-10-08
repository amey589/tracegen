import numpy as np
import matplotlib.pyplot as plt
import sys
file =sys.argv[1]
# Read the file.
print "file name is " + file
f2 = open(file, 'r')
# read the whole file into a single variable, which is a list of every row of the file.
lines = f2.readlines()
f2.close()

# initialize some variable to be lists:
x1 = []
y1 = []

# scan the rows of the file stored in lines, and put the values into some variables:
for line in lines:
    p = line.split(",")
    x1.append(int(p[0].strip()))
    y1.append(int(p[1].strip()))
   
xv = np.array(x1)
yv = np.array(y1)


# now, plot the data:
plt.plot(xv, yv)

plt.show()
