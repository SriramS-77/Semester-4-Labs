#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int arr[20];
    int top;
} STACK;

void push(STACK *ptr, int val)
{
    (ptr->top)++;
    ptr->arr[ptr->top] = val;
    return;
}

int pop(STACK *ptr)
{
    if (ptr->top == -1)
    {
        return -1;
    }
    return ptr->arr[(ptr->top)--];
}

void disp(STACK *ptr)
{
    printf("\nstack:   ");
    for (int i = 0; i <= ptr->top; i++)
    {
        printf("%d\t", ptr->arr[i]);
    }
}

int main()
{
    printf("Enter the number of vertices: ");
    int n, e, v1, v2, ntopo = 0, npush=0, start, in;
    scanf(" %d", &n);
    int **mat = (int **)calloc(n, sizeof(int *));
    int *topo = (int *)calloc(n, sizeof(int));
    int *push_order = (int *)calloc(n, sizeof(int));
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

    STACK stk, *ptr = &stk;
    ptr->top = -1;
    int top, visited, added;

    while(ntopo != n)
    {
        for (int i = 0; i < n; i++)
        {
            in = 0;
            for (int j = 0; j < n; j++)
            {
                if (mat[j][i])
                {
                    in = 1;
                    break;
                }
            }
            if (!in)
            {
                visited = 0;
                for(int k = 0; k<ntopo; k++){
                    if(topo[k] == i){
                        visited = 1;
                        break;
                    }
                }
                if(visited){
                    continue;
                }
                start = i;
                break;
            }
        }
        push(ptr, start);
        push_order[npush++] = start;
        while (ptr->top != -1)
        {
            disp(ptr);
            added = 0;
            top = ptr->arr[ptr->top];
            for (int i = 0; i < n; i++)
            {
                if (!mat[top][i])
                    continue;
                visited = 0;
                for (int j = 0; j < npush; j++)
                {
                    if (i == push_order[j])
                    {
                        visited = 1;
                        break;
                    }
                }
                if (!visited)
                {
                    push(ptr, i);
                    push_order[npush++] = i;
                    printf("Pushed %d\n", i);
                    added = 1;
                    break;
                }
            }
            if (added)
                continue;
            topo[ntopo++] = pop(ptr);
            printf("Popped %d\n", topo[ntopo - 1]);
        }
    }


    printf("\nPush order:\n");
    for (int i = 0; i < npush; i++)
    {
        printf("%d\t", push_order[i]);
    }
    printf("\nTopological sort:\n");
    for (int i = ntopo-1; i > -1; i--)
    {
        printf("%d\t", topo[i]);
    }
    printf("\n");
}