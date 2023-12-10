/*
 To reduce a fraction to lowest terms, first compute th GCD of the numerator
 and denominator. Then divide both the numenator and denominator by the GCD
*/
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int m, n;
    int gcd;
    int reminder;
    int num, denom;

    printf("Enter a fraction: ");
    scanf("%d/%d", &num, &denom);
    m = num;
    n = denom;
    
    if(denom == 0 || num ==0) {
        printf("Numerator or Denominator must not equqal 0\n");
        exit(0);
    }

    while(n != 0) {
        reminder = m % n;
        m = n;
        n = reminder;
        gcd = m; /* introducing gcd as a dedicated variable is not necessary, 
                    m is the gcd and can be used directly w/o gcd value */
        }

    printf("Fraction in lowest terms: %d/%d\n", num/gcd, denom/gcd );
    return 0;
}
