import random

# Random integer between 2 numbers
random_int = random.randint(1,10)
print(random_int)

# Random floating point [0,1] not incliding these two
random_float = random.random()
print(random_float)

# Random between 0.000000... - 4.999...
random_example = random_float * 5
print(random_example)