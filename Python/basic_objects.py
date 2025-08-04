a = [1,2, 'some time',5.3, 'true'] #list
print(a);
print(a[4]);

# result = a[1:4 ]; #this is a slice
result = a[2:3 ]; #this is a slice
print(result);


b = (1,4,5,7,4); # this is a tuple (immutable)

c = {1,2,4,5,6,7,9} # this is a set

d = {
    'a':1,
    'b':3,
    4:'five',
    'd':77
} # this is a dictionary

print(d[4]) # this is an index