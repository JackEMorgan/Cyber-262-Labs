# This is a comment line! It is started with a "#"!
# Jack Morgan, Cyber 262, Professor Hozza, Python Lab, 03/21/2022 (3:26pm)

# change the following line to open different file
file_path='Log-A.strace'

print("Now I am going to open file: "+file_path)
file1=open(file_path)
lines=file1.readlines()
print("Now that the data is got, this file is now to be closed!")
file1.close()

# change the following line to search for another term
term='read'
counter = 0
for line in lines:
    if term in line:
        counter+=1
print("Log File 1 Count: " + str(counter))
print()
count1 = counter

# change the following line to open different file
file_path='Log-B.strace'


print("Now I am going to open file: "+file_path)
file2=open(file_path)
lines=file2.readlines()
print("Now that the data is got, this file is now to be closed!")
file2.close

# change the following line to search for another term
term='read'
counter = 0
for line in lines:
    if term in line:
        counter+=1 
print("Log File 2 Count: " + str(counter))
print()
count2 = counter

# following lines are used to calculate total_count of term and print
total_count = count1+count2
print("Total Count = " + str(total_count))
