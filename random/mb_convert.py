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
  print("\t" + str(bit), "b")
  print("\t" + str(byte), "B")
  print("\t" + str(kilobyte), "KB")
  print("\t" + str(megabyte), "MB")
  print("\t" + str(gigabyte), "GB")
  print("\t" + str(terabyte), "TB")
def main():
  megabyteConvert()
main()
