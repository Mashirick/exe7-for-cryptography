import math


def md5(message):
    # Constants for MD5
    s = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4
    K = [int(abs(math.sin(i + 1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

    # Initial values (A, B, C, D)
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476

    # Helper functions
    def F(X, Y, Z):
        # TODO
        return ((X & Y) | (~X & Z)) & 0xFFFFFFFF

    def G(X, Y, Z):
        # TODO
        return ((X & Z) | (Y & (~Z))) & 0xFFFFFFFF

    def H(X, Y, Z):
        # TODO
        return (X ^ Y ^ Z) & 0xFFFFFFFF

    def I(X, Y, Z):
        # TODO
        return (Y ^ (X | (~Z))) & 0xFFFFFFFF

    # Rotate left function
    def rotate_left(x, n):
        # TODO
        return ((x << n) | (x >> 32 - n)) & 0xFFFFFFFF

    # Padding the message
    original_length = len(message)
    message += b'\x80'

    while len(message) % 64 != 56:
        message += b'\x00'
    message += (original_length * 8).to_bytes(8, byteorder='little')

    # Process each 512-bit block
    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]
        M = [int.from_bytes(chunk[j:j + 4], byteorder='little') for j in range(0, 64, 4)]

        AA, BB, CC, DD = A, B, C, D

        for j in range(64):
            # TODO
            if j >= 0 and j <= 15:
                T = F(BB, CC, DD)
                g = j
            elif j >= 16 and j <= 31:
                T = G(BB, CC, DD)
                g = (5 * j + 1) % 16
            elif j >= 32 and j <= 47:
                T = H(BB, CC, DD)
                g = (3 * j + 5) % 16
            elif j >= 48 and j <= 63:
                T = I(BB, CC, DD)
                g = (7 * j) % 16
            T = (T + AA + K[j] + M[g]) & 0xFFFFFFFF
            AA = DD
            DD = CC
            CC = BB
            BB = BB + rotate_left(T, s[j])

        A = (A + AA) & 0xFFFFFFFF
        B = (B + BB) & 0xFFFFFFFF
        C = (C + CC) & 0xFFFFFFFF
        D = (D + DD) & 0xFFFFFFFF

    # Concatenate the final hash
    result = (A.to_bytes(4, byteorder='little') +
              B.to_bytes(4, byteorder='little') +
              C.to_bytes(4, byteorder='little') +
              D.to_bytes(4, byteorder='little'))
    return result

# MD5 test suite:
# MD5 ("") = d41d8cd98f00b204e9800998ecf8427e
# MD5 ("a") = 0cc175b9c0f1b6a831c399e269772661
# MD5 ("abc") = 900150983cd24fb0d6963f7d28e17f72
# MD5 ("message digest") = f96b697d7cb7938d525a2f31aaf161d0

message = ""
hash_result = md5(message.encode())
print(f"MD5 hash of '{message}': {hash_result.hex()}")
message = "a"
hash_result = md5(message.encode())
print(f"MD5 hash of '{message}': {hash_result.hex()}")
message = "abc"
hash_result = md5(message.encode())
print(f"MD5 hash of '{message}': {hash_result.hex()}")
message = "message digest"
hash_result = md5(message.encode())
print(f"MD5 hash of '{message}': {hash_result.hex()}")


