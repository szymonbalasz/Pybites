def dec_to_base(number, base):
    if number < base:  # base case
        return number
    else:
        return 10 * dec_to_base(number//base, base) + (number % base)


if __name__ == '__main__':
    nums = [24, 177, 256, 1024, 2020]

    for num in nums:
        print(dec_to_base(num, 8))
