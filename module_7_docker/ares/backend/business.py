import os

def get_data():
    file_path = os.path.join(os.path.dirname(__file__), 'names.txt')
    with open(file_path) as f:
        names = f.read()
        names = names.split()
        return names








# def get_data():

#     with open('names.txt') as f:

#         names = f.read()
        
#         names = names.split()

#         return names 