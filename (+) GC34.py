def int_to_roman(num):
  val = [
      1000, 900, 500, 400,
      100, 90, 50, 40,
      10, 9, 5, 4,
      1
      ]
  syms = [
      "M", "CM", "D", "CD",
      "C", "XC", "L", "XL",
      "X", "IX", "V", "IV",
      "I"
      ]
  roman_num = ''
  i = 0
  while  num > 0:
      for _ in range(num // val[i]):
          roman_num += syms[i]
          num -= val[i]
      i += 1
  return roman_num

def print_first_100_roman_numerals():
  for num in range(1, 101):
      print(int_to_roman(num))

if __name__ == "__main__":
    print_first_100_roman_numerals()
