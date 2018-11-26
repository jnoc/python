def megabyteConvert():
  #this converts megabytes into bits, bytes, kilobytes, gigabytes and terrabytes
  # written well before I knew how to actually do python!

  megabyte = float(input("How many MB's do you have? "))
  terabyte = float(megabyte) / 1048576
  gigabyte = float(megabyte) / 1024
  kilobyte = float(megabyte) * 1024
  byte = float(megabyte) * 1048576
  bit = float(megabyte) * 8388608

  print("Your conversons are:\n")
  print("\t" + str(round(bit, 7)), "b")
  print("\t" + str(round(byte, 7)), "B")
  print("\t" + str(round(kilobyte, 7)), "KB")
  print("\t" + str(round(megabyte, 7)), "MB")
  print("\t" + str(round(gigabyte, 7)), "GB")
  print("\t" + str(round(terabyte, 7)), "TB")
  
  input("\n"+"Press enter to close...")
  
def main():
  megabyteConvert()
main()
