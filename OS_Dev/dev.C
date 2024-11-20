#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int multiply(int a, int b) {
    return a * b;
}

int divide(int a, int b) {
    if (b == 0) {
        printf("Error! Division by zero is not allowed.\n");
        return 0;
    }
    return a / b;
}

int main() {
    int choice;
    int num1, num2;

    printf("Simple Calculator in C\n");
    printf("1. Addition\n");
    printf("2. Subtraction\n");
    printf("3. Multiplication\n");
    printf("4. Division\n");
    printf("Enter your choice (1-4): ");
    scanf("%d", &choice);

    printf("Enter first number: ");
    scanf("%d", &num1);
    printf("Enter second number: ");
    scanf("%d", &num2);

    switch (choice) {
        case 1:
            printf("%d + %d = %d\n", num1, num2, add(num1, num2));
            break;
        case 2:
            printf("%d - %d = %d\n", num1, num2, subtract(num1, num2));
            break;
        case 3:
            printf("%d * %d = %d\n", num1, num2, multiply(num1, num2));
            break;
        case 4:
            printf("%d / %d = %d\n", num1, num2, divide(num1, num2));
            break;
        default:
            printf("Invalid choice!\n");
    }

    return 0;
}