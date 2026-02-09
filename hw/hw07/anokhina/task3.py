def character_count(word: str) -> dict:
  """
  Counts the occurrences of each character in a given word.
  """
  cont = {}

  for i in word:
    if i in cont:
      cont[i] += 1
    else:
      cont[i] = 1

  return cont