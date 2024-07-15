import subprocess

# ASCII fish art
def fishart_print():
    fish_art = '''
            ^
        //                        ___   ___
       (*)     "O"                /  _   _  \\
      (*)                           / \\ / \\
     (*)    "O"                    |   |   |    |\\
    //                             |O  |O  |___/  \\     ++
    //              Alfred          \\_/ \\_/    \\   | ++
    //                              _/      __    \\  \\
    /     /|   /\\                  (________/ __   |_/
        / |  |  |                   (___      /   |    |\\
        / /  /   |                     \\     \\|    |___/  |
    |  | |   /                       \\_________      _/   ++++
    /   | |  |                      ++           \\    |
    |   / /   |                              ++   |   /  +++
    /   /  |   |                               ++ /__/
    ~~~ ~~~~   ~~~~~~~~~~~~  ~~~~~~~~~~~~~  ~~~~        ~~+++~~~~ ~
    '''
    print(fish_art)

def main():
    print("What do you want?")
    user_input = input("> ")

    # Take userinput and put into Open_files.py
    subprocess.run(["python", "open_files.py", user_input], check=True)

if __name__ == "__main__":
    fishart_print()
    while True:    
        main()