#!/bin/bash 
 
# Function to check if a string is a palindrome 
check_palindrome() { 
    local str="$1" 
    local len=${#str} 
     
    for ((i = 0; i < len / 2; i++)); do 
        if [ "${str:i:1}" != "${str:len-i-1:1}" ]; then 
            echo "The string '$str' is not a palindrome." 
            return 
        fi 
    done 
     
    echo "The string '$str' is a palindrome." 
} 
 
# Read input from the user 
read -p "Enter a string: " input 
 
# Call the function with the user's input 
check_palindrome "$input"