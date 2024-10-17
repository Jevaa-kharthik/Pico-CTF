flag = "wpjvJAM{jhlzhy_k3jy9wa3k_m0212758}"
real_flag = ""

for char in flag:
    if char.isalpha():
        shift = 7
        if char.islower():
            shifted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
        elif char.isupper():
            shifted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        real_flag += shifted_char
        if char.isnumeric():
            real_flag += char
    else:
        real_flag += char

print(real_flag)

