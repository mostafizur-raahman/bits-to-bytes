#!/usr/bin/env python3
"""
Replace DSA section with NeetCode roadmap — Arrays & Hashing topic.
5 problems, each with brute force → optimal, multi-lang code (C++/Go/Python/Java).
Maximum Bangla + English technical terms pattern.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

# Find DSA section start and Networking section start
dsa_marker = "/* ============== DSA ============== */"
net_marker = "/* ============== NETWORKING ============== */"

dsa_start = text.find(dsa_marker)
assert dsa_start != -1
net_start = text.find(net_marker, dsa_start)
assert net_start != -1

before = text[:dsa_start]
after = text[net_start:]

NEW_DSA = r'''/* ============== DSA ============== */

  // ---- Arrays & Hashing (NeetCode Roadmap Topic 1) ----
  {
    id: "dsa-arrays-hashing",
    subject: "dsa",
    title: "Arrays & Hashing",
    bangla: "অ্যারে ও হ্যাশিং",
    difficulty: "Easy",
    est: "3 hr",
    summary:
      "Arrays & Hashing হলো NeetCode roadmap-এর প্রথম topic। এই chapter-ে ৫টি classic problem solve করা হয়েছে — প্রতিটিতে brute force থেকে optimal approach পর্যন্ত, C++/Go/Python/Java তে code সহ। Hash map কখন O(n) → O(1) করে, সেটা এখানে শিখবে।",
    sections: [
      { type: "h2", id: "overview", title: "Arrays & Hashing Overview" },
      {
        type: "p",
        text: "Array হলো সবচেয়ে basic data structure — contiguous memory-এ same-type elements। Hash map (dictionary) হলো key-value pairs যেখানে lookup O(1)। এই chapter-ে আমরা দেখব কীভাবে hash map use করে brute force O(n²) solution কে O(n) করা যায়। এটাই DSA-র সবচেয়ে important pattern — 'trade space for time'।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি phone book। Brute force: প্রতিটি contact একে একে check করা (O(n))। Hash map: alphabet-অনুযায়ী sorted — সরাসরি correct page-এ যাও (O(1))। আরো space লাগে, কিন্তু অনেক দ্রুত।",
      },

      // ====== PROBLEM 1: Two Sum ======
      { type: "h2", id: "two-sum", title: "Problem 1 — Two Sum" },
      {
        type: "p",
        text: "Problem: একটি array nums ও একটি target দেওয়া আছে। দুটি index খুঁজে বের করো যেখানে nums[i] + nums[j] = target। ঠিক একটি solution আছে, এবং একই element দুবার use করা যাবে না।",
      },
      {
        type: "p",
        text: "Example: nums = [2, 7, 11, 15], target = 9। Output: [0, 1] কারণ nums[0] + nums[1] = 2 + 7 = 9।",
      },

      { type: "h3", title: "Brute Force — O(n²)" },
      {
        type: "p",
        text: "সব possible pair check করো। প্রতিটি element-এর জন্য, বাকি সব element-এর সাথে check করো যে যোগফল target হয় কিনা। দুটি nested loop — O(n²) time, O(1) space। ছোট array-তে কাজ করে, কিন্তু বড় array-তে অনেক slow।",
      },
      {
        type: "multi-code",
        filename: "two_sum_brute",
        codeSamples: {
          cpp: `#include <vector>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[i] + nums[j] == target) {
                return {i, j};
            }
        }
    }
    return {};  // not found
}`,
          go: `package main

func twoSum(nums []int, target int) []int {
    for i := 0; i < len(nums); i++ {
        for j := i + 1; j < len(nums); j++ {
            if nums[i]+nums[j] == target {
                return []int{i, j}
            }
        }
    }
    return nil
}`,
          python: `def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []`,
          java: `public class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{};
    }
}`,
        },
      },

      { type: "h3", title: "Optimal — O(n) with Hash Map" },
      {
        type: "p",
        text: "Hash map use করো। প্রতিটি element-এর জন্য, check করো target - nums[i] map-এ আছে কিনা। যদি থাকে, তুমি দুটি index পেয়ে গেছো। যদি না থাকে, nums[i] কে map-এ add করো। এক pass-ই যথেষ্ট — O(n) time, O(n) space।",
      },
      {
        type: "multi-code",
        filename: "two_sum_optimal",
        codeSamples: {
          cpp: `#include <unordered_map>
#include <vector>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> seen;  // value -> index
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (seen.count(complement)) {
            return {seen[complement], i};
        }
        seen[nums[i]] = i;
    }
    return {};
}`,
          go: `package main

func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)  // value -> index
    for i, num := range nums {
        complement := target - num
        if j, ok := seen[complement]; ok {
            return []int{j, i}
        }
        seen[num] = i
    }
    return nil
}`,
          python: `def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []`,
          java: `import java.util.*;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                return new int[]{seen.get(complement), i};
            }
            seen.put(nums[i], i);
        }
        return new int[]{};
    }
}`,
        },
      },
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute Force — Time: O(n²), Space: O(1)। ছোট input-এ কাজ করে।",
          "Optimal (Hash Map) — Time: O(n), Space: O(n)। বড় input-এ 1000x fast।",
          "Key insight: Hash map একটি element আছে কিনা O(1)-এ check করে, O(n) এর বদলে।",
        ],
      },

      // ====== PROBLEM 2: Contains Duplicate ======
      { type: "h2", id: "contains-duplicate", title: "Problem 2 — Contains Duplicate" },
      {
        type: "p",
        text: "Problem: একটি array দেওয়া আছে। যদি কোনো value দুবার বা তার বেশি আসে, true return করো। যদি সব value unique হয়, false return করো।",
      },
      {
        type: "p",
        text: "Example: nums = [1, 2, 3, 1] → true (1 দুবার এসেছে)। nums = [1, 2, 3, 4] → false।",
      },

      { type: "h3", title: "Brute Force — O(n²)" },
      {
        type: "p",
        text: "প্রতিটি pair compare করো। দুটি nested loop — প্রতিটি element-এর জন্য বাকি সব element check করো। কোনো duplicate পেলে true return করো।",
      },
      {
        type: "multi-code",
        filename: "contains_dup_brute",
        codeSamples: {
          cpp: `bool containsDuplicate(vector<int>& nums) {
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[i] == nums[j]) return true;
        }
    }
    return false;
}`,
          go: `func containsDuplicate(nums []int) bool {
    for i := 0; i < len(nums); i++ {
        for j := i + 1; j < len(nums); j++ {
            if nums[i] == nums[j] {
                return true
            }
        }
    }
    return false
}`,
          python: `def contains_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False`,
          java: `public boolean containsDuplicate(int[] nums) {
    for (int i = 0; i < nums.length; i++) {
        for (int j = i + 1; j < nums.length; j++) {
            if (nums[i] == nums[j]) return true;
        }
    }
    return false;
}`,
        },
      },

      { type: "h3", title: "Optimal 1 — O(n) with Hash Set" },
      {
        type: "p",
        text: "একটি set use করো। প্রতিটি element check করো — যদি already set-এ থাকে, true return করো। নাহলে set-এ add করো। এক pass, O(n) time, O(n) space।",
      },
      {
        type: "multi-code",
        filename: "contains_dup_set",
        codeSamples: {
          cpp: `#include <unordered_set>
bool containsDuplicate(vector<int>& nums) {
    unordered_set<int> seen;
    for (int num : nums) {
        if (seen.count(num)) return true;
        seen.insert(num);
    }
    return false;
}`,
          go: `func containsDuplicate(nums []int) bool {
    seen := make(map[int]bool)
    for _, num := range nums {
        if seen[num] {
            return true
        }
        seen[num] = true
    }
    return false
}`,
          python: `def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False`,
          java: `import java.util.*;
public boolean containsDuplicate(int[] nums) {
    Set<Integer> seen = new HashSet<>();
    for (int num : nums) {
        if (seen.contains(num)) return true;
        seen.add(num);
    }
    return false;
}`,
        },
      },

      { type: "h3", title: "Optimal 2 — O(n log n) with Sorting" },
      {
        type: "p",
        text: "Array sort করো, তারপর adjacent pairs check করো। Sort করার পর duplicate গুলো পাশাপাশি থাকবে। O(n log n) time, O(1) space (in-place sort)। Space save করতে চাইলে এটা ব্যবহার করো।",
      },
      {
        type: "multi-code",
        filename: "contains_dup_sort",
        codeSamples: {
          cpp: `#include <algorithm>
bool containsDuplicate(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] == nums[i - 1]) return true;
    }
    return false;
}`,
          go: `import "sort"
func containsDuplicate(nums []int) bool {
    sort.Ints(nums)
    for i := 1; i < len(nums); i++ {
        if nums[i] == nums[i-1] {
            return true
        }
    }
    return false
}`,
          python: `def contains_duplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False`,
          java: `import java.util.Arrays;
public boolean containsDuplicate(int[] nums) {
    Arrays.sort(nums);
    for (int i = 1; i < nums.length; i++) {
        if (nums[i] == nums[i - 1]) return true;
    }
    return false;
}`,
        },
      },
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute Force — Time: O(n²), Space: O(1)।",
          "Hash Set — Time: O(n), Space: O(n)। সবচেয়ে দ্রুত।",
          "Sorting — Time: O(n log n), Space: O(1)। Space efficient।",
        ],
      },

      // ====== PROBLEM 3: Valid Anagram ======
      { type: "h2", id: "valid-anagram", title: "Problem 3 — Valid Anagram" },
      {
        type: "p",
        text: "Problem: দুটি string s ও t দেওয়া আছে। t কি s-এর anagram? Anagram হলো একই letters rearrange করে তৈরি। যেমন s = 'anagram', t = 'nagaram' → true।",
      },

      { type: "h3", title: "Brute Force — O(n log n) with Sorting" },
      {
        type: "p",
        text: "দুটি string-কে sort করো এবং compare করো। যদি sort করার পর একই হয়, তাহলে anagram। Simple কিন্তু sorting O(n log n)।",
      },
      {
        type: "multi-code",
        filename: "anagram_sort",
        codeSamples: {
          cpp: `#include <algorithm>
bool isAnagram(string s, string t) {
    if (s.size() != t.size()) return false;
    sort(s.begin(), s.end());
    sort(t.begin(), t.end());
    return s == t;
}`,
          go: `import "sort"
import "strings"

func isAnagram(s, t string) bool {
    if len(s) != len(t) {
        return false
    }
    sb := strings.Split(s, "")
    tb := strings.Split(t, "")
    sort.Strings(sb)
    sort.Strings(tb)
    return strings.Join(sb, "") == strings.Join(tb, "")
}`,
          python: `def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)`,
          java: `import java.util.Arrays;
public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) return false;
    char[] sa = s.toCharArray();
    char[] ta = t.toCharArray();
    Arrays.sort(sa);
    Arrays.sort(ta);
    return Arrays.equals(sa, ta);
}`,
        },
      },

      { type: "h3", title: "Optimal — O(n) with Hash Map" },
      {
        type: "p",
        text: "প্রতিটি character-এর frequency count করো। s-এর প্রতিটি char-এর জন্য count++, t-এর জন্য count--। সব count শেষে 0 হলে anagram। অথবা দুটি separate hash map compare করো।",
      },
      {
        type: "multi-code",
        filename: "anagram_hashmap",
        codeSamples: {
          cpp: `#include <unordered_map>
bool isAnagram(string s, string t) {
    if (s.size() != t.size()) return false;
    unordered_map<char, int> count;
    for (char c : s) count[c]++;
    for (char c : t) {
        count[c]--;
        if (count[c] < 0) return false;
    }
    return true;
}`,
          go: `func isAnagram(s, t string) bool {
    if len(s) != len(t) {
        return false
    }
    count := make(map[rune]int)
    for _, c := range s {
        count[c]++
    }
    for _, c := range t {
        count[c]--
        if count[c] < 0 {
            return false
        }
    }
    return true
}`,
          python: `def is_anagram(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        count[c] = count.get(c, 0) - 1
        if count[c] < 0:
            return False
    return True`,
          java: `import java.util.*;
public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) return false;
    Map<Character, Integer> count = new HashMap<>();
    for (char c : s.toCharArray())
        count.put(c, count.getOrDefault(c, 0) + 1);
    for (char c : t.toCharArray()) {
        count.put(c, count.getOrDefault(c, 0) - 1);
        if (count.get(c) < 0) return false;
    }
    return true;
}`,
        },
      },
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Sorting — Time: O(n log n), Space: O(1) বা O(n)।",
          "Hash Map — Time: O(n), Space: O(k) যেখানে k = unique characters।",
          "Bonus: যদি শুধু lowercase English letters হয়, array[26] use করো — O(1) space!",
        ],
      },

      // ====== PROBLEM 4: Group Anagrams ======
      { type: "h2", id: "group-anagrams", title: "Problem 4 — Group Anagrams" },
      {
        type: "p",
        text: "Problem: একটি array of strings দেওয়া আছে। Anagram গুলোকে group করে return করো। প্রতিটি group-এর order যেকোনো হতে পারে।",
      },
      {
        type: "p",
        text: "Example: strs = ['eat','tea','tan','ate','nat','bat'] → [['bat'],['nat','tan'],['ate','eat','tea']]।",
      },

      { type: "h3", title: "Brute Force — O(n² × k log k)" },
      {
        type: "p",
        text: "প্রতিটি string-এর জন্য, বাকি সব string check করো anagram কিনা। প্রতিটি comparison-এ sort করে check করতে হবে। খুব slow — বড় input-এ TLE।",
      },

      { type: "h3", title: "Optimal — O(n × k log k) with Hash Map" },
      {
        type: "p",
        text: "Key insight: দুটি string anagram হলে, sort করার পর তারা identical। তাই sorted string কে hash map-এর key হিসেবে use করো। প্রতিটি string sort করো, এবং সেই sorted key-তে group করো। এক pass — O(n × k log k)।",
      },
      {
        type: "multi-code",
        filename: "group_anagrams",
        codeSamples: {
          cpp: `#include <unordered_map>
#include <algorithm>
vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> groups;
    for (string& s : strs) {
        string key = s;
        sort(key.begin(), key.end());
        groups[key].push_back(s);
    }
    vector<vector<string>> result;
    for (auto& [key, vals] : groups) {
        result.push_back(vals);
    }
    return result;
}`,
          go: `package main

import "sort"
import "strings"

func groupAnagrams(strs []string) [][]string {
    groups := make(map[string][]string)
    for _, s := range strs {
        chars := strings.Split(s, "")
        sort.Strings(chars)
        key := strings.Join(chars, "")
        groups[key] = append(groups[key], s)
    }
    result := make([][]string, 0, len(groups))
    for _, vals := range groups {
        result = append(result, vals)
    }
    return result
}`,
          python: `from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    return list(groups.values())`,
          java: `import java.util.*;

public List<List<String>> groupAnagrams(String[] strs) {
    Map<String, List<String>> groups = new HashMap<>();
    for (String s : strs) {
        char[] chars = s.toCharArray();
        Arrays.sort(chars);
        String key = new String(chars);
        groups.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
    }
    return new ArrayList<>(groups.values());
}`,
        },
      },
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute Force — Time: O(n² × k log k), Space: O(n × k)। অনেক slow।",
          "Optimal — Time: O(n × k log k), Space: O(n × k)। এক pass, hash map grouping।",
          "Bonus: frequency count string কে key হিসেবে use করলে O(n × k) possible।",
        ],
      },

      // ====== PROBLEM 5: Top K Frequent Elements ======
      { type: "h2", id: "top-k-frequent", title: "Problem 5 — Top K Frequent Elements" },
      {
        type: "p",
        text: "Problem: একটি integer array ও একটি k দেওয়া আছে। সবচেয়ে বেশি বার আসা kটি element return করো। Order যেকোনো হতে পারে।",
      },
      {
        type: "p",
        text: "Example: nums = [1,1,1,2,2,3], k = 2 → [1,2]। 1 তিনবার, 2 দুবার, 3 একবার — top 2 হলো 1 ও 2।",
      },

      { type: "h3", title: "Brute Force — O(n log n) with Sorting" },
      {
        type: "p",
        text: "Frequency count করো, তারপর frequency অনুযায়ী sort করো, এবং top k নাও। Sorting এর কারণে O(n log n)।",
      },
      {
        type: "multi-code",
        filename: "top_k_sort",
        codeSamples: {
          cpp: `#include <unordered_map>
#include <algorithm>
vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int, int> freq;
    for (int n : nums) freq[n]++;
    vector<pair<int, int>> pairs;
    for (auto& [n, f] : freq) pairs.push_back({f, n});
    sort(pairs.rbegin(), pairs.rend());
    vector<int> result;
    for (int i = 0; i < k; i++) result.push_back(pairs[i].second);
    return result;
}`,
          go: `import "sort"

func topKFrequent(nums []int, k int) []int {
    freq := make(map[int]int)
    for _, n := range nums {
        freq[n]++
    }
    type pair struct{ f, n int }
    pairs := make([]pair, 0, len(freq))
    for n, f := range freq {
        pairs = append(pairs, pair{f, n})
    }
    sort.Slice(pairs, func(i, j int) bool {
        return pairs[i].f > pairs[j].f
    })
    result := make([]int, 0, k)
    for i := 0; i < k; i++ {
        result = append(result, pairs[i].n)
    }
    return result
}`,
          python: `def top_k_frequent(nums, k):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    sorted_items = sorted(freq.items(), key=lambda x: -x[1])
    return [item[0] for item in sorted_items[:k]]`,
          java: `import java.util.*;
public int[] topKFrequent(int[] nums, int k) {
    Map<Integer, Integer> freq = new HashMap<>();
    for (int n : nums) freq.merge(n, 1, Integer::sum);
    List<int[]> list = new ArrayList<>();
    for (var e : freq.entrySet()) list.add(new int[]{e.getValue(), e.getKey()});
    list.sort((a, b) -> b[0] - a[0]);
    int[] result = new int[k];
    for (int i = 0; i < k; i++) result[i] = list.get(i)[1];
    return result;
}`,
        },
      },

      { type: "h3", title: "Optimal — O(n) with Bucket Sort" },
      {
        type: "p",
        text: "Bucket sort use করো! একটি array তৈরি করো যেখানে index = frequency, value = সেই frequency-যুক্ত elements। উপর থেকে নিচে iterate করে top k নাও। কোনো sorting নেই — O(n) time!",
      },
      {
        type: "multi-code",
        filename: "top_k_bucket",
        codeSamples: {
          cpp: `#include <unordered_map>
vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int, int> freq;
    for (int n : nums) freq[n]++;

    // bucket[i] = elements with frequency i
    vector<vector<int>> bucket(nums.size() + 1);
    for (auto& [n, f] : freq) bucket[f].push_back(n);

    vector<int> result;
    for (int i = bucket.size() - 1; i >= 0 && result.size() < k; i--) {
        for (int n : bucket[i]) {
            result.push_back(n);
            if (result.size() == k) break;
        }
    }
    return result;
}`,
          go: `func topKFrequent(nums []int, k int) []int {
    freq := make(map[int]int)
    for _, n := range nums {
        freq[n]++
    }

    // bucket[i] = elements with frequency i
    bucket := make([][]int, len(nums)+1)
    for n, f := range freq {
        bucket[f] = append(bucket[f], n)
    }

    result := make([]int, 0, k)
    for i := len(bucket) - 1; i >= 0 && len(result) < k; i-- {
        for _, n := range bucket[i] {
            result = append(result, n)
            if len(result) == k {
                return result
            }
        }
    }
    return result
}`,
          python: `def top_k_frequent(nums, k):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    # bucket[i] = elements with frequency i
    bucket = [[] for _ in range(len(nums) + 1)]
    for n, f in freq.items():
        bucket[f].append(n)

    result = []
    for i in range(len(bucket) - 1, 0, -1):
        for n in bucket[i]:
            result.append(n)
            if len(result) == k:
                return result
    return result`,
          java: `import java.util.*;
public int[] topKFrequent(int[] nums, int k) {
    Map<Integer, Integer> freq = new HashMap<>();
    for (int n : nums) freq.merge(n, 1, Integer::sum);

    // bucket[i] = elements with frequency i
    List<Integer>[] bucket = new List[nums.length + 1];
    for (var e : freq.entrySet()) {
        int f = e.getValue();
        if (bucket[f] == null) bucket[f] = new ArrayList<>();
        bucket[f].add(e.getKey());
    }

    int[] result = new int[k];
    int idx = 0;
    for (int i = bucket.length - 1; i >= 0 && idx < k; i--) {
        if (bucket[i] != null) {
            for (int n : bucket[i]) {
                result[idx++] = n;
                if (idx == k) return result;
            }
        }
    }
    return result;
}`,
        },
      },
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Sorting — Time: O(n log n), Space: O(n)। Simple কিন্তু sorting overhead।",
          "Bucket Sort — Time: O(n), Space: O(n)। কোনো sorting নেই, linear time!",
          "Key insight: যেহেতু frequency সর্বোচ্চ n হতে পারে, bucket array-র size n+1 যথেষ্ট।",
        ],
      },

      { type: "h2", id: "summary", title: "Chapter Summary" },
      {
        type: "list",
        items: [
          "Two Sum — Hash map দিয়ে O(n²) → O(n)। complement = target - nums[i] pattern।",
          "Contains Duplicate — Hash set দিয়ে O(n²) → O(n)। অথবা sort করে O(n log n), O(1) space।",
          "Valid Anagram — Frequency count দিয়ে O(n log n) → O(n)।",
          "Group Anagrams — Sorted string কে hash key হিসেবে use করে grouping।",
          "Top K Frequent — Bucket sort দিয়ে O(n log n) → O(n)। কোনো sorting নেই!",
          "Core pattern: Hash map একটি value আছে কিনা O(1)-এ check করে — এটাই brute force কে optimal করার সবচেয়ে common technique।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: পরের topic হলো Two Pointers — যেখানে দুটি pointer array-র দুই প্রান্ত থেকে move করে problem solve করে। Sorting + Two Pointers অনেক problem-এ O(n²) → O(n) বা O(n log n) করে।",
      },
    ],
  },

'''

new_text = before + NEW_DSA + after

# Verify
assert 'id: "dsa-arrays-hashing"' in new_text, "dsa-arrays-hashing missing"
assert 'id: "dsa-arrays"' not in new_text, "old dsa-arrays still present"
assert 'id: "dsa-recursion"' not in new_text, "old dsa-recursion still present"
assert 'id: "dsa-trees"' not in new_text, "old dsa-trees still present"
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Arrays & Hashing topic added with 5 problems. File size: {len(new_text)} bytes")
