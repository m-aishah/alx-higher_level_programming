#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

int intCmp(int a[], int b[], int length);
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
	int forward[1024], backward[1024];
	int index = 0, length;

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
	length = index + 1;
	for (index = 0; forward[index]; index++)
	{
		backward[index] = forward[length - index - 1];
	}

	return (intCmp(forward, backward, length));
}

/**
 * intCmp - A function to compare 2 integer arrays
 * @a: First array
 * @b: second array
 * @length: Length of the arrays
 * Return: 1, if the integers are the same
 *	0- otherwise
 */

int intCmp(int a[], int b[], int length)
{
	int i;

	for (i = 0; i < length; i++)
	{
		if (a[i] != b[i])
		return (0);
	}
	return (1);
}
