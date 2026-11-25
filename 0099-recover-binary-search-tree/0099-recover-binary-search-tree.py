class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = second = prev = None
        curr = root

        while curr:
            if not curr.left:
                # Process current node
                if prev and prev.val > curr.val:
                    if not first:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right
            else:
                # Find inorder predecessor
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if not pred.right:
                    # Create temporary thread and move left
                    pred.right = curr
                    curr = curr.left
                else:
                    # Revert thread, process current node, and move right
                    pred.right = None
                    if prev and prev.val > curr.val:
                        if not first:
                            first = prev
                        second = curr
                    prev = curr
                    curr = curr.right

        # Swap the values of the two misplaced nodes
        first.val, second.val = second.val, first.val
