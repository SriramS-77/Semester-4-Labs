#include <stdio.h>
#include <stdlib.h>

int max(int a, int b){
    if(a > b)
        return a;
    return b;
}

int main()
{
    printf("Enter the number of items: ");
    int n, w;
    scanf(" %d", &n);

    int *weight = (int *)calloc(n, sizeof(int));
    int *profit = (int *)calloc(n, sizeof(int));

    printf("Enter weights and profits for them: ");

    for (int i = 0; i < n; i++)
    {
        scanf(" %d %d", weight+i, profit+i);
    }

    printf("Enter total possible weight: ");
    scanf(" %d", &w);

    int **mat = (int**) calloc(n+1, sizeof(int*));

    for(int i=0; i<n+1; i++){
        mat[i] = (int*) calloc(w+1, sizeof(int));
    }

    for(int i=0; i<n+1; i++){
        for(int j=0; j<w+1; j++){
            if (!i || !j)
                mat[i][j] = 0;
            else{
                if(j - weight[i-1] < 0)
                    mat[i][j] = mat[i-1][j];
                else{
                    mat[i][j] = max(mat[i-1][j], profit[i-1] + mat[i-1][j-weight[i-1]]);
                }
            }
        }
    }

    printf("Maximum profit possible = %d\n", mat[n][w]);

    printf("\nMatrix:\n\n");

    for(int i=0; i<n+1; i++){
        for(int j=0; j<w+1; j++){
            printf("%d\t", mat[i][j]);
        }
        printf("\n");
    }
}