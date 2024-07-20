import keyword

# Function to check for keywords in a list of words
def find_keywords(word_list):
    keywords_found = [word for word in word_list if keyword.iskeyword(word)]
    return keywords_found

# Function to get a list of words from the user
def get_user_input():
    while True:
        try:
            user_input = input("Enter words separated by commas (e.g., while, hello, if): ")
            words = [word.strip() for word in user_input.split(',')]
            return words
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

# Function to display the results
def display_results(keywords_found):
    if keywords_found:
        print("Keywords found in the list:", ", ".join(keywords_found))
    else:
        print("No keywords found in the list.")
    print("All Python keywords:", ", ".join(keyword.kwlist))

def main():
    words_to_check = get_user_input()
    keywords_in_list = find_keywords(words_to_check)
    display_results(keywords_in_list)

if __name__ == "__main__":
    main()
