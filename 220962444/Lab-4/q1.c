#include <stdio.h>
#include <stdlib.h>

void empty(int *arr, int n)
{
    for (int i = 0; i < n; i++)
    {
        arr[i] = 0;
    }
}

int *create(int *taken, int pos, int n)
{
    int *arr = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; i++)
    {
        if (i == pos)
        {
            arr[i] = 1;
            continue;
        }
        arr[i] = taken[i];
    }
    return arr;
}

int brute(int **arr, int *taken, int n, int cur, int min)
{
    if (cur == n)
    {
        return min;
    }
    int small = -1, val;
    for (int i = 0; i < n; i++)
    {
        if (taken[i])
            continue;
        else
        {
            val = brute(arr, create(taken, i, n), n, cur + 1, min + arr[cur][i]);
            if (small == -1 || val < small)
            {
                small = val;
            }
        }
    }
    return small;
}

int main()
{
    printf("Enter the number of people and jobs: ");
    int n;
    scanf(" %d", &n);
    int **arr = (int **)calloc(n, sizeof(int *));
    int *taken = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; i++)
    {
        arr[i] = (int *)calloc(n, sizeof(int));
        printf("Enter the weights for jobs done by person %d: ", i + 1);
        for (int j = 0; j < n; j++)
        {
            scanf(" %d", *(arr + i) + j);
        }
    }
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
        {
            printf("%d ", arr[i][j]);
        }
    int min = -1;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
        }
    }

    int res = brute(arr, taken, n, 0, 0);

    printf("\n\nResult = %d\n\n", res);
}