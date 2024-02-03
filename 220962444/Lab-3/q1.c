# include <stdio.h>
# include <stdlib.h>

int main(){
    printf("Enter number of elements: ");
    int n, count=0, temp, swap;
    scanf(" %d", &n);
    int *arr = (int*) calloc(n, sizeof(int));
    printf("Enter the numbers: ");
    for(int i=0; i<n; i++){
        scanf(" %d", arr+i);
    }
    printf("Before sorting:\n");
    for(int i=0; i<n; i++){
        printf("%d\t", arr[i]);
    }
    for(int i=0; i<n-1; i++){
        swap=0;
        for(int j=0; j<n-1-i; j++){
            count++;
            if(arr[j] > arr[j+1]){
                swap=1;
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
            if(!swap) break;
        }
    }
    printf("\n\nAfter sorting:\n");
    for (int i = 0; i < n; i++){
        printf("%d\t", arr[i]);
    }
    printf("\n\nCount of swaps = %d\n", count);
}