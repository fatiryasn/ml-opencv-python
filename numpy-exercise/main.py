import numpy as np


def output(x):
    print("array elements: ", x)
    print("array shape: ", x.shape)
    print("element type: ", type(x[0]))
    print("-------------------------------------------------- \n")

##------
#NUMPY ARRAYS
##------
#1. with .zeros()
a1 = np.zeros(3)
output(a1)

#2. with .ones()
a2 = np.ones(3)
output(a2)

#3. with .empty()
a3 = np.empty(3)
output(a3)

#4. with .linspace()
a4 = np.linspace(2, 10, 5)
output(a4)

#5 with .array()
a5 = np.array([1,2,3,4,5,6,7,8,9])
output(a5)

#2D array
a6 = np.ones((2,4))
output(a6)

#3D array
a7 = np.ones((2,4,2))
output(a7)


##------
#NUMPY RANDOM
##------

#1. randint
r1 = np.random.randint(10, size=5)
output(r1)

#2. rand
r2 = np.random.rand(10)
output(r2)

#3. randn
r3 = np.random.randn(2, 3)
output(r3)

#4. choice
r4 = np.random.choice(r1, 2)
output(r4)

#5. uniform
r5 = np.random.uniform(10, 20, 5)
output(r5)