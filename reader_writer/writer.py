def create_write_to_file(result):
    f = open("widd.out", "w+")
    f.write(str(result))
    f.close()
