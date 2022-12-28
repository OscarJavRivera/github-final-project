import numpy as np

# convert binary to integer
x = int("11111111",2) # = 255
y = int("00000010",2) # = 2

x=np.uint8(x) # convert bumber to unsigend 8 bit representation
y=np.uint8(y)
print(x+y)