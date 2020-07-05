"""
    Test if all the videos in the path got thumbnailed
    if i==j that is if output is true then all ok
    
"""
import os
i=0
j=0
path="C:\\Users\\KIIT\\Videos\\python\\Python\\Python\\"
destination="C:\\Users\\KIIT\\videoJatra\\"
for d in os.listdir(path):
    i+=1
for h in os.listdir(destination):
    j+=1

j*=2
print(i==j)
