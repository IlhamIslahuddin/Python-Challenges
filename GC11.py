def golden_ratio(length):
    width = length/1.618
    print (f"With a length of {length} you should have a width of {width:.1f}")
    return width

if __name__ == "__main__":
    golden_ratio(100)
