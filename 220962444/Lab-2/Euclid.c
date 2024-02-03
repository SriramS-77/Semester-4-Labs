#include <stdio.h>
unsigned int EuclidGCD(unsigned int m, unsigned int n)
{
    unsigned int r;
    int opcount = 0; // variable to count how many times the basic operation executes.
    while (n != 0)
    {
        opcount++;
        r = m % n;
        m = n;
        n = r;
    }
    printf("Operation count = %d\n", opcount);
    return m;
}
int main()
{
    int m, n;
    printf("Enter the 2 numbers: ");
    scanf("%d", &m);
    scanf("%d", &n);
    printf("GCD of two numbers using Euclid's method is % d\n",
           EuclidGCD(m, n));
    return 0;
}