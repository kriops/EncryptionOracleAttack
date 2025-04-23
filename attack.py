import re
import string

from message_sender import MessageSender

FLAG_PATTERN = re.compile(r"^TG25\{\S+\}$")
BLOCK_SIZE = 16

if __name__ == "__main__":
    sender = MessageSender(block_size=BLOCK_SIZE)
    flag = ""
    while FLAG_PATTERN.fullmatch(flag) is None:
        baseline_plaintext = "Q" * (
            BLOCK_SIZE + (BLOCK_SIZE - 1) - (len(flag) % BLOCK_SIZE)
        )
        baseline_ciphertext = sender.send(baseline_plaintext)
        print(baseline_plaintext, "-->", baseline_ciphertext)

        for c in string.printable:
            guess_plaintext = baseline_plaintext + flag + c
            guess_ciphertext = sender.send(guess_plaintext)
            print(guess_plaintext, "-->", guess_ciphertext)
            chunk_num = 1 + (len(flag) // 16)
            if baseline_ciphertext[chunk_num] == guess_ciphertext[chunk_num]:
                flag += c
                print(flag)
                break
