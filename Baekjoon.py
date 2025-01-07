import sys

def main():
    melody = input().split()
    a = True
    d = True
    for i in range(len(melody)-1):
        if int(melody[i]) != int(melody[i+1]) + 1 :
            d = False
        elif int(melody[i]) != int(melody[i+1]) -1:
            a = False
            
    if a:
        print("ascending")
    elif d:
        print("descending")
    else:
        print("mixed")

if __name__ == "__main__":
    main()
