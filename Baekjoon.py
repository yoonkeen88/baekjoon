

def main():
    n = int(input())  # Number of strings
    on_li = []
    
    for i in range(n):
        a = input().split()
        a.append(str(i))  # Append index to each string
        on_li.append(a)  # Append index to each string
    
    # Sort based on the first two characters (as integers) and the last character
    on_li.sort(key=lambda x: (int(x[0]), int(x[-1])))
    
    # Output the strings without the index part
    for i in on_li:
        print(i[0],i[1])  # Remove the index at the end before printing

if __name__ == "__main__":
    main()