f = open('data.txt','r+')

# Read the entire file
data = f.read()

# print the data
print(data)

# write to the file
f.write('This is a new line')

# Close the file
f.close()



###########################################################

file = open('data.txt','r')
# create of list of lines
line_list = file.readlines() # it will show \n with content and also create list 


# line_list = file.readline()  #it will show you line by line but it dont create list

# print the list of lines 
print(line_list)

file.close()