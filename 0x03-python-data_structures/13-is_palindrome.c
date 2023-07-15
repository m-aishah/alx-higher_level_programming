#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
    listint_t *traverse;
    char forward[1024], backward[1024];
    int index = 0;

    if (*head == NULL)
        return (0);

    traverse = *head;
printf("%d", traverse->n);    
while (traverse->next != NULL)
    {
        forward[index] = traverse->n;
        index++;
    }
printf("%s", forward);
    forward[index] = traverse->n;
    for (index = 0; forward[index]; index++)
    {
        backward[index] = forward[strlen(forward) - index];
    }

    return (strcmp(forward, backward));
}
