def read_file(file_name):
    with open(file_name) as file:
        datafile = file.readlines()
    for line in datafile:
        line = line.replace(".", "").replace(",", "").lower()
        stroke = line.split()
        words_set = set(stroke)
        return words_set


def save_file(file_name, words: set):
    with open(file_name, 'w') as file:
        file.write(f"Всего уникальных слов: {words.__len__()}\n")
        file.write("========================================\n")

        for word in sorted(words):
            file.write(f"{word}\n")


def main():
    words = read_file("data.txt")
    save_file("save.txt", words)


main()
