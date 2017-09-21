def final_velocity (initial_velocity, acceleration, time):
    ans=initial_velocity+(acceleration*time)
    return ans

def distance_traveled (initial_velocity, acceleration, time):
    ans=(initial_velocity*time) + ((acceleration*time*time)/2)
    return ans

def main ():
    time=int(input("Time spent on the road (s)= "))
    acceleration=int(input("Acceleration (m/s2)= "))
    distance=int(input("Distance (m)= "))
    initial_velocity=0
    max_velocity=60
    for duration in range (0, time+1):
        print("Duration:", duration, end=" ")
        print("Distance (*=10m): ", "*" *int(distance_traveled(initial_velocity,acceleration, duration)/10))
    if (final_velocity(initial_velocity, acceleration, duration)>max_velocity):
        print("Speed limit was "+ str(final_velocity(initial_velocity, acceleration, duration)) +" m/s")
        print("Maximum speed limit "+str(max_velocity)+" m/s reached, please drive carefully!")
    else:
        print("Speed limit was "+ str(final_velocity(initial_velocity, acceleration, duration)) +" m/s")
        print("Maximum speed limit "+str(max_velocity)+ ", thankyou for driving carefully.");
    if (distance_traveled(initial_velocity,acceleration, time)>= distance):
        print("Distance travelled was "+ str(distance_traveled(initial_velocity,acceleration,time))+" m")
        print("Distance reached!")
    else:
        print("Distance travelled was "+ str(distance_traveled(initial_velocity,acceleration,time))+" m")
        print("Didn't reach distance...")
main()
