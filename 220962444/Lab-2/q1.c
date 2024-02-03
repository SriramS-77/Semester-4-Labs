# include <stdio.h>

int gcd(int a, int b){
    int q, opcount=1;
    q = a<b ? a : b;
    while(!(a%q==0 && b%q==0)){
        q--;
        opcount++;
    }
    printf("Opcount is %d\n", opcount);
    return q;
}

int main(){
    printf("Enter the 2 numbers: ");
    int a, b;
    scanf(" %d %d", &a, &b);
    int GCD = gcd(a,b);
    printf("GCD is %d\n", GCD);
}