/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution
{
public:
    ListNode* rotateRight(ListNode* head, int k)
    {
        int len = 0;

        ListNode* new_head;
        new_head = head;

        while(head != NULL)
        {
            len++;
            head = head->next;
        }

        if(len == 0)
        {
            return(new_head);
        }

        int first_element_index = len - (k%len);

        ListNode* new_start_element;

        head = new_head;

        for(int i=1; i<first_element_index; i++)
        {
            head = head->next;
        }

        new_start_element = head->next;
        head->next = NULL;

        if(new_start_element == NULL)
        {
            return(new_head);
        }

        head = new_start_element;



        while(head->next != NULL)
        {
            head = head->next;
        }

        head->next = new_head;

        return(new_start_element);
    }
};
