def get_phone(country, first, last):
    return f"{country}-{first}-{last}"

phone_num = get_phone(first=1124, last=82493, country=542)
print(phone_num)