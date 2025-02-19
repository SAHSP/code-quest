# 📋 Construct Smallest Number From DI String

## 📝 Problem Statement

You are given a 0-indexed string `pattern` of length `n`, consisting of the characters `'I'` (increasing) and `'D'` (decreasing).

You need to create a string `num` of length `n + 1`, which:
1. Consists of the digits '1' to '9', with each digit used at most once.
2. Fulfills the conditions:
   - If `pattern[i] == 'I'`, then `num[i] < num[i + 1]` ⬆️.
   - If `pattern[i] == 'D'`, then `num[i] > num[i + 1]` ⬇️.

The task is to return the lexicographically smallest possible string `num` that satisfies these conditions.

### ⚙️ Constraints
- `1 <= pattern.length <= 8`
- `pattern` consists of only the characters `'I'` (increasing) and `'D'` (decreasing).

## 🧩 Examples

| Example       | Input               | Output      | Explanation                                                                 |
|---------------|---------------------|-------------|-----------------------------------------------------------------------------|
| **Example 1** | `pattern = "IIIDIDDD"` | `123549876` | At indices 0, 1, 2, and 4: `num[i] < num[i+1]` ⬆️; indices 3, 5, 6, 7: `num[i] > num[i+1]` ⬇️. Lexicographically smallest is `123549876`. |
| **Example 2** | `pattern = "DDD"`     | `4321`      | All digits must be in decreasing order (`num[i] > num[i+1]` ⬇️). Smallest possible value is `4321`. |

## 🚀 Solution Approach

1. **Recursive Approach with Backtracking:**
   - A recursive helper function `rerun()` is used when the pattern has a decreasing sequence (`'D'`). This helps to assign numbers in the correct order while maintaining the lexicographical constraint.
   - Numbers are placed in a list `x` that is initialized with zeros. The `smallestNumber()` method iterates through the pattern and assigns values based on whether the current character is `'I'` or `'D'`.
   
2. **Time Complexity:** O(n), where n is the length of the pattern.

3. **Space Complexity:** O(n), for storing the result in the list `x` and the recursive stack.

---

