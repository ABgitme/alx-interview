#!/usr/bin/python3
"""
This module contains the function canUnlockAll,
which determines if all boxes in a list of locked boxes
can be unlocked using keys provided in the boxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    Args:
        boxes (list of lists): A list where each index represents
        a box and contains a list of keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.

    Example:
        boxes = [[1], [2], [3], [4], []]
        print(canUnlockAll(boxes))  # Output: True

        boxes = [[1, 4, 6], [2], [0, 4, 1],
        [5, 6, 2], [3], [4, 1], [6]]
        print(canUnlockAll(boxes))  # Output: True

        boxes = [[1, 4], [2], [0, 4, 1], [3],
        [], [4, 1], [5, 6]]
        print(canUnlockAll(boxes))  # Output: False
    """
    # Set to keep track of unlocked boxes
    unlocked = set([0])
    # Stack for DFS traversal, starting with the first box (0)
    keys = [0]

    # Perform DFS-like traversal
    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                keys.append(key)

    # If all boxes are unlocked,
    # the size of unlocked should match the number of boxes
    return len(unlocked) == len(boxes)
