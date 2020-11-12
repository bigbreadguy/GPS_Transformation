import numpy as np
import math

class Transform():
    def __init__(self):
        super(Transform, self).__init__()
        self.a = 6378137
        self.b = 6356752.314
        self.eSquare = 0.006694380067
        self.k = 1

        self.T = np.asarray([[ 1.03466810e-01,  7.13570091e-02,  5.73534641e-03, 5.05296982e+03],
                           [ 8.11689225e-01,  5.65044091e-01,  4.99815586e-02, -9.02607910e+02],
                           [ 1.64660097e-02,  1.14957868e-02,  1.03403378e-03, -1.75385986e+02],
                           [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, 1.00000000e+00]])

    def n(self, latitude, longitude=0):
        return self.a / (math.sqrt(1-self.eSquare*math.pow(math.sin(latitude*(math.pi/180)), 2)))
    
    def gps2ecef(self, latitude, longitude, altitude):
        x = (self.n(latitude) + altitude) * math.cos(latitude * (math.pi / 180)) * math.cos(longitude * (math.pi / 180))
        y = (self.n(latitude) + altitude) * math.cos(latitude * (math.pi / 180)) * math.sin(longitude * (math.pi / 180))
        z = ((math.pow(self.b, 2) / math.pow(self.a, 2)) * self.n(latitude) + altitude) * math.sin(latitude * (math.pi / 180))
        return x,y,z
        
    def exec(self, latitude, longitude, altitude=0):
        xa, ya, za = self.gps2ecef(latitude, longitude, altitude)
        return np.dot(self.T, np.asarray([xa, ya, za, 1]).reshape(-1,1)).reshape(-1)