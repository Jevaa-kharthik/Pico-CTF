flag = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
real_flag = ""

for char in flag:
    if char.isalpha():
        shift = 13
        if char.islower():
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        elif char.isupper():
            shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        real_flag += shifted_char
        if char.isnumeric():
            real_flag += char
    else:
        real_flag += char

print(real_flag)

