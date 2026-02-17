"""
author: Ruhan
date: 02/14/2026
0.4 - Functions Review Exercises
"""
import math




# Exercise 1
def sum_cubes(n):
    """
    Calculate the sum of the first n cubes and prints the result
   
    Arg: n (int) - The number of cubes to sum
   
    Returns: none




    """
    # TODO: Write your code here


    total = 0


    for i in range(1, n+1):
        total = total + i**3


    print(total)




# Test cases for sum_cubes
sum_cubes(0)    # Expected: 0
sum_cubes(1)    # Expected: 1
sum_cubes(5)    # Expected: 225
sum_cubes(10)   # Expected: 3025
sum_cubes(50)   # Expected: 1625625




# Exercise 2:
def volume_sphere(r):
    """
    Calculates the volume of a sphere given its radius.




    Arg: r (float) - Radius of the sphere.




    Returns (float): Volume of the sphere.
   
    """
    # TODO: Write your code here


    v = 4/3*math.pi*(r**3)


    return v


volume_sphere(5)


print(volume_sphere(5))








def area_sphere(r):
    """
    Calculates the surface area of a sphere given its radius.




    Arg: r (float) - Radius of the sphere.




    Returns:
    float: Surface area of the sphere.
    """
    # TODO: Write your code here


    sa = 4*math.pi*(r**2)


    return sa


area_sphere(3)
print(area_sphere(3))






# Test Cases for volume_sphere and area_sphere
radii = [0, 1, 4, 10.4, 100.344]
for r in radii:
    vol = volume_sphere(r)
    area = area_sphere(r)
    print("Radius:", r, "-> Volume:", round(vol, 2), "Area:", round(area, 2))




# Expected Results:
# Radius: 0 -> Volume: 0.00, Area: 0.00
# Radius: 1 -> Volume: 4.19, Area: 12.57
# Radius: 4 -> Volume: 268.08, Area: 201.06
# Radius: 10.4 -> Volume: 4711.82, Area: 1359.18
# Radius: 100.344 -> Volume: 4232167.40, Area: 126529.76




# Exercise 3: This concept is used frequently when sorting values.
def swap(a, b):
    """
    Swaps two input values and returns them in reversed order.




    Parameters:
    a: First value.
    b: Second value.




    Returns:
    tuple: A tuple containing the values in reversed order (b, a).
    """
    return(b, a)




# Test cases for swap
x, y = swap(3, 5)
print(x, y)  # Expected: 5 3




x, y = swap("Boo", "Hoo")
print(x, y)  # Expected: Hoo Boo








# Exercise 4: Challenge\
import math
def approximate_pi(n):
    """
        Approximates the value of pi using the Leibniz series:
        pi ≈ 4/1 - 4/3 + 4/5 - 4/7 + ...




        Arg: n (int) - Number of terms to include in the approximation.




        Returns (float): Approximated value of pi.
        """
    total = 0
   
    for i in range(n):
       
        denominator = (2*i + 1)
       
        if i % 2 == 0:
            total = total + 4/denominator


        else:
            total = total - 4/denominator


    return total


approximate_pi(3)
approximate_pi(10)
approximate_pi(100)
approximate_pi(1000)


# Test cases for approximate_pi
print(approximate_pi(3))     # Expected: 3.466666666666667
print(approximate_pi(10))    # Expected: 3.0418396189294032
print(approximate_pi(100))   # Expected: 3.1315929035585537
print(approximate_pi(1000))  # Expected: 3.140592653839794




# Do you notice anything interesting with the outputs?


# Its getting closer to 3.14, which is the constant for pi





