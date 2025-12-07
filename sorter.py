def bubble_sort(nums):
    # Holds every recorded step 
    steps = []

    # Works on a copy so original user input stays unchanged
    arr = nums.copy()
    n = len(arr)

    # Initial state
    steps.append({
        "type": "init",
        "array": arr.copy()
    })

    # Bubble sort 
    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):

            # Records a comparison step
            steps.append({
                "type": "compare",
                "i": j,
                "j": j + 1,
                "array": arr.copy()
            })

            # Performs swap if needed
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

                # Records the swap
                steps.append({
                    "type": "swap",
                    "i": j,
                    "j": j + 1,
                    "array": arr.copy()
                })

        # EFf no swaps occur exit early
        if not swapped:
            break

    # Displays done when sorting is complete
    steps.append({
        "type": "done",
        "array": arr.copy()
    })

    return steps
