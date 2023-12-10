/*
 Euclid's GCD algorithm:
 Lem m and n be variables containing the two numbers
 In n is 0, then stop: m contains th GCD. Otherwise, 
 compute the reminder when m is divided by n. Copy n
 into m and copy the remainder into n. Then repeat the 
 process, starting with testing whether n is 0.
*/
#include <stdio.h>

void printdiv(int div) {
    printf("Greates common dvisor: %d\n", div);
}

int main(void) {
    int num1, num2;
    int commondiv = 0;
    int reminder;

    printf("Enter two integers: ");
    scanf("%d %d", &num1, &num2);

    while (1) {
        if (num1 == 0 || num2 == 0) {
            printdiv(commondiv);
            break;
        }
        reminder = num1 % num2;
        num1 = num2;
        num2 = reminder;
        commondiv = num1;
        printf("num1 = %d, num2 = %d, commondiv = %d\n", num1, num2, commondiv);
    }
    return 0;
}
