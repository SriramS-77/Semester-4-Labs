#include <stdio.h>

int isPrime(int a, int* opcount){
    int prime=1;
    for(int i=2; i<=a/2; i++){
        (*opcount)++;
        if(a%i==0){
            prime=0;
            break;
        }
    }
    return prime;
}

int GCD(int a, int b)
{
    int gcd=1, div, opcount=0;
    int min = a<b ? a : b;
    for(int i = 2; i<=min/2+1; i++){
        if(isPrime(i, &opcount)){
            div=i;
            opcount++;
            while(a%div==0 && b%div==0){
                gcd *= i;
                div *= i;
                opcount++;
            }
        }
    }
    printf("Opcount of the operation = %d\n", opcount);
    return gcd;
}

int main()
{
    printf("Enter the 2 numbers: ");
    int a, b;
    scanf(" %d %d", &a, &b);
    int gcd = GCD(a, b);
    printf("GCD is %d\n", gcd);
}