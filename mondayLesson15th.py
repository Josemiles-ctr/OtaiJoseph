# Sets, Lists, and Tuples in Python
#Characteristics of sets, lists, and tuples
#Sets: Unordered, mutable, no duplicate elements
#Lists: Ordered, mutable, allows duplicate elements
#Tuples: Ordered, immutable, allows duplicate elements

cars={"suzuki","honda","toyota", "bmw", "suzuki", 2, 5, 2}

#Adding elements
cars.add("mercedes")
catlerry={"cat","dog","rabbit", "hamster", "parrot", "cat", "bmw"}

#Removing elements
cars.remove("honda")
print(cars)

#Adding multiple elements
cars.update(["audi", "ford", "nissan"])
print(cars)

#Intersection
shared_cars=cars.intersection(catlerry)
print(shared_cars)

#Union
all_cars=cars.union(catlerry)
print(all_cars)


#Lists
fruits=["apple", "banana", "orange", "grape", "banana", 1, 2, 3]
#Adding elements
fruits.append("kiwi")
print(fruits)

#Removing elements
fruits.remove("banana")
print(fruits)

#Adding multiple elements
fruits.extend(["mango", "pineapple", "watermelon"])
print(fruits)

#Gettint specific elements
print(fruits[2]) # Accessing the third element (index starts at 0)
print(fruits[-1]) # Accessing the last element

#Accessing element by name
print("Mango is in index:", fruits.index("mango"))

#Use of a constructor to create a list
numbers=list((1, 2, 3, 4, 5))
print(numbers)

#Adding item at specific index
fruits.insert(1, "strawberry")
print(fruits)

#Updating an element
fruits[0] = "blueberry"
print(fruits)

#Iterating through a list
for fruit in fruits:
    print(fruit)
    
#Tuples
colors=("red", "green", "blue", "yellow", "red", 1, 2, 3)
#Accessing elements
print(colors[1]) # Accessing the second element
print(colors[-1]) # Accessing the last element  

#Use of a constructor to create a tuple
shapes=tuple(("circle", "square", "triangle"))
print(shapes)

#Iterating through a tuple
for color in colors:
    print(color)
    
#Adding elements to a tuple (tuples are immutable, so we create a new tuple)
new_colors=colors + ("purple",)
print(new_colors)


# Convertin a list in to a tuple
fruits_tuple=tuple(fruits)
print(fruits_tuple)

# Converting a tuple into a list
colors_list=list(colors)
print(colors_list)

#Set operations
A={1, 2, 3, 4, 5}
B={4, 5, 6, 7, 8}
#Union
union_set=A.union(B)
print("Union:", union_set)
#Intersection
intersection_set=A.intersection(B)
print("Intersection:", intersection_set)
#Difference(elements in A but not in B)
difference_set=A.difference(B)
print("Difference (A - B):", difference_set)
#Symmetric Difference(elements in either A or B but not in both)
sym_diff_set=A.symmetric_difference(B)
print("Symmetric Difference:", sym_diff_set)

# Accessing tuple elements
my_tuple=(10, 20, 30, 40, 50)
print(my_tuple[0]) # Accessing the first element
print(my_tuple[2]) # Accessing the third element
print(my_tuple[-1]) # Accessing the last element   

#Exercise:
#Deleting a tuple (tuples are immutable, so we cannot delete individual elements, but we can delete the entire tuple)
del my_tuple

#Concatenating tuples
tuple1=(1, 2, 3)
tuple2=(4, 5, 6)
concatenated_tuple=tuple1 + tuple2
print(concatenated_tuple)

#Updating a tuple (tuples are immutable, so we create a new tuple)
updated_tuple=tuple1 + (7, 8, 9)
print(updated_tuple)