def print_inverted_pyramid(rows):
    for i in range(1,rows+1):
        spaces = " " * (rows - i)
        s_pattern = "S " * i
        print(spaces + s_pattern)

# Example test case
rows = 5  # You can modify this value as needed
print_inverted_pyramid(rows)
