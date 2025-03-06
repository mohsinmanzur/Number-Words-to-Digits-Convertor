# Convert Number Words to Digits in Python

This Python script converts number words (e.g., `"two hundred thousand"`) into their numeric equivalents (`200000`). It supports numbers up to **billions** and correctly handles multipliers like `"hundred"`, `"thousand"`, `"million"`, and `"billion"`.

## Features

- ✅ Converts words like `"three hundred fifty-two"` to `352`  
- ✅ Handles large numbers like `"one million two hundred thousand five"` → `1200005`  
- ✅ Works with standalone multipliers like `"hundred"` → `100`  
- ✅ Efficient **O(n)** time complexity  

## Usage

```python
print(numtodigit('seven hundred eighty six thousand three hundred'))  
# Output: 786300  

print(numtodigit('one million two hundred thousand five'))  
# Output: 1200005
```
## How It Works
1. Splits the input string into words.
2. Identifies numbers ("one", "twenty", etc.) and accumulates their values.
3. Applies multipliers ("hundred", "thousand", etc.) correctly.
4. Returns the final numeric value.

## Efficiency
1. Time Complexity: O(n) (Processes words in a single loop)
2. Space Complexity: O(1) (Uses only a few integer variables)

## Contributing
Feel free to suggest improvements or add support for more number formats!
