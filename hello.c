#include <stdio.h>

void foo(int arg)
{
    int n = 42;
    printf("foo %d %d\n", n, arg);
}

int main(void) {
    printf("hello, world\n");
    foo(28);
}