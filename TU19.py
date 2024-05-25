#writes to a seperate text file called "counter.txt"
def countdown():
  with open("counter.txt","w") as new_file:
      for i in range(10,0,-1):
          line_to_write = str(i)+"\n"
          new_file.write(line_to_write)

if _name__ == "__main__":
  countdown()
