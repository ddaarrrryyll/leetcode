/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


struct TreeNode* deleteNode(struct TreeNode* root, int key){
    // base case
    if (root == NULL) return NULL;
    
    // traversing BST
    if (key < root->val) {root->left = deleteNode(root->left, key);}
    else if (key > root->val) {root->right = deleteNode(root->right, key);}
    // conditions met
    else if (key == root->val) {
        // if no children return NULL and 1 child
        if (root->left == NULL && root->right == NULL) return NULL;
        if (root->left == NULL && root->right != NULL) return root->right;
        if (root->left != NULL && root->right == NULL) return root->left;
        
        // 2 children, return left / right child 
        struct TreeNode *temp = root->left;
        // right most value of left child will be the biggest value smaller than right child
        // similarly left most value of right child will be smallest value bigger than left child
        // move target value and remove target value from original position
        while (temp->right != NULL) temp = temp->right;
        root->val = temp->val;
        root->left = deleteNode(root->left, temp->val);
    }
    return root;
}