import codecs

def line_to_json(line):
    data = line.split(",")
    return "  { \"name\": \"%s\", \"email\": \"%s\" }" % (data[0], data[2])

file = codecs.open("dummy.csv", "r", "shift_jis")
file.readline() # Skip the first line.
json_str = "[\n" + ',\n'.join(map(line_to_json, file)) + "\n]\n"
file.close()

file = codecs.open("dummy.json", "w", "utf-8")
file.write(json_str)
file.close()

