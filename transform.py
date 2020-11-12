import numpy as np
import pandas as pd
import math

class Transform():
    def __init__(self, layers):
        super(Transform, self).__init__()
        a = 6378137
        b = 6356752.314
        eSquare = 0.006694380067
        k = 1

        self.n = lambda latitude, longitude : a / (math.sqrt(1-eSquare*math.pow(math.sin(latitude*(math.pi/180)), 2)))

        self.gps2ecef = lambda latitude, longitude, altitude :
                        (self.n(latitude) + altitude) * math.cos(latitude * (math.pi / 180)) * math.cos(longitude * (math.pi / 180)),
                        (self.n(latitude) + altitude) * math.cos(latitude * (math.pi / 180)) * math.sin(longitude * (math.pi / 180)),
                        ((math.pow(b, 2) / math.pow(a, 2)) * self.n(latitude) + altitude) * math.sin(latitude * (math.pi / 180))

        self.T = np.asarray([[ 1.03466810e-01,  7.13570091e-02,  5.73534641e-03, 5.05296982e+03],
                           [ 8.11689225e-01,  5.65044091e-01,  4.99815586e-02, -9.02607910e+02],
                           [ 1.64660097e-02,  1.14957868e-02,  1.03403378e-03, -1.75385986e+02],
                           [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 1.00000000e+00]])
    
    def exec(latitude, longitude, altitude=0):
        xa, ya, za = self.gps2ecef(latitude, longitude, altitude)
        return np.dot(self.T, np.asarray([xa, ya, za, 1]).reshape(-1,1)).reshape(-1)

