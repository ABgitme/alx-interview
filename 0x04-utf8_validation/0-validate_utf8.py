#!/usr/bin/python3


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): A list of integers where each integer represents a byte.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes remaining in the current UTF-8 character
    bytes_remaining = 0

    for num in data:
        # Get the last 8 bits of the integer to represent the byte
        byte = num & 0xFF

        if bytes_remaining == 0:
            # Determine how many bytes the character has
            if (byte >> 7) == 0b0:       # 1-byte character (0xxxxxxx)
                bytes_remaining = 0
            elif (byte >> 5) == 0b110:   # 2-byte character (110xxxxx)
                bytes_remaining = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character (1110xxxx)
                bytes_remaining = 2
            elif (byte >> 3) == 0b11110: # 4-byte character (11110xxx)
                bytes_remaining = 3
            else:
                return False
        else:
            # Check that the byte is a continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            bytes_remaining -= 1

    # If bytes_remaining is 0, all characters are valid
    return bytes_remaining == 0
