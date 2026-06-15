#Exercise 3
def area_of_a_circle(radius):
    """Calculate the area of a circle given its radius."""
    import math
    return math.pi * radius ** 2

#Exercise 4: Demonstrating global and local variable scopes
global_var = "I am a global variable"

def demonstrate_variable_scopes():
    local_var = "I am a local variable"
    print(global_var)  
    print(local_var)  

# radius = float(input("Enter the radius of the circle: "))
# area = area_of_a_circle(radius)
# print(f"The area of the circle with radius {radius} is: {area}")

