#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include "lists.h"

/**
 * insert_node - inserts a node in a proper place of sorted list
 * @head: first node of linked list
 * @number: number to add in linked list
 *
 * Return: Address of new node or NULL if failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *n_node;
	listint_t *tmp;

	if (!head)
		return (NULL);

	n_node = malloc(sizeof(listint_t));
	if (!n_node)
		return (NULL);
	n_node->n = number;

	tmp = *head;
	if (tmp)
	{
		if (tmp->n >= number)
		{
			n_node->next = tmp;
			*head = n_node;
		}
		else
		{
			while (tmp->next)
			{
				if (tmp->next->n < number)
					tmp = tmp->next;
				else
					break;
			}
			n_node->next = tmp->next;
			tmp->next = n_node;
		}
	}
	else
	{
		*head = n_node;
		n_node->next = NULL;
	}
	return (n_node);
}

