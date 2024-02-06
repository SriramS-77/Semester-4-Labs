#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    char str[100], pat[50];
    printf("Enter the string: ");
    fgets(str, 100, stdin);
    printf("Enter the pattern to match: ");
    fgets(pat, 50, stdin);
    int n = strlen(str)-1, count=0, j=0, l = strlen(pat)-1, match=0;
    for(int i=0; i<n-l+1; i++){
        j=0;
        count++;
        while(str[i+j]==pat[j]){
            j++;
            if(j==l){
                match = 1;
                break;
            }
            count++;
        }
        if(match) break;
    }
    if(match) printf("\nPattern matched!\n");
    else printf("\nPattern not matched!\n");
    printf("Count of comparisons = %d\n", count);
}