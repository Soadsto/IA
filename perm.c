#include <stdio.h>
int p[10], u[10], c, n;

void init()
{
    printf("n: "); scanf("%d", &n);
    for(int i = 0; i < n; ++i) 
        u[i] = 0;
    c = 0;
}

void imprime()
{
    for(int i = 0; i < n; ++i)
        printf("%4d", p[i]);
    printf("\n");
}

void permuta()
{
    for(int i = 0; i < n; ++i)
        if(!u[i])
        {
            p[c++] = i + 1;
            u[i] = 1;
            if(c == n)
                imprime();
            else
                permuta();
            --c;
            u[i] = 0;
        }
}

int main()
{
    init();
    permuta();
    return 0;
}