import os
import shlex
import time
import subprocess
import compactnts as cpn
import compactcalc as cpc
import sys
import shutil
global uimp
global params

print("""

 ██████   ██████               ███████████                    █████     
░░██████ ██████               ░░███░░░░░███                  ░░███      
 ░███░█████░███  █████ ████    ░███    ░███  ██████    █████  ░███████  
 ░███░░███ ░███ ░░███ ░███     ░██████████  ░░░░░███  ███░░   ░███░░███ 
 ░███ ░░░  ░███  ░███ ░███     ░███░░░░░███  ███████ ░░█████  ░███ ░███ 
 ░███      ░███  ░███ ░███     ░███    ░███ ███░░███  ░░░░███ ░███ ░███ 
 █████     █████ ░░███████  ██ ███████████ ░░████████ ██████  ████ █████
░░░░░     ░░░░░   ░░░░░███ ░░ ░░░░░░░░░░░   ░░░░░░░░ ░░░░░░  ░░░░ ░░░░░ 
                  ███ ░███                                              
                 ░░██████                                               
                  ░░░░░░                                              

""")

def App():

    while True:
        uimp = input(f"{os.getcwd()} $ ")

        try:
            params = shlex.split(uimp)
        except Exception as e:
            print("Failed to run command")
            continue

        if uimp.strip().lower().startswith("echo"):
            if len(params) > 1:
                print(" ".join(params[1:]))
        elif uimp.strip().lower().startswith("exit"):
            print("Exiting...")
            time.sleep(2)
            break
        elif uimp.strip().lower().startswith("ls"):
            for item in os.listdir(os.getcwd()):
                print(item)
        elif uimp.strip().lower().startswith("mkdir"):
            if len(params) > 1:
                os.makedirs(os.path.join(os.getcwd(), params[1]), exist_ok=True)
                print(f"Directory '{params[1]}' created.")
            else:
                print("Please provide a directory name.")
        elif uimp.strip().lower().startswith("mkf"):
            if len(params) > 1:
                with open(os.path.join(os.getcwd(), params[1]), 'w') as f:
                    pass
                print(f"File '{params[1]}' created.")
            else:
                print("Please provide a file name.")
        elif uimp.strip().lower().startswith("rm"):
            if len(params) > 1:
                try:
                    os.remove(os.path.join(os.getcwd(), params[1]))
                    print(f"File '{params[1]}' removed.")
                except FileNotFoundError:
                    print(f"File '{params[1]}' not found.")
            else:
                print("Please provide a file name.")
        elif uimp.strip().lower().startswith("rmvdir"):
            if len(params) > 1:
                try:
                    os.rmdir(os.path.join(os.getcwd(), params[1]))
                    print(f"Directory '{params[1]}' removed.")
                except FileNotFoundError:
                    print(f"Directory '{params[1]}' not found.")
                except OSError:
                    print(f"Directory '{params[1]}' is not empty.")
            else:
                print("Please provide a directory name.")

        elif uimp.strip().lower().startswith("cd"):
            if len(params) > 1:
                try:
                    os.chdir(params[1])
                except FileNotFoundError:
                    print(f"Directory '{params[1]}' not found.")
                except NotADirectoryError:
                    print(f"'{params[1]}' is not a directory.")
                except PermissionError:
                    print(f"Permission denied to access '{params[1]}'.")
            else:
                print("Please specify a directory to change to.")
        elif uimp.strip().lower().startswith("pwd"):
            print(os.getcwd())
        elif uimp.strip().lower().startswith("ostype"):
            print(os.name)
        elif uimp.strip().lower().startswith("whoami"):
            print(os.getlogin())
        elif uimp.strip().lower().startswith("cnts"):
            cpn.gapp()
        elif uimp.strip().lower().startswith("calc"):
            cpc.gapp2()
        elif uimp.strip().lower().startswith("help"):
            print("""

            Available commands:
            echo [text] - Prints the specified text to the console.
            exit - Exits the application.
            ls - Lists the contents of the current directory.
            mkdirs [directory_name] - Creates a new directory with the specified name.
            mk [file_name] - Creates a new file with the specified name.
            rm [file_name] - Removes the specified file.
            rmvdir [directory_name] - Removes the specified directory (must be empty).
            cd [directory_path] - Changes the current working directory to the specified path.
            pwd - Prints the current working directory.
            ostype - Displays the operating system type.
            whoami - Displays the current user name.
            cnts - Opens a simple text editor (Compact Notepad).
            calc - Opens a simple calculator (Compact Calculator).
            help - Displays this help message.
            winano - Opens winano.
            mv [source] [destination] - Moves a file or directory.
            cp [source] [destination] - Copies a file or directory.

            """)
        elif uimp.strip().lower().startswith("destroy"):
            break
        elif uimp.strip().lower().startswith("runsh"):
            if len(params) > 1:
                script_path = params[1]
                if os.path.isfile(script_path):
                    try:
                        subprocess.run(["bash", script_path], check=True)
                    except subprocess.CalledProcessError as e:
                        print(f"Error executing script: {e}")
                else:
                    print(f"Script '{script_path}' not found.")
            else:
                print("Please provide a script path to run.")
        elif uimp.strip().lower().startswith("winano"):
            print("Press control + d + enter [linux, mac] or control + z + enter to finish the file")
            content = sys.stdin.read()

            with open(os.path.join(os.getcwd(), params[1]), "w") as f:
                f.write(content)
                print("Saved successfully")
        elif uimp.strip().lower().startswith("mv"):
            if len(params) > 2:
                src = os.path.join(os.getcwd(), params[1])
                dst = os.path.join(os.getcwd(), params[2])
                try:
                    shutil.move(src, dst)
                    print(f"Successfully moved '{params[1]}' to '{params[2]}'.")
                except FileNotFoundError:
                    print(f"Source path '{params[1]}' not found.")
                except PermissionError:
                    print(f"Permission denied to access the path.")
                except Exception as e:
                    print(f"Error moving: {e}")
            else:
                print("Usage: mv [source] [destination]")
        elif uimp.strip().lower().startswith("cp"):
            if len(params) > 2:
                src = os.path.join(os.getcwd(), params[1])
                dst = os.path.join(os.getcwd(), params[2])
                try:
                    if os.path.isdir(src):
                        shutil.copytree(src, dst)
                        print(f"Successfully copied directory '{params[1]}' to '{params[2]}'.")
                    else:
                        shutil.copy2(src, dst)
                        print(f"Successfully copied file '{params[1]}' to '{params[2]}'.")
                except FileNotFoundError:
                    print(f"Source path '{params[1]}' not found.")
                except FileExistsError:
                    print(f"Destination path '{params[2]}' already exists.")
                except PermissionError:
                    print(f"Permission denied to access the path.")
                except Exception as e:
                    print(f"Error copying: {e}")
            else:
                print("Usage: cp [source] [destination]")
        else:
            print(f"Command '{uimp}' not recognized.")
            continue
            

if __name__ == "__main__":
    App()