#include <stdio.h>
#include <stdlib.h>


int heapify(int arr[], int n, int i){
    int largest = i, temp, opcount = 0;
    int l = 2 * i + 1;
    int r = 2 * i + 2;
    if (l < n && arr[l] < arr[largest])
        largest = l;
    if (r < n && arr[r] < arr[largest])
        largest = r;
    if (largest != i){
        temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        return 1 + heapify(arr, n, largest);
    }
    return 0;
}

void heap(int arr[], int n, int *opcount){
    for (int i = n/2 - 1; i >= 0; i--){
        *opcount += heapify(arr, n, i);
    }
}

int main(){
    int n, opcount = 0;
    printf("Enter number of elements: ");
    scanf(" %d", &n);
    int *arr = (int*) calloc(n, sizeof(int));
    printf("Enter the elements:\n");
    for (int i = 0; i < n; i++)
    {
        scanf(" %d", arr + i);
    }
    heap(arr, n, &opcount);
    for (int i=0; i<n; i++){
        printf("%d\t", arr[i]);
    }
    printf("\nOpcount = %d\n", opcount);
}