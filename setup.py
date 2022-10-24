def test_goal_1(msg):
  reversed = [[72,101,114,122,108,105,99,104,101,110],[71,108,252,99,107,119,117,110,115,99,104],[122,117,109],[71,101,98,117,114,116,115,116,97,103]]
  if (msg==reversed): print("Goal #1 succeeded")
  else: exit("Error at Goal #1: the items of the list are not yet in correct order")

def test_goal_2(msg):
  nums = ["0","1","2","3","4","5","6","7","8","9"]
  try:
    stringified = "".join([i for s in msg for i in s])
    for num in nums:
      if num in stringified: raise
    print("Goal #2 succeeded")
  except: exit("Error at Goal #2: decryption unsuccessful")

def test_goal_3(msg):
  solution = "Herzlichen Glückwunsch zum Geburtstag"
  if msg == solution: print("Congratulations, you successfully decrypted the message!")
  else: exit("Error at Goal #3: wrong format")
  
def decrypt_alien(inp): return chr(inp)

secret_msg = [[110,101,104,99,105,108,122,114,101,72],[104,99,115,110,117,119,107,99,252,108,71],[109,117,122],[103,97,116,115,116,114,117,98,101,71]]