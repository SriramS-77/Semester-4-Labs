#include <stdio.h>
#include <stdlib.h>

int check(int arr[], int n, int key){
    for(int i=0; i<n; i++){
        if(arr[i] == key){
            return 1;
        }
    }
    return 0;
}

int main()
{
    printf("Enter the number of vertices: ");
    int n, e, v1, v2, ntopo = 0, start, in;
    scanf(" %d", &n);
    int **mat = (int **)calloc(n, sizeof(int *));
    int *topo = (int *)calloc(n, sizeof(int));
    int *indegree = (int *)calloc(n, sizeof(int));
    for (int i = 0; i < n; i++)
    {
        mat[i] = (int *)calloc(n, sizeof(int));
    }
    printf("Enter number of edges: ");
    scanf(" %d", &e);
    for (int i = 0; i < e; i++)
    {
        printf("Enter indegree vertex and outdegree vertex: ");
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

    for(int i=0; i<n; i++){
        in = 0;
        for(int j=0; j<n; j++){
            if(mat[j][i]){
                in++;
            }
        }
        indegree[i] = in;
    }

    while(ntopo != n){
        start = -1;
        for(int i=0; i<n; i++){
            if(!(indegree[i]) && !check(topo, ntopo, i)){
                start = i;
                break;
            }
        }
        if(start == -1){
            printf("\nTopological sort not possible!\n");
            break;
        }
        topo[ntopo++] = start;
        for(int i=0; i<n; i++){
            if(mat[start][i]){
                indegree[i]--;
            }
        }
    }

    printf("\nTopological sort:\n");
    for (int i = 0; i < ntopo; i++)
    {
        printf("%d\t", topo[i]);
    }
    printf("\n");
}