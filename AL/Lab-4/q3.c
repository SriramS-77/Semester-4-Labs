#include <stdio.h>
#include <stdlib.h>
# define MAX 20

typedef struct
{
    int arr[MAX];
    int front, back;
} QUEUE;

void enqueue(QUEUE *ptr, int val)
{
    if(ptr->front == -1){
        ptr->front = 0;
    }
    ptr->back = (ptr->back + 1) % MAX;
    ptr->arr[ptr->back] = val;
    return;
}

int dequeue(QUEUE *ptr)
{
    int val;
    if (ptr->front == -1)
    {
        return -1;
    }
    if (ptr->front == ptr->back){
        val = ptr->arr[ptr->front];
        ptr->front = ptr->back = -1;
    }
    else{
        val = ptr->arr[ptr->front];
        ptr->front = (ptr->front + 1) % MAX;
    }
    return val;
}

void disp(QUEUE *ptr)
{
    printf("\nqueue:   ");
    if (ptr->front == -1){
        printf("None\n");
        return;
    }
    for (int i = ptr->front; ; i = (i + 1)%MAX)
    {
        printf("%d\t", ptr->arr[i]);
        if(i == ptr->back){
            break;
        }
    }
    printf("\n");
}

int main()
{
    printf("Enter the number of vertices: ");
    int n, e, v1, v2, nvisit;
    scanf(" %d", &n);
    int **mat = (int **)calloc(n, sizeof(int *));
    int *visit = (int *)calloc(n, sizeof(int));
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

    QUEUE q, *ptr = &q;
    ptr->front = ptr->back = -1;
    enqueue(ptr, 0);
    visit[nvisit++] = 0;
    int top = dequeue(ptr), visited;
    while (top != -1)
    {
        for (int i = 0; i < n; i++)
        {
            if (!mat[top][i])
                continue;
            visited = 0;
            for (int j = 0; j < nvisit; j++)
            {
                if (i == visit[j])
                {
                    visited = 1;
                    break;
                }
            }
            if (!visited)
            {
                visit[nvisit++] = i;
                enqueue(ptr, i);
            }
        }
        top = dequeue(ptr);
    }
    printf("\nOrder of visiting:\n");
    for(int i=0; i<nvisit; i++){
        printf("%d\t", visit[i]);
    }
    printf("\n");
}