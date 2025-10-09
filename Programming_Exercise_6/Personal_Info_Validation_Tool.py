# Joe Botelle
# Programming Exercise 6: Validation Tool

# This program validates social security numbers, phone numbers, and zip codes.

# import regular expression module
import re


# Use re.fullmatch to match input to each number's pattern
def validate_format(value, label):
        patterns = {
            "Social Security Number": (r"\d{3}-\d{2}-\d{4}", "xxx-xx-xxxx"),
            "Phone Number": (r"\d{3}-\d{3}-\d{4}", "xxx-xxx-xxxx"),
            "Zip Code": (r"\d{5}(-\d{4})?", "xxxxx or xxxxx-xxxx")
        }
        pattern, example = patterns.get(label)
        if re.fullmatch(pattern, value):
            return True
        print(f"Please check your entry for {label} and re-enter exactly as shown. {example}: ")
        return False


#remove all non-digit characters from input
def clean_input(raw):
    return re.sub(r'\D', '', raw)


# Validate Social Security number: must be exactly 9 digits and follow SSA rules
def validate_social(social):
    digits = clean_input(social)
    if len(digits) != 9:
        return False

    area = digits[:3]
    group = digits[3:5]
    serial = digits[5:]

    if area == '000' or area == '666' or int(area) >= 900:
        return False
    if group == '00':
        return False
    if serial == '0000':
        return False

    return True


# Validate phone number: must be 10 digits and follow NANP rules
def validate_phone(phone):

    digits = clean_input(phone)
    if len(digits) != 10:
        return False

    area = digits[:3]
    exchange = digits[3:6]

    if area[0] in ('0', '1'):
        return False
    if exchange[0] in ('0', '1'):
        return False
    if area in ('911', '411', '211', '555'):
        return False

    return True


# Validate Zip code: must be 5 or 9 digits and follow USPS rules
def validate_zip(zip_code):

    digits = clean_input(zip_code)
    # Reject all zero and all nine inputs and any input not 5 or 9 digit in length
    if len(digits) not in (5, 9):
        return False
    if digits in ('00000', '000000000', '99999', '999999999'):
        return False

    # Reject unsused prefixes and zips outside of USPS range
    prefix = digits[:3]
    if prefix in ('000', '004'):
        return False
    if len(digits) == 5 and not (501 <= int(digits) <= 99950):
        return False
    if len(digits) == 9 and not (501 <= int(digits) <= 99950):
        return False

    return True


# Main Function
def main():
    print("Welcome to Personal Info Validation Tool.")
    print("This program will validate U.S. SSN's, Phone Numbers, and Zip Codes.\n")

    # Setup to loop until user exits
    while True:
        print("*" * 70)

        # Prompt the user for personal information and check for correct format using re.fullmatch
        while True:
            social = input("Please enter the Social Security Number (xxx-xx-xxxx): ")
            if validate_format(social, "Social Security Number"):
                break

        while True:
            phone = input("Thank you. Please enter the Phone Number (xxx-xxx-xxxx): ")
            if validate_format(phone, "Phone Number"):
                break

        while True:
            zip_code = input("Perfect. Please enter the Zip Code (xxxxx or xxxxx-xxxx): ")
            if validate_format(zip_code, "Zip Code"):
                break

        # Print the validation results
        print('\nValidation Results:')
        print("*" * 70)
        print(f"Social Security Number is: {'Valid' if validate_social(social) else 'Invalid'}")
        print(f"Phone Number is: {'Valid' if validate_phone(phone) else 'Invalid'}")
        print(f"Zip Code is: {'Valid' if validate_zip(zip_code) else 'Invalid'}")
        print("*" * 70)

        # Retry loop for yes/no prompt
        attempts = 0
        while True:
            again = input("Do you want to continue? (yes/no): ").strip().lower()
            if again == 'yes':
                break
            elif again == 'no':
                print("Thank you for using this program. Goodbye!")
                return
            else:
                attempts += 1
                if attempts >= 3:
                    print("Too many invalid responses. Thank you for using this program. Goodbye!")
                    return
                print("I'm sorry, I didn't understand that. Please enter 'yes' or 'no'.")

if __name__ == '__main__':
    main()

