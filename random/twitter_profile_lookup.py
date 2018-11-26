import webbrowser

def body():
  print("This is a brief twitter profile viewer.")
  question = input("What profile would you like to visit? ")
  variable = 'https://twitter.com/intent/user?screen_name=' + question

  print("Visiting", variable)
  webbrowser.open(variable)
  
def main():
  body()
main()
