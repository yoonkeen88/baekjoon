def main():
    n = int(input())  # Number of strings
    scores = []
    for i in range(n):
        s = input()
        scores.append(0)
        score = 0
        for j in range(len(s)):
            if s[j] == 'X':
                score = 0
            elif s[j] == 'O':
                if score == 0:
                    score = 1
                else:
                    score +=1
            scores[i] += score

    for i in scores:
        print(i)
 

if __name__ == "__main__":
    main()