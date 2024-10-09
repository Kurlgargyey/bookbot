def main():
	with open("books/frankenstein.txt") as f:
		contents = f.read()
		print(contents)
		print(word_count(contents))

def word_count(string) -> int:
	return len(string.split())

main()