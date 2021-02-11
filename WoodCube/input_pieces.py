def input_new_piece():
    running = True
    current_position = [0, 0, 0]
    vectors = []
    if current_position not in vectors:
        print("Added", current_position)
        vectors.append(current_position)
    while running == True:


        keypress = input()


        if keypress == "w":
            current_position[0] += 1
        elif keypress == "s":
            current_position[0] -= 1
        elif keypress == "d":
            current_position[1] += 1
        elif keypress == "a":
            current_position[1] -= 1
        elif keypress == "e":
            current_position[2] += 1
        elif keypress == "c":
            current_position[2] -= 1

        print("Added", current_position)
        vectors.append(current_position)

        if keypress == "undo":
            current_position = last_position
        elif keypress == "quit":
            return vectors
        elif keypress == "reset":
            current_position = [0,0,0]
            vectors = []
        elif keypress == "tostart":
            current_position = [0,0,0]
        if current_position not in vectors:
            print("Added", current_position)
            vectors.append(current_position)
        last_position = current_position


print(input_new_piece())




