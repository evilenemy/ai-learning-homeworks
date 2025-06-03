try:
  with open("sample.txt", "r") as file:
    pass
except FileNotFoundError:
  with open("sample.txt", "w") as file:
    file.write(input("Enter some text for sample.txt: "))

with open("sample.txt", "r+") as file:
  words = [word.lower() for word in file.read().replace("\n", " ").replace(",", "").replace(".", "").split() if word.isalpha()]
  unique_words = set(words)
  words_count = {}
  for word in unique_words:
    words_count[word] = words.count(word)
  ranking_num = 5
  try:
    ranking_num = int(input("Please, enter number for show top words: "))
  except ValueError:
    print("You give incorrect symbol. You should enter number, by default this number is 5")
  results = f"Total words: {len(words)}\nTop {ranking_num} most common words:"
  for word, times in sorted(words_count.items(), key=lambda item: item[1], reverse=True)[:ranking_num]:
    results += f"\n{word} - {times} times"
  print(results)
  with open("word_count_report.txt", "w") as file2:
    file2.write("Word Count Report\n"+results)
  