def sort():
    with open("./resources/guesses.txt") as file:

        lines = file.read()

    lines = lines.split("\n")
    lines.sort()
    lines = "\n".join(lines)


    new_file = open("./resources/guesses(2).txt", "w")

    new_file.write(lines)
    new_file.close()


sort()