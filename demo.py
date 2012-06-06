def main():
    print("Hello, welcome")
    with open(__file__, "rt") as f:
        for line in f:
            handle_line(line)
    return 0

def handle_line(line):
    line_stripped = line.rstrip()
    print(line_stripped)

if __name__ == "__main__":
    main()
