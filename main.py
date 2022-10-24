from setup import test_goal_1, test_goal_2, test_goal_3, decrypt_alien, secret_msg

"""
A secret message from outer space has been captured via the Parkes-Observatorium!
It's on you to decrypt the message.
"""

# Goal #1: Bring the message into the right order
# During translation the order of the message has gotten messed up. Reverse the order of each array in the message.

test_goal_1(secret_msg)

# Goal #2: Decrypt the numbers
# No one can understand what all these numbers mean. Using the decrypt_alien function, get a step closer to revealing the message.

test_goal_2(secret_msg)

# Goal #2: Now bring it all together

test_goal_3(secret_msg)