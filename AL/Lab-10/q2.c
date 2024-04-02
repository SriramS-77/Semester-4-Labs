#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("Enter the number of vertices: ");
    int n, e, v1, v2, w;
    scanf(" %d", &n);
    int **mat = (int **)calloc(n, sizeof(int *));

    for (int i = 0; i < n; i++)
    {
        mat[i] = (int *)calloc(n, sizeof(int));
    }
    printf("Enter number of edges: ");
    scanf(" %d", &e);
    for (int i = 0; i < e; i++)
    {
        printf("Enter outdegree vertex and indegree vertex: ");
        scanf(" %d %d %d", &v1, &v2, &w);
        mat[v1][v2] = w;
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if(mat[i][j] == 0 && i != j)
                mat[i][j] = 999999;
            printf("%d\t", mat[i][j]);
        }
        printf("\n");
    }

    for (int k=0; k<n; k++){
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if (mat[k][j] + mat[i][k] < mat[i][j]){
                    mat[i][j] = mat[k][j] + mat[i][k];
                }
            }
        }
    }

    printf("\nShort path between vertices: \n");

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%d\t", mat[i][j]);
        }
        printf("\n");
    }
   
}