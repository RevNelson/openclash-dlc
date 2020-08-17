def writeYAML(filename, data):

    with open(filename, "w") as output_file:
        for line in data:
            try:
                output_file.write(line + "\n")
            except Exception as err:
                print(err)
