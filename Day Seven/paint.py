def paint_calc(height, width, cover):
    num_of_cans = (height * width) / cover
    return round(num_of_cans)

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

print(f"Total cans required are {paint_calc(height=test_h, width=test_w, cover=coverage)}")
