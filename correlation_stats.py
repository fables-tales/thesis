import csv
import numpy
from pylab import *

if __name__ == "__main__":
    c = csv.reader(open("correlation.csv"))

    build = []
    for idx,row in enumerate(c):
        if idx != 0:
            build.append([float(x) for x in row[1:]])

    print build

    d = numpy.array(build)
    build = []
    for i in xrange(0,25):
        for j in xrange(0,25):
            if i != j:
                build.append(d[i,j])

    print build
    print numpy.mean(build),numpy.std(build)
