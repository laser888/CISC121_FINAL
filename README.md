# Bubble Sort
# Why I Chose Bubble Sort
I chose bubble sort because it was the easiest sorting algorithm for me to understand, it clicked right away. I also have a creative idea for how to visualize the comparisons and swaps.
## Demo video/gif/screenshot of test

## Problem Breakdown & Computational Thinking (You can add a flowchart and write the four pillars of computational thinking briefly in bullets)

# Decomposition:
Bubble Sort works by repeatedly scanning the list from left to right and comparing pairs of adjacent values. If a pair is out of order, the algorithm swaps the two elements. After each full pass, the largest remaining value moves toward the end of the list. This cotinues until the algorithm completes a full pass without performing any swaps. 

# Pattern Recognition:
During every pass, the algorithm performs the same pattern: compare two neighbouring elements, check whether they need to be swapped, then move one step to the right. Each pass reduces the number of unsorted elements.

# Abstraction:
To visualize the algorithm, only the essential details need to be shown: the values themselves, which two elements are being compared ata given moment, and when a swap takes place. Details such as loop counters, index variables, and the internal mechanics of each pass can be left out because they do not help the user understand the core behaviour of the algorithm.

# Algorithm Design:
The user will enter a list of integers separated by commas into a text box. The program will convert this string into a list and run Bubble Sort on it. As the algorithm processes the list, each comparison and swap will be recorded and sent to the UI so the user can see the list change step-by-step. The output will show the updates in real time, ending with the fully sorted list.

# Data Structure:
The values will be stored as a list of integers.



## Steps to Run

## Hugging Face Link

## Author & Acknowledgment
https://gemini.google.com/share/9b58237c460c 