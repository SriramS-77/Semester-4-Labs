#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void generate_harr(int *harr, char *str, int n){
    int dist;
    for(int i=0; i < n; i++){
        dist = 1;
        for(int j=i-1; ; j--, dist++){
            if(j == -1){
                dist = i + 1;
                break;
            }
            if(str[j] == str[i]){
                break;
            }
        }
        harr[i] = dist;
    }
    for(int i=0; i<n; i++){
        printf("%d ", harr[i]);
    }
}

int find_pattern_in_string(char *str, int m, char *pat, int n, int *harr){
    int j, last;
    for(int i = 0; i < m-n+1; i++){
        j = n - 1;
        last = -1;
        while(str[i+j] == pat[j]){
            if (j == 0){
                return i;
            }
            last = j;
            j--;
        }
        if (last == -1){
            continue;
        }
        i += harr[last] - 1;
    }
    return -1;
}

int main()
{
    char str[100], pat[20];
    printf("Enter the string: ");
    fgets(str, 100, stdin);
    printf("Enter the pattern: ");
    fgets(pat, 20, stdin);
    int *harr = (int*) calloc(strlen(pat) - 1, sizeof(int));
    generate_harr(harr, pat, strlen(pat) - 1);
    int index = find_pattern_in_string(str, strlen(str)-1, pat, strlen(pat)-1, harr);
    printf("Found at %d index!!!\n", index);
}