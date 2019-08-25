#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#### ANLY550 Homework5
#### Hongyang Zheng


# Length is a list that stores the length for each word in the text
# Words is a list that stores each word in the text
# M is the maximum length that each line can be
def neatness(Length, Words, M):
    
    # n is the total number of words
    n = len(Words)

    # The number of extra spaces from word i to word j in one line
    extra = [[float('Inf') for i in range(n)] for j in range(n)]
    for i in range(n):
        extra[i][i] = M - Length[i]
        for j in range(i+1, n):
            extra[i][j] = extra[i][j-1] - Length[j] - 1

    # The part penalty from word i to word j in one line
    part_p = [[float('Inf') for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i, n):
            if extra[i][j] < 0:
                part_p[i][j] = float('Inf')
            elif j == n-1 and extra[i][j] >= 0:
                part_p[i][j] = 0
            else:
                part_p[i][j] = extra[i][j] ** 3

    # p[j] is the optimized total penalty for word 1 to word j
    p = [float('Inf') for i in range(n)]
    start_word = [0 for i in range(n)]
    end_word = [0 for i in range(n)]
    
    for j in range(n):
        # Update the penalty
        p[j] = part_p[0][j]  
        end_word[j] = j
        
        for i in range(j):
            if p[i] + part_p[i+1][j] < p[j]:
                # Update the penalty
                p[j] = p[i] + part_p[i+1][j] 
                start_word[j] = i+1
                end_word[j] = j

    # Find the start word and end word for each line 
    start = []
    end = []
    start.append(start_word[-1])
    end.append(end_word[-1])
    
    while start[-1] != 0:
        for index, i in enumerate(end_word):
            if i == start[-1] - 1:
                end.append(i)
                start.append(start_word[index])
                
    # Print the neat paragraph
    for i in range(len(start)-1, -1, -1):
        s = start[i]
        e = end[i]
        for w in range(s, e + 1):
            print(Words[w], end=" ")
        print()

    return print("When we have M =", M, "\nPenalty of the optimal solution is", p[-1], "\n")

if __name__ == "__main__":
    
    # Load the text
    text = "Buffy the Vampire Slayer fans are sure to get their fix with the DVD release of the show's first season. The three-disc collection includes all 12 episodes as well as many extras. There is a collection of interviews by the show's creator Joss Whedon in which he explains his inspiration for the show as well as comments on the various cast members.  Much of the same material is covered in more depth with Whedon's commentary track for the show's first two episodes that make up the Buffy the Vampire Slayer pilot. The most interesting points of Whedon's commentary come from his explanation of the learning curve he encountered shifting from blockbuster films like Toy Story to a much lower-budget television series. The first disc also includes a short interview with David Boreanaz who plays the role of Angel. Other features include the script for the pilot episodes, a trailer, a large photo gallery of publicity shots and in-depth biographies of Whedon and several of the show's stars, including Sarah Michelle Gellar, Alyson Hannigan and Nicholas Brendon."
    
    # Split the text into words
    text = text.split(" ")
    
    # Create two lists to store the results
    Length=[]
    Words=[]
    
    for index, word in enumerate(text):
        Length.append(len(word))
        Words.append(word)
    
    # Case 1: When M=40
    M1 = 40
    neatness(Length, Words, M1)
    
    # Case 2: When M=72
    M2 = 72
    neatness(Length, Words, M2)

