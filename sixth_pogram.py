import re

# Function to validate a postal code
def is_valid_postal_code(postal_code):
    pattern = re.compile(r'^\d{5}(-\d{4})?$')
    return bool(pattern.match(postal_code))

# Function to get postal codes from the user
def get_user_input():
    while True:
        try:
            user_input = input("Enter postal codes separated by commas (e.g., 12345, 12345-6789): ")
            postal_codes = [code.strip() for code in user_input.split(',')]
            return postal_codes
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

# Function to display the validation results
def display_results(postal_codes):
    for code in postal_codes:
        if is_valid_postal_code(code):
            print(f"'{code}' is a valid postal code.")
        else:
            print(f"'{code}' is not a valid postal code.")

def main():
    postal_codes = get_user_input()
    display_results(postal_codes)

if __name__ == "__main__":
    main()
