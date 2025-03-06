digits = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
            'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'fourty': 40, 'fifty': 50, 'sixty': 60,
            'seventy': 70, 'eighty': 80, 'ninety': 90}

multiples = {'hundred': 100, 'thousand': 1000, 'million': 1000000, 'billion': 1000000000}

def numtodigit(str):
    nums = str.split(' ')
    temp = 0
    total = 0

    for word in nums:
        word = word.lower()
        if word in digits.keys():
            temp += digits[word]
        
        elif word in multiples.keys():
            if temp == 0:
                temp = 1

            temp *= multiples[word]

            if multiples[word] > 100:
                total += temp
                temp = 0
    
    total += temp
    return total

num = input('Enter number: ')
print(numtodigit(num))