import numpy as np
import matplotlib.pyplot as plt

def cssp(depth):
    gammaa=0.0113/1000
    lat = 0
    za=1000
    h=1000
    ca=1500
    if abs(lat)<67.5:
        eta=2*(za-depth)/h
        speed=ca*(1+h*gammaa*(np.exp(eta) - eta - 1)/2)
    else:
        speed = ca*(1+gammaa*z)
    return speed

def main():
    a = []
    for i in range(0,10000):
        a.append(cssp(i))
    plt.plot(a,range(0,10000),'b')
    plt.title('Speed of Sound (10km)')
    plt.gca().invert_yaxis()
    plt.ylabel('Depth (m)')
    plt.xlabel('Speed (m/s)')
    plt.grid(True,'both','both')
    plt.show()
    return

if __name__ == "__main__":
    main()