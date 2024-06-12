def denary_to_bcd(denary):
    # Convert the denary number to a string of binary digits
    binary = bin(denary)[2:]
    
    # Pad the binary string with leading zeros to ensure each digit has 4 bits
    while len(binary) % 4 != 0:
        binary = '0' + binary
    
    # Split the binary string into groups of 4 digits
    binary_groups = [binary[i:i+4] for i in range(0, len(binary), 4)]
    
    # Convert each group of 4 binary digits to its equivalent BCD representation
    bcd = ''
    for group in binary_groups:
        bcd += str(int(group, 2))
    
    return bcd

if __name__ == "__main__":
    denary_number = 16
    bcd_representation = denary_to_bcd(denary_number)
    print("Denary:", denary_number)
    print("BCD:", bcd_representation)
