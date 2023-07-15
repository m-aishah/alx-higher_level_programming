#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - a function in C that checks
 *		if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome,
 *		1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *traverse;
	char forward[1024], backward[1024];
	int index = 0;

	if (*head == NULL || (*head)->next == NULL)
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
printf("%s", forward);
	for (index = 0; forward[index]; index++)
	{
		backward[index] = forward[strlen(forward) - index - 1];
	}
	backward[index] = '\0';
printf("%s", backward);
	if (!(strcmp(forward, backward)))
		return (1);
	else
		return (0);
}
