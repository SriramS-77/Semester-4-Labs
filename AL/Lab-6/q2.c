#include <stdio.h>
#include <stdlib.h>

int quicksort(int *arr, int n)
{
    if (n < 2)
    {
        return 0;
    }
    printf("%d\t", n);
    int pivot = arr[0], i = 0, j = n, temp, opcount = 0;
    while (i < j)
    {
        opcount += 2;
        do
        {
            opcount++;
            i++;
        } while (arr[i] < pivot && i < n);
        do
        {
            opcount++;
            j--;
        } while (arr[j] > pivot && j > -1);
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    temp = arr[i];
    arr[i] = arr[j];
    arr[j] = arr[0];
    arr[0] = temp;
    return opcount + quicksort(arr, j) + quicksort(arr + j + 1, n - 1 - j);
}

int main()
{
    int n;
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

    int opcount = quicksort(arr, n);
    printf("\nSorted array:\n");
    for (int i = 0; i < n; i++)
    {
        printf("%d\t", arr[i]);
    }
    printf("\nOpcount = %d\n", opcount);
}