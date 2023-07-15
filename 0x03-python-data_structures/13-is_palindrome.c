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
		return (1);
	
	traverse = *head;
	while (traverse->next != NULL)
	{
		forward[index] = traverse->n;
		index++;
		traverse = traverse->next;
	}
	forward[index] = traverse->n;
	forward[index + 1] = '\0';
	for (index = 0; forward[index]; index++)
	{
		backward[index] = forward[strlen(forward) - index - 1];
	}
	backward[index] = '\0';
    
	if (!(strcmp(forward, backward)))
		return (1);
	else
		return (0);
}
