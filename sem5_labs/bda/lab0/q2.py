import streamlit as st
import numpy as np
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr

def parallel_selection_sort(arr):
    n = len(arr)
    for i in range(n//2):
        min_idx = i
        max_idx = i
        for j in range(i, n-i):
            if arr[j] < arr[min_idx]:
                min_idx = j
            if arr[j] > arr[max_idx]:
                max_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        if max_idx == i:
            max_idx = min_idx
        if max_idx != n-i-1:
            arr[n-i-1], arr[max_idx] = arr[max_idx], arr[n-i-1]
        yield arr

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        yield arr
        yield from heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        yield arr
        yield from heapify(arr, i, 0)

def merge_sort(arr, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    yield from merge_sort(arr, left, mid)
    yield from merge_sort(arr, mid + 1, right)
    yield from merge(arr, left, mid, right)
    yield arr

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = arr[left:mid+1]
    R = arr[mid+1:right+1]
    i = j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        yield arr
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        yield arr
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        yield arr

def quick_sort(arr, low, high):
    if low < high:
        pi, arr = partition(arr, low, high)
        yield arr
        yield from quick_sort(arr, low, pi - 1)
        yield from quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1, arr

def augment_sort(arr):
    # Example of an augmented sort that switches between quicksort and insertion sort
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
                yield arr
            arr[j + 1] = key
            yield arr

    def quicksort(arr, low, high):
        if low < high:
            pi, arr = partition(arr, low, high)
            yield arr
            yield from quicksort(arr, low, pi - 1)
            yield from quicksort(arr, pi + 1, high)
        elif high - low < 10:  # Switch to insertion sort for small segments
            yield from insertion_sort(arr[low:high + 1])

    yield from quicksort(arr, 0, len(arr) - 1)

def main():
    st.title("Sorting Algorithms Visualization")
    
    st.sidebar.header("Settings")
    array_size = st.sidebar.slider("Array Size", 5, 50, 10, key="array_size_slider")
    speed = st.sidebar.slider("Speed (seconds)", 0.1, 1.0, 0.3, key="speed_slider")

    array = np.random.randint(1, 101, array_size)
    st.write("Unsorted Array:")
    st.bar_chart(array)

    sorting_algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Parallel Selection Sort": parallel_selection_sort,
        "Heap Sort": heap_sort,
        "Merge Sort": lambda arr: merge_sort(arr, 0, len(arr) - 1),
        "Quick Sort": lambda arr: quick_sort(arr, 0, len(arr) - 1),
        "Augment Sort": augment_sort
    }

    if st.button("Start Sorting"):
        with st.expander("Bubble Sort"):
            bubble_sort_array = array.copy()
            bubble_placeholder = st.empty()
            for arr in bubble_sort(bubble_sort_array):
                bubble_placeholder.bar_chart(arr)
                time.sleep(speed)

        with st.expander("Selection Sort"):
            selection_sort_array = array.copy()
            selection_placeholder = st.empty()
            for arr in selection_sort(selection_sort_array):
                selection_placeholder.bar_chart(arr)
                time.sleep(speed)

        with st.expander("Parallel Selection Sort"):
            parallel_selection_sort_array = array.copy()
            parallel_selection_placeholder = st.empty()
            for arr in parallel_selection_sort(parallel_selection_sort_array):
                parallel_selection_placeholder.bar_chart(arr)
                time.sleep(speed)

        with st.expander("Heap Sort"):
            heap_sort_array = array.copy()
            heap_placeholder = st.empty()
            for arr in heap_sort(heap_sort_array):
                heap_placeholder.bar_chart(arr)
                time.sleep(speed)

        with st.expander("Merge Sort"):
            merge_sort_array = array.copy()
            merge_placeholder = st.empty()
            for arr in merge_sort(merge_sort_array, 0, len(merge_sort_array) - 1):
                merge_placeholder.bar_chart(arr)
                time.sleep(speed)

        with st.expander("Quick Sort"):
            quick_sort_array = array.copy()
            quick_placeholder = st.empty()
            for arr in quick_sort(quick_sort_array, 0, len(quick_sort_array) - 1):
                quick_placeholder.bar_chart(arr)
                time.sleep(speed)

        with st.expander("Augment Sort"):
            augment_sort_array = array.copy()
            augment_placeholder = st.empty()
            for arr in augment_sort(augment_sort_array):
                augment_placeholder.bar_chart(arr)
                time.sleep(speed)

if __name__ == "__main__":
    main()
