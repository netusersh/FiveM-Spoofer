import os
import time
import subprocess
import shutil
import sys

os.system("title 0xNetUserSH")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        clear_screen()
        print("\n==============================================================================                                                               ")
        print("\n                             \033[37mWelcome To \033[31mFiveM \033[37mSpoofer.                                                               ")
        print("\n           \033[33m[\033[37m1\033[33m] \033[37m: Remove XBOX Apps           \033[33m[\033[37m2\033[33m] \033[37m: Clear FiveM Cache          ") 
        print("\n           \033[33m[\033[37m3\033[33m] \033[37m: Unlink Rockstar Folder     \033[33m[\033[37m4\033[33m] \033[37m: Clear FiveM Logs           ") 
        print("\n           \033[33m[\033[37m5\033[33m] \033[37m: Clear Windows Temp         \033[33m[\033[37m6\033[33m] \033[37m: Credits                    ") 
        print("\n                                  \033[33m[\033[37m7\033[33m] \033[37m: Quit                                                                 ") 
        print("\n==============================================================================")
        print("\033[33m[\033[37m-\033[33m] \033[37mChoice : ", end="")
        choice = input()

        if choice == "1":
            remove_xbox_apps()
        elif choice == "2":
            delete_specific_folders()
        elif choice == "3":
            unlink_rockstar_folder()
        elif choice == "4":
            clear_fivem_caches()
        elif choice == "5":
            clear_windows_temp()
        elif choice == "6":
            our_team()
        elif choice == "7":
            exit_program()
        else:
            print("\033[31m[\033[37m-\033[31m] \033[37mInvalid choice. Try again.")
            time.sleep(2)

def remove_xbox_apps():
    try:
        commands = [
            "Get-AppxPackage *XboxApp* | Remove-AppxPackage",
            "Get-AppxPackage *XboxGameOverlay* | Remove-AppxPackage",
            "Get-AppxPackage *XboxGamingOverlay* | Remove-AppxPackage",
            "Get-AppxPackage *XboxIdentityProvider* | Remove-AppxPackage",
            "Get-AppxPackage *XboxSpeechToTextOverlay* | Remove-AppxPackage",
            "Get-AppxPackage *GamingServices* | Remove-AppxPackage",
            "Get-AppxPackage *GameBar* | Remove-AppxPackage",
        ]
        
        for command in commands:
            subprocess.run(["powershell", "-Command", command], check=True)
        print("\033[32m[\033[37m+\033[32m] \033[37mXbox apps removed successfully.")
        time.sleep(2)
    except subprocess.CalledProcessError as e:
        print(f"\033[31m[\033[37m-\033[31m] \033[37mError while removing Xbox apps: {e}")
        time.sleep(2)

def delete_specific_folders():
    folders_to_delete = [
        os.path.join(os.environ['LOCALAPPDATA'], "FiveM", "FiveM.app", "data", "cache"),
        os.path.join(os.environ['LOCALAPPDATA'], "FiveM", "FiveM.app", "data", "server-cache"),
        os.path.join(os.environ['LOCALAPPDATA'], "FiveM", "FiveM.app", "data", "nui-storage"),
        os.path.join(os.environ['LOCALAPPDATA'], "FiveM", "FiveM.app", "data", "server-cache-priv"),
    ]
    
    for folder in folders_to_delete:
        try:
            if os.path.exists(folder):
                shutil.rmtree(folder)
                print(f"Deleted: {folder}")
            else:
                print(f"\033[31m[\033[37m-\033[31m] \033[37mError With : {folder}.")
        except Exception as e:
            print(f"\033[31m[\033[37m-\033[31m] \033[37mError With {folder}: {e}.")
    time.sleep(2)

def unlink_rockstar_folder():
    folder_to_delete = os.path.join(os.environ['LOCALAPPDATA'], "DigitalEntitlements")
    try:
        if os.path.exists(folder_to_delete):
            shutil.rmtree(folder_to_delete)
            print("\033[32m[\033[37m+\033[32m] \033[37mRockstar Unlinked Successfully.")
        else:
            print("\033[31m[\033[37m-\033[31m] \033[37mRockstar Was Already Unlicked.")
    except Exception as e:
        print(f"\033[31m[\033[37m-\033[31m] \033[37mError Unlicking Rockstar : {e}.")
    time.sleep(2)

def clear_fivem_caches():
    folders_to_delete = [
        os.path.join(os.environ['LOCALAPPDATA'], "FiveM", "FiveM.app", "crashes"),
        os.path.join(os.environ['LOCALAPPDATA'], "FiveM", "FiveM.app", "logs")
    ]
    
    for folder in folders_to_delete:
        try:
            if os.path.exists(folder):
                shutil.rmtree(folder)
            else:
                print(f"\033[31m[\033[37m-\033[31m] \033[37mError With Files. Files Already deleted.")
        except Exception as e:
            print(f"\033[31m[\033[37m-\033[31m] \033[37mError clearing FiveM caches: {e}.")
    time.sleep(2)

def clear_windows_temp():
    temp_folder = os.environ['TEMP']
    try:
        for root, dirs, files in os.walk(temp_folder):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                except Exception as e:
                    print(f"Error deleting file {file}: {e}")
            for dir in dirs:
                try:
                    shutil.rmtree(os.path.join(root, dir))
                except Exception as e:
                    print(f"\033[31m[\033[37m-\033[31m] \033[37mError Cleaning Windows : {e}.")
        print("\033[32m[\033[37m+\033[32m] \033[37mWindows Cleared Successfully.")
    except Exception as e:
        print(f"\033[31m[\033[37m-\033[31m] \033[37mError Clearing Windows : {e}.")
    time.sleep(2)

def our_team():
    clear_screen()
    print("\n\033[33m==============================================================================                ")
    print("\n                       \033[37mThis Script Has Been Developped By \033[31m0xNetUserSH                 ")
    print("\n            Github\033[37m: https://github.com/netusersh    \033[31m0x \033[37m: https://discord.gg/0x")
    print("\n\033[33m==============================================================================                ")
    print("\n                     \033[37m(going back to menu in 10s)                                              ")
    time.sleep(10)

def exit_program():
    clear_screen()
    print("Disconnecting...")
    time.sleep(1)
    sys.exit(0)

if __name__ == "__main__":
    menu()