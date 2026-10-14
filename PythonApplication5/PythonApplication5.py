'''
Ross Young
10/13/2026
Program to draw a model of an object thrown upward in vertical motion.
'''

# Function to calculate the time it takes for an object to reach its maximum height
def time_to_peak(vertical_speed, gravity=-32): # Default gravity is set to -32 ft/s^2 for gravitational acceleration
    time = -vertical_speed / gravity # Calculate the time to reach maximum height using the formula v = aT + V_0
    return time

# Function to calculate the maximum height of an object thrown upward
def maximum_height(vertical_speed, gravity=-32, initial_height=0): # Assume the initial height is 0 if not specified
    height_time = time_to_peak(vertical_speed, gravity)
    height = 0.5 * gravity * height_time ** 2 + vertical_speed * height_time + initial_height # Calculate the maximum height using the formula y = 1/2aT^2 + V_0T + Y_0
    return height

# Function to calculate the total flight time of an object thrown upward
def total_flight_time(vertical_speed, gravity=-32):
    total_time = 2 * time_to_peak(vertical_speed, gravity) # Total flight time is twice the time to peak
    return total_time


'''
# To test, below is code to print the results for an object thrown upward with a vertical speed of 64 ft/s.

# Print the time required to reach maximum height for an object thrown upward with a vertical speed of 64 ft/s
print("Time to reach maximum height:", time_to_peak(64), "seconds")
'''