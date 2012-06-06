def handle_line(line):
    line_stripped = line.rstrip()
    print(line_stripped)

print("Hello, welcome")
with open(__file__, "rt") as f:
    for line in f:
        handle_line(line)
