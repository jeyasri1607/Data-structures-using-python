def bubble_sort(marks):
    n = len(marks)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]

# Insertion Sort Function
def insertion_sort(marks):
    for i in range(1, len(marks)):
        key = marks[i]
        j = i - 1
        while j >= 0 and marks[j] > key:
            marks[j + 1] = marks[j]
            j -= 1
        marks[j + 1] = key

# Main Program
marks = [75, 60, 85, 50, 90, 70]
print("Original marks:", marks)

# Bubble Sort
bubble_sorted = marks.copy()
bubble_sort(bubble_sorted)
print("Marks after Bubble Sort:", bubble_sorted)

# Insertion Sort
insertion_sorted = marks.copy()
insertion_sort(insertion_sorted)
print("Marks after Insertion Sort:", insertion_sorted)
