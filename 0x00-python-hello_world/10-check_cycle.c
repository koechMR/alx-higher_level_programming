#include "lists.h"
/**
 * check_cycle - checks if the linked list has a circle
 * @list: linked list to be checked
 * Return: 1 if the list has a cycle and 0 if doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = fast = list;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
