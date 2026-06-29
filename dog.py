class Student:
	def __init__(self, name, age):
            self.name = name
            self.age = age
	def register(self, course):
					print(f"{self.name} has registered for {course}.")
				
				
joseph=Student("Joseph", 20)
joseph.register("Mathematics")

print(f"Student Name: {joseph.name}")
