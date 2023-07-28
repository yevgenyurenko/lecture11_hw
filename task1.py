
# first script to create a file
with open('myfile.txt', 'w') as file:
    file.write('Hello file world!\n')

# second script to read a file
with open('myfile.txt', 'r') as file:
    file_contents = file.read()
    print(file_contents)