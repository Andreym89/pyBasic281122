import os


path_mac = '~/Desktop'
print(os.path.join('folder', 'file'))

#os.mkdir(r'files/folder_1') #error if exist
os.makedirs(r'files/folder_1', exist_ok = True) #ok if exists
with open(r'files/folder_1/new.txt', 'w'):
    pass

os.remove(r'files/folder_1/new.txt') # remove file
os.rmdir(r'files/folder_1')

print(os.listdir('files'))

# 
# def del_not_empty_directory(path: str):
#     #get list of path objects
#     if os.path.isdir(path):
#         elements = os.listdir(path)
#         for element in elements:
#             path_to_element = os.path.join(path, element)
#             if os.path.isdir(path_to_element):
#                 del_not_empty_directory(path_to_element)
#                 #os.rmdir(path_to_element)
#             else:
#                 os.remove(path_to_element)
#         os.rmdir(path)