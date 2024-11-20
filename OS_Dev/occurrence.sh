#!/bin/bash

# Prompt user for the main string and substring
read -p "Enter the main string: " main_string
read -p "Enter the substring: " substring

# Initialize variables
count=0
positions=()

# Check if the substring exists in the main string
if [[ $main_string == *$substring* ]]; then
    echo "Substring found in the main string."
    
    # Use a loop to find all occurrences and their positions
    temp_string="$main_string"
    start_pos=0
    while [[ $temp_string == *$substring* ]]; do
        # Find the position of the current occurrence
        pos=$(expr index "$temp_string" "$substring")
        actual_pos=$((start_pos + pos))
        positions+=("$actual_pos")
        
        # Update the string and start position for next search
        temp_string=${temp_string:$pos}
        start_pos=$((actual_pos))
        
        # Increment the count
        count=$((count + 1))
    done
    
    # Print the results
    echo "Number of occurrences: $count"
    echo "Positions: ${positions[@]}"
else
    echo "Substring not found in the main string."
fi
