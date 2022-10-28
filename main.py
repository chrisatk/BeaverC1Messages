answer = "1001001100010100010111000";
key = { 
  't':'1', 
  'e':'00', 
  'a':'0010', 
  'k':'0110', 
  'c':'1010', 
  'r':'1110'
}
options = [
  "teacrate",
  "eatcake",
  "takecare",
  "retake"
]

# Loop through each of the options
for option in options:
  check = "" # initialize an empty string to check against the answer
  # Loop through each character in the word
  for char in option:
    # Convert the characters to the binary values in the key dict
    check = check + key[char]
  if check == answer:
    # Compare the converted option to the answer to find a winner
     print(option+" is the answer")