#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a node in a sorted linked list
 *
 * @head: pointer to a pointer to the head node
 * @number: data to be held by the new node
 *
 * Return: pointer to the newly created node
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *next_node, *new;

	if (head == NULL)
		return (NULL);
	temp = *head;
	/* create the new node */
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (number < temp->n)
	{
		new->next = temp;
		*head = new;

		return (new);
	}
	while (temp != NULL)
	{
		next_node = temp->next;
		if (next_node->n > number)
			break;
		temp = temp->next;
	}

	if (temp == NULL)
	{
		new->next = NULL;
		temp->next = new;

		return (new);
	}
	temp->next = new;
	new->next = next_node;
	return (new);
}

