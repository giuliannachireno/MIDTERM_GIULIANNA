LIST = [10, 20, 30, 40, 50]
print("Original list:", LIST)
LIST[2] = 99
print("Modified list:", LIST)

STRING = "giulianna"
print("Original string:", STRING)

try:
    STRING[0] = "G"
except TypeError as error:
    print("Error:", error)

new_string = "G" + STRING[1:]
print("Modified string:", new_string)