# The Spiral Memory Algorithm
# Goal -- to find the distance to the center of any given integer
# Note that for each layer of squares embedded within the spiral space,
#      elements located in the bottom right corner consitute a sequnce of
#      perfect squares for odd numbers ---
#      1 = 1 * 1
#      9 = 3 * 3
#      25 = 5 * 5
#      ...

# And if we spread each layer of squares into rows, we have the following:
# 1
# 2 3 4 5 6 7 8 9
# 10 11 12 ..... 25
# 26 27 .... ... 49
# Thus, the number of elements contained in each row = k * 8,
# where k is the order of the end point within the odd number sequence 1, 3, 5, 7, ...

# Steps: 1) locating which layer of squares that the number is embedded;
#        2) find the coordinates of the number given the coordinates of
#           the four corner points of the square


from math import sqrt
def find_index(num):
    root_of_n = int(sqrt(num))  # find the nearest integer root
    if root_of_n % 2 == 0:
        floor_odd = root_of_n - 1 # find the lower bound for the odd root
    if root_of_n % 2 == 1:
        floor_odd = root_of_n
    ceil_odd = floor_odd + 2   # find the upper bound for the odd root
    shell_index = int((ceil_odd - 1) / 2 ) # find the index of the odd root in the odd number sequence
    return shell_index, ceil_odd

# test cases
#print(find_index(100000))
#print(find_index(2345678))

def find_dist(num, k, ceil_odd): # k is the shell index
# this function does two things:
# (a) find the coordinates of num, and (b) return the distance from (0, 0)
    x = k
    y = -k  # initialize the coordinates using the position of (ceil_odd)**2
    end_point = (ceil_odd)**2  # find the end point
    half_point = int(end_point - k * 8 / 2)  # find the half point, whose coord would be (-k, k)
    third_quarter_point = int(end_point - k * 8 / 4)  # find the 3/4 point, (-k, -k)
    first_quarter_point = int(half_point - k * 8 / 4) # find the 1/4 point, (k, k)
    if num >= half_point:
        if num >= third_quarter_point:
            x = x - (end_point - num)
        elif num < third_quarter_point:
            x = -x
            y = y + (third_quarter_point - num)
    elif num < half_point:
        if num >= first_quarter_point:
            y = -y
            x = -x + (half_point - num)
        elif num < first_quarter_point:
            y = -y - (first_quarter_point - num)
    return abs(x) + abs(y)

# test cases
#print(find_coord(100000, 158, 317))
#print(find_coord(2345678, 766, 1533))

def main():
    print("Please enter an integer")
    a_number = int(input("> "))
    the_index, the_ceil_odd = find_index(a_number)
    distance = find_dist(a_number, the_index, the_ceil_odd)
    print(f"The distance from {a_number} to the center is {distance}.")

main()
