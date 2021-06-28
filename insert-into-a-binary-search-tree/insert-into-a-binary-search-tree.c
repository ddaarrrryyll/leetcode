/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


struct TreeNode* insertIntoBST(struct TreeNode* root, int val){
    // printf("%d\n", root->val);
    if (!root) {
        struct TreeNode* temp = malloc(sizeof(struct TreeNode));
        temp->left = NULL;
        temp->right = NULL;
        temp->val = val;
        root = temp;
        printf("inserted %d in %p\n", root->val, root);
    } else {
        printf("%d at %p\n", root->val, root);
        if (val > root->val) root->right = insertIntoBST(root->right, val);
        else root->left = insertIntoBST(root->left, val);
    
        printf("%d curr %p left %p right %p\n", root->val, root, root->left, root->right);
    }
    
    return root;
}