#include <iostream>
#include <queue>

using namespace std;

class TreeNode {
public:
	int val;
	TreeNode* left;
	TreeNode* right;
	TreeNode(int x): val(x), left(nullptr), right(nullptr){}
};

void xianxu(TreeNode* root) {
	if (root == nullptr) {
		return;
	}
	cout << root->val << " ";
	xianxu(root->left);
	xianxu(root->right);
}

void zhongxu(TreeNode* root) {
	if (root == nullptr) {
		return;
	}
	zhongxu(root->left);
	cout << root->val << " ";
	zhongxu(root->right);
}

void houxu(TreeNode* root) {
	if (root == nullptr) {
		return;
	}
	houxu(root->left);
	houxu(root->right);
	cout << root->val << " ";
}

void cengxu(TreeNode* root) {
	if (root == nullptr) {
		return;
	}
	
	queue<TreeNode*> q;
	q.push(root);
	while (!q.empty()) {
		int size = q.size();
		for (int i = 0; i < size; i++) {
			TreeNode* node = q.front();
			cout << node->val << " ";
			q.pop();
			if (node->left) {
				q.push(node->left);
			}
			if (node->right) {
				q.push(node->right);
			}
		}
	}
}