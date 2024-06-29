vertical_count = int(input("enter value vertical count"))            # no of rows needed.
horizontal_count = int(input("enter value for horizontal count"))      # no of columns needed.
temp = (horizontal_count // 2 + 1)                                     # temp is the repeating count of first line.
for h in range(temp):
    print(" ___    ", end="")                           # printing first line.
print()                                                 # required first line printed and exited from the line.
for v in range(vertical_count):                                      # loop for row repeat - 2nd line.
    for h in range(temp - 1):                           # loop for column repeat - 2nd line.
        print("/   \\___", end='')                      # repeating element.
    print("/   \\")                                     # 2nd line ends.
    for h in range(temp - 1):                           # loop for column repeat - 3rd line.
        print("\\___/   ", end="")                      # repeating element.
    print("\\___/")                                     # 3rd line ends.
