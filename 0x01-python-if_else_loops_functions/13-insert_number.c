#include "lists.h"
/**
 * insert_node - function in C that inserts a number
 * @head: pointer to the head of a list
 * @number: number to insert into list
 * Return: pointer to new node on sucess and NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t)), *top = *head;
	listint_t *prev = top;

	if (!new_node)
		return (NULL);
	new_node->n = number;

	if (!top)
	{
		new_node->next = top, *head = new_node;
		return (new_node);
	}

	while (top->next)
	{
		if (top->n < number)
			prev = top, top = top->next;
		else
			break;
	}
	new_node->next = (top->next) ? top : NULL;
	if (prev == top)
		*head = new_node;
	else
	{
		if (top->next)
			prev->next = new_node;
		else
			top->next = new_node;
	}
	return (new_node);
}
