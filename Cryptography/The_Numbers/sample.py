def convert_number_to_alphabet(input):
    numbers = input.split()

    final_string = ""


    for num in numbers:
        if num.isnumeric():
            number = int(num)

            if 1 <= number <= 26:
                letter = chr(96 + number)
                final_string += letter
        else:
            final_string += num
    return final_string

enc_flag = "16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }"

flag = convert_number_to_alphabet(enc_flag)

print(flag)
