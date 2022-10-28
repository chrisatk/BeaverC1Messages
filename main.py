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

for option in options:
  check = ""
  for char in option:
    check = check + key[char]
  if check == answer:
     print(option+" is the answer")