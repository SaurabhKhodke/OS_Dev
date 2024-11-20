#!/bin/bash 
 
# Bubble Sort Function 
bubble_sort() { 
    local arr=("$@") 
    local n=${#arr[@]} 
 
    for ((i = 0; i < n-1; i++)); do 
        for ((j = 0; j < n-i-1; j++)); do 
            if [ "${arr[j]}" -gt "${arr[j+1]}" ]; then 
                # Swap 
                temp="${arr[j]}" 
                arr[j]="${arr[j+1]}" 
                arr[j+1]="$temp" 
            fi 
        done 
    done 
 
    echo "Sorted array: ${arr[@]}" 
} 
 
# Example  
array=(45 27 18 11 10 17 99) 
echo "Original array: ${array[@]}" 
bubble_sort "${array[@]}" 