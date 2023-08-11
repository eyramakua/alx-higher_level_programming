#include "lists.h"
#include <stdio.h>

/**
* check_cycle - checks if the linked list contains a cycle
*@list: linked list to check
*
*Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *dull = list;
	listint_t *speed = list;

	if(!list)
		return (0);

	while (dull && speed && speed->next)
	{
		dull = dull->next;
		speed = speed->next;
		if (dull == speed)
			return (1);
	}
	return (0);
}
