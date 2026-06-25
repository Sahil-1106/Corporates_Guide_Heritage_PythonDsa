# =========================
# Part A – Frequency Counter
# =========================

def freq_counter(arr):
    """Return a dictionary with frequency of each integer in arr."""
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq


def most_frequent_element(freq_dict):
    """Return the element with the highest frequency."""
    max_count = -1
    most_freq = None

    for num, count in freq_dict.items():
        if count > max_count:
            max_count = count
            most_freq = num

    return most_freq, max_count


def elements_appearing_once(freq_dict):
    """Return a list of elements that appear exactly once."""
    once = []
    for num, count in freq_dict.items():
        if count == 1:
            once.append(num)
    return once


# ======================
# Part B – Anagram Check
# ======================

def is_anagram(s1, s2):
    """Return True if s1 and s2 are anagrams, False otherwise."""
    if len(s1) != len(s2):
        return False

    freq = {}

    for ch in s1:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] == 0:
            del freq[ch]

    return len(freq) == 0


def is_anagram_clean(s1, s2):
    """
    Bonus version:
    - removes spaces
    - converts both strings to lowercase
    """
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return is_anagram(s1, s2)


# ====================
# Part C – Two Sum
# ====================

def two_sum(nums, target):
    """
    Return indices [i, j] such that nums[i] + nums[j] == target.

    The 'complement' is the number we still need to reach the target.
    For each num, complement = target - num.
    We store complements in a hash map so we can find matches in O(1) average time.
    """
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []


# ============================
# Part D – Bonus / Challenge
# ============================

def length_of_longest_substring(s):
    """Sliding window + hash set."""
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


def first_non_repeating_character(s):
    """Return the first character that appears only once, or '' if none."""
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch

    return ""


def group_anagrams(words):
    """Group anagrams together using sorted word as the hash map key."""
    groups = {}

    for word in words:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    return list(groups.values())


class HashTable:
    """Simple hash table with chaining."""

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        bucket = self.table[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        idx = self._hash(key)
        bucket = self.table[idx]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self._hash(key)
        bucket = self.table[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False


# ====================
# Testing / Output
# ====================

print("\n" + "=" * 60)
print("PART A - FREQUENCY COUNTER")
print("=" * 60)

arr = [1, 2, 3, 2, 1, 1, 4]
freq = freq_counter(arr)
print("Frequency Counter:", freq)
most_num, most_count = most_frequent_element(freq)
print("Most Frequent Element:", most_num, "appears", most_count, "times")
print("Elements Appearing Exactly Once:", elements_appearing_once(freq))

print("\n" + "=" * 60)
print("PART B - ANAGRAM CHECK")
print("=" * 60)

print('"listen" and "silent" ->', is_anagram("listen", "silent"))
print('"triangle" and "integral" ->', is_anagram("triangle", "integral"))
print('"apple" and "pale" ->', is_anagram("apple", "pale"))
print('"rat" and "car" ->', is_anagram("rat", "car"))
print('"Dormitory" and "Dirty room" ->', is_anagram_clean("Dormitory", "Dirty room"))
print('"School master" and "The classroom" ->', is_anagram_clean("School master", "The classroom"))

print("\n" + "=" * 60)
print("PART C - TWO SUM")
print("=" * 60)
print("nums=[2,7,11,15], target=9 ->", two_sum([2, 7, 11, 15], 9))
print("nums=[3,2,4], target=6 ->", two_sum([3, 2, 4], 6))
print("nums=[3,3], target=6 ->", two_sum([3, 3], 6))

print("\n" + "=" * 60)
print("PART D - BONUS CHALLENGES")
print("=" * 60)
print('"abcabcbb" ->', length_of_longest_substring("abcabcbb"))
print('"bbbbb" ->', length_of_longest_substring("bbbbb"))
print('"pwwkew" ->', length_of_longest_substring("pwwkew"))
print('"leetcode" ->', first_non_repeating_character("leetcode"))
print('"aabb" ->', first_non_repeating_character("aabb"))
print('Group anagrams ->', group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

ht = HashTable()
ht.insert("name", "Sahil")
ht.insert("age", 21)
ht.insert("city", "Patna")
print("HashTable get name ->", ht.get("name"))
print("HashTable get age ->", ht.get("age"))
print("HashTable delete age ->", ht.delete("age"))
print("HashTable get age after delete ->", ht.get("age"))