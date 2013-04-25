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

    print d.shape
    img = imshow(d)
    img.set_cmap("Spectral")
    colorbar()
    img.set_interpolation('nearest')
    xlabel("Feature index")
    ylabel("Feature index")
    title("Correlation of features")
    savefig("correlation_awesome.png")
    show()
