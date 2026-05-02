'''Implement Quick Sort, a Divide and Conquer algorithm, to sort an array, arr[] in ascending order.
Given an array arr[], with starting index low and ending index high, complete the functions partition() and quickSort().
Use the last element as the pivot, so that all elements less than or equal to the pivot come before it, and elements greater than the pivot follow it.

Note: low and high are inclusive.'''
#code
class Solution:
    # Function to sort an array using quick sort algorithm.
    def quickSort(self, arr, low, high):
        if low < high:
            # pi is partitioning index, arr[pi] is now at right place
            pi = self.partition(arr, low, high)
            
            # Separately sort elements before partition and after partition
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)
    
    def partition(self, arr, low, high):
        # Using the last element as the pivot
        pivot = arr[high]
        
        # Index of smaller element and indicates the right position 
        # of pivot found so far
        i = low - 1
        
        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if arr[j] <= pivot:
                i += 1
                # Swap arr[i] and arr[j]
                arr[i], arr[j] = arr[j], arr[i]
        
        # Swap the pivot element with the element at i+1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        
        # Return the position where the pivot was placed
        return i + 1
