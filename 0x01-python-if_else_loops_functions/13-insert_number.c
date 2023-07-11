#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *traverse1 = *head, *traverse2 = *head;
	listint_t *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;
	
	while (traverse1->n < number && traverse1->next != NULL)
	{
		traverse2 = traverse1;
		traverse1 = traverse1->next;
	}
	
	if (traverse1->next == NULL)
		add_nodeint_end(head, number);
	else
	{
		traverse2->next = newNode;
		newNode->next = traverse1;
	}
	return (newNode);
}
