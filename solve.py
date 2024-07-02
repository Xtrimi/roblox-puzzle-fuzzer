import argparse
import pyautogui
import pydirectinput
import time

def focus():
    w = pyautogui.getWindowsWithTitle("Roblox")[0]
    w.activate()
    time.sleep(1)

def brute(wordlist):
    focus()

    with open(wordlist) as file:
        for word in file:
            pydirectinput.press("/")
            time.sleep(0.1)

            #print(f"Sending {word}")
            pyautogui.write("/e ", interval=0) #Send /e first to prevent sending accidental /clear or /emote
            pyautogui.typewrite(word)
            pydirectinput.press("enter")

    print("Bruteforce completed")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = """Bruteforces all words in /e command using given wordlist.
Move your cursor to your screen's top left corner to terminate the process""")
    parser.add_argument("wordlist")
    arguments = parser.parse_args()

    wordlist = arguments.wordlist
    brute(wordlist)