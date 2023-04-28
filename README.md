# digitize

#### digitize - open source available library for determining the bit depth of a number with the output of its name

Install using pip:
```py
pip install digitize
```

# Basic Usage

```python
from digitize import discharge, Language

print(discharge(5000)) # Output: 5,000
print(discharge(51030.4853)) # Output: 51,030.48
print(discharge(51030.4853, True, Language.EN)) # Output: 51,030.48 thousand
```
