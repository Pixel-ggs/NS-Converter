'''
Number system converter between hexadecimal, binary and denary
Used Copilot to simplify and cleanup code a bit but the actual stuff was by me

'''

# importing modules
import os, subprocess

# defining variables
start_base = int(input("\nFor \033[32mBinary\033[0m -> \033[36mDenary\033[0m, enter 1.\n\nFor \033[36mDenary\033[0m -> \
\033[32mBinary\033[0m, enter 0.\n\nFor \033[33mHexadecimal\033[0m -> \033[36mDenary\033[0m, enter 2.\n\n"))
remainders = []
values = []

# hexadecimal -> denary conversion
if start_base == 2:
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True) # clear terminal

    start_num = input("\nEnter the \033[33mhexadecimal\033[0m number. (e.g. \"018D65B\")\n\n")
    digits = list(start_num)[::-1]
    total = 0

    for i in range(len(digits)):

        # invalid input
        if digits[i] not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"):
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True) # clear terminal
            print("\033[33mInvalid input\033[0m")
            break

        if digits[i] == "A":
            digits[i] = "10"
        if digits[i] == "B":
            digits[i] = "11"
        if digits[i] == "C":
            digits[i] = "12"
        if digits[i] == "D":
            digits[i] = "13"
        if digits[i] == "E":
            digits[i] = "14"
        if digits[i] == "F":
            digits[i] = "15"

        # generating the denary
        total += int(digits[i]) * (16 ** i)
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True) # clear terminal

    # final output
    print(f"\033[36mDenary\033[0m equivalent of \033[33m{start_num}\033[0m:\n\n\033[33m{total}\033[0m")

# binary -> denary conversion
elif start_base == 1:
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True) # clear terminal

    start_num = input("\nEnter the \033[32mbinary\033[0m number. (e.g. \"1000011\")\n\n")
    digits = list(start_num)[::-1]
    total = 0

    for i in range(len(digits)):

        # invalid input
        if digits[i] not in ("0", "1"):
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True) # clear terminal
            print("\033[31mInvalid input\033[0m")
            break

        # generating the denary
        total += int(digits[i]) * (2 ** i)
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True) # clear terminal

    # final output
    print(f"\n\033[36mDenary\033[0m equivalent of \033[33m{start_num}\033[0m:\n\n\033[33m{total}\033[0m\n")

# denary -> binary conversion
elif start_base == 0:
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True) # clear terminal

    start_num = int(input("\nEnter the \033[36mdenary\033[0m number. (e.g. \"135\")\n\n"))
    division = start_num

    while True:

        # final output
        if division < 1:
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True) # clear terminal

            remainders.reverse()
            final_binary = "".join(remainders)
            print(f"\n\033[32mBinary\033[0m equivalent of \033[33m{start_num}\033[0m:\n\n\033[33m{final_binary}\033[0m\n")

            break # stop code

        # generating the binary
        else: 
            division, remainder = divmod(division, 2)
            remainders.append(str(remainder))

# invalid input
else:
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True) # clear terminal
    print("\n\033[31mInvalid Input\033[0m\n")

input("\nPress enter to exit\n\n")
