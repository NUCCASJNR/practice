#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * main - get process identification
 
 *
 * Return: Always 0.
 */
int main(void)
{
    pid_t my_pid;
    /* check man getpid for the syntax*/

    my_pid = getpid();
    printf("%u\n", my_pid);
    return (0);
}