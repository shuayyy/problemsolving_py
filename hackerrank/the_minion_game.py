def minion_game(st):
    kevin_score = 0
    stuart_score = 0
    cp = []
    n = len(st)
    i = 0
    count = 0
    # Generate all substrings with repetitions
    for i in range(n):  # Loop over starting index
        for j in range(i + 1, n + 1):  # Loop over end index
            substring = st[i:j]
            cp.append(substring)  # Append substrings to the list with repetitions

    # print(cp)  # Show all substrings including repetitions

    # Calculate scores including repetitions
    for i in range(len(cp)):
        ref = cp[i]
        if ref[count] in 'AEIOU':  # Vowel check on first index of substring
            kevin_score += 1
        else:
            stuart_score += 1

    # Print results after the scores are calculated
    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)