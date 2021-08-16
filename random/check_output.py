import subprocess

# subprocess.check_output example

def example():
    set = ["l", "L", "w", "W"]
    option = input("Linux or Windows example? [l/w] ")
    while True:
        if str(option) in set:
            if option == set[0] or option == set[1]:
                output = subprocess.check_output("ifconfig", shell=True).decode()
                break
            else:
                output = subprocess.check_output("ipconfig", shell=True).decode()
                break
        else:
            option = input("[l/w] please! ")
    print(output)

if __name__ == "__main__":
    example()
