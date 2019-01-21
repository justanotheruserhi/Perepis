try:
    v = int(input('V1'))
    V = int(input('V2'))
    t = int(input('Time'))

    def decorator(acceleration):
        a=acceleration(v, V, t)
        S = v*t + (a*t*t)//2
        print('The distance is ', S, ' meters')

    @decorator
    def acceleration(v, V, t):
        a =(V-v)//t
        print('The acceleration is ', a, ' m/s^2')

    acceleration(v,V,t)

except TypeError:
    print('The integer type is required')

except ZeroDivisionError:
    print('The time cannot be equal to zero')

