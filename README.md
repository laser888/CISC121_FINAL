## Bubble Sort
# Why I Chose Bubble Sort
I chose bubble sort because it was the easiest sorting algorithm for me to understand, it clicked right away. I also have a creative idea for how to visualize the comparisons and swaps.
## Demo video/gif/screenshot of test



https://github.com/user-attachments/assets/b5adbaf5-5d6a-4275-a4d5-e44e8bc4954a



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

<img width="440" height="1951" alt="BubbleSort drawio" src="https://github.com/user-attachments/assets/1b5e538a-76e1-471d-89a6-a25b8764e66f" />

## Steps to Run:
1. Use the default list, or enter a comma separated list of integers into the input box, or click random to generate a list automatically.

2. Click Load/Reset to load the values into the visualizer

3. Press play to start the Bubble Sort animation

4. Adjust the playback speed slider while the algorithm is running if you want it to go faster or slower.

5. Press pause at any time to stop the animation.

## Hugging Face Link
https://huggingface.co/spaces/137hrs/Bubble_Sort_Visualizer

## Author & Acknowledgment
Author: Denis Rodin

Note: At first, I wanted to build a much more complex animation system with water and bubble effects. I explored doing this with Gradio but found it insufficient, so I started learning Pillow. Eventually, I realized my original idea was too ambitious, so I simplified the project.

Acknowledgements:
While developing this project i used a few tools to help me polish and debug my code:

1. I used Google's Gemini to help identify and fix several bugs in my draft, especially issues involving the animation loop, frame timing, and how the UI updated between steps. It helped me trouble shoot places where the code wasn't behaving in the way I expected.
Chat link: https://gemini.google.com/share/9b58237c460c 

2. I also used VS Code's built in GitHub Copilot for small auto completions such as finishing comments or simple ilnes of code.
