import os
from colorama import Fore, Style

adjusted_frame = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main(adjusted_frame, target_frame = 0):
    if target_frame == 0:
        target_frame = int(input("Target Frame: "))
    else:
        print(f"Target Frame: {target_frame}")

    hit_frame = int(input("Hit Frame: "))
    difference = abs(target_frame-hit_frame)
    print(f"\nDifference: {difference}")
    if target_frame < hit_frame:
        difference = difference*-1

    if adjusted_frame == 0:
        adjusted_frame = target_frame + difference
    else:
        adjusted_frame = adjusted_frame + difference


    print(f"\nAdjusted Frame: {Fore.GREEN}{adjusted_frame}{Style.RESET_ALL}\n\nR to reset target frame, enter to continue calculating")
    choice = input()
    clear_screen()
    if choice.lower() == "r":
        adjusted_frame = 0
        target_frame = 0
        clear_screen()
    main(adjusted_frame, target_frame)

clear_screen()
main(adjusted_frame)