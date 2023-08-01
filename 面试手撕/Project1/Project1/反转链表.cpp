#include <iostream>

using namespace std;


class ListNode {
public:
	int val;
	ListNode* next;
	ListNode(int x):val(x), next(nullptr){}
};

//ListNode* reverse(ListNode* head) {
//	ListNode* curr = head;
//	ListNode* pre = nullptr;
//	while (curr) {
//		ListNode* next = curr->next;
//		curr->next = pre;
//		pre = curr;
//		curr = next;
//	}
//	return pre;
//}

//// µü´ú
//ListNode* reverse(ListNode* head) {
//	ListNode* curr = head;
//	ListNode* prev = nullptr;
//	while (curr) {
//		ListNode* next = curr->next;
//		curr->next = prev;
//		prev = curr;
//		curr = next;
//	}
//	return prev;
//}

// µÝ¹é
ListNode* reverse(ListNode* head) {
	if (head == nullptr || head->next == nullptr) {
		return head;
	}
	ListNode* newhead = reverse(head->next);
	head->next->next = head;
	head->next = nullptr;
	return newhead;
}

void Print(ListNode* head) {
	ListNode* curr = head;
	while (curr) {
		cout << curr->val << " ";
		curr = curr->next;
	}
	cout << endl;
}

//void main() {
//	ListNode* node1 = new ListNode(1);
//	ListNode* node2 = new ListNode(2);
//	ListNode* node3 = new ListNode(3);
//
//	node1->next = node2;
//	node2->next = node3;
//	Print(node1);
//	ListNode* head = reverse(node1);
//	Print(head);
//}

