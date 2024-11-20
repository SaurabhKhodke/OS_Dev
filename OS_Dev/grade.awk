#!/usr/bin/awk -f

{
    # Input format is: "Name Score"
    name = $1
    score = $2

    # Determine grade based on score
    if (score < 40) {
        grade = "Fail"
    } else if (score >= 90 && score <= 100) {
        grade = "A"
    } else if (score >= 80 && score < 90) {
        grade = "B"
    } else if (score >= 70 && score < 80) {
        grade = "C"
    } else if (score >= 60 && score < 70) {
        grade = "D"
    } else {
        grade = "E"
    }

    # Print student's name and grade
    print name, grade
}
