# Python Utils

5 pure-Python utilities built during Month 1 (Week 1) of my data science learning roadmap.
## What it does
- `prime_sieve(n)` — Find all primes up to n using Sieve of Eratosthenes
- `caesar_cipher(text, shift, decrypt=False)` — Encode/decode Caesar cipher

## How to run
```bash
python test_utils.py
```

## Examples
```python
from utils import *

# Prime sieve
number = 30
print(tils.prime_sieve(number))
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Caesar cipher
text = hello
shift = 4
mode = encrypt
print(utils.caesar_cipher(text, shift, mode))
# Output: "lipps"
```
Built during **Month 1 (Day 10 checkpoint)** of my [12-month Data Science roadmap](https://github.com/YashrajMishra02/pythonLearning).
