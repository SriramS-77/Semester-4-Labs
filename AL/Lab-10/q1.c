#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("Enter the number of vertices: ");
    int n, e, v1, v2;
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
        scanf(" %d %d", &v1, &v2);
        mat[v1][v2] = 1;
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%d\t", mat[i][j]);
        }
        printf("\n");
    }

    int opcount = 0;

    for (int k=0; k<n; k++){
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                opcount++;
                if (mat[k][j] == 1 && mat[i][k] == 1){
                    mat[i][j] = 1;
                }
            }
        }
    }

    printf("\nTransitive Closure: \n");

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%d\t", mat[i][j]);
        }
        printf("\n");
    }

    printf("\nOpcount = %d\n", opcount);
   
}