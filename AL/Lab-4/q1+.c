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

int brute(int **arr, int *taken, int n, int cur, int min, int last)
{
    static int opcount = 0;
    if (cur == n)
    {
        return min;
    }
    else if (cur == n - 1)
    {
        if (last)
        {
            printf("\nOpcount = %d\n", opcount);
        }
    }
    int small = -1, val, lastt;
    for (int i = 0; i < n; i++)
    {
        lastt = 0;
        if (taken[i])
            continue;
        else
        {
            if (i == n - 1 - cur && last)
            {
                lastt = 1;
            }
            opcount++;
            val = brute(arr, create(taken, i, n), n, cur + 1, min + arr[cur][i], lastt);
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

    int res = brute(arr, taken, n, 0, 0, 1);

    printf("\n\nResult = %d\n\n", res);
}