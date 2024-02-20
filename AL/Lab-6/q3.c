#include <stdio.h>
#include <stdlib.h>

int merge(int arr[], int low, int mid, int high){
    int opcount = 0, l1=0, l2=0, l=low;
    int a1[mid - low + 1], a2[high - mid];
    for(int i = low; i <= mid; i++)
        a1[i - low] = arr[i];
    for(int i = mid+1; i <= high; i++)
        a2[i - mid - 1] = arr[i];
    while (l1 < mid - low + 1 && l2 < high - mid){
        opcount++;
        if (a1[l1] < a2[l2]){
            arr[l++] = a1[l1++];
        }
        else{
            arr[l++] = a2[l2++];
        }
    }
    while(l1 < mid - low + 1)
        arr[l++] = a1[l1++];
    while(l2 < high - mid)
        arr[l++] = a2[l2++];
    return opcount;
}

void merge_sort(int arr[], int low, int high, int *count){
    if(high > low){
        int mid = (high + low) / 2;
        merge_sort(arr, low, mid, count);
        merge_sort(arr, mid+1, high, count);
        *count += merge(arr, low, mid, high);
    }
}

int main()
{
    int n, opcount = 0;
    printf("Enter number of elements: ");
    scanf(" %d", &n);
    int *arr = (int*) calloc(n, sizeof(int));
    printf("Enter the elemnets:\n");
    for (int i = 0; i < n; i++)
    {
        scanf(" %d", arr + i);
    }

    for (int i = 0; i < n; i++)
    {
        printf("%d\t", arr[i]);
    }

    merge_sort(arr, 0, n-1, &opcount);
    printf("\nSorted array:\n");
    for (int i = 0; i < n; i++)
    {
        printf("%d\t", arr[i]);
    }
    printf("\nOpcount = %d\n", opcount);
}