def input_new_piece():
    running = True
    x = int(input("Set x starting position:"))
    y = int(input("Set y starting position:"))
    z = int(input("Set z starting position:"))
    current_position = [x, y, z]
    vectors = []

    while running == True:

        print("Added", current_position)
        copy = current_position[:]
        vectors.append(copy)

        keypress = input()

        if keypress == "w":
            current_position[1] += 1
        elif keypress == "s":
            current_position[1] -= 1
        elif keypress == "d":
            current_position[0] += 1
        elif keypress == "a":
            current_position[0] -= 1
        elif keypress == "e":
            current_position[2] += 1
        elif keypress == "c":
            current_position[2] -= 1
        elif keypress == "undo":
            current_position = last_position
        elif keypress == "quit":
            return vectors
        elif keypress == "clear":
            vectors = []
        elif keypress == "tostart":
            current_position = [0,0,0]
        elif keypress == "save":
            file_name =  input("Enter filename:") + ".txt"
            file = open("pieces/" + file_name, "w")
            file.write(str(vectors))
            print("File:", file_name, "saved!")
            return vectors
        if current_position not in vectors:
            print("Added", current_position)
            vectors.append(current_position)
        last_position = current_position


print(input_new_piece())




