import type { Topic } from "./types";

export const DSA_TOPICS: Topic[] = [
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

  // ---- Two Pointers ----
  {
    id: "dsa-two-pointers",
    subject: "dsa",
    title: "Two Pointers",
    bangla: "টু পয়েন্টারস",
    difficulty: "Medium",
    est: "2.5 hr",
    summary: "Two Pointers pattern-এ দুটি pointer array-র দুই প্রান্স থেকে move করে। ৫টি classic problem — brute force থেকে optimal two pointer approach পর্যন্ত।",
    sections: [
      { type: "h2", id: "prob-1", title: "Problem 1 — Valid Palindrome" },
      { type: "p", text: "একটি string দেওয়া আছে। এটি palindrome কিনা check করো (শুধু alphanumeric, case insensitive)।" },
      { type: "p", text: "Example: s = 'A man, a plan, a canal: Panama' → true" },
      { type: "h3", title: "Brute Force — O(n) with extra string" },
      { type: "p", text: "String clean করো, reverse করো, compare করো। Extra space O(n)।" },
      {
        type: "multi-code",
        filename: "prob_1_brute",
        codeSamples: {
          cpp: `bool isPalindrome(string s) {
    string clean;
    for(char c : s)
        if(isalnum(c)) clean += tolower(c);
    return clean == string(clean.rbegin(), clean.rend());
}`,
          go: `func isPalindrome(s string) bool {
    var clean strings.Builder
    for _, c := range s {
        if unicode.IsLetter(c) || unicode.IsDigit(c) {
            clean.WriteRune(unicode.ToLower(c))
        }
    }
    str := clean.String()
    for i := 0; i < len(str)/2; i++ {
        if str[i] != str[len(str)-1-i] { return false }
    }
    return true
}`,
          python: `def is_palindrome(s):
    clean = [c.lower() for c in s if c.isalnum()]
    return clean == clean[::-1]`,
          java: `public boolean isPalindrome(String s) {
    StringBuilder sb = new StringBuilder();
    for (char c : s.toCharArray())
        if (Character.isLetterOrDigit(c))
            sb.append(Character.toLowerCase(c));
    String str = sb.toString();
    return str.equals(new StringBuilder(str).reverse().toString());
}`
        },
      },,
      { type: "h3", title: "Optimal — O(n) Two Pointers, O(1) space" },
      { type: "p", text: "দুটি pointer — একটি শুরুতে, একটি শেষে। দুটি alphanumeric character compare করো। না মিললে false। মিললে দুটি pointer কে এক ধাপ কাছে আনো।" },
      {
        type: "multi-code",
        filename: "prob_1_optimal",
        codeSamples: {
          cpp: `bool isPalindrome(string s) {
    int l = 0, r = s.size() - 1;
    while (l < r) {
        while (l < r && !isalnum(s[l])) l++;
        while (l < r && !isalnum(s[r])) r--;
        if (tolower(s[l]) != tolower(s[r])) return false;
        l++; r--;
    }
    return true;
}`,
          go: `func isPalindrome(s string) bool {
    l, r := 0, len(s)-1
    for l < r {
        for l < r && !isAlnum(rune(s[l])) { l++ }
        for l < r && !isAlnum(rune(s[r])) { r-- }
        if toLower(s[l]) != toLower(s[r]) { return false }
        l++; r--
    }
    return true
}`,
          python: `def is_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum(): l += 1
        while l < r and not s[r].isalnum(): r -= 1
        if s[l].lower() != s[r].lower(): return False
        l += 1; r -= 1
    return True`,
          java: `public boolean isPalindrome(String s) {
    int l = 0, r = s.length() - 1;
    while (l < r) {
        while (l < r && !Character.isLetterOrDigit(s.charAt(l))) l++;
        while (l < r && !Character.isLetterOrDigit(s.charAt(r))) r--;
        if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) return false;
        l++; r--;
    }
    return true;
}`
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute — Time: O(n), Space: O(n)। Extra string।",
          "Two Pointers — Time: O(n), Space: O(1)। কোনো extra string নেই।",
          "Key: দুটি pointer দুই প্রান্ত থেকে move করে — এটাই two pointers pattern।"
        ],
      },,
      { type: "h2", id: "prob-2", title: "Problem 2 — Two Sum II — Sorted Array" },
      { type: "p", text: "একটি sorted array ও target দেওয়া আছে। দুটি index খুঁজে বের করো (1-indexed) যেখানে যোগফল target।" },
      { type: "p", text: "Example: numbers = [2,7,11,15], target = 9 → [1,2]" },
      { type: "h3", title: "Brute Force — O(n²) nested loops" },
      { type: "p", text: "প্রতিটি pair check করো। Sorted হওয়া সত্ত্বেও brute force করলে O(n²)।" },
      {
        type: "multi-code",
        filename: "prob_2_brute",
        codeSamples: {
          cpp: `vector<int> twoSum(vector<int>& n, int t) {
    for(int i=0;i<n.size();i++)
        for(int j=i+1;j<n.size();j++)
            if(n[i]+n[j]==t) return {i+1,j+1};
    return {};
}`,
          go: `func twoSum(n []int, t int) []int {
    for i := 0; i < len(n); i++ {
        for j := i+1; j < len(n); j++ {
            if n[i]+n[j]==t { return []int{i+1,j+1} }
        }
    }
    return nil
}`,
          python: `def two_sum(n, t):
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if n[i]+n[j]==t: return [i+1, j+1]`,
          java: `public int[] twoSum(int[] n, int t) {
    for(int i=0;i<n.length;i++)
        for(int j=i+1;j<n.length;j++)
            if(n[i]+n[j]==t) return new int[]{i+1,j+1};
    return new int[]{};
}`
        },
      },,
      { type: "h3", title: "Optimal — O(n) Two Pointers" },
      { type: "p", text: "Array sorted! দুটি pointer — left শুরুতে, right শেষে। যোগফল < target হলে left++, > target হলে right--। সরাসরি O(n)!" },
      {
        type: "multi-code",
        filename: "prob_2_optimal",
        codeSamples: {
          cpp: `vector<int> twoSum(vector<int>& n, int t) {
    int l=0, r=n.size()-1;
    while(l<r){
        int s=n[l]+n[r];
        if(s==t) return {l+1,r+1};
        if(s<t) l++; else r--;
    }
    return {};
}`,
          go: `func twoSum(n []int, t int) []int {
    l, r := 0, len(n)-1
    for l < r {
        s := n[l]+n[r]
        if s==t { return []int{l+1,r+1} }
        if s<t { l++ } else { r-- }
    }
    return nil
}`,
          python: `def two_sum(n, t):
    l, r = 0, len(n)-1
    while l < r:
        s = n[l]+n[r]
        if s==t: return [l+1, r+1]
        if s<t: l+=1
        else: r-=1`,
          java: `public int[] twoSum(int[] n, int t) {
    int l=0, r=n.length-1;
    while(l<r){
        int s=n[l]+n[r];
        if(s==t) return new int[]{l+1,r+1};
        if(s<t) l++; else r--;
    }
    return new int[]{};
}`
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute — Time: O(n²), Space: O(1)।",
          "Two Pointers — Time: O(n), Space: O(1)। Sorted array-তে সবচেয়ে efficient।",
          "Key: sorted array হলে two pointers এক পাসে solve করে।"
        ],
      },,
      { type: "h2", id: "prob-3", title: "Problem 3 — 3Sum" },
      { type: "p", text: "একটি array দেওয়া আছে। এমন সব unique triplet খুঁজে বের করো যাদের যোগফল 0।" },
      { type: "p", text: "Example: nums = [-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]" },
      { type: "h3", title: "Brute Force — O(n³) triple nested loops" },
      { type: "p", text: "তিনটি nested loop — সব triplet check করো। খুব slow, O(n³)।" },
      {
        type: "multi-code",
        filename: "prob_3_brute",
        codeSamples: {
          cpp: `vector<vector<int>> threeSum(vector<int>& n) {
    set<vector<int>> res;
    for(int i=0;i<n.size();i++)
        for(int j=i+1;j<n.size();j++)
            for(int k=j+1;k<n.size();k++)
                if(n[i]+n[j]+n[k]==0){
                    vector<int> t={n[i],n[j],n[k]};
                    sort(t.begin(),t.end());
                    res.insert(t);
                }
    return vector<vector<int>>(res.begin(),res.end());
}`,
          go: `func threeSum(n []int) [][]int {
    res := make(map[[3]int]bool)
    for i:=0;i<len(n);i++ {
        for j:=i+1;j<len(n);j++ {
            for k:=j+1;k<len(n);k++ {
                if n[i]+n[j]+n[k]==0 {
                    t := []int{n[i],n[j],n[k]}
                    sort.Ints(t)
                    res[[3]int{t[0],t[1],t[2]}] = true
                }
            }
        }
    }
    // convert map to slice
    return nil
}`,
          python: `def three_sum(n):
    res = set()
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            for k in range(j+1, len(n)):
                if n[i]+n[j]+n[k]==0:
                    res.add(tuple(sorted([n[i],n[j],n[k]])))
    return [list(t) for t in res]`,
          java: `public List<List<Integer>> threeSum(int[] n) {
    Set<List<Integer>> res = new HashSet<>();
    for(int i=0;i<n.length;i++)
        for(int j=i+1;j<n.length;j++)
            for(int k=j+1;k<n.length;k++)
                if(n[i]+n[j]+n[k]==0) {
                    List<Integer> t = Arrays.asList(n[i],n[j],n[k]);
                    Collections.sort(t);
                    res.add(t);
                }
    return new ArrayList<>(res);
}`
        },
      },,
      { type: "h3", title: "Optimal — O(n²) Sort + Two Pointers" },
      { type: "p", text: "Array sort করো। প্রতিটি element-এর জন্য, বাকি array-তে two pointer দিয়ে pair খুঁজো যাদের যোগফল -nums[i]। Skip duplicates।" },
      {
        type: "multi-code",
        filename: "prob_3_optimal",
        codeSamples: {
          cpp: `vector<vector<int>> threeSum(vector<int>& n) {
    sort(n.begin(),n.end());
    vector<vector<int>> res;
    for(int i=0;i<(int)n.size()-2;i++){
        if(i>0 && n[i]==n[i-1]) continue;
        int l=i+1, r=n.size()-1;
        while(l<r){
            int s=n[i]+n[l]+n[r];
            if(s==0){res.push_back({n[i],n[l],n[r]});
                while(l<r&&n[l]==n[l+1])l++;
                while(l<r&&n[r]==n[r-1])r--;
                l++;r--;}
            else if(s<0)l++; else r--;
        }
    }
    return res;
}`,
          go: `func threeSum(n []int) [][]int {
    sort.Ints(n)
    var res [][]int
    for i := 0; i < len(n)-2; i++ {
        if i > 0 && n[i] == n[i-1] { continue }
        l, r := i+1, len(n)-1
        for l < r {
            s := n[i]+n[l]+n[r]
            if s == 0 {
                res = append(res, []int{n[i],n[l],n[r]})
                for l < r && n[l] == n[l+1] { l++ }
                for l < r && n[r] == n[r-1] { r-- }
                l++; r--
            } else if s < 0 { l++ } else { r-- }
        }
    }
    return res
}`,
          python: `def three_sum(n):
    n.sort()
    res = []
    for i in range(len(n)-2):
        if i > 0 and n[i] == n[i-1]: continue
        l, r = i+1, len(n)-1
        while l < r:
            s = n[i]+n[l]+n[r]
            if s == 0:
                res.append([n[i],n[l],n[r]])
                while l < r and n[l]==n[l+1]: l+=1
                while l < r and n[r]==n[r-1]: r-=1
                l+=1; r-=1
            elif s < 0: l+=1
            else: r-=1
    return res`,
          java: `public List<List<Integer>> threeSum(int[] n) {
    Arrays.sort(n);
    List<List<Integer>> res = new ArrayList<>();
    for(int i=0;i<n.length-2;i++){
        if(i>0 && n[i]==n[i-1]) continue;
        int l=i+1, r=n.length-1;
        while(l<r){
            int s=n[i]+n[l]+n[r];
            if(s==0){res.add(Arrays.asList(n[i],n[l],n[r]));
                while(l<r&&n[l]==n[l+1])l++;
                while(l<r&&n[r]==n[r-1])r--;
                l++;r--;}
            else if(s<0)l++; else r--;
        }
    }
    return res;
}`
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute — Time: O(n³), Space: O(1)। খুব slow।",
          "Sort + Two Pointers — Time: O(n²), Space: O(1)। n² কারণ প্রতিটি element-এর জন্য two pointer pass।",
          "Key: sort করে duplicate skip করা সহজ হয়।"
        ],
      },,
      { type: "h2", id: "prob-4", title: "Problem 4 — Container With Most Water" },
      { type: "p", text: "একটি height array দেওয়া আছে। দুটি line দিয়ে সর্বোচ্চ water container বানাও।" },
      { type: "p", text: "Example: height = [1,8,6,2,5,4,8,3,7] → 49" },
      { type: "h3", title: "Brute Force — O(n²) all pairs" },
      { type: "p", text: "সব possible pair check করো। প্রতিটি pair-এর জন্য area calculate করো। Maximum নাও।" },
      {
        type: "multi-code",
        filename: "prob_4_brute",
        codeSamples: {
          cpp: `int maxArea(vector<int>& h) {
    int mx=0;
    for(int i=0;i<h.size();i++)
        for(int j=i+1;j<h.size();j++)
            mx=max(mx,min(h[i],h[j])*(j-i));
    return mx;
}`,
          go: `func maxArea(h []int) int {
    mx := 0
    for i := 0; i < len(h); i++ {
        for j := i+1; j < len(h); j++ {
            area := min(h[i],h[j])*(j-i)
            if area > mx { mx = area }
        }
    }
    return mx
}`,
          python: `def max_area(h):
    mx = 0
    for i in range(len(h)):
        for j in range(i+1, len(h)):
            mx = max(mx, min(h[i],h[j])*(j-i))
    return mx`,
          java: `public int maxArea(int[] h) {
    int mx=0;
    for(int i=0;i<h.length;i++)
        for(int j=i+1;j<h.length;j++)
            mx=Math.max(mx,Math.min(h[i],h[j])*(j-i));
    return mx;
}`
        },
      },,
      { type: "h3", title: "Optimal — O(n) Two Pointers — greedy" },
      { type: "p", text: "দুটি pointer — left ও right। ছোট height-ওয়ালা pointer কে move করাও (বড় height-এর pointer move করলে area কমবে, কারণ width কমছে এবং height বাড়ছে না)।" },
      {
        type: "multi-code",
        filename: "prob_4_optimal",
        codeSamples: {
          cpp: `int maxArea(vector<int>& h) {
    int l=0,r=h.size()-1,mx=0;
    while(l<r){
        mx=max(mx,min(h[l],h[r])*(r-l));
        if(h[l]<h[r])l++; else r--;
    }
    return mx;
}`,
          go: `func maxArea(h []int) int {
    l, r, mx := 0, len(h)-1, 0
    for l < r {
        area := min(h[l],h[r])*(r-l)
        if area > mx { mx = area }
        if h[l] < h[r] { l++ } else { r-- }
    }
    return mx
}`,
          python: `def max_area(h):
    l, r, mx = 0, len(h)-1, 0
    while l < r:
        mx = max(mx, min(h[l],h[r])*(r-l))
        if h[l] < h[r]: l += 1
        else: r -= 1
    return mx`,
          java: `public int maxArea(int[] h) {
    int l=0,r=h.length-1,mx=0;
    while(l<r){
        mx=Math.max(mx,Math.min(h[l],h[r])*(r-l));
        if(h[l]<h[r])l++; else r--;
    }
    return mx;
}`
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute — Time: O(n²), Space: O(1)।",
          "Two Pointers — Time: O(n), Space: O(1)। Greedy choice — ছোট height move করাও।",
          "Key: বড় height-এর pointer ধরে রাখো, ছোটটা move করাও — সর্বোচ্চ area পাবে।"
        ],
      },,
      { type: "h2", id: "prob-5", title: "Problem 5 — Trapping Rain Water" },
      { type: "p", text: "একটি height array দেওয়া আছে। কত পানি trapped হবে তা বের করো।" },
      { type: "p", text: "Example: height = [0,1,0,2,1,0,1,3,2,1,2,1] → 6" },
      { type: "h3", title: "Brute Force — O(n²) each position check" },
      { type: "p", text: "প্রতিটি position-এর জন্য, left max ও right max আলাদাভাবে calculate করো। Water = min(left_max, right_max) - height[i]।" },
      {
        type: "multi-code",
        filename: "prob_5_brute",
        codeSamples: {
          cpp: `int trap(vector<int>& h) {
    int n=h.size(), water=0;
    for(int i=0;i<n;i++){
        int lm=0,rm=0;
        for(int j=0;j<=i;j++) lm=max(lm,h[j]);
        for(int j=i;j<n;j++) rm=max(rm,h[j]);
        water+=min(lm,rm)-h[i];
    }
    return water;
}`,
          go: `func trap(h []int) int {
    n, water := len(h), 0
    for i := 0; i < n; i++ {
        lm, rm := 0, 0
        for j := 0; j <= i; j++ { if h[j] > lm { lm = h[j] } }
        for j := i; j < n; j++ { if h[j] > rm { rm = h[j] } }
        water += min(lm, rm) - h[i]
    }
    return water
}`,
          python: `def trap(h):
    water = 0
    for i in range(len(h)):
        lm = max(h[:i+1]) if h[:i+1] else 0
        rm = max(h[i:]) if h[i:] else 0
        water += min(lm, rm) - h[i]
    return water`,
          java: `public int trap(int[] h) {
    int n=h.length, water=0;
    for(int i=0;i<n;i++){
        int lm=0,rm=0;
        for(int j=0;j<=i;j++) lm=Math.max(lm,h[j]);
        for(int j=i;j<n;j++) rm=Math.max(rm,h[j]);
        water+=Math.min(lm,rm)-h[i];
    }
    return water;
}`
        },
      },,
      { type: "h3", title: "Optimal — O(n) Two Pointers — optimal" },
      { type: "p", text: "দুটি pointer — left ও right। left_max ও right_max track করো। যে পক্ষের max ছোট, সেই পক্ষ move করাও। Water = max - height[current]।" },
      {
        type: "multi-code",
        filename: "prob_5_optimal",
        codeSamples: {
          cpp: `int trap(vector<int>& h) {
    int l=0,r=h.size()-1,lm=0,rm=0,water=0;
    while(l<r){
        if(h[l]<h[r]){
            lm=max(lm,h[l]);
            water+=lm-h[l];
            l++;
        } else {
            rm=max(rm,h[r]);
            water+=rm-h[r];
            r--;
        }
    }
    return water;
}`,
          go: `func trap(h []int) int {
    l, r, lm, rm, water := 0, len(h)-1, 0, 0, 0
    for l < r {
        if h[l] < h[r] {
            if h[l] > lm { lm = h[l] } else { water += lm - h[l] }
            l++
        } else {
            if h[r] > rm { rm = h[r] } else { water += rm - h[r] }
            r--
        }
    }
    return water
}`,
          python: `def trap(h):
    l, r = 0, len(h)-1
    lm, rm, water = 0, 0, 0
    while l < r:
        if h[l] < h[r]:
            lm = max(lm, h[l])
            water += lm - h[l]
            l += 1
        else:
            rm = max(rm, h[r])
            water += rm - h[r]
            r -= 1
    return water`,
          java: `public int trap(int[] h) {
    int l=0,r=h.length-1,lm=0,rm=0,water=0;
    while(l<r){
        if(h[l]<h[r]){
            lm=Math.max(lm,h[l]);
            water+=lm-h[l];
            l++;
        } else {
            rm=Math.max(rm,h[r]);
            water+=rm-h[r];
            r--;
        }
    }
    return water;
}`
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute — Time: O(n²), Space: O(1)। প্রতিটি position-এ left/right max আলাদা।",
          "Two Pointers — Time: O(n), Space: O(1)। এক pass, দুটি max track।",
          "Key: ছোট max-ওয়ালা পক্ষ move করাও — কারণ water ছোট max দ্বারা নির্ধারিত।"
        ],
      },,
      { type: "h2", id: "tp-summary", title: "Chapter Summary" },
      { type: "list", items: [
        "Valid Palindrome — Two pointers দুই প্রান্ত থেকে move করে, O(1) space।",
        "Two Sum II — Sorted array-তে two pointers এক পাসে solve।",
        "3Sum — Sort + two pointers, duplicate skip। O(n²)।",
        "Container With Most Water — Greedy: ছোট height move করাও।",
        "Trapping Rain Water — Two pointers + left/right max track।",
        "Core pattern: sorted বা palindromic structure-তে দুটি pointer দুই প্রান্ত থেকে move করে।",
      ]},
      { type: "callout", calloutTone: "tip", text: "Tip: পরের topic হলো Stack — LIFO structure যা matching ও evaluation problems-এ powerful।" }
    ],
  },

  // ---- Stack ----
  {
    id: "dsa-stack",
    subject: "dsa",
    title: "Stack",
    bangla: "স্ট্যাক",
    difficulty: "Medium",
    est: "2.5 hr",
    summary: "Stack হলো LIFO data structure। ৫টি classic problem — valid parentheses, min stack, postfix evaluation, next greater element, largest rectangle।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      { type: "p", text: "Stack হলো Last-In-First-Out structure। সবশেষে ঢোকা element সবার আগে বের হয়। Stack ব্যবহার করো যখন তোমাকে 'সবশেষ seen' বা 'matching' track করতে হবে। Real-life thinking — একটি stack of plates। সবশেষে রাখা plate সবার আগে তোলা যায়।" },
      { type: "h2", id: "prob-1", title: "Problem 1 — Valid Parentheses" },
      { type: "p", text: "একটি string দেওয়া আছে। Parentheses valid কিনা check করো।" },
      { type: "p", text: "Example: s = '()[]{}' → true" },
      { type: "h3", title: "Brute Force — O(n) counting (limited)" },
      { type: "p", text: "শুধু এক ধরনের bracket হলে count দিয়ে check করা যায়, কিন্তু multiple types-এ কাজ করে না।" },
      {
        type: "multi-code",
        filename: "prob_1_brute",
        codeSamples: {
          cpp: `bool isValid(string s) {
    int bal=0;
    for(char c:s){
        if(c=='('||c=='['||c=='{') bal++;
        else bal--;
        if(bal<0) return false;
    }
    return bal==0;
}`,
          go: `func isValid(s string) bool {
    bal := 0
    for _, c := range s {
        if c=='('||c=='['||c=='{' { bal++ } else { bal-- }
        if bal < 0 { return false }
    }
    return bal == 0
}`,
          python: `def is_valid(s):
    bal = 0
    for c in s:
        if c in '([{': bal += 1
        else: bal -= 1
        if bal < 0: return False
    return bal == 0`,
          java: `public boolean isValid(String s) {
    int bal=0;
    for(char c:s.toCharArray()){
        if("([{".indexOf(c)>=0) bal++; else bal--;
        if(bal<0) return false;
    }
    return bal==0;
}`
        },
      },,
      { type: "h3", title: "Optimal — O(n) with Stack" },
      { type: "p", text: "Stack use করো। Opening bracket হলে push করো, closing bracket হলে top-এর সাথে match করো ও pop করো। শেষে stack empty হলে valid।" },
      {
        type: "multi-code",
        filename: "prob_1_optimal",
        codeSamples: {
          cpp: `bool isValid(string s) {
    stack<char> st;
    for(char c:s){
        if(c=='(') st.push(')');
        else if(c=='[') st.push(']');
        else if(c=='{') st.push('}');
        else if(st.empty()||st.top()!=c) return false;
        else st.pop();
    }
    return st.empty();
}`,
          go: `func isValid(s string) bool {
    var st []byte
    for i := 0; i < len(s); i++ {
        c := s[i]
        if c=='(' { st = append(st, ')') } else
        if c=='[' { st = append(st, ']') } else
        if c=='{' { st = append(st, '}') } else {
            if len(st)==0 || st[len(st)-1]!=c { return false }
            st = st[:len(st)-1]
        }
    }
    return len(st)==0
}`,
          python: `def is_valid(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    for c in s:
        if c in pairs: stack.append(pairs[c])
        elif not stack or stack.pop() != c: return False
    return not stack`,
          java: `public boolean isValid(String s) {
    Stack<Character> st = new Stack<>();
    for(char c:s.toCharArray()){
        if(c=='(') st.push(')');
        else if(c=='[') st.push(']');
        else if(c=='{') st.push('}');
        else if(st.isEmpty()||st.pop()!=c) return false;
    }
    return st.isEmpty();
}`
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Counting — শুধু single type-এ কাজ করে, multiple types-এ fail।",
          "Stack — Time: O(n), Space: O(n)। সব bracket type handle করে।",
          "Key: Stack LIFO — closing bracket সবসময় সবশেষে opening bracket-এর সাথে match করে।"
        ],
      },,
      { type: "h2", id: "prob-2", title: "Problem 2 — Min Stack" },
      { type: "p", text: "একটি stack design করো যা push, pop, top, getMin O(1)-এ করে।" },
      { type: "p", text: "Example: push(5), push(2), getMin()→2, pop(), getMin()→5" },
      { type: "h3", title: "Brute Force — O(n) scan for min" },
      { type: "p", text: "getMin হলে পুরো stack scan করো। কিন্তু এটি O(n), O(1) নয়।" },
      {
        type: "multi-code",
        filename: "prob_2_brute",
        codeSamples: {
          cpp: `int getMin() {
    int mn = INT_MAX;
    for(int v : data) mn = min(mn, v);
    return mn;
}`,
          go: `func getMin() int {
    mn := data[0]
    for _, v := range data {
        if v < mn { mn = v }
    }
    return mn
}`,
          python: `def get_min(self):
    return min(self.data)`,
          java: `public int getMin() {
    int mn = Integer.MAX_VALUE;
    for(int v : data) mn = Math.min(mn, v);
    return mn;
}`
        },
      },,
      { type: "h3", title: "Optimal — O(1) with auxiliary min stack" },
      { type: "p", text: "আরেকটি stack রাখো যা প্রতিটি push-এ current minimum track করে। getMin হলে শুধু top return করো।" },
      {
        type: "multi-code",
        filename: "prob_2_optimal",
        codeSamples: {
          cpp: `stack<int> st, mn;
void push(int x) {
    st.push(x);
    mn.push(mn.empty() ? x : min(mn.top(), x));
}
int getMin() { return mn.top(); }`,
          go: `var st, mn []int
func push(x int) {
    st = append(st, x)
    if len(mn)==0 { mn = append(mn, x) } else { mn = append(mn, min(mn[len(mn)-1], x)) }
}
func getMin() int { return mn[len(mn)-1] }`,
          python: `def __init__(self):
    self.st = []
    self.mn = []
def push(self, x):
    self.st.append(x)
    self.mn.append(min(x, self.mn[-1]) if self.mn else x)
def getMin(self):
    return self.mn[-1]`,
          java: `Stack<Integer> st = new Stack<>(), mn = new Stack<>();
public void push(int x) {
    st.push(x);
    mn.push(mn.isEmpty() ? x : Math.min(mn.peek(), x));
}
public int getMin() { return mn.peek(); }`
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute — getMin O(n), বাকি O(1)।",
          "Auxiliary stack — সব operation O(1), extra O(n) space।",
          "Key: trade space for time — extra stack দিয়ে min O(1) করা।"
        ],
      },,
      { type: "h2", id: "prob-3", title: "Problem 3 — Evaluate Reverse Polish Notation" },
      { type: "p", text: "Postfix expression evaluate করো।" },
      { type: "p", text: "Example: tokens = ['2','1','+','3','*'] → 9" },
      { type: "h3", title: "Brute Force — Recursive parse" },
      { type: "p", text: "Recursively expression parse করো। কিন্তু এটি complex এবং inefficient।" },
      {
        type: "multi-code",
        filename: "prob_3_brute",
        codeSamples: {
          cpp: `// Recursive approach — complex, O(n²) worst case
int evalRPN(vector<string>& t) {
    // recursively find last operator, split, evaluate
    // very inefficient for large inputs
    return 0;
}`,
          go: `// Recursive — complex, not practical
func evalRPN(t []string) int { return 0 }`,
          python: `def eval_rpn(tokens):
    # Recursive — complex
    pass`,
          java: `// Recursive — complex
public int evalRPN(String[] t) { return 0; }`
        },
      },,
      { type: "h3", title: "Optimal — O(n) with Stack" },
      { type: "p", text: "Stack use করো। Number হলে push, operator হলে দুটি pop করে evaluate, result push করো।" },
      {
        type: "multi-code",
        filename: "prob_3_optimal",
        codeSamples: {
          cpp: `int evalRPN(vector<string>& t) {
    stack<int> st;
    for(auto& s:t){
        if(s=="+"||s=="-"||s=="*"||s=="/"){
            int b=st.top();st.pop();
            int a=st.top();st.pop();
            if(s=="+")st.push(a+b);
            else if(s=="-")st.push(a-b);
            else if(s=="*")st.push(a*b);
            else st.push(a/b);
        } else st.push(stoi(s));
    }
    return st.top();
}`,
          go: `func evalRPN(t []string) int {
    var st []int
    for _, s := range t {
        if s == "+" || s == "-" || s == "*" || s == "/" {
            b := st[len(st)-1]; st = st[:len(st)-1]
            a := st[len(st)-1]; st = st[:len(st)-1]
            switch s {
            case "+": st = append(st, a+b)
            case "-": st = append(st, a-b)
            case "*": st = append(st, a*b)
            case "/": st = append(st, a/b)
            }
        } else {
            n, _ := strconv.Atoi(s)
            st = append(st, n)
        }
    }
    return st[0]
}`,
          python: `def eval_rpn(tokens):
    st = []
    for s in tokens:
        if s in '+-*/':
            b, a = st.pop(), st.pop()
            if s=='+': st.append(a+b)
            elif s=='-': st.append(a-b)
            elif s=='*': st.append(a*b)
            else: st.append(int(a/b))
        else: st.append(int(s))
    return st[0]`,
          java: `public int evalRPN(String[] t) {
    Stack<Integer> st = new Stack<>();
    for(String s:t){
        if(s.equals("+")||s.equals("-")||s.equals("*")||s.equals("/")){
            int b=st.pop(), a=st.pop();
            switch(s){
            case "+": st.push(a+b); break;
            case "-": st.push(a-b); break;
            case "*": st.push(a*b); break;
            case "/": st.push(a/b); break;
            }
        } else st.push(Integer.parseInt(s));
    }
    return st.peek();
}`
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Recursive — complex, impractical।",
          "Stack — Time: O(n), Space: O(n)। সহজ ও efficient।",
          "Key: postfix evaluation-এ stack হলো natural choice।"
        ],
      },,
      { type: "h2", id: "prob-4", title: "Problem 4 — Daily Temperatures" },
      { type: "p", text: "প্রতিটি দিনের জন্য, কত দিন পরে বেশি উষ্ণ দিন আসবে তা বের করো।" },
      { type: "p", text: "Example: temps = [73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0]" },
      { type: "h3", title: "Brute Force — O(n²) nested loops" },
      { type: "p", text: "প্রতিটি দিনের জন্য, পরের সব দিন check করে বেশি উষ্ণ খুঁজে বের করো।" },
      {
        type: "multi-code",
        filename: "prob_4_brute",
        codeSamples: {
          cpp: `vector<int> dailyTemperatures(vector<int>& t) {
    vector<int> r(t.size());
    for(int i=0;i<t.size();i++)
        for(int j=i+1;j<t.size();j++)
            if(t[j]>t[i]){r[i]=j-i;break;}
    return r;
}`,
          go: `func dailyTemperatures(t []int) []int {
    r := make([]int, len(t))
    for i := 0; i < len(t); i++ {
        for j := i+1; j < len(t); j++ {
            if t[j] > t[i] { r[i] = j-i; break }
        }
    }
    return r
}`,
          python: `def daily_temperatures(t):
    r = [0]*len(t)
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            if t[j] > t[i]: r[i] = j-i; break
    return r`,
          java: `public int[] dailyTemperatures(int[] t) {
    int[] r = new int[t.length];
    for(int i=0;i<t.length;i++)
        for(int j=i+1;j<t.length;j++)
            if(t[j]>t[i]){r[i]=j-i;break;}
    return r;
}`
        },
      },,
      { type: "h3", title: "Optimal — O(n) Monotonic Stack" },
      { type: "p", text: "Stack-এ indices রাখো (decreasing temperatures)। বর্তমান temp যদি stack top-এর চেয়ে বেশি হয়, pop করে answer set করো।" },
      {
        type: "multi-code",
        filename: "prob_4_optimal",
        codeSamples: {
          cpp: `vector<int> dailyTemperatures(vector<int>& t) {
    vector<int> r(t.size());
    stack<int> st;
    for(int i=0;i<t.size();i++){
        while(!st.empty() && t[i]>t[st.top()]){
            int prev=st.top(); st.pop();
            r[prev]=i-prev;
        }
        st.push(i);
    }
    return r;
}`,
          go: `func dailyTemperatures(t []int) []int {
    r := make([]int, len(t))
    var st []int
    for i := 0; i < len(t); i++ {
        for len(st)>0 && t[i]>t[st[len(st)-1]] {
            prev := st[len(st)-1]; st = st[:len(st)-1]
            r[prev] = i-prev
        }
        st = append(st, i)
    }
    return r
}`,
          python: `def daily_temperatures(t):
    r = [0]*len(t)
    st = []
    for i, temp in enumerate(t):
        while st and temp > t[st[-1]]:
            prev = st.pop()
            r[prev] = i - prev
        st.append(i)
    return r`,
          java: `public int[] dailyTemperatures(int[] t) {
    int[] r = new int[t.length];
    Stack<Integer> st = new Stack<>();
    for(int i=0;i<t.length;i++){
        while(!st.isEmpty() && t[i]>t[st.peek()]){
            int prev = st.pop();
            r[prev] = i-prev;
        }
        st.push(i);
    }
    return r;
}`
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute — Time: O(n²), Space: O(1)।",
          "Monotonic Stack — Time: O(n), Space: O(n)। প্রতিটি element সর্বোচ্চ একবার push ও pop হয়।",
          "Key: monotonic stack — next greater element খোঁজার classic pattern।"
        ],
      },,
      { type: "h2", id: "prob-5", title: "Problem 5 — Largest Rectangle in Histogram" },
      { type: "p", text: "একটি histogram-এ সবচেয়ে বড় rectangle-এর area বের করো।" },
      { type: "p", text: "Example: heights = [2,1,5,6,2,3] → 10" },
      { type: "h3", title: "Brute Force — O(n²) expand from each bar" },
      { type: "p", text: "প্রতিটি bar-এর জন্য দুই দিকে expand করে যতদূর সম্ভব যাও। Area = height × width।" },
      {
        type: "multi-code",
        filename: "prob_5_brute",
        codeSamples: {
          cpp: `int largestRectangleArea(vector<int>& h) {
    int mx=0;
    for(int i=0;i<h.size();i++){
        int mn=h[i];
        for(int j=i;j<h.size();j++){
            mn=min(mn,h[j]);
            mx=max(mx,mn*(j-i+1));
        }
    }
    return mx;
}`,
          go: `func largestRectangleArea(h []int) int {
    mx := 0
    for i := 0; i < len(h); i++ {
        mn := h[i]
        for j := i; j < len(h); j++ {
            if h[j] < mn { mn = h[j] }
            area := mn*(j-i+1)
            if area > mx { mx = area }
        }
    }
    return mx
}`,
          python: `def largest_rectangle_area(h):
    mx = 0
    for i in range(len(h)):
        mn = h[i]
        for j in range(i, len(h)):
            mn = min(mn, h[j])
            mx = max(mx, mn*(j-i+1))
    return mx`,
          java: `public int largestRectangleArea(int[] h) {
    int mx=0;
    for(int i=0;i<h.length;i++){
        int mn=h[i];
        for(int j=i;j<h.length;j++){
            mn=Math.min(mn,h[j]);
            mx=Math.max(mx,mn*(j-i+1));
        }
    }
    return mx;
}`
        },
      },,
      { type: "h3", title: "Optimal — O(n) Monotonic Stack" },
      { type: "p", text: "Stack-এ increasing heights রাখো। ছোট height আসলে pop করে area calculate করো।" },
      {
        type: "multi-code",
        filename: "prob_5_optimal",
        codeSamples: {
          cpp: `int largestRectangleArea(vector<int>& h) {
    stack<int> st;
    h.push_back(0);
    int mx=0;
    for(int i=0;i<h.size();i++){
        while(!st.empty() && h[i]<h[st.top()]){
            int height=h[st.top()]; st.pop();
            int width=st.empty()?i:i-st.top()-1;
            mx=max(mx,height*width);
        }
        st.push(i);
    }
    return mx;
}`,
          go: `func largestRectangleArea(h []int) int {
    h = append(h, 0)
    var st []int
    mx := 0
    for i := 0; i < len(h); i++ {
        for len(st)>0 && h[i]<h[st[len(st)-1]] {
            height := h[st[len(st)-1]]; st = st[:len(st)-1]
            width := i
            if len(st)>0 { width = i-st[len(st)-1]-1 }
            if height*width > mx { mx = height*width }
        }
        st = append(st, i)
    }
    return mx
}`,
          python: `def largest_rectangle_area(h):
    h = h + [0]
    st = []
    mx = 0
    for i in range(len(h)):
        while st and h[i] < h[st[-1]]:
            height = h[st.pop()]
            width = i if not st else i - st[-1] - 1
            mx = max(mx, height * width)
        st.append(i)
    return mx`,
          java: `public int largestRectangleArea(int[] h) {
    int[] heights = Arrays.copyOf(h, h.length+1);
    Stack<Integer> st = new Stack<>();
    int mx = 0;
    for(int i=0;i<heights.length;i++){
        while(!st.isEmpty() && heights[i]<heights[st.peek()]){
            int height = heights[st.pop()];
            int width = st.isEmpty() ? i : i-st.peek()-1;
            mx = Math.max(mx, height*width);
        }
        st.push(i);
    }
    return mx;
}`
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute — Time: O(n²), Space: O(1)।",
          "Monotonic Stack — Time: O(n), Space: O(n)।",
          "Key: increasing stack — ছোট height আসলে pop করে area calculate।"
        ],
      },,
      { type: "h2", id: "summary", title: "Chapter Summary" },
      {
        type: "list",
        items: [
          "Valid Parentheses — Stack দিয়ে matching, O(n)।",
          "Min Stack — auxiliary stack দিয়ে O(1) getMin।",
          "RPN Evaluate — Stack দিয়ে postfix evaluation।",
          "Daily Temperatures — Monotonic stack, next greater element।",
          "Largest Rectangle — Increasing stack, area calculation।",
          "Core pattern: Stack ব্যবহার করো যখন 'সবশেষ seen' বা 'matching' দরকার।"
        ],
      },
      { type: "callout", calloutTone: "tip", text: "Tip: পরের topic হলো Binary Search — sorted array-তে O(log n) search।" }
    ],
  },

  // ---- Binary Search ----
  {
    id: "dsa-binary-search",
    subject: "dsa",
    title: "Binary Search",
    bangla: "বাইনারি সার্চ",
    difficulty: "Medium",
    est: "2 hr",
    summary: "Binary Search sorted array-তে O(log n)-এ element খুঁজে বের করে। ৫টি classic problem।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      { type: "p", text: "Binary Search হলো divide and conquer approach — sorted array-কে প্রতিটি step-এ অর্ধেক করে ভাগ করে। O(log n) time, O(1) space। Real-life thinking — phone book-এ একটি নাম খুঁজছো। মাঝখানে খুলো — আগে নাকি পরে? অর্ধেক বাদ দাও। বারবার করো।" },
      { type: "h2", id: "prob-1", title: "Problem 1 — Binary Search" },
      { type: "p", text: "Sorted array-তে একটি target খুঁজে বের করো।" },
      { type: "p", text: "Example: nums = [-1,0,3,5,9,12], target = 9 → 4" },
      { type: "h3", title: "Brute Force — O(n) linear scan" },
      { type: "p", text: "একে একে প্রতিটি element check করো।" },
      {
        type: "multi-code",
        filename: "prob_1_brute",
        codeSamples: {
          cpp: `int search(vector<int>& n, int t) {
    for(int i=0;i<n.size();i++) if(n[i]==t) return i;
    return -1;
}`,
          go: `func search(n []int, t int) int {
    for i, v := range n { if v == t { return i } }
    return -1
}`,
          python: `def search(n, t):
    for i, v in enumerate(n):
        if v == t: return i
    return -1`,
          java: `public int search(int[] n, int t) {
    for(int i=0;i<n.length;i++) if(n[i]==t) return i;
    return -1;
}`
        },
      },,
      { type: "h3", title: "Optimal — O(log n) Binary Search" },
      { type: "p", text: "মাঝখানে check করো। ছোট হলে ডান দিকে, বড় হলে বাম দিকে। প্রতি বার অর্ধেক।" },
      {
        type: "multi-code",
        filename: "prob_1_optimal",
        codeSamples: {
          cpp: `int search(vector<int>& n, int t) {
    int l=0, r=n.size()-1;
    while(l<=r){
        int m=l+(r-l)/2;
        if(n[m]==t) return m;
        if(n[m]<t) l=m+1; else r=m-1;
    }
    return -1;
}`,
          go: `func search(n []int, t int) int {
    l, r := 0, len(n)-1
    for l <= r {
        m := l + (r-l)/2
        if n[m] == t { return m }
        if n[m] < t { l = m+1 } else { r = m-1 }
    }
    return -1
}`,
          python: `def search(n, t):
    l, r = 0, len(n)-1
    while l <= r:
        m = (l+r)//2
        if n[m]==t: return m
        if n[m]<t: l=m+1
        else: r=m-1
    return -1`,
          java: `public int search(int[] n, int t) {
    int l=0, r=n.length-1;
    while(l<=r){
        int m=l+(r-l)/2;
        if(n[m]==t) return m;
        if(n[m]<t) l=m+1; else r=m-1;
    }
    return -1;
}`
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Linear — Time: O(n), Space: O(1)।",
          "Binary Search — Time: O(log n), Space: O(1)। প্রতি step-এ অর্ধেক।",
          "Key: sorted array + divide in half = O(log n)।"
        ],
      },,
      { type: "h2", id: "prob-2", title: "Problem 2 — Search in Rotated Sorted Array" },
      { type: "p", text: "Rotated sorted array-তে target খুঁজে বের করো।" },
      { type: "p", text: "Example: nums = [4,5,6,7,0,1,2], target = 0 → 4" },
      { type: "h3", title: "Brute Force — O(n) linear scan" },
      { type: "p", text: "একে একে প্রতিটি check করো।" },
      {
        type: "multi-code",
        filename: "prob_2_brute",
        codeSamples: {
          cpp: `int search(vector<int>& n, int t) {
    for(int i=0;i<n.size();i++) if(n[i]==t) return i;
    return -1;
}`,
          go: `func search(n []int, t int) int {
    for i, v := range n { if v == t { return i } }
    return -1
}`,
          python: `def search(n, t):
    for i, v in enumerate(n):
        if v == t: return i
    return -1`,
          java: `public int search(int[] n, int t) {
    for(int i=0;i<n.length;i++) if(n[i]==t) return i;
    return -1;
}`
        },
      },,
      { type: "h3", title: "Optimal — O(log n) Modified Binary Search" },
      { type: "p", text: "মাঝখানে check করো — কোন অর্ধেক sorted? Sorted অর্ধেকে target আছে কিনা দেখো।" },
      {
        type: "multi-code",
        filename: "prob_2_optimal",
        codeSamples: {
          cpp: `int search(vector<int>& n, int t) {
    int l=0, r=n.size()-1;
    while(l<=r){
        int m=l+(r-l)/2;
        if(n[m]==t) return m;
        if(n[l]<=n[m]){
            if(n[l]<=t&&t<n[m]) r=m-1; else l=m+1;
        } else {
            if(n[m]<t&&t<=n[r]) l=m+1; else r=m-1;
        }
    }
    return -1;
}`,
          go: `func search(n []int, t int) int {
    l, r := 0, len(n)-1
    for l <= r {
        m := l + (r-l)/2
        if n[m] == t { return m }
        if n[l] <= n[m] {
            if n[l] <= t && t < n[m] { r = m-1 } else { l = m+1 }
        } else {
            if n[m] < t && t <= n[r] { l = m+1 } else { r = m-1 }
        }
    }
    return -1
}`,
          python: `def search(n, t):
    l, r = 0, len(n)-1
    while l <= r:
        m = (l+r)//2
        if n[m] == t: return m
        if n[l] <= n[m]:
            if n[l] <= t < n[m]: r = m-1
            else: l = m+1
        else:
            if n[m] < t <= n[r]: l = m+1
            else: r = m-1
    return -1`,
          java: `public int search(int[] n, int t) {
    int l=0, r=n.length-1;
    while(l<=r){
        int m=l+(r-l)/2;
        if(n[m]==t) return m;
        if(n[l]<=n[m]){
            if(n[l]<=t&&t<n[m]) r=m-1; else l=m+1;
        } else {
            if(n[m]<t&&t<=n[r]) l=m+1; else r=m-1;
        }
    }
    return -1;
}`
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Linear — Time: O(n)।",
          "Modified Binary Search — Time: O(log n)।",
          "Key: কোন অর্ধেক sorted তা determine করো, তারপর target কোন অর্ধেক আছে দেখো।"
        ],
      },,
      { type: "h2", id: "prob-3", title: "Problem 3 — Find Minimum in Rotated Array" },
      { type: "p", text: "Rotated sorted array-তে সবচেয়ে ছোট element খুঁজে বের করো।" },
      { type: "p", text: "Example: nums = [3,4,5,1,2] → 1" },
      { type: "h3", title: "Brute Force — O(n) linear scan" },
      { type: "p", text: "পুরো array scan করে min বের করো।" },
      {
        type: "multi-code",
        filename: "prob_3_brute",
        codeSamples: {
          cpp: `int findMin(vector<int>& n) {
    int mn = n[0];
    for(int v : n) mn = min(mn, v);
    return mn;
}`,
          go: `func findMin(n []int) int {
    mn := n[0]
    for _, v := range n { if v < mn { mn = v } }
    return mn
}`,
          python: `def find_min(n):
    return min(n)`,
          java: `public int findMin(int[] n) {
    int mn = n[0];
    for(int v : n) mn = Math.min(mn, v);
    return mn;
}`
        },
      },,
      { type: "h3", title: "Optimal — O(log n) Binary Search" },
      { type: "p", text: "মাঝখানে check করো — বাম দিক sorted কিনা। যদি sorted হয় এবং n[mid] > n[right], তাহলে minimum ডান দিকে।" },
      {
        type: "multi-code",
        filename: "prob_3_optimal",
        codeSamples: {
          cpp: `int findMin(vector<int>& n) {
    int l=0, r=n.size()-1;
    while(l<r){
        int m=l+(r-l)/2;
        if(n[m]>n[r]) l=m+1;
        else r=m;
    }
    return n[l];
}`,
          go: `func findMin(n []int) int {
    l, r := 0, len(n)-1
    for l < r {
        m := l + (r-l)/2
        if n[m] > n[r] { l = m+1 } else { r = m }
    }
    return n[l]
}`,
          python: `def find_min(n):
    l, r = 0, len(n)-1
    while l < r:
        m = (l+r)//2
        if n[m] > n[r]: l = m+1
        else: r = m
    return n[l]`,
          java: `public int findMin(int[] n) {
    int l=0, r=n.length-1;
    while(l<r){
        int m=l+(r-l)/2;
        if(n[m]>n[r]) l=m+1; else r=m;
    }
    return n[l];
}`
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Linear — Time: O(n)।",
          "Binary Search — Time: O(log n)।",
          "Key: n[mid] > n[right] হলে minimum ডান দিকে, নাহলে বাম দিকে (বা mid-তে)।"
        ],
      },,
      { type: "h2", id: "prob-4", title: "Problem 4 — Search a 2D Matrix" },
      { type: "p", text: "Sorted 2D matrix-তে target খুঁজে বের করো।" },
      { type: "p", text: "Example: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 → true" },
      { type: "h3", title: "Brute Force — O(m×n) scan all" },
      { type: "p", text: "প্রতিটি cell check করো।" },
      {
        type: "multi-code",
        filename: "prob_4_brute",
        codeSamples: {
          cpp: `bool searchMatrix(vector<vector<int>>& m, int t) {
    for(auto& r:m) for(int v:r) if(v==t) return true;
    return false;
}`,
          go: `func searchMatrix(m [][]int, t int) bool {
    for _, r := range m { for _, v := range r { if v == t { return true } } }
    return false
}`,
          python: `def search_matrix(m, t):
    for row in m:
        if t in row: return True
    return False`,
          java: `public boolean searchMatrix(int[][] m, int t) {
    for(int[] r:m) for(int v:r) if(v==t) return true;
    return false;
}`
        },
      },,
      { type: "h3", title: "Optimal — O(log(m×n)) Binary Search" },
      { type: "p", text: "Matrix কে একটি sorted 1D array হিসেবে treat করো। index = mid / cols (row), mid % cols (col)।" },
      {
        type: "multi-code",
        filename: "prob_4_optimal",
        codeSamples: {
          cpp: `bool searchMatrix(vector<vector<int>>& m, int t) {
    int rows=m.size(), cols=m[0].size();
    int l=0, r=rows*cols-1;
    while(l<=r){
        int mid=l+(r-l)/2;
        int v=m[mid/cols][mid%cols];
        if(v==t) return true;
        if(v<t) l=mid+1; else r=mid-1;
    }
    return false;
}`,
          go: `func searchMatrix(m [][]int, t int) bool {
    rows, cols := len(m), len(m[0])
    l, r := 0, rows*cols-1
    for l <= r {
        mid := l + (r-l)/2
        v := m[mid/cols][mid%cols]
        if v == t { return true }
        if v < t { l = mid+1 } else { r = mid-1 }
    }
    return false
}`,
          python: `def search_matrix(m, t):
    rows, cols = len(m), len(m[0])
    l, r = 0, rows*cols-1
    while l <= r:
        mid = (l+r)//2
        v = m[mid//cols][mid%cols]
        if v == t: return True
        if v < t: l = mid+1
        else: r = mid-1
    return False`,
          java: `public boolean searchMatrix(int[][] m, int t) {
    int rows=m.length, cols=m[0].length;
    int l=0, r=rows*cols-1;
    while(l<=r){
        int mid=l+(r-l)/2;
        int v=m[mid/cols][mid%cols];
        if(v==t) return true;
        if(v<t) l=mid+1; else r=mid-1;
    }
    return false;
}`
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute — Time: O(m×n)।",
          "Binary Search — Time: O(log(m×n))।",
          "Key: 2D index কে 1D index-এ convert করো — mid/cols (row), mid%cols (col)।"
        ],
      },,
      { type: "h2", id: "prob-5", title: "Problem 5 — Koko Eating Bananas" },
      { type: "p", text: "Koko কে কত rate-এ banana খেতে হবে যাতে h ঘণ্টায় সব pile শেষ হয়।" },
      { type: "p", text: "Example: piles = [3,6,7,11], h = 8 → 4" },
      { type: "h3", title: "Brute Force — O(n × max) try all rates" },
      { type: "p", text: "১ থেকে max(piles) পর্যন্ত প্রতিটি rate try করো।" },
      {
        type: "multi-code",
        filename: "prob_5_brute",
        codeSamples: {
          cpp: `int minEatingSpeed(vector<int>& p, int h) {
    int mx = *max_element(p.begin(), p.end());
    for(int k=1;k<=mx;k++){
        int hrs=0;
        for(int v:p) hrs += (v+k-1)/k;
        if(hrs<=h) return k;
    }
    return mx;
}`,
          go: `func minEatingSpeed(p []int, h int) int {
    mx := 0
    for _, v := range p { if v > mx { mx = v } }
    for k := 1; k <= mx; k++ {
        hrs := 0
        for _, v := range p { hrs += (v+k-1)/k }
        if hrs <= h { return k }
    }
    return mx
}`,
          python: `def min_eating_speed(p, h):
    for k in range(1, max(p)+1):
        hrs = sum((v+k-1)//k for v in p)
        if hrs <= h: return k
    return max(p)`,
          java: `public int minEatingSpeed(int[] p, int h) {
    int mx = 0;
    for(int v : p) mx = Math.max(mx, v);
    for(int k=1;k<=mx;k++){
        int hrs=0;
        for(int v:p) hrs += (v+k-1)/k;
        if(hrs<=h) return k;
    }
    return mx;
}`
        },
      },,
      { type: "h3", title: "Optimal — O(n × log max) Binary Search on Answer" },
      { type: "p", text: "Rate-এর উপর binary search করো — ১ থেকে max(piles)। প্রতিটি mid-এর জন্য total hours check করো।" },
      {
        type: "multi-code",
        filename: "prob_5_optimal",
        codeSamples: {
          cpp: `int minEatingSpeed(vector<int>& p, int h) {
    int l=1, r=*max_element(p.begin(),p.end());
    while(l<r){
        int m=l+(r-l)/2, hrs=0;
        for(int v:p) hrs+=(v+m-1)/m;
        if(hrs<=h) r=m; else l=m+1;
    }
    return l;
}`,
          go: `func minEatingSpeed(p []int, h int) int {
    l, r := 1, 0
    for _, v := range p { if v > r { r = v } }
    for l < r {
        m := l + (r-l)/2
        hrs := 0
        for _, v := range p { hrs += (v+m-1)/m }
        if hrs <= h { r = m } else { l = m+1 }
    }
    return l
}`,
          python: `def min_eating_speed(p, h):
    l, r = 1, max(p)
    while l < r:
        m = (l+r)//2
        hrs = sum((v+m-1)//m for v in p)
        if hrs <= h: r = m
        else: l = m+1
    return l`,
          java: `public int minEatingSpeed(int[] p, int h) {
    int l=1, r=0;
    for(int v:p) r=Math.max(r,v);
    while(l<r){
        int m=l+(r-l)/2, hrs=0;
        for(int v:p) hrs+=(v+m-1)/m;
        if(hrs<=h) r=m; else l=m+1;
    }
    return l;
}`
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute — Time: O(n × max(piles))।",
          "Binary Search on Answer — Time: O(n × log max(piles))।",
          "Key: answer space-এ binary search — 'binary search on answer' pattern।"
        ],
      },,
      { type: "h2", id: "summary", title: "Chapter Summary" },
      {
        type: "list",
        items: [
          "Binary Search — sorted array-তে O(log n)।",
          "Rotated Array — কোন অর্ধেক sorted তা determine করো।",
          "Find Min — n[mid] vs n[right] দিয়ে direction।",
          "2D Matrix — 1D index-এ convert করে binary search।",
          "Koko — Binary search on answer space।",
          "Core pattern: sorted + divide in half = O(log n)।"
        ],
      },
      { type: "callout", calloutTone: "tip", text: "Tip: পরের topic হলো Sliding Window — fixed ও variable size window দিয়ে substring problems solve করা।" }
    ],
  },

  // ---- Sliding Window ----
  {
    id: "dsa-sliding-window",
    subject: "dsa",
    title: "Sliding Window",
    bangla: "স্লাইডিং উইন্ডো",
    difficulty: "Medium",
    est: "2.5 hr",
    summary: "Sliding Window fixed বা variable size window দিয়ে substring problems solve করে। ৫টি classic problem।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      { type: "p", text: "Sliding Window হলো একটি technique যেখানে একটি 'window' array বা string-এর উপর move করে। Fixed window (size স্থির) বা variable window (size পরিবর্তনশীল) হতে পারে। Real-life thinking — একটি magnifying glass দিয়ে একটি long document পড়ছো। Glass কে এক সাইড থেকে আরেক সাইডে move করো, প্রতিটি position-এ যা দেখো সেটাই window-এর content।" },
      { type: "h2", id: "prob-1", title: "Problem 1 — Best Time to Buy/Sell Stock" },
      { type: "p", text: "একটি price array দেওয়া আছে। Best buy-sell profit বের করো।" },
      { type: "h3", title: "Brute Force — O(n²) all pairs" },
      { type: "p", text: "প্রতিটি buy day-এর জন্য সব future sell day check করো।" },
      {
        type: "multi-code",
        filename: "dsa-sliding-window_p1_brute",
        codeSamples: {
          cpp: `int maxProfit(vector<int>& p) {
    int mx=0;
    for(int i=0;i<p.size();i++)
        for(int j=i+1;j<p.size();j++)
            mx=max(mx,p[j]-p[i]);
    return mx;
}`,
          go: `func maxProfit(p []int) int {
    mx := 0
    for i := 0; i < len(p); i++ {
        for j := i+1; j < len(p); j++ {
            if p[j]-p[i] > mx { mx = p[j]-p[i] }
        }
    }
    return mx
}`,
          python: `def max_profit(p):
    mx = 0
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            mx = max(mx, p[j]-p[i])
    return mx`,
          java: `public int maxProfit(int[] p) {
    int mx=0;
    for(int i=0;i<p.length;i++)
        for(int j=i+1;j<p.length;j++)
            mx=Math.max(mx,p[j]-p[i]);
    return mx;
}`,
        },
      },,
      { type: "h3", title: "Optimal — O(n) Sliding Window" },
      { type: "p", text: "একটি pointer 'min_price' track করে। বর্তমান price - min_price = profit। max profit রাখো।" },
      {
        type: "multi-code",
        filename: "dsa-sliding-window_p1_optimal",
        codeSamples: {
          cpp: `int maxProfit(vector<int>& p) {
    int mn=INT_MAX, mx=0;
    for(int v:p){mn=min(mn,v);mx=max(mx,v-mn);}
    return mx;
}`,
          go: `func maxProfit(p []int) int {
    mn, mx := p[0], 0
    for _, v := range p {
        if v < mn { mn = v }
        if v-mn > mx { mx = v-mn }
    }
    return mx
}`,
          python: `def max_profit(p):
    mn, mx = float('inf'), 0
    for v in p:
        mn = min(mn, v)
        mx = max(mx, v-mn)
    return mx`,
          java: `public int maxProfit(int[] p) {
    int mn=Integer.MAX_VALUE, mx=0;
    for(int v:p){mn=Math.min(mn,v);mx=Math.max(mx,v-mn);}
    return mx;
}`,
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute — Time: O(n²)।",
          "Sliding Window — Time: O(n), Space: O(1)।",
          "Key: সর্বনিম্ন price track করে profit maximize করো।"
        ],
      },,
      { type: "h2", id: "prob-2", title: "Problem 2 — Longest Substring Without Repeating" },
      { type: "p", text: "সবচেয়ে বড় substring যাতে কোনো repeating character নেই।" },
      { type: "h3", title: "Brute Force — O(n²) check all substrings" },
      { type: "p", text: "প্রতিটি starting position থেকে expand করে দেখো।" },
      {
        type: "multi-code",
        filename: "dsa-sliding-window_p2_brute",
        codeSamples: {
          cpp: `int lengthOfLongestSubstring(string s) {
    int mx=0;
    for(int i=0;i<s.size();i++){
        set<char> seen;
        for(int j=i;j<s.size();j++){
            if(seen.count(s[j]))break;
            seen.insert(s[j]);
            mx=max(mx,j-i+1);
        }
    }
    return mx;
}`,
          go: `func lengthOfLongestSubstring(s string) int {
    mx := 0
    for i := 0; i < len(s); i++ {
        seen := make(map[byte]bool)
        for j := i; j < len(s); j++ {
            if seen[s[j]] { break }
            seen[s[j]] = true
            if j-i+1 > mx { mx = j-i+1 }
        }
    }
    return mx
}`,
          python: `def length_of_longest(s):
    mx = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen: break
            seen.add(s[j])
            mx = max(mx, j-i+1)
    return mx`,
          java: `public int lengthOfLongestSubstring(String s) {
    int mx=0;
    for(int i=0;i<s.length();i++){
        Set<Character> seen=new HashSet<>();
        for(int j=i;j<s.length();j++){
            if(seen.contains(s.charAt(j)))break;
            seen.add(s.charAt(j));
            mx=Math.max(mx,j-i+1);
        }
    }
    return mx;
}`,
        },
      },,
      { type: "h3", title: "Optimal — O(n) Sliding Window + Set" },
      { type: "p", text: "দুটি pointer — left ও right। Right move করে expand করো। Duplicate হলে left move করে shrink করো।" },
      {
        type: "multi-code",
        filename: "dsa-sliding-window_p2_optimal",
        codeSamples: {
          cpp: `int lengthOfLongestSubstring(string s) {
    set<char> st;
    int l=0, mx=0;
    for(int r=0;r<s.size();r++){
        while(st.count(s[r])){st.erase(s[l]);l++;}
        st.insert(s[r]);
        mx=max(mx,r-l+1);
    }
    return mx;
}`,
          go: `func lengthOfLongestSubstring(s string) int {
    seen := make(map[byte]int)
    l, mx := 0, 0
    for r := 0; r < len(s); r++ {
        if idx, ok := seen[s[r]]; ok && idx >= l {
            l = idx + 1
        }
        seen[s[r]] = r
        if r-l+1 > mx { mx = r-l+1 }
    }
    return mx
}`,
          python: `def length_of_longest(s):
    seen = {}
    l, mx = 0, 0
    for r, c in enumerate(s):
        if c in seen and seen[c] >= l:
            l = seen[c] + 1
        seen[c] = r
        mx = max(mx, r-l+1)
    return mx`,
          java: `public int lengthOfLongestSubstring(String s) {
    Map<Character,Integer> seen=new HashMap<>();
    int l=0,mx=0;
    for(int r=0;r<s.length();r++){
        if(seen.containsKey(s.charAt(r))&&seen.get(s.charAt(r))>=l)
            l=seen.get(s.charAt(r))+1;
        seen.put(s.charAt(r),r);
        mx=Math.max(mx,r-l+1);
    }
    return mx;
}`,
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute — Time: O(n²), Space: O(n)।",
          "Sliding Window — Time: O(n), Space: O(n)।",
          "Key: hash map দিয়ে character-এর last index track করো।"
        ],
      },,
      { type: "h2", id: "prob-3", title: "Problem 3 — Longest Repeating Character Replacement" },
      { type: "p", text: "String-এ kটি character replace করে longest repeating substring বানাও।" },
      { type: "h3", title: "Brute Force — O(n²) check all windows" },
      { type: "p", text: "প্রতিটি window চেক করো, kটি replace করে সব same করা যায় কিনা।" },
      {
        type: "multi-code",
        filename: "dsa-sliding-window_p3_brute",
        codeSamples: {
          cpp: `int characterReplacement(string s, int k) {
    int mx=0;
    for(int i=0;i<s.size();i++)
        for(int j=i;j<s.size();j++){
            int freq[26]={},mf=0;
            for(int x=i;x<=j;x++){freq[s[x]-'A']++;mf=max(mf,freq[s[x]-'A']);}
            if(j-i+1-mf<=k)mx=max(mx,j-i+1);
        }
    return mx;
}`,
          go: `// O(n²) approach
func characterReplacement(s string, k int) int {
    mx := 0
    for i := 0; i < len(s); i++ {
        for j := i; j < len(s); j++ {
            freq := [26]int{}
            mf := 0
            for x := i; x <= j; x++ { freq[s[x]-'A']++; if freq[s[x]-'A']>mf { mf=freq[s[x]-'A'] } }
            if j-i+1-mf <= k && j-i+1 > mx { mx = j-i+1 }
        }
    }
    return mx
}`,
          python: `def character_replacement(s, k):
    mx = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            from collections import Counter
            freq = Counter(s[i:j+1])
            mf = max(freq.values())
            if j-i+1-mf <= k: mx = max(mx, j-i+1)
    return mx`,
          java: `public int characterReplacement(String s, int k) {
    int mx=0;
    for(int i=0;i<s.length();i++)
        for(int j=i;j<s.length();j++){
            int[] f=new int[26];int mf=0;
            for(int x=i;x<=j;x++){f[s.charAt(x)-'A']++;mf=Math.max(mf,f[s.charAt(x)-'A']);}
            if(j-i+1-mf<=k)mx=Math.max(mx,j-i+1);
        }
    return mx;
}`,
        },
      },,
      { type: "h3", title: "Optimal — O(n) Sliding Window" },
      { type: "p", text: "Window-এ সবচেয়ে common character-এর count track করো। window - max_count > k হলে shrink।" },
      {
        type: "multi-code",
        filename: "dsa-sliding-window_p3_optimal",
        codeSamples: {
          cpp: `int characterReplacement(string s, int k) {
    int freq[26]={}, l=0, mf=0, mx=0;
    for(int r=0;r<s.size();r++){
        freq[s[r]-'A']++;
        mf=max(mf,freq[s[r]-'A']);
        while(r-l+1-mf>k){freq[s[l]-'A']--;l++;}
        mx=max(mx,r-l+1);
    }
    return mx;
}`,
          go: `func characterReplacement(s string, k int) int {
    freq := [26]int{}
    l, mf, mx := 0, 0, 0
    for r := 0; r < len(s); r++ {
        freq[s[r]-'A']++
        if freq[s[r]-'A'] > mf { mf = freq[s[r]-'A'] }
        for r-l+1-mf > k { freq[s[l]-'A']--; l++ }
        if r-l+1 > mx { mx = r-l+1 }
    }
    return mx
}`,
          python: `def character_replacement(s, k):
    freq = {}
    l = mf = mx = 0
    for r in range(len(s)):
        freq[s[r]] = freq.get(s[r], 0) + 1
        mf = max(mf, freq[s[r]])
        while r-l+1-mf > k:
            freq[s[l]] -= 1
            l += 1
        mx = max(mx, r-l+1)
    return mx`,
          java: `public int characterReplacement(String s, int k) {
    int[] f=new int[26];int l=0,mf=0,mx=0;
    for(int r=0;r<s.length();r++){
        f[s.charAt(r)-'A']++;mf=Math.max(mf,f[s.charAt(r)-'A']);
        while(r-l+1-mf>k){f[s.charAt(l)-'A']--;l++;}
        mx=Math.max(mx,r-l+1);
    }
    return mx;
}`,
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute — Time: O(n³)।",
          "Sliding Window — Time: O(n), Space: O(1)।",
          "Key: window - max_freq <= k হলে valid window।"
        ],
      },,
      { type: "h2", id: "prob-4", title: "Problem 4 — Permutation in String" },
      { type: "p", text: "s2-তে কোনো substring কি s1-এর permutation? " },
      { type: "h3", title: "Brute Force — O(n! × m) generate all permutations" },
      { type: "p", text: "s1-এর সব permutation generate করে s2-এ খুঁজো। খুব slow!" },
      {
        type: "multi-code",
        filename: "dsa-sliding-window_p4_brute",
        codeSamples: {
          cpp: `bool checkInclusion(string s1, string s2) {
    // generate all permutations of s1, check each in s2
    // O(n! × m) — impractical
    return false;
}`,
          go: `// O(n!) — impractical
func checkInclusion(s1, s2 string) bool { return false }`,
          python: `from itertools import permutations
def check_inclusion(s1, s2):
    for p in set(permutations(s1)):
        if ''.join(p) in s2: return True
    return False`,
          java: `// O(n!) — impractical
public boolean checkInclusion(String s1, String s2) { return false; }`,
        },
      },,
      { type: "h3", title: "Optimal — O(n) Sliding Window + Frequency" },
      { type: "p", text: "Fixed window (size = len(s1))। Frequency array compare করো। Match হলে true।" },
      {
        type: "multi-code",
        filename: "dsa-sliding-window_p4_optimal",
        codeSamples: {
          cpp: `bool checkInclusion(string s1, string s2) {
    int n=s1.size(),m=s2.size();
    if(n>m)return false;
    vector<int> f1(26),f2(26);
    for(int i=0;i<n;i++){f1[s1[i]-'a']++;f2[s2[i]-'a']++;}
    if(f1==f2)return true;
    for(int i=n;i<m;i++){f2[s2[i]-'a']++;f2[s2[i-n]-'a']--;if(f1==f2)return true;}
    return false;
}`,
          go: `func checkInclusion(s1, s2 string) bool {
    n, m := len(s1), len(s2)
    if n > m { return false }
    f1, f2 := [26]int{}, [26]int{}
    for i := 0; i < n; i++ { f1[s1[i]-'a']++; f2[s2[i]-'a']++ }
    if f1 == f2 { return true }
    for i := n; i < m; i++ {
        f2[s2[i]-'a']++; f2[s2[i-n]-'a']--
        if f1 == f2 { return true }
    }
    return false
}`,
          python: `def check_inclusion(s1, s2):
    from collections import Counter
    n = len(s1)
    c1 = Counter(s1)
    c2 = Counter(s2[:n])
    if c1 == c2: return True
    for i in range(n, len(s2)):
        c2[s2[i]] += 1
        c2[s2[i-n]] -= 1
        if c2[s2[i-n]] == 0: del c2[s2[i-n]]
        if c1 == c2: return True
    return False`,
          java: `public boolean checkInclusion(String s1, String s2) {
    int n=s1.length(),m=s2.length();
    if(n>m)return false;
    int[] f1=new int[26],f2=new int[26];
    for(int i=0;i<n;i++){f1[s1.charAt(i)-'a']++;f2[s2.charAt(i)-'a']++;}
    if(Arrays.equals(f1,f2))return true;
    for(int i=n;i<m;i++){f2[s2.charAt(i)-'a']++;f2[s2.charAt(i-n)-'a']--;if(Arrays.equals(f1,f2))return true;}
    return false;
}`,
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Permutations — Time: O(n! × m)। Impractical।",
          "Sliding Window — Time: O(n + m), Space: O(1)।",
          "Key: fixed window + frequency array compare।"
        ],
      },,
      { type: "h2", id: "prob-5", title: "Problem 5 — Minimum Window Substring" },
      { type: "p", text: "s-তে সবচেয়ে ছোট substring যাতে t-এর সব character আছে।" },
      { type: "h3", title: "Brute Force — O(n²) check all windows" },
      { type: "p", text: "প্রতিটি starting ও ending position check করো।" },
      {
        type: "multi-code",
        filename: "dsa-sliding-window_p5_brute",
        codeSamples: {
          cpp: `string minWindow(string s, string t) {
    string res;
    for(int i=0;i<s.size();i++)
        for(int j=i;j<s.size();j++){
            // check if s[i..j] contains all of t
            // O(n² × k)
        }
    return res;
}`,
          go: `// O(n²) approach
func minWindow(s, t string) string {
    res := ""
    // check all windows
    return res
}`,
          python: `def min_window(s, t):
    from collections import Counter
    need = Counter(t)
    res = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            window = Counter(s[i:j])
            if all(window[c] >= need[c] for c in need):
                if not res or j-i < len(res):
                    res = s[i:j]
    return res`,
          java: `// O(n²) approach
public String minWindow(String s, String t) {
    String res = "";
    // check all windows
    return res;
}`,
        },
      },,
      { type: "h3", title: "Optimal — O(n) Sliding Window + Counter" },
      { type: "p", text: "দুটি pointer — expand right, contract left। Need map track করো। সব need মিটলে window shrink করো।" },
      {
        type: "multi-code",
        filename: "dsa-sliding-window_p5_optimal",
        codeSamples: {
          cpp: `string minWindow(string s, string t) {
    unordered_map<char,int> need,have;
    for(char c:t)need[c]++;
    int l=0,need_cnt=need.size(),have_cnt=0,mn=INT_MAX,ml=0;
    for(int r=0;r<s.size();r++){
        have[s[r]]++;
        if(need.count(s[r])&&have[s[r]]==need[s[r]])have_cnt++;
        while(have_cnt==need_cnt){
            if(r-l+1<mn){mn=r-l+1;ml=l;}
            have[s[l]]--;
            if(need.count(s[l])&&have[s[l]]<need[s[l]])have_cnt--;
            l++;
        }
    }
    return mn==INT_MAX?"":s.substr(ml,mn);
}`,
          go: `func minWindow(s, t string) string {
    need, have := map[byte]int{}, map[byte]int{}
    for i := 0; i < len(t); i++ { need[t[i]]++ }
    l, needCnt, haveCnt, mn, ml := 0, len(need), 0, len(s)+1, 0
    for r := 0; r < len(s); r++ {
        have[s[r]]++
        if _, ok := need[s[r]]; ok && have[s[r]] == need[s[r]] { haveCnt++ }
        for haveCnt == needCnt {
            if r-l+1 < mn { mn = r-l+1; ml = l }
            have[s[l]]--
            if _, ok := need[s[l]]; ok && have[s[l]] < need[s[l]] { haveCnt-- }
            l++
        }
    }
    if mn > len(s) { return "" }
    return s[ml : ml+mn]
}`,
          python: `def min_window(s, t):
    from collections import Counter
    need = Counter(t)
    have = {}
    l = need_cnt = len(need)
    have_cnt = 0
    ml = mn = 0
    res = ""
    for r, c in enumerate(s):
        have[c] = have.get(c, 0) + 1
        if c in need and have[c] == need[c]: have_cnt += 1
        while have_cnt == need_cnt:
            if not res or r-l+1 < len(res):
                res = s[l:r+1]
            have[s[l]] -= 1
            if s[l] in need and have[s[l]] < need[s[l]]: have_cnt -= 1
            l += 1
    return res`,
          java: `public String minWindow(String s, String t) {
    Map<Character,Integer> need=new HashMap<>(),have=new HashMap<>();
    for(char c:t.toCharArray())need.merge(c,1,Integer::sum);
    int l=0,needCnt=need.size(),haveCnt=0,mn=Integer.MAX_VALUE,ml=0;
    for(int r=0;r<s.length();r++){
        have.merge(s.charAt(r),1,Integer::sum);
        if(need.containsKey(s.charAt(r))&&have.get(s.charAt(r)).equals(need.get(s.charAt(r))))haveCnt++;
        while(haveCnt==needCnt){
            if(r-l+1<mn){mn=r-l+1;ml=l;}
            have.merge(s.charAt(l),-1,Integer::sum);
            if(need.containsKey(s.charAt(l))&&have.get(s.charAt(l))<need.get(s.charAt(l)))haveCnt--;
            l++;
        }
    }
    return mn==Integer.MAX_VALUE?"":s.substring(ml,ml+mn);
}`,
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute — Time: O(n² × k)।",
          "Sliding Window — Time: O(n), Space: O(k)।",
          "Key: expand right, contract left when all needs met।"
        ],
      },,
      { type: "h2", id: "summary", title: "Chapter Summary" },
      { type: "callout", calloutTone: "tip", text: "Tip: পরের topic হলো Linked List — pointer দিয়ে nodes এর সাথে connected।" }
    ],
  },

  // ---- Linked List ----
  {
    id: "dsa-linked-list",
    subject: "dsa",
    title: "Linked List",
    bangla: "লিংকড লিস্ট",
    difficulty: "Medium",
    est: "2.5 hr",
    summary: "Linked List হলো pointer-যুক্ত nodes-এর একটি chain। ৫টি classic problem।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      { type: "p", text: "Linked List-এ প্রতিটি node একটি value ও একটি next pointer ধারণ করে। Array-র মতোই, কিন্তু contiguous memory-তে নয়। Real-life thinking — একটি treasure hunt! প্রতিটি clue পরের clue-এর address ধারণ করে। তোমাকে একে একে follow করতে হয়।" },
      { type: "h2", id: "prob-1", title: "Problem 1 — Reverse Linked List" },
      { type: "p", text: "একটি singly linked list reverse করো।" },
      { type: "h3", title: "Brute Force — O(n) with stack" },
      { type: "p", text: "সব nodes stack-এ push করে আবার pop করে reverse করো।" },
      {
        type: "multi-code",
        filename: "dsa-linked-list_p1_brute",
        codeSamples: {
          cpp: `ListNode* reverseList(ListNode* head) {
    stack<ListNode*> st;
    while(head){st.push(head);head=head->next;}
    ListNode dummy(0);ListNode* cur=&dummy;
    while(!st.empty()){cur->next=st.top();st.pop();cur=cur->next;}
    cur->next=nullptr;return dummy.next;
}`,
          go: `func reverseList(head *ListNode) *ListNode {
    var st []*ListNode
    for p := head; p != nil; p = p.Next { st = append(st, p) }
    dummy := &ListNode{}
    cur := dummy
    for i := len(st)-1; i >= 0; i-- { cur.Next = st[i]; cur = cur.Next }
    cur.Next = nil
    return dummy.Next
}`,
          python: `def reverse_list(head):
    st = []
    while head:
        st.append(head)
        head = head.next
    dummy = ListNode()
    cur = dummy
    while st:
        cur.next = st.pop()
        cur = cur.next
    cur.next = None
    return dummy.next`,
          java: `public ListNode reverseList(ListNode head) {
    Stack<ListNode> st = new Stack<>();
    while(head!=null){st.push(head);head=head.next;}
    ListNode dummy=new ListNode();
    ListNode cur=dummy;
    while(!st.isEmpty()){cur.next=st.pop();cur=cur.next;}
    cur.next=null;return dummy.next;
}`,
        },
      },,
      { type: "h3", title: "Optimal — O(n) Iterative with 3 pointers" },
      { type: "p", text: "prev, cur, next — তিনটি pointer ব্যবহার করো। cur->next = prev করে pointer উল্টে দাও।" },
      {
        type: "multi-code",
        filename: "dsa-linked-list_p1_optimal",
        codeSamples: {
          cpp: `ListNode* reverseList(ListNode* head) {
    ListNode *prev=nullptr,*cur=head;
    while(cur){ListNode* nxt=cur->next;cur->next=prev;prev=cur;cur=nxt;}
    return prev;
}`,
          go: `func reverseList(head *ListNode) *ListNode {
    var prev *ListNode
    cur := head
    for cur != nil {
        nxt := cur.Next
        cur.Next = prev
        prev = cur
        cur = nxt
    }
    return prev
}`,
          python: `def reverse_list(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev`,
          java: `public ListNode reverseList(ListNode head) {
    ListNode prev=null,cur=head;
    while(cur!=null){ListNode nxt=cur.next;cur.next=prev;prev=cur;cur=nxt;}
    return prev;
}`,
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Stack — Time: O(n), Space: O(n)।",
          "3 Pointers — Time: O(n), Space: O(1)।",
          "Key: pointer উল্টে দাও — cur->next = prev।"
        ],
      },,
      { type: "h2", id: "prob-2", title: "Problem 2 — Merge Two Sorted Lists" },
      { type: "p", text: "দুটি sorted linked list merge করো।" },
      { type: "h3", title: "Brute Force — O(n+m) extract to array" },
      { type: "p", text: "দুটি list কে array-তে convert করে merge করে আবার list বানাও।" },
      {
        type: "multi-code",
        filename: "dsa-linked-list_p2_brute",
        codeSamples: {
          cpp: `ListNode* mergeTwoLists(ListNode* a, ListNode* b) {
    vector<int> vals;
    while(a){vals.push_back(a->val);a=a->next;}
    while(b){vals.push_back(b->val);b=b->next;}
    sort(vals.begin(),vals.end());
    ListNode dummy(0);ListNode* cur=&dummy;
    for(int v:vals){cur->next=new ListNode(v);cur=cur->next;}
    return dummy.next;
}`,
          go: `func mergeTwoLists(a, b *ListNode) *ListNode {
    var vals []int
    for p := a; p != nil; p = p.Next { vals = append(vals, p.Val) }
    for p := b; p != nil; p = p.Next { vals = append(vals, p.Val) }
    sort.Ints(vals)
    dummy := &ListNode{}
    cur := dummy
    for _, v := range vals { cur.Next = &ListNode{Val: v}; cur = cur.Next }
    return dummy.Next
}`,
          python: `def merge_two_lists(a, b):
    vals = []
    while a: vals.append(a.val); a = a.next
    while b: vals.append(b.val); b = b.next
    vals.sort()
    dummy = ListNode()
    cur = dummy
    for v in vals: cur.next = ListNode(v); cur = cur.next
    return dummy.next`,
          java: `public ListNode mergeTwoLists(ListNode a, ListNode b) {
    List<Integer> vals=new ArrayList<>();
    while(a!=null){vals.add(a.val);a=a.next;}
    while(b!=null){vals.add(b.val);b=b.next;}
    Collections.sort(vals);
    ListNode dummy=new ListNode();ListNode cur=dummy;
    for(int v:vals){cur.next=new ListNode(v);cur=cur.next;}
    return dummy.next;
}`,
        },
      },,
      { type: "h3", title: "Optimal — O(n+m) Iterative Merge" },
      { type: "p", text: "দুটি pointer দিয়ে ছোট node কে প্রথমে রাখো। next pointer adjust করো।" },
      {
        type: "multi-code",
        filename: "dsa-linked-list_p2_optimal",
        codeSamples: {
          cpp: `ListNode* mergeTwoLists(ListNode* a, ListNode* b) {
    ListNode dummy(0);ListNode* cur=&dummy;
    while(a&&b){
        if(a->val<=b->val){cur->next=a;a=a->next;}
        else{cur->next=b;b=b->next;}
        cur=cur->next;
    }
    cur->next=a?a:b;
    return dummy.next;
}`,
          go: `func mergeTwoLists(a, b *ListNode) *ListNode {
    dummy := &ListNode{}
    cur := dummy
    for a != nil && b != nil {
        if a.Val <= b.Val { cur.Next = a; a = a.Next } else { cur.Next = b; b = b.Next }
        cur = cur.Next
    }
    if a != nil { cur.Next = a } else { cur.Next = b }
    return dummy.Next
}`,
          python: `def merge_two_lists(a, b):
    dummy = ListNode()
    cur = dummy
    while a and b:
        if a.val <= b.val: cur.next = a; a = a.next
        else: cur.next = b; b = b.next
        cur = cur.next
    cur.next = a or b
    return dummy.next`,
          java: `public ListNode mergeTwoLists(ListNode a, ListNode b) {
    ListNode dummy=new ListNode();ListNode cur=dummy;
    while(a!=null&&b!=null){
        if(a.val<=b.val){cur.next=a;a=a.next;}
        else{cur.next=b;b=b.next;}
        cur=cur.next;
    }
    cur.next=a!=null?a:b;
    return dummy.next;
}`,
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Array — Time: O((n+m) log(n+m)), Space: O(n+m)।",
          "Iterative Merge — Time: O(n+m), Space: O(1)।",
          "Key: ছোট node প্রথমে — merge sort-এর merge step।"
        ],
      },,
      { type: "h2", id: "prob-3", title: "Problem 3 — Linked List Cycle" },
      { type: "p", text: "Linked list-এ cycle আছে কিনা detect করো।" },
      { type: "h3", title: "Brute Force — O(n) with hash set" },
      { type: "p", text: "প্রতিটি visited node কে set-এ store করো। পুনরায় visit হলে cycle আছে।" },
      {
        type: "multi-code",
        filename: "dsa-linked-list_p3_brute",
        codeSamples: {
          cpp: `bool hasCycle(ListNode* head) {
    set<ListNode*> visited;
    while(head){
        if(visited.count(head))return true;
        visited.insert(head);
        head=head->next;
    }
    return false;
}`,
          go: `func hasCycle(head *ListNode) bool {
    visited := make(map[*ListNode]bool)
    for p := head; p != nil; p = p.Next {
        if visited[p] { return true }
        visited[p] = true
    }
    return false
}`,
          python: `def has_cycle(head):
    visited = set()
    while head:
        if head in visited: return True
        visited.add(head)
        head = head.next
    return False`,
          java: `public boolean hasCycle(ListNode head) {
    Set<ListNode> visited=new HashSet<>();
    while(head!=null){
        if(visited.contains(head))return true;
        visited.add(head);
        head=head.next;
    }
    return false;
}`,
        },
      },,
      { type: "h3", title: "Optimal — O(n) Floyd's Cycle Detection" },
      { type: "p", text: "দুটি pointer — slow (1 step), fast (2 steps)। Fast যদি slow কে catch করে, cycle আছে।" },
      {
        type: "multi-code",
        filename: "dsa-linked-list_p3_optimal",
        codeSamples: {
          cpp: `bool hasCycle(ListNode* head) {
    ListNode *slow=head,*fast=head;
    while(fast&&fast->next){
        slow=slow->next;
        fast=fast->next->next;
        if(slow==fast)return true;
    }
    return false;
}`,
          go: `func hasCycle(head *ListNode) bool {
    slow, fast := head, head
    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
        if slow == fast { return true }
    }
    return false
}`,
          python: `def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return True
    return False`,
          java: `public boolean hasCycle(ListNode head) {
    ListNode slow=head,fast=head;
    while(fast!=null&&fast.next!=null){
        slow=slow.next;
        fast=fast.next.next;
        if(slow==fast)return true;
    }
    return false;
}`,
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Hash Set — Time: O(n), Space: O(n)।",
          "Floyd's — Time: O(n), Space: O(1)।",
          "Key: slow ও fast pointer — fast যদি slow কে catch করে, cycle।"
        ],
      },,
      { type: "h2", id: "prob-4", title: "Problem 4 — Remove Nth Node From End" },
      { type: "p", text: "শেষ থেকে Nতম node remove করো।" },
      { type: "h3", title: "Brute Force — O(n) two passes" },
      { type: "p", text: "প্রথমে length count করো, তারপর (length - n)তম node-এ যাও।" },
      {
        type: "multi-code",
        filename: "dsa-linked-list_p4_brute",
        codeSamples: {
          cpp: `ListNode* removeNthFromEnd(ListNode* head, int n) {
    int len=0;
    for(ListNode* p=head;p;p=p->next)len++;
    if(len==n)return head->next;
    ListNode* p=head;
    for(int i=0;i<len-n-1;i++)p=p->next;
    p->next=p->next->next;
    return head;
}`,
          go: `func removeNthFromEnd(head *ListNode, n int) *ListNode {
    ln := 0
    for p := head; p != nil; p = p.Next { ln++ }
    if ln == n { return head.Next }
    p := head
    for i := 0; i < ln-n-1; i++ { p = p.Next }
    p.Next = p.Next.Next
    return head
}`,
          python: `def remove_nth_from_end(head, n):
    length = 0
    p = head
    while p: length += 1; p = p.next
    if length == n: return head.next
    p = head
    for _ in range(length - n - 1): p = p.next
    p.next = p.next.next
    return head`,
          java: `public ListNode removeNthFromEnd(ListNode head, int n) {
    int len=0;
    for(ListNode p=head;p!=null;p=p.next)len++;
    if(len==n)return head.next;
    ListNode p=head;
    for(int i=0;i<len-n-1;i++)p=p.next;
    p.next=p.next.next;
    return head;
}`,
        },
      },,
      { type: "h3", title: "Optimal — O(n) Two Pointers — one pass" },
      { type: "p", text: "fast pointer কে n step আগে পাঠাও। তারপর slow ও fast একসাথে move করো। Fast শেষে গেলে slow Nth-এ আছে।" },
      {
        type: "multi-code",
        filename: "dsa-linked-list_p4_optimal",
        codeSamples: {
          cpp: `ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode dummy(0);dummy.next=head;
    ListNode *fast=&dummy,*slow=&dummy;
    for(int i=0;i<n;i++)fast=fast->next;
    while(fast->next){fast=fast->next;slow=slow->next;}
    slow->next=slow->next->next;
    return dummy.next;
}`,
          go: `func removeNthFromEnd(head *ListNode, n int) *ListNode {
    dummy := &ListNode{Next: head}
    fast, slow := dummy, dummy
    for i := 0; i < n; i++ { fast = fast.Next }
    for fast.Next != nil { fast = fast.Next; slow = slow.Next }
    slow.Next = slow.Next.Next
    return dummy.Next
}`,
          python: `def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n): fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next`,
          java: `public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy=new ListNode(0,head);
    ListNode fast=dummy,slow=dummy;
    for(int i=0;i<n;i++)fast=fast.next;
    while(fast.next!=null){fast=fast.next;slow=slow.next;}
    slow.next=slow.next.next;
    return dummy.next;
}`,
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Two Passes — Time: O(n), Space: O(1)।",
          "Two Pointers — Time: O(n), Space: O(1)। One pass!",
          "Key: fast কে n step আগে পাঠাও — distance gap maintain করে।"
        ],
      },,
      { type: "h2", id: "prob-5", title: "Problem 5 — Reorder List" },
      { type: "p", text: "Linked list কে এমনভাবে reorder করো: L0→Ln→L1→Ln-1→L2→Ln-2→…" },
      { type: "h3", title: "Brute Force — O(n²) repeatedly find tail" },
      { type: "p", text: "প্রতিটি step-এ tail find করে সেটিকে current node-এর পরে insert করো।" },
      {
        type: "multi-code",
        filename: "dsa-linked-list_p5_brute",
        codeSamples: {
          cpp: `void reorderList(ListNode* head) {
    if(!head||!head->next)return;
    ListNode* cur=head;
    while(cur&&cur->next){
        ListNode* prev=nullptr,*tail=head;
        while(tail->next){prev=tail;tail=tail->next;}
        if(prev)prev->next=nullptr;
        tail->next=cur->next;
        cur->next=tail;
        cur=tail->next;
    }
}`,
          go: `func reorderList(head *ListNode) {
    if head == nil || head.Next == nil { return }
    cur := head
    for cur != nil && cur.Next != nil {
        var prev *ListNode
        tail := head
        for tail.Next != nil { prev = tail; tail = tail.Next }
        if prev != nil { prev.Next = nil }
        tail.Next = cur.Next
        cur.Next = tail
        cur = tail.Next
    }
}`,
          python: `def reorder_list(head):
    if not head or not head.next: return
    cur = head
    while cur and cur.next:
        prev = None
        tail = head
        while tail.next: prev = tail; tail = tail.next
        if prev: prev.next = None
        tail.next = cur.next
        cur.next = tail
        cur = tail.next`,
          java: `public void reorderList(ListNode head) {
    if(head==null||head.next==null)return;
    ListNode cur=head;
    while(cur!=null&&cur.next!=null){
        ListNode prev=null,tail=head;
        while(tail.next!=null){prev=tail;tail=tail.next;}
        if(prev!=null)prev.next=null;
        tail.next=cur.next;
        cur.next=tail;
        cur=tail.next;
    }
}`,
        },
      },,
      { type: "h3", title: "Optimal — O(n) Find Middle + Reverse + Merge" },
      { type: "p", text: "১. Slow-fast pointer দিয়ে middle খুঁজো। ২. দ্বিতীয় অর্ধ reverse করো। ৩. দুটি অর্ধ merge করো।" },
      {
        type: "multi-code",
        filename: "dsa-linked-list_p5_optimal",
        codeSamples: {
          cpp: `void reorderList(ListNode* head) {
    ListNode *slow=head,*fast=head->next;
    while(fast&&fast->next){slow=slow->next;fast=fast->next->next;}
    ListNode* second=slow->next;
    slow->next=nullptr;
    ListNode* prev=nullptr;
    while(second){ListNode* nxt=second->next;second->next=prev;prev=second;second=nxt;}
    ListNode* first=head;
    while(prev){ListNode* tmp1=first->next;
        ListNode* tmp2=prev->next;
        first->next=prev;prev->next=tmp1;
        first=tmp1;prev=tmp2;}
}`,
          go: `func reorderList(head *ListNode) {
    slow, fast := head, head.Next
    for fast != nil && fast.Next != nil { slow = slow.Next; fast = fast.Next.Next }
    second := slow.Next
    slow.Next = nil
    var prev *ListNode
    for second != nil { nxt := second.Next; second.Next = prev; prev = second; second = nxt }
    first := head
    for prev != nil {
        tmp1, tmp2 := first.Next, prev.Next
        first.Next = prev; prev.Next = tmp1
        first = tmp1; prev = tmp2
    }
}`,
          python: `def reorder_list(head):
    if not head or not head.next: return
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next; fast = fast.next.next
    second = slow.next
    slow.next = None
    prev = None
    while second:
        nxt = second.next; second.next = prev; prev = second; second = nxt
    first = head
    while prev:
        tmp1, tmp2 = first.next, prev.next
        first.next = prev; prev.next = tmp1
        first = tmp1; prev = tmp2`,
          java: `public void reorderList(ListNode head) {
    ListNode slow=head,fast=head.next;
    while(fast!=null&&fast.next!=null){slow=slow.next;fast=fast.next.next;}
    ListNode second=slow.next;
    slow.next=null;
    ListNode prev=null;
    while(second!=null){ListNode nxt=second.next;second.next=prev;prev=second;second=nxt;}
    ListNode first=head;
    while(prev!=null){
        ListNode t1=first.next,t2=prev.next;
        first.next=prev;prev.next=t1;
        first=t1;prev=t2;
    }
}`,
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Repeated tail find — Time: O(n²)।",
          "Middle + Reverse + Merge — Time: O(n), Space: O(1)।",
          "Key: find middle, reverse second half, interleave merge।"
        ],
      },,
      { type: "h2", id: "summary", title: "Chapter Summary" },
      { type: "callout", calloutTone: "tip", text: "Tip: পরের topic হলো Trees — hierarchical data structure যা recursion দিয়ে সুন্দরভাবে solve হয়।" }
    ],
  },

  // ---- Trees ----
  {
    id: "dsa-trees",
    subject: "dsa",
    title: "Trees",
    bangla: "ট্রি",
    difficulty: "Hard",
    est: "3 hr",
    summary: "Tree হলো hierarchical data structure। ৫টি classic problem — traversal, BST, ও construction।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      { type: "p", text: "Tree হলো একটি hierarchical structure যেখানে প্রতিটি node-এর সর্বোচ্চ দুটি children (left ও right) থাকে। Root হলো সবার উপরের node, leaf হলো যাদের কোনো child নেই। Real-life thinking — একটি family tree! প্রতিটি মানুষের parents (children in tree terms) ও descendants। Root হলো পূর্বপুরুষ।" },
      { type: "h2", id: "prob-1", title: "Problem 1 — Invert Binary Tree" },
      { type: "p", text: "একটি binary tree কে mirror করো।" },
      { type: "h3", title: "Brute Force — O(n) with explicit stack" },
      { type: "p", text: "Stack দিয়ে প্রতিটি node-এ যাও, children swap করো।" },
      {
        type: "multi-code",
        filename: "dsa-trees_p1_brute",
        codeSamples: {
          cpp: `TreeNode* invertTree(TreeNode* root) {
    if(!root)return nullptr;
    stack<TreeNode*> st;
    st.push(root);
    while(!st.empty()){
        TreeNode* n=st.top();st.pop();
        swap(n->left,n->right);
        if(n->left)st.push(n->left);
        if(n->right)st.push(n->right);
    }
    return root;
}`,
          go: `func invertTree(root *TreeNode) *TreeNode {
    if root == nil { return nil }
    var st []*TreeNode
    st = append(st, root)
    for len(st) > 0 {
        n := st[len(st)-1]; st = st[:len(st)-1]
        n.Left, n.Right = n.Right, n.Left
        if n.Left != nil { st = append(st, n.Left) }
        if n.Right != nil { st = append(st, n.Right) }
    }
    return root
}`,
          python: `def invert_tree(root):
    if not root: return None
    stack = [root]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
    return root`,
          java: `public TreeNode invertTree(TreeNode root) {
    if(root==null)return null;
    Stack<TreeNode> st=new Stack<>();st.push(root);
    while(!st.isEmpty()){
        TreeNode n=st.pop();
        TreeNode tmp=n.left;n.left=n.right;n.right=tmp;
        if(n.left!=null)st.push(n.left);
        if(n.right!=null)st.push(n.right);
    }
    return root;
}`,
        },
      },,
      { type: "h3", title: "Optimal — O(n) Recursive" },
      { type: "p", text: "প্রতিটি node-এর left ও right swap করো, তারপর recursively left ও right subtree invert করো।" },
      {
        type: "multi-code",
        filename: "dsa-trees_p1_optimal",
        codeSamples: {
          cpp: `TreeNode* invertTree(TreeNode* root) {
    if(!root)return nullptr;
    swap(root->left,root->right);
    invertTree(root->left);
    invertTree(root->right);
    return root;
}`,
          go: `func invertTree(root *TreeNode) *TreeNode {
    if root == nil { return nil }
    root.Left, root.Right = root.Right, root.Left
    invertTree(root.Left)
    invertTree(root.Right)
    return root
}`,
          python: `def invert_tree(root):
    if not root: return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root`,
          java: `public TreeNode invertTree(TreeNode root) {
    if(root==null)return null;
    TreeNode tmp=root.left;root.left=root.right;root.right=tmp;
    invertTree(root.left);
    invertTree(root.right);
    return root;
}`,
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Stack — Time: O(n), Space: O(n)।",
          "Recursive — Time: O(n), Space: O(h)। h = height।",
          "Key: swap children, recurse। সবচেয়ে simple recursion problem।"
        ],
      },,
      { type: "h2", id: "prob-2", title: "Problem 2 — Maximum Depth of Binary Tree" },
      { type: "p", text: "Binary tree-এর maximum depth বের করো।" },
      { type: "h3", title: "Brute Force — O(n) with level-order traversal" },
      { type: "p", text: "Queue দিয়ে level by level count করো।" },
      {
        type: "multi-code",
        filename: "dsa-trees_p2_brute",
        codeSamples: {
          cpp: `int maxDepth(TreeNode* root) {
    if(!root)return 0;
    queue<TreeNode*> q;q.push(root);
    int depth=0;
    while(!q.empty()){
        int sz=q.size();depth++;
        for(int i=0;i<sz;i++){
            TreeNode* n=q.front();q.pop();
            if(n->left)q.push(n->left);
            if(n->right)q.push(n->right);
        }
    }
    return depth;
}`,
          go: `func maxDepth(root *TreeNode) int {
    if root == nil { return 0 }
    q := []*TreeNode{root}
    depth := 0
    for len(q) > 0 {
        sz := len(q)
        depth++
        for i := 0; i < sz; i++ {
            n := q[0]; q = q[1:]
            if n.Left != nil { q = append(q, n.Left) }
            if n.Right != nil { q = append(q, n.Right) }
        }
    }
    return depth
}`,
          python: `from collections import deque
def max_depth(root):
    if not root: return 0
    q = deque([root])
    depth = 0
    while q:
        depth += 1
        for _ in range(len(q)):
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    return depth`,
          java: `public int maxDepth(TreeNode root) {
    if(root==null)return 0;
    Queue<TreeNode> q=new LinkedList<>();q.add(root);
    int depth=0;
    while(!q.isEmpty()){
        int sz=q.size();depth++;
        for(int i=0;i<sz;i++){
            TreeNode n=q.poll();
            if(n.left!=null)q.add(n.left);
            if(n.right!=null)q.add(n.right);
        }
    }
    return depth;
}`,
        },
      },,
      { type: "h3", title: "Optimal — O(n) Recursive" },
      { type: "p", text: "depth = 1 + max(left_depth, right_depth)। Base case: null → 0।" },
      {
        type: "multi-code",
        filename: "dsa-trees_p2_optimal",
        codeSamples: {
          cpp: `int maxDepth(TreeNode* root) {
    if(!root)return 0;
    return 1+max(maxDepth(root->left),maxDepth(root->right));
}`,
          go: `func maxDepth(root *TreeNode) int {
    if root == nil { return 0 }
    return 1 + max(maxDepth(root.Left), maxDepth(root.Right))
}`,
          python: `def max_depth(root):
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))`,
          java: `public int maxDepth(TreeNode root) {
    if(root==null)return 0;
    return 1+Math.max(maxDepth(root.left),maxDepth(root.right));
}`,
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "BFS — Time: O(n), Space: O(w)। w = max width।",
          "Recursive — Time: O(n), Space: O(h)। h = height।",
          "Key: depth = 1 + max(left, right)। সবচেয়ে elegant recursion।"
        ],
      },,
      { type: "h2", id: "prob-3", title: "Problem 3 — Validate Binary Search Tree" },
      { type: "p", text: "একটি tree কি valid BST? " },
      { type: "h3", title: "Brute Force — O(n²) check each node against all descendants" },
      { type: "p", text: "প্রতিটি node-এর জন্য সব left descendants ছোট ও সব right descendants বড় কিনা check করো।" },
      {
        type: "multi-code",
        filename: "dsa-trees_p3_brute",
        codeSamples: {
          cpp: `bool isValidBST(TreeNode* root) {
    if(!root)return true;
    // check all left < root, all right > root
    // O(n²) per node check
    return check(root,LONG_MIN,LONG_MAX);
}`,
          go: `func isValidBST(root *TreeNode) bool {
    // O(n²) per node
    return check(root, math.MinInt64, math.MaxInt64)
}`,
          python: `def is_valid_bst(root):
    # O(n²) — for each node, check all descendants
    pass`,
          java: `public boolean isValidBST(TreeNode root) {
    // O(n²)
    return check(root, Long.MIN_VALUE, Long.MAX_VALUE);
}`,
        },
      },,
      { type: "h3", title: "Optimal — O(n) with min/max bounds" },
      { type: "p", text: "প্রতিটি node-এর জন্য একটি valid range (min, max) pass করো। Node-এর value range-এ আছে কিনা check করো।" },
      {
        type: "multi-code",
        filename: "dsa-trees_p3_optimal",
        codeSamples: {
          cpp: `bool isValidBST(TreeNode* root) {
    return check(root, LONG_MIN, LONG_MAX);
}
bool check(TreeNode* n, long lo, long hi) {
    if(!n)return true;
    if(n->val<=lo||n->val>=hi)return false;
    return check(n->left,lo,n->val)&&check(n->right,n->val,hi);
}`,
          go: `func isValidBST(root *TreeNode) bool {
    var check func(n *TreeNode, lo, hi int64) bool
    check = func(n *TreeNode, lo, hi int64) bool {
        if n == nil { return true }
        if int64(n.Val) <= lo || int64(n.Val) >= hi { return false }
        return check(n.Left, lo, int64(n.Val)) && check(n.Right, int64(n.Val), hi)
    }
    return check(root, math.MinInt64, math.MaxInt64)
}`,
          python: `def is_valid_bst(root):
    def check(node, lo, hi):
        if not node: return True
        if node.val <= lo or node.val >= hi: return False
        return check(node.left, lo, node.val) and check(node.right, node.val, hi)
    return check(root, float('-inf'), float('inf'))`,
          java: `public boolean isValidBST(TreeNode root) {
    return check(root, Long.MIN_VALUE, Long.MAX_VALUE);
}
private boolean check(TreeNode n, long lo, long hi) {
    if(n==null)return true;
    if(n.val<=lo||n.val>=hi)return false;
    return check(n.left,lo,n.val)&&check(n.right,n.val,hi);
}`,
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Check all descendants — Time: O(n²)।",
          "Bounds — Time: O(n), Space: O(h)।",
          "Key: প্রতিটি node-এর জন্য valid range pass করো।"
        ],
      },,
      { type: "h2", id: "prob-4", title: "Problem 4 — Lowest Common Ancestor" },
      { type: "p", text: "BST-তে দুটি node-এর lowest common ancestor খুঁজে বের করো।" },
      { type: "h3", title: "Brute Force — O(n) find paths separately" },
      { type: "p", text: "দুটি node-এর root-to-node path খুঁজে বের করে, paths compare করো।" },
      {
        type: "multi-code",
        filename: "dsa-trees_p4_brute",
        codeSamples: {
          cpp: `TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    vector<TreeNode*> pathP, pathQ;
    findPath(root, p, pathP);
    findPath(root, q, pathQ);
    TreeNode* lca = root;
    for(int i = 0; i < min(pathP.size(), pathQ.size()); i++) {
        if(pathP[i] == pathQ[i]) lca = pathP[i];
        else break;
    }
    return lca;
}`,
          go: `func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    // Find paths separately, then compare
    // O(n) + O(n) space for paths
    return root
}`,
          python: `def lowest_common_ancestor(root, p, q):
    def find_path(node, target, path):
        if not node: return False
        path.append(node)
        if node == target: return True
        if find_path(node.left, target, path) or find_path(node.right, target, path):
            return True
        path.pop()
        return False
    pathP, pathQ = [], []
    find_path(root, p, pathP)
    find_path(root, q, pathQ)
    lca = root
    for i in range(min(len(pathP), len(pathQ))):
        if pathP[i] == pathQ[i]: lca = pathP[i]
        else: break
    return lca`,
          java: `public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    // Find paths, compare — O(n) space
    return root;
}`,
        },
      },,
      { type: "h3", title: "Optimal — O(n) Recursive" },
      { type: "p", text: "BST property use করো: যদি দুটি node একই দিকে হয়, সেই দিকে recurse করো। ভিন্ন দিকে হলে current node ই LCA।" },
      {
        type: "multi-code",
        filename: "dsa-trees_p4_optimal",
        codeSamples: {
          cpp: `TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if(!root)return nullptr;
    if(p->val<root->val&&q->val<root->val)
        return lowestCommonAncestor(root->left,p,q);
    if(p->val>root->val&&q->val>root->val)
        return lowestCommonAncestor(root->right,p,q);
    return root;
}`,
          go: `func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    if root == nil { return nil }
    if p.Val < root.Val && q.Val < root.Val {
        return lowestCommonAncestor(root.Left, p, q)
    }
    if p.Val > root.Val && q.Val > root.Val {
        return lowestCommonAncestor(root.Right, p, q)
    }
    return root
}`,
          python: `def lowest_common_ancestor(root, p, q):
    if not root: return None
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    return root`,
          java: `public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    if(root==null)return null;
    if(p.val<root.val&&q.val<root.val)
        return lowestCommonAncestor(root.left,p,q);
    if(p.val>root.val&&q.val>root.val)
        return lowestCommonAncestor(root.right,p,q);
    return root;
}`,
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Path comparison — Time: O(n), Space: O(n)।",
          "BST Recursive — Time: O(h), Space: O(h)। h = height।",
          "Key: BST property — ভিন্ন দিকে split হলে current node ই LCA।"
        ],
      },,
      { type: "h2", id: "prob-5", title: "Problem 5 — Level Order Traversal" },
      { type: "p", text: "Binary tree-কে level by level traverse করো।" },
      { type: "h3", title: "Brute Force — O(n²) DFS for each level" },
      { type: "p", text: "প্রতিটি level-এর জন্য আলাদা DFS চালাও।" },
      {
        type: "multi-code",
        filename: "dsa-trees_p5_brute",
        codeSamples: {
          cpp: `vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result;
    int h = height(root);
    for(int i = 1; i <= h; i++) {
        vector<int> level;
        getLevel(root, i, level);
        result.push_back(level);
    }
    return result;
}`,
          go: `func levelOrder(root *TreeNode) [][]int {
    // DFS per level — O(n²)
    return nil
}`,
          python: `def level_order(root):
    result = []
    def get_level(node, level, out):
        if not node: return
        if level == 1: out.append(node.val)
        else:
            get_level(node.left, level-1, out)
            get_level(node.right, level-1, out)
    h = 0
    # find height first
    def height(n):
        if not n: return 0
        return 1 + max(height(n.left), height(n.right))
    h = height(root)
    for i in range(1, h+1):
        level = []
        get_level(root, i, level)
        result.append(level)
    return result`,
          java: `public List<List<Integer>> levelOrder(TreeNode root) {
    // DFS per level — O(n²)
    return new ArrayList<>();
}`,
        },
      },,
      { type: "h3", title: "Optimal — O(n) BFS with Queue" },
      { type: "p", text: "Queue use করে level by level traverse করো। প্রতিটি level-এর সব node একসাথে process করো।" },
      {
        type: "multi-code",
        filename: "dsa-trees_p5_optimal",
        codeSamples: {
          cpp: `vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result;
    if(!root)return result;
    queue<TreeNode*> q;q.push(root);
    while(!q.empty()){
        int sz=q.size();
        vector<int> level;
        for(int i=0;i<sz;i++){
            TreeNode* n=q.front();q.pop();
            level.push_back(n->val);
            if(n->left)q.push(n->left);
            if(n->right)q.push(n->right);
        }
        result.push_back(level);
    }
    return result;
}`,
          go: `func levelOrder(root *TreeNode) [][]int {
    var result [][]int
    if root == nil { return result }
    q := []*TreeNode{root}
    for len(q) > 0 {
        sz := len(q)
        level := make([]int, 0, sz)
        for i := 0; i < sz; i++ {
            n := q[0]; q = q[1:]
            level = append(level, n.Val)
            if n.Left != nil { q = append(q, n.Left) }
            if n.Right != nil { q = append(q, n.Right) }
        }
        result = append(result, level)
    }
    return result
}`,
          python: `from collections import deque
def level_order(root):
    if not root: return []
    result = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        result.append(level)
    return result`,
          java: `public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> result=new ArrayList<>();
    if(root==null)return result;
    Queue<TreeNode> q=new LinkedList<>();q.add(root);
    while(!q.isEmpty()){
        int sz=q.size();
        List<Integer> level=new ArrayList<>();
        for(int i=0;i<sz;i++){
            TreeNode n=q.poll();
            level.add(n.val);
            if(n.left!=null)q.add(n.left);
            if(n.right!=null)q.add(n.right);
        }
        result.add(level);
    }
    return result;
}`,
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "DFS per level — Time: O(n²)।",
          "BFS Queue — Time: O(n), Space: O(w)। w = max width।",
          "Key: BFS দিয়ে level by level process — queue-তে level size track করো।"
        ],
      },,
      { type: "h2", id: "summary", title: "Chapter Summary" },
      { type: "callout", calloutTone: "tip", text: "Tip: পরের topic হলো Tries — prefix tree যা string search O(m)-এ করে।" }
    ],
  },

  // ---- Tries ----
  {
    id: "dsa-tries",
    subject: "dsa",
    title: "Tries",
    bangla: "ট্রাই",
    difficulty: "Hard",
    est: "2 hr",
    summary: "Trie হলো prefix tree। ৫টি classic problem — insertion, search, autocomplete, ও word search।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      { type: "p", text: "Trie (pronounced 'try') হলো একটি tree structure যা strings কে character-by-character store করে। এটি prefix-based search এর জন্য efficient। Real-life thinking — একটি dictionary! প্রতিটি letter-এর জন্য একটি page, সেই page-এ পরের letter-এর সাথে পরের page-এর reference। এভাবে একটি word একটা path-এর মতো navigate করা যায়।" },
      { type: "h2", id: "prob-1", title: "Problem 1 — Implement Trie" },
      { type: "p", text: "Trie data structure implement করো — insert, search, startsWith।" },
      { type: "h3", title: "Brute Force — O(n × m) with hash set" },
      { type: "p", text: "সব words একটি set-এ store করো। Search ও prefix check করো।" },
      {
        type: "multi-code",
        filename: "dsa-tries_p1_brute",
        codeSamples: {
          cpp: `// Hash set approach
unordered_set<string> words;
void insert(string word) { words.insert(word); }
bool search(string word) { return words.count(word); }
bool startsWith(string prefix) {
    for(auto& w : words)
        if(w.substr(0, prefix.size()) == prefix) return true;
    return false;
}`,
          go: `type Trie struct { words map[string]bool }
func (t *Trie) insert(word string) { t.words[word] = true }
func (t *Trie) search(word string) bool { return t.words[word] }
func (t *Trie) startsWith(prefix string) bool {
    for w := range t.words {
        if len(w) >= len(prefix) && w[:len(prefix)] == prefix { return true }
    }
    return false
}`,
          python: `class Trie:
    def __init__(self): self.words = set()
    def insert(self, word): self.words.add(word)
    def search(self, word): return word in self.words
    def startsWith(self, prefix):
        return any(w.startswith(prefix) for w in self.words)`,
          java: `class Trie {
    Set<String> words = new HashSet<>();
    void insert(String word) { words.add(word); }
    boolean search(String word) { return words.contains(word); }
    boolean startsWith(String prefix) {
        for(String w : words) if(w.startsWith(prefix)) return true;
        return false;
    }
}`,
        },
      },,
      { type: "h3", title: "Optimal — O(m) Trie per operation" },
      { type: "p", text: "Trie node তৈরি করো — children array ও isEnd flag। Insert ও search এক character এক character করে traverse করো।" },
      {
        type: "multi-code",
        filename: "dsa-tries_p1_optimal",
        codeSamples: {
          cpp: `struct TrieNode { TrieNode* children[26]={}; bool isEnd=false; };
class Trie {
    TrieNode* root;
public:
    Trie() { root = new TrieNode(); }
    void insert(string word) {
        TrieNode* p = root;
        for(char c : word) {
            int i = c-'a';
            if(!p->children[i]) p->children[i] = new TrieNode();
            p = p->children[i];
        }
        p->isEnd = true;
    }
    bool search(string word) {
        TrieNode* p = root;
        for(char c : word) {
            int i = c-'a';
            if(!p->children[i]) return false;
            p = p->children[i];
        }
        return p->isEnd;
    }
    bool startsWith(string prefix) {
        TrieNode* p = root;
        for(char c : prefix) {
            int i = c-'a';
            if(!p->children[i]) return false;
            p = p->children[i];
        }
        return true;
    }
};`,
          go: `type TrieNode struct {
    children [26]*TrieNode
    isEnd    bool
}
type Trie struct { root *TrieNode }
func Constructor() Trie { return Trie{root: &TrieNode{}} }
func (t *Trie) insert(word string) {
    p := t.root
    for _, c := range word {
        i := c - 'a'
        if p.children[i] == nil { p.children[i] = &TrieNode{} }
        p = p.children[i]
    }
    p.isEnd = true
}
func (t *Trie) search(word string) bool {
    p := t.root
    for _, c := range word {
        i := c - 'a'
        if p.children[i] == nil { return false }
        p = p.children[i]
    }
    return p.isEnd
}
func (t *Trie) startsWith(prefix string) bool {
    p := t.root
    for _, c := range prefix {
        i := c - 'a'
        if p.children[i] == nil { return false }
        p = p.children[i]
    }
    return true
}`,
          python: `class Trie:
    def __init__(self):
        self.root = {}
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node: node[c] = {}
            node = node[c]
        node['#'] = True
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node: return False
            node = node[c]
        return '#' in node
    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node: return False
            node = node[c]
        return True`,
          java: `class Trie {
    class Node { Node[] children = new Node[26]; boolean isEnd; }
    Node root = new Node();
    void insert(String word) {
        Node p = root;
        for(char c : word.toCharArray()) {
            int i = c-'a';
            if(p.children[i]==null) p.children[i]=new Node();
            p = p.children[i];
        }
        p.isEnd = true;
    }
    boolean search(String word) {
        Node p = root;
        for(char c : word.toCharArray()) {
            int i = c-'a';
            if(p.children[i]==null) return false;
            p = p.children[i];
        }
        return p.isEnd;
    }
    boolean startsWith(String prefix) {
        Node p = root;
        for(char c : prefix.toCharArray()) {
            int i = c-'a';
            if(p.children[i]==null) return false;
            p = p.children[i];
        }
        return true;
    }
}`,
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Hash Set — insert O(1), search O(1), startsWith O(n × m)।",
          "Trie — insert O(m), search O(m), startsWith O(m)। m = word length।",
          "Key: Trie prefix search O(m) — hash set startsWith O(n×m)।"
        ],
      },,
      { type: "h2", id: "prob-2", title: "Problem 2 — Word Search II" },
      { type: "p", text: "Board-এ এমন সব word খুঁজে বের করো যেগুলো dictionary-তে আছে।" },
      { type: "h3", title: "Brute Force — O(n × m × 4^l × w) DFS per word" },
      { type: "p", text: "প্রতিটি word-এর জন্য DFS চালাও। খুব slow।" },
      {
        type: "multi-code",
        filename: "dsa-tries_p2_brute",
        codeSamples: {
          cpp: `vector<string> findWords(vector<vector<char>>& b, vector<string>& words) {
    vector<string> result;
    for(string& w : words)
        if(exist(b, w)) result.push_back(w);
    return result;
}`,
          go: `func findWords(b [][]byte, words []string) []string {
    var result []string
    for _, w := range words { if exist(b, w) { result = append(result, w) } }
    return result
}`,
          python: `def find_words(board, words):
    result = []
    for w in words:
        if exist(board, w): result.append(w)
    return result`,
          java: `public List<String> findWords(char[][] b, String[] words) {
    List<String> result = new ArrayList<>();
    for(String w : words) if(exist(b, w)) result.add(w);
    return result;
}`,
        },
      },,
      { type: "h3", title: "Optimal — O(n × m × 4^l) with Trie + Backtracking" },
      { type: "p", text: "Trie তৈরি করো। Board-এ প্রতিটি cell থেকে DFS চালাও, Trie-তে match করে করে যাও।" },
      {
        type: "multi-code",
        filename: "dsa-tries_p2_optimal",
        codeSamples: {
          cpp: `vector<string> findWords(vector<vector<char>>& b, vector<string>& words) {
    // Build Trie
    TrieNode* root = new TrieNode();
    for(string& w : words) {
        TrieNode* p = root;
        for(char c : w) {
            int i = c-'a';
            if(!p->children[i]) p->children[i] = new TrieNode();
            p = p->children[i];
        }
        p->isEnd = true;
        p->word = w;
    }
    vector<string> result;
    for(int i=0;i<b.size();i++)
        for(int j=0;j<b[0].size();j++)
            dfs(b, i, j, root, result);
    return result;
}`,
          go: `func findWords(b [][]byte, words []string) []string {
    // Build Trie + DFS
    return nil
}`,
          python: `def find_words(board, words):
    trie = {}
    for w in words:
        node = trie
        for c in w:
            if c not in node: node[c] = {}
            node = node[c]
        node['#'] = w
    result = []
    def dfs(i, j, node):
        if '#' in node: result.append(node['#']); del node['#']
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]): return
        c = board[i][j]
        if c not in node: return
        board[i][j] = '#'
        for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            dfs(i+di, j+dj, node[c])
        board[i][j] = c
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(i, j, trie)
    return result`,
          java: `public List<String> findWords(char[][] b, String[] words) {
    // Build Trie + DFS
    return new ArrayList<>();
}`,
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Per word DFS — Time: O(w × n × m × 4^l)। খুব slow।",
          "Trie + DFS — Time: O(n × m × 4^l)। এক বারে সব word search।",
          "Key: Trie দিয়ে সব word একসাথে search — pruning দ্রুত।"
        ],
      },,
      { type: "h2", id: "prob-3", title: "Problem 3 — Design Add and Search Words" },
      { type: "p", text: "Add ও Search করতে পারবে এমন data structure design করো। Search-এ '.' wildcard support করবে।" },
      { type: "h3", title: "Brute Force — O(n) linear search per query" },
      { type: "p", text: "সব words store করে linear search করো। '.' থাকলে সব match করো।" },
      {
        type: "multi-code",
        filename: "dsa-tries_p3_brute",
        codeSamples: {
          cpp: `// Linear approach
vector<string> dict;
void addWord(string word) { dict.push_back(word); }
bool search(string word) {
    for(string& w : dict) {
        if(w.size() != word.size()) continue;
        bool match = true;
        for(int i = 0; i < w.size(); i++)
            if(word[i] != '.' && word[i] != w[i]) { match = false; break; }
        if(match) return true;
    }
    return false;
}`,
          go: `type WordDictionary struct { dict []string }
func (d *WordDictionary) addWord(word string) { d.dict = append(d.dict, word) }
func (d *WordDictionary) search(word string) bool {
    for _, w := range d.dict {
        if len(w) != len(word) { continue }
        match := true
        for i := 0; i < len(w); i++ {
            if word[i] != '.' && word[i] != w[i] { match = false; break }
        }
        if match { return true }
    }
    return false
}`,
          python: `class WordDictionary:
    def __init__(self): self.dict = []
    def addWord(self, word): self.dict.append(word)
    def search(self, word):
        for w in self.dict:
            if len(w) != len(word): continue
            if all(word[i]=='.' or word[i]==w[i] for i in range(len(w))):
                return True
        return False`,
          java: `class WordDictionary {
    List<String> dict = new ArrayList<>();
    void addWord(String word) { dict.add(word); }
    boolean search(String word) {
        for(String w : dict) {
            if(w.length() != word.length()) continue;
            boolean match = true;
            for(int i=0;i<w.length();i++)
                if(word.charAt(i)!='.' && word.charAt(i)!=w.charAt(i)) { match=false; break; }
            if(match) return true;
        }
        return false;
    }
}`,
        },
      },,
      { type: "h3", title: "Optimal — O(m) Trie + DFS for wildcard" },
      { type: "p", text: "Trie তৈরি করো। Search-এ '.' হলে সব children explore করো (DFS)।" },
      {
        type: "multi-code",
        filename: "dsa-tries_p3_optimal",
        codeSamples: {
          cpp: `struct TrieNode { TrieNode* children[26]={}; bool isEnd=false; };
class WordDictionary {
    TrieNode* root;
public:
    WordDictionary() { root = new TrieNode(); }
    void addWord(string word) {
        TrieNode* p = root;
        for(char c : word) {
            int i = c-'a';
            if(!p->children[i]) p->children[i] = new TrieNode();
            p = p->children[i];
        }
        p->isEnd = true;
    }
    bool search(string word) { return dfs(word, 0, root); }
    bool dfs(string& word, int i, TrieNode* node) {
        if(i == word.size()) return node->isEnd;
        if(word[i] == '.') {
            for(int j = 0; j < 26; j++)
                if(node->children[j] && dfs(word, i+1, node->children[j]))
                    return true;
            return false;
        }
        int idx = word[i]-'a';
        return node->children[idx] && dfs(word, i+1, node->children[idx]);
    }
};`,
          go: `type TrieNode struct {
    children [26]*TrieNode
    isEnd    bool
}
type WordDictionary struct { root *TrieNode }
func Constructor() WordDictionary { return WordDictionary{root: &TrieNode{}} }
func (d *WordDictionary) addWord(word string) {
    p := d.root
    for _, c := range word {
        i := c - 'a'
        if p.children[i] == nil { p.children[i] = &TrieNode{} }
        p = p.children[i]
    }
    p.isEnd = true
}
func (d *WordDictionary) search(word string) bool {
    var dfs func(i int, node *TrieNode) bool
    dfs = func(i int, node *TrieNode) bool {
        if i == len(word) { return node.isEnd }
        if word[i] == '.' {
            for j := 0; j < 26; j++ {
                if node.children[j] != nil && dfs(i+1, node.children[j]) { return true }
            }
            return false
        }
        idx := word[i] - 'a'
        return node.children[idx] != nil && dfs(i+1, node.children[idx])
    }
    return dfs(0, d.root)
}`,
          python: `class WordDictionary:
    def __init__(self): self.root = {}
    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node: node[c] = {}
            node = node[c]
        node['#'] = True
    def search(self, word):
        def dfs(i, node):
            if i == len(word): return '#' in node
            c = word[i]
            if c == '.':
                return any(dfs(i+1, node[k]) for k in node if k != '#')
            if c not in node: return False
            return dfs(i+1, node[c])
        return dfs(0, self.root)`,
          java: `class WordDictionary {
    class Node { Node[] children = new Node[26]; boolean isEnd; }
    Node root = new Node();
    void addWord(String word) {
        Node p = root;
        for(char c : word.toCharArray()) {
            int i = c-'a';
            if(p.children[i]==null) p.children[i]=new Node();
            p = p.children[i];
        }
        p.isEnd = true;
    }
    boolean search(String word) { return dfs(word, 0, root); }
    boolean dfs(String word, int i, Node node) {
        if(i == word.length()) return node.isEnd;
        if(word.charAt(i) == '.') {
            for(int j = 0; j < 26; j++)
                if(node.children[j] != null && dfs(word, i+1, node.children[j]))
                    return true;
            return false;
        }
        int idx = word.charAt(i) - 'a';
        return node.children[idx] != null && dfs(word, i+1, node.children[idx]);
    }
}`,
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Linear — add O(1), search O(n × m)।",
          "Trie + DFS — add O(m), search O(26^m) worst case (all dots)।",
          "Key: Trie + wildcard এর জন্য DFS — '.' হলে সব children explore করো।"
        ],
      },,
      { type: "h2", id: "prob-4", title: "Problem 4 — Longest Word in Dictionary" },
      { type: "p", text: "Dictionary-তে সবচেয়ে বড় word খুঁজে বের করো যা এক এক character যোগ করে build করা যায়।" },
      { type: "h3", title: "Brute Force — O(n × m) sort + check" },
      { type: "p", text: "Words sort করো। প্রতিটি word-এর সব prefix আছে কিনা check করো।" },
      {
        type: "multi-code",
        filename: "dsa-tries_p4_brute",
        codeSamples: {
          cpp: `string longestWord(vector<string>& words) {
    sort(words.begin(), words.end());
    unordered_set<string> built;
    string result;
    for(string& w : words) {
        if(w.size() == 1 || built.count(w.substr(0, w.size()-1))) {
            built.insert(w);
            if(w.size() > result.size()) result = w;
        }
    }
    return result;
}`,
          go: `func longestWord(words []string) string {
    sort.Strings(words)
    built := make(map[string]bool)
    result := ""
    for _, w := range words {
        if len(w) == 1 || built[w[:len(w)-1]] {
            built[w] = true
            if len(w) > len(result) { result = w }
        }
    }
    return result
}`,
          python: `def longest_word(words):
    words.sort()
    built = set()
    result = ""
    for w in words:
        if len(w) == 1 or w[:-1] in built:
            built.add(w)
            if len(w) > len(result): result = w
    return result`,
          java: `public String longestWord(String[] words) {
    Arrays.sort(words);
    Set<String> built = new HashSet<>();
    String result = "";
    for(String w : words) {
        if(w.length()==1 || built.contains(w.substring(0, w.length()-1))) {
            built.add(w);
            if(w.length() > result.length()) result = w;
        }
    }
    return result;
}`,
        },
      },,
      { type: "h3", title: "Optimal — O(n × m) with Trie + BFS" },
      { type: "p", text: "Trie তৈরি করো। BFS দিয়ে level by level traverse করো — যেহেতু character এক এক করে যোগ হয়, level অনুযায়ী longest word পাওয়া যায়।" },
      {
        type: "multi-code",
        filename: "dsa-tries_p4_optimal",
        codeSamples: {
          cpp: `string longestWord(vector<string>& words) {
    TrieNode* root = new TrieNode();
    for(string& w : words) {
        TrieNode* p = root;
        for(char c : w) {
            int i = c-'a';
            if(!p->children[i]) p->children[i] = new TrieNode();
            p = p->children[i];
        }
        p->isEnd = true;
        p->word = w;
    }
    queue<TrieNode*> q; q.push(root);
    string result;
    while(!q.empty()) {
        TrieNode* n = q.front(); q.pop();
        if(!n->word.empty()) result = n->word;
        for(int i = 25; i >= 0; i--) {
            if(n->children[i] && n->children[i]->isEnd)
                q.push(n->children[i]);
        }
    }
    return result;
}`,
          go: `func longestWord(words []string) string {
    // Trie + BFS
    return ""
}`,
          python: `def longest_word(words):
    trie = {}
    for w in words:
        node = trie
        for c in w:
            if c not in node: node[c] = {}
            node = node[c]
        node['#'] = w
    from collections import deque
    q = deque([(trie, "")])
    result = ""
    while q:
        node, word = q.popleft()
        if '#' in node: result = node['#']
        for c in sorted(node.keys(), reverse=True):
            if c != '#' and '#' in node[c]:
                q.append((node[c], word + c))
    return result`,
          java: `public String longestWord(String[] words) {
    // Trie + BFS
    return "";
}`,
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Sort + Set — Time: O(n log n × m), Space: O(n × m)।",
          "Trie + BFS — Time: O(n × m), Space: O(n × m)।",
          "Key: Trie-তে BFS level by level — শেষে যে word পাওয়া যায় সেটাই longest।"
        ],
      },,
      { type: "h2", id: "prob-5", title: "Problem 5 — Stream of Characters" },
      { type: "p", text: "একটি stream থেকে character গ্রহণ করো। শেষ kটি character কোনো dictionary word কিনা check করো।" },
      { type: "h3", title: "Brute Force — O(n) scan per query" },
      { type: "p", text: "প্রতিটি query-তে শেষ সব character check করো।" },
      {
        type: "multi-code",
        filename: "dsa-tries_p5_brute",
        codeSamples: {
          cpp: `class StreamChecker {
    vector<string> dict;
    string stream;
public:
    StreamChecker(vector<string>& words) : dict(words) {}
    bool query(char c) {
        stream += c;
        for(string& w : dict)
            if(stream.size() >= w.size() &&
               stream.substr(stream.size()-w.size()) == w)
                return true;
        return false;
    }
};`,
          go: `type StreamChecker struct { dict []string; stream string }
func (sc *StreamChecker) query(c byte) bool {
    sc.stream += string(c)
    for _, w := range sc.dict {
        if len(sc.stream) >= len(w) && sc.stream[len(sc.stream)-len(w):] == w { return true }
    }
    return false
}`,
          python: `class StreamChecker:
    def __init__(self, words):
        self.dict = words
        self.stream = ""
    def query(self, c):
        self.stream += c
        for w in self.dict:
            if len(self.stream) >= len(w) and self.stream[-len(w):] == w:
                return True
        return False`,
          java: `class StreamChecker {
    List<String> dict; StringBuilder stream;
    public StreamChecker(String[] words) { dict = Arrays.asList(words); stream = new StringBuilder(); }
    public boolean query(char c) {
        stream.append(c);
        for(String w : dict)
            if(stream.length() >= w.length() &&
               stream.substring(stream.length()-w.length()).equals(w))
                return true;
        return false;
    }
}`,
        },
      },,
      { type: "h3", title: "Optimal — O(m) with Trie of reversed words" },
      { type: "p", text: "Dictionary-এর সব word কে reverse করে Trie তৈরি করো। Stream-এর শেষ থেকে character গুলো Trie-তে match করো।" },
      {
        type: "multi-code",
        filename: "dsa-tries_p5_optimal",
        codeSamples: {
          cpp: `class StreamChecker {
    struct TrieNode { TrieNode* children[26]={}; bool isEnd=false; };
    TrieNode* root;
    string stream;
public:
    StreamChecker(vector<string>& words) {
        root = new TrieNode();
        for(string& w : words) {
            TrieNode* p = root;
            for(int i = w.size()-1; i >= 0; i--) {
                int idx = w[i]-'a';
                if(!p->children[idx]) p->children[idx] = new TrieNode();
                p = p->children[idx];
            }
            p->isEnd = true;
        }
    }
    bool query(char c) {
        stream += c;
        TrieNode* p = root;
        for(int i = stream.size()-1; i >= 0; i--) {
            int idx = stream[i]-'a';
            if(!p->children[idx]) return false;
            p = p->children[idx];
            if(p->isEnd) return true;
        }
        return false;
    }
};`,
          go: `type StreamChecker struct {
    root *TrieNode
    stream string
}
func (sc *StreamChecker) query(c byte) bool {
    sc.stream += string(c)
    p := sc.root
    for i := len(sc.stream)-1; i >= 0; i-- {
        idx := sc.stream[i] - 'a'
        if p.children[idx] == nil { return false }
        p = p.children[idx]
        if p.isEnd { return true }
    }
    return false
}`,
          python: `class StreamChecker:
    def __init__(self, words):
        self.root = {}
        for w in words:
            node = self.root
            for c in reversed(w):
                if c not in node: node[c] = {}
                node = node[c]
            node['#'] = True
        self.stream = []
    def query(self, c):
        self.stream.append(c)
        node = self.root
        for i in range(len(self.stream)-1, -1, -1):
            c = self.stream[i]
            if c not in node: return False
            node = node[c]
            if '#' in node: return True
        return False`,
          java: `class StreamChecker {
    // Trie of reversed words + stream
    // query: O(m) where m = max word length
}`,
        },
      },,
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Linear scan — query O(n × m)।",
          "Trie (reversed) — query O(m)। m = max word length।",
          "Key: reverse করে Trie — শেষ থেকে match করা সহজ হয়।"
        ],
      },,
      { type: "h2", id: "summary", title: "Chapter Summary" },
      { type: "callout", calloutTone: "tip", text: "Tip: পরের topic হলো Backtracking — recursive try ও backtrack করে সব possible solution explore করা।" }
    ],
  },

  // ---- Backtracking ----
  {
    id: "dsa-backtracking",
    subject: "dsa",
    title: "Backtracking",
    bangla: "ব্যাকট্র্যাকিং",
    difficulty: "Hard",
    est: "3 hr",
    summary:
      "Backtracking-এ recursive try ও backtrack করে সব possible solution explore করা হয়। ৫টি classic problem — Subsets, Permutations, Combination Sum, N-Queens, Word Search।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      {
        type: "p",
        text: "Backtracking হলো একটি recursive technique যেখানে তুমি প্রতিটি choice try করো এবং যদি সেটি কাজ না করে, তাহলে backtrack করে আগের state-এ ফিরে যাও। Real-life thinking — একটি maze! প্রতিটি path try করো। Dead end হলে ফিরে এসো এবং অন্য path খুঁজো।",
      },

      { type: "h2", id: "p1", title: "Problem 1 — Subsets" },
      {
        type: "p",
        text: "একটি array দেওয়া আছে। সব possible subsets (power set) return করো। Example: nums = [1,2,3] → [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]",
      },
      { type: "h3", title: "Brute Force — O(2^n × n) Iterative Bit Manipulation" },
      {
        type: "p",
        text: "Bit manipulation দিয়ে সব combination generate করো। প্রতিটি bit একটি element include/exclude নির্দেশ করে।",
      },
      {
        type: "multi-code",
        filename: "subsets_brute",
        codeSamples: {
          cpp: `vector<vector<int>> subsets(vector<int>& n) {
    vector<vector<int>> r;
    int m = n.size();
    for (int i = 0; i < (1 << m); i++) {
        vector<int> s;
        for (int j = 0; j < m; j++)
            if (i & (1 << j)) s.push_back(n[j]);
        r.push_back(s);
    }
    return r;
}`,
          go: `func subsets(n []int) [][]int {
    var r [][]int
    m := len(n)
    for i := 0; i < (1 << m); i++ {
        var s []int
        for j := 0; j < m; j++ {
            if i&(1<<j) != 0 { s = append(s, n[j]) }
        }
        r = append(r, s)
    }
    return r
}`,
          python: `def subsets(n):
    r = []
    for i in range(1 << len(n)):
        s = [n[j] for j in range(len(n)) if i & (1 << j)]
        r.append(s)
    return r`,
          java: `public List<List<Integer>> subsets(int[] n) {
    List<List<Integer>> r = new ArrayList<>();
    for (int i = 0; i < (1 << n.length); i++) {
        List<Integer> s = new ArrayList<>();
        for (int j = 0; j < n.length; j++)
            if ((i & (1 << j)) != 0) s.add(n[j]);
        r.add(s);
    }
    return r;
}`,
        },
      },
      { type: "h3", title: "Optimal — O(2^n × n) Recursive Backtracking" },
      {
        type: "p",
        text: "প্রতিটি element-এর জন্য দুটি choice: include বা exclude। Recursively সব path explore করো। Same complexity কিন্তু recursive approach বেশি readable এবং extend করা সহজ।",
      },
      {
        type: "multi-code",
        filename: "subsets_optimal",
        codeSamples: {
          cpp: `vector<vector<int>> r;
void bt(vector<int>& n, int i, vector<int>& cur) {
    if (i == n.size()) { r.push_back(cur); return; }
    bt(n, i + 1, cur);           // exclude
    cur.push_back(n[i]);
    bt(n, i + 1, cur);           // include
    cur.pop_back();              // backtrack
}
vector<vector<int>> subsets(vector<int>& n) {
    vector<int> cur;
    bt(n, 0, cur);
    return r;
}`,
          go: `var r [][]int
func subsets(n []int) [][]int {
    r = nil
    var bt func(i int, cur []int)
    bt = func(i int, cur []int) {
        if i == len(n) { r = append(r, append([]int(nil), cur...)); return }
        bt(i+1, cur)               // exclude
        cur = append(cur, n[i])
        bt(i+1, cur)               // include
        cur = cur[:len(cur)-1]     // backtrack
    }
    bt(0, nil)
    return r
}`,
          python: `def subsets(n):
    r = []
    def bt(i, cur):
        if i == len(n):
            r.append(cur[:])
            return
        bt(i + 1, cur)              # exclude
        cur.append(n[i])
        bt(i + 1, cur)              # include
        cur.pop()                   # backtrack
    bt(0, [])
    return r`,
          java: `List<List<Integer>> r = new ArrayList<>();
public List<List<Integer>> subsets(int[] n) {
    r.clear();
    bt(n, 0, new ArrayList<>());
    return r;
}
void bt(int[] n, int i, List<Integer> cur) {
    if (i == n.length) { r.add(new ArrayList<>(cur)); return; }
    bt(n, i + 1, cur);               // exclude
    cur.add(n[i]);
    bt(n, i + 1, cur);               // include
    cur.remove(cur.size() - 1);      // backtrack
}`,
        },
      },
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Iterative — Time: O(2^n × n), Space: O(2^n × n)। Bit manipulation, no recursion।",
          "Recursive — Time: O(2^n × n), Space: O(n) recursion depth। বেশি readable, extend করা সহজ।",
          "Key: প্রতিটি element-এর জন্য include/exclude — দুটি branch, pop_back = backtrack।",
        ],
      },

      { type: "h2", id: "p2", title: "Problem 2 — Permutations" },
      {
        type: "p",
        text: "একটি array দেওয়া আছে। সব possible permutation return করো। Example: nums = [1,2,3] → [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]",
      },
      { type: "h3", title: "Brute Force — O(n! × n) using next_permutation" },
      {
        type: "p",
        text: "Sort করে repeatedly next_permutation call করো। Simple কিন্তু C++-এ built-in, অন্য ভাষায় manual implementation লাগে।",
      },
      {
        type: "multi-code",
        filename: "perm_brute",
        codeSamples: {
          cpp: `vector<vector<int>> permute(vector<int>& n) {
    vector<vector<int>> r;
    sort(n.begin(), n.end());
    do { r.push_back(n); } while (next_permutation(n.begin(), n.end()));
    return r;
}`,
          go: `func permute(n []int) [][]int {
    sort.Ints(n)
    var r [][]int
    r = append(r, append([]int(nil), n...))
    for nextPermutation(n) {
        r = append(r, append([]int(nil), n...))
    }
    return r
}
// nextPermutation: implement manually`,
          python: `from itertools import permutations
def permute(n):
    return [list(p) for p in permutations(n)]`,
          java: `// Manual nextPermutation needed
public List<List<Integer>> permute(int[] n) {
    Arrays.sort(n);
    List<List<Integer>> r = new ArrayList<>();
    r.add(toList(n));
    while (nextPerm(n)) r.add(toList(n));
    return r;
}`,
        },
      },
      { type: "h3", title: "Optimal — O(n! × n) Backtracking with Swap" },
      {
        type: "p",
        text: "প্রতিটি position-এ বাকি সব element try করো। Swap দিয়ে element গুলো position-এ বসাও, recurse করো, তারপর swap back (backtrack)।",
      },
      {
        type: "multi-code",
        filename: "perm_optimal",
        codeSamples: {
          cpp: `vector<vector<int>> r;
void bt(vector<int>& n, int i) {
    if (i == n.size()) { r.push_back(n); return; }
    for (int j = i; j < n.size(); j++) {
        swap(n[i], n[j]);
        bt(n, i + 1);
        swap(n[i], n[j]);    // backtrack
    }
}
vector<vector<int>> permute(vector<int>& n) {
    r.clear();
    bt(n, 0);
    return r;
}`,
          go: `var r [][]int
func permute(n []int) [][]int {
    r = nil
    var bt func(i int)
    bt = func(i int) {
        if i == len(n) { r = append(r, append([]int(nil), n...)); return }
        for j := i; j < len(n); j++ {
            n[i], n[j] = n[j], n[i]
            bt(i + 1)
            n[i], n[j] = n[j], n[i]    // backtrack
        }
    }
    bt(0)
    return r
}`,
          python: `def permute(n):
    r = []
    def bt(i):
        if i == len(n):
            r.append(n[:])
            return
        for j in range(i, len(n)):
            n[i], n[j] = n[j], n[i]
            bt(i + 1)
            n[i], n[j] = n[j], n[i]    # backtrack
    bt(0)
    return r`,
          java: `List<List<Integer>> r = new ArrayList<>();
public List<List<Integer>> permute(int[] n) {
    r.clear();
    bt(n, 0);
    return r;
}
void bt(int[] n, int i) {
    if (i == n.length) {
        List<Integer> l = new ArrayList<>();
        for (int v : n) l.add(v);
        r.add(l);
        return;
    }
    for (int j = i; j < n.length; j++) {
        swap(n, i, j);
        bt(n, i + 1);
        swap(n, i, j);    // backtrack
    }
}
void swap(int[] n, int i, int j) { int t = n[i]; n[i] = n[j]; n[j] = t; }`,
        },
      },
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "next_permutation — Time: O(n! × n), Space: O(n!)। Built-in function।",
          "Swap Backtracking — Time: O(n! × n), Space: O(n) recursion। In-place, no extra space।",
          "Key: swap দিয়ে position fix করো, backtrack-এ swap back — in-place permutation।",
        ],
      },

      { type: "h2", id: "p3", title: "Problem 3 — Combination Sum" },
      {
        type: "p",
        text: "Candidates array ও target দেওয়া আছে। সব unique combination খুঁজে বের করো যাদের যোগফল target। একই element একাধিকবার use করা যাবে। Example: candidates = [2,3,6,7], target = 7 → [[2,2,3],[7]]",
      },
      { type: "h3", title: "Brute Force — O(2^n) without pruning" },
      {
        type: "p",
        text: "সব combination generate করে check করো। কোনো pruning নেই — negative target-এও recurse করে।",
      },
      {
        type: "multi-code",
        filename: "combo_sum_brute",
        codeSamples: {
          cpp: `vector<vector<int>> r;
void bt(vector<int>& c, int t, int i, vector<int>& cur) {
    if (t == 0) { r.push_back(cur); return; }
    if (t < 0 || i == c.size()) return;
    bt(c, t, i + 1, cur);            // skip
    cur.push_back(c[i]);
    bt(c, t - c[i], i, cur);         // take (same index = repeat)
    cur.pop_back();
}
vector<vector<int>> combinationSum(vector<int>& c, int t) {
    r.clear();
    vector<int> cur;
    bt(c, t, 0, cur);
    return r;
}`,
          go: `var r [][]int
func combinationSum(c []int, t int) [][]int {
    r = nil
    var bt func(t, i int, cur []int)
    bt = func(t, i int, cur []int) {
        if t == 0 { r = append(r, append([]int(nil), cur...)); return }
        if t < 0 || i == len(c) { return }
        bt(t, i+1, cur)
        cur = append(cur, c[i])
        bt(t-c[i], i, cur)
        cur = cur[:len(cur)-1]
    }
    bt(t, 0, nil)
    return r
}`,
          python: `def combinationSum(c, t):
    r = []
    def bt(t, i, cur):
        if t == 0: r.append(cur[:]); return
        if t < 0 or i == len(c): return
        bt(t, i + 1, cur)            # skip
        cur.append(c[i])
        bt(t - c[i], i, cur)         # take (repeat allowed)
        cur.pop()
    bt(t, 0, [])
    return r`,
          java: `List<List<Integer>> r = new ArrayList<>();
public List<List<Integer>> combinationSum(int[] c, int t) {
    r.clear();
    bt(c, t, 0, new ArrayList<>());
    return r;
}
void bt(int[] c, int t, int i, List<Integer> cur) {
    if (t == 0) { r.add(new ArrayList<>(cur)); return; }
    if (t < 0 || i == c.length) return;
    bt(c, t, i + 1, cur);               // skip
    cur.add(c[i]);
    bt(c, t - c[i], i, cur);            // take
    cur.remove(cur.size() - 1);
}`,
        },
      },
      { type: "h3", title: "Optimal — O(2^n) with Sort + Pruning" },
      {
        type: "p",
        text: "Array sort করো। যদি c[j] > remaining target, break করো (baki সব বড়)। এটি unnecessary branches cut করে।",
      },
      {
        type: "multi-code",
        filename: "combo_sum_optimal",
        codeSamples: {
          cpp: `vector<vector<int>> r;
void bt(vector<int>& c, int t, int i, vector<int>& cur) {
    if (t == 0) { r.push_back(cur); return; }
    for (int j = i; j < c.size(); j++) {
        if (c[j] > t) break;       // pruning: sorted, baki সব বড়
        cur.push_back(c[j]);
        bt(c, t - c[j], j, cur);   // j = repeat allowed
        cur.pop_back();
    }
}
vector<vector<int>> combinationSum(vector<int>& c, int t) {
    sort(c.begin(), c.end());
    r.clear();
    vector<int> cur;
    bt(c, t, 0, cur);
    return r;
}`,
          go: `var r [][]int
func combinationSum(c []int, t int) [][]int {
    sort.Ints(c)
    r = nil
    var bt func(t, i int, cur []int)
    bt = func(t, i int, cur []int) {
        if t == 0 { r = append(r, append([]int(nil), cur...)); return }
        for j := i; j < len(c); j++ {
            if c[j] > t { break }     // pruning
            cur = append(cur, c[j])
            bt(t-c[j], j, cur)
            cur = cur[:len(cur)-1]
        }
    }
    bt(t, 0, nil)
    return r
}`,
          python: `def combinationSum(c, t):
    c.sort()
    r = []
    def bt(t, i, cur):
        if t == 0: r.append(cur[:]); return
        for j in range(i, len(c)):
            if c[j] > t: break       # pruning
            cur.append(c[j])
            bt(t - c[j], j, cur)    # j = repeat
            cur.pop()
    bt(t, 0, [])
    return r`,
          java: `List<List<Integer>> r = new ArrayList<>();
public List<List<Integer>> combinationSum(int[] c, int t) {
    Arrays.sort(c);
    r.clear();
    bt(c, t, 0, new ArrayList<>());
    return r;
}
void bt(int[] c, int t, int i, List<Integer> cur) {
    if (t == 0) { r.add(new ArrayList<>(cur)); return; }
    for (int j = i; j < c.length; j++) {
        if (c[j] > t) break;           // pruning
        cur.add(c[j]);
        bt(c, t - c[j], j, cur);      // j = repeat
        cur.remove(cur.size() - 1);
    }
}`,
        },
      },
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Without pruning — Time: O(2^n)। Negative target-এও recurse হয়।",
          "Sort + Pruning — Time: O(2^n) কিন্তু অনেক কম branch। c[j] > t হলে break।",
          "Key: sort করে early termination — c[j] > t হলে বাকি সব বাদ।",
        ],
      },

      { type: "h2", id: "p4", title: "Problem 4 — N-Queens" },
      {
        type: "p",
        text: "n×n chessboard-এ nটি Queen এমনভাবে বসাও যে কেউ একে অপরকে attack করতে না পারে। সব possible solution return করো। Example: n = 4 → 2 solutions।",
      },
      { type: "h3", title: "Brute Force — O(n!) check all placements" },
      {
        type: "p",
        text: "প্রতিটি row-তে প্রতিটি column try করো। Valid কিনা check করো — সব row, column, diagonal scan। কোনো optimization নেই।",
      },
      {
        type: "multi-code",
        filename: "nqueens_brute",
        codeSamples: {
          cpp: `bool valid(vector<string>& b, int r, int c, int n) {
    for (int i = 0; i < r; i++)
        if (b[i][c] == 'Q') return false;
    for (int i = r - 1, j = c - 1; i >= 0 && j >= 0; i--, j--)
        if (b[i][j] == 'Q') return false;
    for (int i = r - 1, j = c + 1; i >= 0 && j < n; i--, j++)
        if (b[i][j] == 'Q') return false;
    return true;
}
vector<vector<string>> r;
void bt(vector<string>& b, int row, int n) {
    if (row == n) { r.push_back(b); return; }
    for (int c = 0; c < n; c++) {
        if (valid(b, row, c, n)) {
            b[row][c] = 'Q';
            bt(b, row + 1, n);
            b[row][c] = '.';
        }
    }
}
vector<vector<string>> solveNQueens(int n) {
    r.clear();
    vector<string> b(n, string(n, '.'));
    bt(b, 0, n);
    return r;
}`,
          go: `var r [][]string
func solveNQueens(n int) [][]string {
    r = nil
    b := make([]string, n)
    for i := range b { b[i] = strings.Repeat(".", n) }
    var bt func(row int)
    bt = func(row int) {
        if row == n { r = append(r, append([]string(nil), b...)); return }
        for c := 0; c < n; c++ {
            if valid(b, row, c, n) {
                b[row] = b[row][:c] + "Q" + b[row][c+1:]
                bt(row + 1)
                b[row] = b[row][:c] + "." + b[row][c+1:]
            }
        }
    }
    bt(0)
    return r
}
func valid(b []string, r, c, n int) bool {
    for i := 0; i < r; i++ { if b[i][c] == 'Q' { return false } }
    for i, j := r-1, c-1; i >= 0 && j >= 0; i, j = i-1, j-1 { if b[i][j] == 'Q' { return false } }
    for i, j := r-1, c+1; i >= 0 && j < n; i, j = i-1, j+1 { if b[i][j] == 'Q' { return false } }
    return true
}`,
          python: `def solveNQueens(n):
    r = []
    def valid(b, row, col):
        for i in range(row):
            if b[i][col] == 'Q': return False
            if col - (row - i) >= 0 and b[i][col - (row - i)] == 'Q': return False
            if col + (row - i) < n and b[i][col + (row - i)] == 'Q': return False
        return True
    def bt(b, row):
        if row == n:
            r.append(b[:])
            return
        for col in range(n):
            if valid(b, row, col):
                b[row] = b[row][:col] + 'Q' + b[row][col+1:]
                bt(b, row + 1)
                b[row] = b[row][:col] + '.' + b[row][col+1:]
    bt(['.' * n] * n)
    return r`,
          java: `List<List<String>> r = new ArrayList<>();
public List<List<String>> solveNQueens(int n) {
    r.clear();
    char[][] b = new char[n][n];
    for (int i = 0; i < n; i++) Arrays.fill(b[i], '.');
    bt(b, 0, n);
    return r;
}
void bt(char[][] b, int row, int n) {
    if (row == n) {
        List<String> sol = new ArrayList<>();
        for (char[] row2 : b) sol.add(new String(row2));
        r.add(sol);
        return;
    }
    for (int c = 0; c < n; c++) {
        if (valid(b, row, c, n)) {
            b[row][c] = 'Q';
            bt(b, row + 1, n);
            b[row][c] = '.';
        }
    }
}
boolean valid(char[][] b, int r, int c, int n) {
    for (int i = 0; i < r; i++) if (b[i][c] == 'Q') return false;
    for (int i = r-1, j = c-1; i >= 0 && j >= 0; i--, j--) if (b[i][j] == 'Q') return false;
    for (int i = r-1, j = c+1; i >= 0 && j < n; i--, j++) if (b[i][j] == 'Q') return false;
    return true;
}`,
        },
      },
      { type: "h3", title: "Optimal — O(n!) with HashSet Tracking" },
      {
        type: "p",
        text: "Column, positive diagonal (r+c), ও negative diagonal (r-c) তিনটি HashSet-এ track করো। O(1) validation — কোনো loop লাগে না।",
      },
      {
        type: "multi-code",
        filename: "nqueens_optimal",
        codeSamples: {
          cpp: `vector<vector<string>> r;
unordered_set<int> col, pos, neg;
void bt(vector<string>& b, int row, int n) {
    if (row == n) { r.push_back(b); return; }
    for (int c = 0; c < n; c++) {
        if (col.count(c) || pos.count(row + c) || neg.count(row - c))
            continue;
        col.insert(c); pos.insert(row + c); neg.insert(row - c);
        b[row][c] = 'Q';
        bt(b, row + 1, n);
        b[row][c] = '.';
        col.erase(c); pos.erase(row + c); neg.erase(row - c);
    }
}
vector<vector<string>> solveNQueens(int n) {
    r.clear();
    col.clear(); pos.clear(); neg.clear();
    vector<string> b(n, string(n, '.'));
    bt(b, 0, n);
    return r;
}`,
          go: `var r [][]string
var col, pos, neg map[int]bool
func solveNQueens(n int) [][]string {
    r = nil
    col, pos, neg = map[int]bool{}, map[int]bool{}, map[int]bool{}
    b := make([]string, n)
    for i := range b { b[i] = strings.Repeat(".", n) }
    var bt func(row int)
    bt = func(row int) {
        if row == n { r = append(r, append([]string(nil), b...)); return }
        for c := 0; c < n; c++ {
            if col[c] || pos[row+c] || neg[row-c] { continue }
            col[c] = true; pos[row+c] = true; neg[row-c] = true
            b[row] = b[row][:c] + "Q" + b[row][c+1:]
            bt(row + 1)
            b[row] = b[row][:c] + "." + b[row][c+1:]
            delete(col, c); delete(pos, row+c); delete(neg, row-c)
        }
    }
    bt(0)
    return r
}`,
          python: `def solveNQueens(n):
    r = []
    col, pos, neg = set(), set(), set()
    b = ['.' * n for _ in range(n)]
    def bt(row):
        if row == n:
            r.append(b[:])
            return
        for c in range(n):
            if c in col or row + c in pos or row - c in neg:
                continue
            col.add(c); pos.add(row + c); neg.add(row - c)
            b[row] = b[row][:c] + 'Q' + b[row][c+1:]
            bt(row + 1)
            b[row] = b[row][:c] + '.' + b[row][c+1:]
            col.discard(c); pos.discard(row + c); neg.discard(row - c)
    bt(0)
    return r`,
          java: `List<List<String>> r = new ArrayList<>();
Set<Integer> col, pos, neg;
public List<List<String>> solveNQueens(int n) {
    r.clear();
    col = new HashSet<>(); pos = new HashSet<>(); neg = new HashSet<>();
    char[][] b = new char[n][n];
    for (int i = 0; i < n; i++) Arrays.fill(b[i], '.');
    bt(b, 0, n);
    return r;
}
void bt(char[][] b, int row, int n) {
    if (row == n) {
        List<String> sol = new ArrayList<>();
        for (char[] row2 : b) sol.add(new String(row2));
        r.add(sol);
        return;
    }
    for (int c = 0; c < n; c++) {
        if (col.contains(c) || pos.contains(row + c) || neg.contains(row - c))
            continue;
        col.add(c); pos.add(row + c); neg.add(row - c);
        b[row][c] = 'Q';
        bt(b, row + 1, n);
        b[row][c] = '.';
        col.remove(c); pos.remove(row + c); neg.remove(row - c);
    }
}`,
        },
      },
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Full validation — Time: O(n!), Space: O(n²)। প্রতিটি placement-এ সব row/diagonal scan।",
          "HashSet — Time: O(n!), Space: O(n)। Column ও diagonal O(1)-এ check।",
          "Key: r+c ও r-c দিয়ে diagonal track — প্রতিটি diagonal-এর একটি unique value।",
        ],
      },

      { type: "h2", id: "p5", title: "Problem 5 — Word Search" },
      {
        type: "p",
        text: "একটি m×n grid ও একটি word দেওয়া আছে। Word টি grid-এ আছে কিনা check করো। প্রতিটি cell থেকে উপর/নিচ/বাম/ডান যাওয়া যায়, একই cell দুবার use করা যাবে না। Example: board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = 'ABCCED' → true",
      },
      { type: "h3", title: "Brute Force — O(n × m × 4^l) DFS per cell" },
      {
        type: "p",
        text: "প্রতিটি cell থেকে DFS চালাও। Character match হলে চার দিকে explore করো। Visited cell-কে temporarily mark করো, backtrack-এ restore করো।",
      },
      {
        type: "multi-code",
        filename: "word_search",
        codeSamples: {
          cpp: `bool exist(vector<vector<char>>& b, string w) {
    for (int i = 0; i < b.size(); i++)
        for (int j = 0; j < b[0].size(); j++)
            if (bt(b, w, 0, i, j)) return true;
    return false;
}
bool bt(vector<vector<char>>& b, string& w, int k, int i, int j) {
    if (k == w.size()) return true;
    if (i < 0 || i >= b.size() || j < 0 || j >= b[0].size()
        || b[i][j] != w[k]) return false;
    char t = b[i][j];
    b[i][j] = '#';     // mark visited
    bool f = bt(b, w, k+1, i+1, j) || bt(b, w, k+1, i-1, j)
           || bt(b, w, k+1, i, j+1) || bt(b, w, k+1, i, j-1);
    b[i][j] = t;       // backtrack
    return f;
}`,
          go: `func exist(b [][]byte, w string) bool {
    for i := 0; i < len(b); i++ {
        for j := 0; j < len(b[0]); j++ {
            if bt(b, w, 0, i, j) { return true }
        }
    }
    return false
}
func bt(b [][]byte, w string, k, i, j int) bool {
    if k == len(w) { return true }
    if i < 0 || i >= len(b) || j < 0 || j >= len(b[0])
        || b[i][j] != w[k] { return false }
    t := b[i][j]
    b[i][j] = '#'
    f := bt(b, w, k+1, i+1, j) || bt(b, w, k+1, i-1, j)
        || bt(b, w, k+1, i, j+1) || bt(b, w, k+1, i, j-1)
    b[i][j] = t
    return f
}`,
          python: `def exist(b, w):
    def bt(k, i, j):
        if k == len(w): return True
        if i < 0 or i >= len(b) or j < 0 or j >= len(b[0])
            or b[i][j] != w[k]: return False
        t = b[i][j]
        b[i][j] = '#'
        f = (bt(k+1, i+1, j) or bt(k+1, i-1, j)
          or bt(k+1, i, j+1) or bt(k+1, i, j-1))
        b[i][j] = t
        return f
    for i in range(len(b)):
        for j in range(len(b[0])):
            if bt(0, i, j): return True
    return False`,
          java: `public boolean exist(char[][] b, String w) {
    for (int i = 0; i < b.length; i++)
        for (int j = 0; j < b[0].length; j++)
            if (bt(b, w, 0, i, j)) return true;
    return false;
}
boolean bt(char[][] b, String w, int k, int i, int j) {
    if (k == w.length()) return true;
    if (i < 0 || i >= b.length || j < 0 || j >= b[0].length
        || b[i][j] != w.charAt(k)) return false;
    char t = b[i][j];
    b[i][j] = '#';
    boolean f = bt(b, w, k+1, i+1, j) || bt(b, w, k+1, i-1, j)
              || bt(b, w, k+1, i, j+1) || bt(b, w, k+1, i, j-1);
    b[i][j] = t;
    return f;
}`,
        },
      },
      { type: "h3", title: "Optimal — Same DFS with Early Termination" },
      {
        type: "p",
        text: "Character match না হলে immediately return false — এটাই ইতিমধ্যে optimal। DFS with backtracking-ই এই problem-এর best approach। কোনো ভিন্ন algorithm দরকার নেই। একমাত্র optimization হলো board-এ mark করার জন্য অতিরিক্ত visited array না ব্যবহার করে board-কেই modify করা।",
      },
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "DFS — Time: O(n × m × 4^l)। l = word length। প্রতিটি cell থেকে ৪ দিকে explore।",
          "Space — O(l) recursion depth। কোনো extra array নেই, board-কেই mark করা হয়।",
          "Key: board-এ visited cell mark করো ('#'), backtrack-এ restore করো। Early termination on mismatch।",
        ],
      },

      { type: "h2", id: "summary", title: "Chapter Summary" },
      {
        type: "list",
        items: [
          "Subsets — include/exclude backtracking, O(2^n)। pop_back = backtrack।",
          "Permutations — swap backtracking, O(n!)। swap → recurse → swap back।",
          "Combination Sum — sort + prune, একই element repeat allowed।",
          "N-Queens — column ও diagonal HashSet tracking, O(n!)।",
          "Word Search — DFS + mark/unmark board cells।",
          "Core pattern: try choice → recurse → undo choice (backtrack)। এটাই backtracking-এর মূল mantra।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: পরের topic হলো Heap / Priority Queue — O(log n) insert ও extract।",
      },
    ],
  },

  // ---- Heap / Priority Queue ----
  {
    id: "dsa-heap",
    subject: "dsa",
    title: "Heap / Priority Queue",
    bangla: "হিপ / প্রায়োরিটি কিউ",
    difficulty: "Medium",
    est: "2 hr",
    summary:
      "Heap হলো complete binary tree যা priority-based access দেয়। ৫টি classic problem — Kth Largest in Stream, Last Stone Weight, K Closest Points, Task Scheduler, Find Median from Data Stream।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      {
        type: "p",
        text: "Heap হলো একটি complete binary tree যেখানে parent সবসময় children-এর চেয়ে বড় (max-heap) বা ছোট (min-heap)। Priority Queue হিসেবে O(log n) insert ও extract দেয়। Real-life thinking — ER queue! সবচেয়ে critical patient কে আগে দেখা হয়, কে আগে এসেছে তা নয়।",
      },
      {
        type: "p",
        text: "Heap-এর দুটি main flavor — Min-Heap (root সবার চেয়ে ছোট) ও Max-Heap (root সবার চেয়ে বড়)। Array representation-এ parent index i হলে children হলো 2i+1 ও 2i+2 (0-indexed)। Standard library-তে C++ priority_queue default max-heap, Python heapq min-heap, Go container/heap min-heap, Java PriorityQueue min-heap। Problem-solving-এ খুব common pattern হলো 'k largest/smallest' — সেখানে k size-এর opposite heap রাখো (k largest চাইলে min-heap of size k)।",
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: 'top k' ধরনের problem-এ সবসময় opposite heap use করো — k largest চাইলে min-heap of size k, k smallest চাইলে max-heap of size k। এতে heap ছোট থাকে ও efficiency বাড়ে।",
      },

      { type: "h2", id: "p1", title: "Problem 1 — Kth Largest Element in a Stream" },
      {
        type: "p",
        text: "একটি class design করো যা একটি stream থেকে number add করে এবং সবসময় kth largest element return করে। Example: k = 3, initial = [4,5,8,2]। add(3) → 4, add(5) → 5, add(10) → 5, add(9) → 8, add(4) → 8।",
      },
      {
        type: "p",
        text: "Key insight — kth largest মানে sorted array-এ index k-1 (0-indexed)। আমাদের শুধু k largest গুলো track করলেই হয়, বাকি সব discard করতে পারি। এর জন্য min-heap of size k খুব perfect।",
      },
      { type: "h3", title: "Brute Force — O(n log n) per add" },
      {
        type: "p",
        text: "প্রত্যেক add-এ নতুন element যোগ করে array sort করো, তারপর k-1 index return করো। Simple কিন্তু very slow। n add হলে total O(n² log n) — large stream-এ কাজ করবে না।",
      },
      {
        type: "multi-code",
        filename: "kth_largest_stream_brute",
        codeSamples: {
          cpp: `class KthLargest {
    int k;
    vector<int> nums;
public:
    KthLargest(int k, vector<int>& n) : k(k), nums(n) {}
    int add(int val) {
        nums.push_back(val);
        sort(nums.begin(), nums.end());
        return nums[nums.size() - k];
    }
};`,
          go: `type KthLargest struct {
    k    int
    nums []int
}
func Constructor(k int, n []int) KthLargest {
    return KthLargest{k, n}
}
func (kl *KthLargest) Add(val int) int {
    kl.nums = append(kl.nums, val)
    sort.Ints(kl.nums)
    return kl.nums[len(kl.nums)-kl.k]
}`,
          python: `class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
    def add(self, val):
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]`,
          java: `class KthLargest {
    int k;
    List<Integer> nums;
    public KthLargest(int k, int[] n) {
        this.k = k;
        nums = new ArrayList<>();
        for (int x : n) nums.add(x);
    }
    public int add(int val) {
        nums.add(val);
        Collections.sort(nums);
        return nums.get(nums.size() - k);
    }
}`,
        },
      },
      { type: "h3", title: "Optimal — O(log k) per add with Min-Heap" },
      {
        type: "p",
        text: "Min-heap of size k রাখো। Heap-এর root হলো kth largest। নতুন element যদি root-এর চেয়ে বড় হয়, তাহলে root pop করে নতুন element push করো। ছোট হলে ignore। এতে প্রতি add O(log k) — k সাধারণত ছোট থাকে, তাই খুব fast।",
      },
      {
        type: "multi-code",
        filename: "kth_largest_stream_optimal",
        codeSamples: {
          cpp: `class KthLargest {
    int k;
    priority_queue<int, vector<int>, greater<int>> pq;  // min-heap
public:
    KthLargest(int k, vector<int>& n) : k(k) {
        for (int x : n) {
            pq.push(x);
            if (pq.size() > k) pq.pop();
        }
    }
    int add(int val) {
        pq.push(val);
        if (pq.size() > k) pq.pop();
        return pq.top();
    }
};`,
          go: `import "container/heap"
type IntHeap []int
func (h IntHeap) Len() int { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x any) { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() any {
    old := *h; n := len(old); x := old[n-1]; *h = old[:n-1]; return x
}
type KthLargest struct { k int; h *IntHeap }
func Constructor(k int, n []int) KthLargest {
    h := &IntHeap{}
    heap.Init(h)
    for _, x := range n { heap.Push(h, x); if h.Len() > k { heap.Pop(h) } }
    return KthLargest{k, h}
}
func (kl *KthLargest) Add(val int) int {
    heap.Push(kl.h, val)
    if kl.h.Len() > kl.k { heap.Pop(kl.h) }
    return (*kl.h)[0]
}`,
          python: `import heapq
class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.h = []
        for x in nums:
            heapq.heappush(self.h, x)
            if len(self.h) > k:
                heapq.heappop(self.h)
    def add(self, val):
        heapq.heappush(self.h, val)
        if len(self.h) > self.k:
            heapq.heappop(self.h)
        return self.h[0]`,
          java: `class KthLargest {
    int k;
    PriorityQueue<Integer> pq;  // min-heap by default
    public KthLargest(int k, int[] n) {
        this.k = k;
        pq = new PriorityQueue<>();
        for (int x : n) {
            pq.offer(x);
            if (pq.size() > k) pq.poll();
        }
    }
    public int add(int val) {
        pq.offer(val);
        if (pq.size() > k) pq.poll();
        return pq.peek();
    }
}`,
        },
      },
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute — Time: O(n log n) per add, Space: O(n)। প্রতি add-এ sort হয়।",
          "Optimal — Time: O(log k) per add, Space: O(k)। Heap সবসময় k element hold করে।",
          "Key: kth largest চাইলে min-heap of size k। এটাই 'top k' pattern-এর মূল।",
        ],
      },

      { type: "h2", id: "p2", title: "Problem 2 — Last Stone Weight" },
      {
        type: "p",
        text: "একটি array of stones দেওয়া আছে যেখানে stones[i] = ওই stone-এর weight। প্রতি turn-এ দুটি heaviest stone বেছে smash করো। যদি সমান হয় দুটোই destroy, না হয় lighter destroy ও heavier টা (heavier - lighter) weight নিয়ে রয়ে যায়। শেষ পর্যন্ত একটি বা শূন্য stone বাকি থাকবে — সেটি return করো। Example: [2,7,4,1,8,1] → 1।",
      },
      {
        type: "p",
        text: "Key insight — প্রতি turn-এ max দুটি element দরকার এবং পরে হয়তো একটি নতুন element insert করতে হবে। এটা exactly max-heap-এর use case! প্রতি iteration-এ max দুটি extract করে smash করো, আবার insert করো।",
      },
      { type: "h3", title: "Brute Force — O(n²) Repeated Linear Max" },
      {
        type: "p",
        text: "প্রতি turn-ে linear scan দিয়ে দুটি max খুঁজে বের করো। n turns, প্রতি turn-ে O(n) → total O(n²)। ছোট array-তে চলবে কিন্তু efficiency খারাপ।",
      },
      {
        type: "multi-code",
        filename: "last_stone_brute",
        codeSamples: {
          cpp: `int lastStoneWeight(vector<int>& s) {
    while (s.size() > 1) {
        sort(s.begin(), s.end(), greater<int>());
        int y = s[0], x = s[1];
        s.erase(s.begin(), s.begin()+2);
        if (y != x) s.push_back(y - x);
    }
    return s.empty() ? 0 : s[0];
}`,
          go: `func lastStoneWeight(s []int) int {
    for len(s) > 1 {
        sort.Sort(sort.Reverse(sort.IntSlice(s)))
        y, x := s[0], s[1]
        s = s[2:]
        if y != x { s = append(s, y-x) }
    }
    if len(s) == 0 { return 0 }
    return s[0]
}`,
          python: `def lastStoneWeight(s):
    while len(s) > 1:
        s.sort(reverse=True)
        y, x = s[0], s[1]
        s = s[2:]
        if y != x:
            s.append(y - x)
    return s[0] if s else 0`,
          java: `public int lastStoneWeight(int[] s) {
    List<Integer> l = new ArrayList<>();
    for (int x : s) l.add(x);
    while (l.size() > 1) {
        l.sort(Collections.reverseOrder());
        int y = l.get(0), x = l.get(1);
        l.subList(0, 2).clear();
        if (y != x) l.add(y - x);
    }
    return l.isEmpty() ? 0 : l.get(0);
}`,
        },
      },
      { type: "h3", title: "Optimal — O(n log n) with Max-Heap" },
      {
        type: "p",
        text: "Max-heap দিয়ে সব stones ঢুকাও। যতক্ষণ একাধিক stone আছে, দুটি max extract করো, smash করো, আর যদি ফলাফল positive হয় push করো। প্রতি operation O(log n), মোট n operations → O(n log n)।",
      },
      {
        type: "multi-code",
        filename: "last_stone_optimal",
        codeSamples: {
          cpp: `int lastStoneWeight(vector<int>& s) {
    priority_queue<int> pq(s.begin(), s.end());  // max-heap
    while (pq.size() > 1) {
        int y = pq.top(); pq.pop();
        int x = pq.top(); pq.pop();
        if (y != x) pq.push(y - x);
    }
    return pq.empty() ? 0 : pq.top();
}`,
          go: `func lastStoneWeight(s []int) int {
    h := &IntHeap{}
    for _, x := range s { heap.Push(h, -x) }  // negate for max-heap
    for h.Len() > 1 {
        y := -heap.Pop(h).(int)
        x := -heap.Pop(h).(int)
        if y != x { heap.Push(h, -(y - x)) }
    }
    if h.Len() == 0 { return 0 }
    return -(*h)[0]
}`,
          python: `import heapq
def lastStoneWeight(s):
    h = [-x for x in s]   # max-heap via negation
    heapq.heapify(h)
    while len(h) > 1:
        y = -heapq.heappop(h)
        x = -heapq.heappop(h)
        if y != x:
            heapq.heappush(h, -(y - x))
    return -h[0] if h else 0`,
          java: `public int lastStoneWeight(int[] s) {
    PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
    for (int x : s) pq.offer(x);
    while (pq.size() > 1) {
        int y = pq.poll();
        int x = pq.poll();
        if (y != x) pq.offer(y - x);
    }
    return pq.isEmpty() ? 0 : pq.peek();
}`,
        },
      },
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute — Time: O(n² log n) (sort per iteration), Space: O(n)। অথবা O(n²) linear scan।",
          "Optimal — Time: O(n log n), Space: O(n)। প্রতি smash O(log n), মোট n smash।",
          "Key: 'top 2 element বারবার দরকার' — এই pattern-এ max-heap perfect।",
        ],
      },

      { type: "h2", id: "p3", title: "Problem 3 — K Closest Points to Origin" },
      {
        type: "p",
        text: "একটি points array ও একটি integer k দেওয়া আছে। Origin (0,0) থেকে সবচেয়ে কাছের k points return করো। Distance = sqrt(x² + y²) কিন্তু comparison-এর জন্য sqrt করার দরকার নেই — squared distance ও same ordering দেয়। Example: points = [[1,3],[-2,2]], k = 1 → [[-2,2]]।",
      },
      {
        type: "p",
        text: "Key insight — আমরা শুধু k closest চাই, full sort করার দরকার নেই। Max-heap of size k রাখলে — যদি নতুন point-এর distance heap-এর max থেকে ছোট হয়, max কে pop করে নতুনটা push করো।",
      },
      { type: "h3", title: "Brute Force — O(n log n) Full Sort" },
      {
        type: "p",
        text: "সব points কে distance অনুসারে sort করো, প্রথম k return করো। Simple কিন্তু অপ্রয়োজনীয়ভাবে সব element sort করে — n অনেক বড় হলে wasteful।",
      },
      {
        type: "multi-code",
        filename: "k_closest_brute",
        codeSamples: {
          cpp: `vector<vector<int>> kClosest(vector<vector<int>>& p, int k) {
    sort(p.begin(), p.end(), [](auto& a, auto& b) {
        return a[0]*a[0] + a[1]*a[1] < b[0]*b[0] + b[1]*b[1];
    });
    return vector<vector<int>>(p.begin(), p.begin() + k);
}`,
          go: `func kClosest(p [][]int, k int) [][]int {
    sort.Slice(p, func(i, j int) bool {
        di := p[i][0]*p[i][0] + p[i][1]*p[i][1]
        dj := p[j][0]*p[j][0] + p[j][1]*p[j][1]
        return di < dj
    })
    return p[:k]
}`,
          python: `def kClosest(p, k):
    p.sort(key=lambda x: x[0]*x[0] + x[1]*x[1])
    return p[:k]`,
          java: `public int[][] kClosest(int[][] p, int k) {
    Arrays.sort(p, (a, b) ->
        Integer.compare(a[0]*a[0] + a[1]*a[1], b[0]*b[0] + b[1]*b[1]));
    return Arrays.copyOf(p, k);
}`,
        },
      },
      { type: "h3", title: "Optimal — O(n log k) with Max-Heap of size k" },
      {
        type: "p",
        text: "Max-heap of size k রাখো। প্রতি point-এর জন্য, heap ছোট হলে insert করো, না হয় max থেকে ছোট হলে max pop করে insert করো। Final heap-এর সব elements ই k closest। খুব বড় n-এর জন্য এটা অনেক বেশি efficient।",
      },
      {
        type: "multi-code",
        filename: "k_closest_optimal",
        codeSamples: {
          cpp: `vector<vector<int>> kClosest(vector<vector<int>>& p, int k) {
    auto dist = [](auto& a) { return a[0]*a[0] + a[1]*a[1]; };
    auto cmp = [&](auto& a, auto& b) { return dist(a) < dist(b); };
    priority_queue<vector<int>, vector<vector<int>>, decltype(cmp)> pq(cmp);  // max-heap by dist
    for (auto& x : p) {
        pq.push(x);
        if (pq.size() > k) pq.pop();
    }
    vector<vector<int>> r;
    while (!pq.empty()) { r.push_back(pq.top()); pq.pop(); }
    return r;
}`,
          go: `type Pt struct { x, y, d int }
type MaxH []Pt
func (h MaxH) Len() int { return len(h) }
func (h MaxH) Less(i, j int) bool { return h[i].d > h[j].d }
func (h MaxH) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *MaxH) Push(x any) { *h = append(*h, x.(Pt)) }
func (h *MaxH) Pop() any { old := *h; n := len(old); x := old[n-1]; *h = old[:n-1]; return x }
func kClosest(p [][]int, k int) [][]int {
    h := &MaxH{}
    for _, v := range p {
        d := v[0]*v[0] + v[1]*v[1]
        heap.Push(h, Pt{v[0], v[1], d})
        if h.Len() > k { heap.Pop(h) }
    }
    r := make([][]int, 0, k)
    for h.Len() > 0 { pt := heap.Pop(h).(Pt); r = append(r, []int{pt.x, pt.y}) }
    return r
}`,
          python: `import heapq
def kClosest(p, k):
    h = []
    for x, y in p:
        d = x*x + y*y
        heapq.heappush(h, (-d, x, y))   # max-heap via negation
        if len(h) > k:
            heapq.heappop(h)
    return [[x, y] for (_, x, y) in h]`,
          java: `public int[][] kClosest(int[][] p, int k) {
    // max-heap by distance (b before a)
    PriorityQueue<int[]> pq = new PriorityQueue<>(
        (a, b) -> Integer.compare(
            b[0]*b[0] + b[1]*b[1], a[0]*a[0] + a[1]*a[1]));
    for (int[] x : p) {
        pq.offer(x);
        if (pq.size() > k) pq.poll();
    }
    int[][] r = new int[k][2];
    int i = 0;
    while (!pq.isEmpty()) r[i++] = pq.poll();
    return r;
}`,
        },
      },
      { type: "h3", title: "Alternative — O(n) Average Quickselect" },
      {
        type: "p",
        text: "Quickselect partition-based approach দিয়ে average O(n) possible। কিন্তু worst case O(n²) ও implementation জটিল — interview-তে heap-ই সবচেয়ে নিরাপদ ও practical choice।",
      },
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute — Time: O(n log n), Space: O(log n) sort stack। n ছোট হলে fine।",
          "Optimal Heap — Time: O(n log k), Space: O(k)। n >> k হলে big win।",
          "Quickselect — Time: O(n) avg, O(n²) worst। Implement কঠিন কিন্তু fastest average।",
          "Key: 'top k smallest/largest' চাইলে heap of size k সবচেয়ে practical approach।",
        ],
      },

      { type: "h2", id: "p4", title: "Problem 4 — Task Scheduler" },
      {
        type: "p",
        text: "একটি tasks array দেওয়া আছে যেখানে প্রতিটি char একটি task type। একই task-এর মধ্যে অন্তত n units gap থাকতে হবে। মোট কমপন units কত লাগবে return করো। Example: tasks = ['A','A','A','B','B','B'], n = 2 → 8 (A → B → idle → A → B → idle → A → B)।",
      },
      {
        type: "p",
        text: "Key insight — সবচেয়ে বেশি frequency ওয়ালা task-টা সবচেয়ে বেশি constraint তৈরি করে। max_freq task টা (max_freq - 1) বার n+1 দৈর্ঘ্যের chunk নেয়, তারপর সবশেষে 1 টা আরো। Math: (max_freq - 1) × (n + 1) + count_of_max_freq। কিন্তু যদি task-এর সংখ্যা এই value থেকে বেশি হয়, তাহলে কোনো idle লাগবে না — answer হবে tasks.length।",
      },
      { type: "h3", title: "Brute Force — O(time) Simulation" },
      {
        type: "p",
        text: "প্রতি cycle-এ সব available task থেকে সবচেয়ে recent না হওয়া বেছে করো। প্রতিটি step হিসেব করতে হবে — very slow কিন্তু correct।",
      },
      {
        type: "multi-code",
        filename: "task_scheduler_brute",
        codeSamples: {
          cpp: `int leastInterval(vector<char>& t, int n) {
    vector<int> cnt(26, 0), cool(26, 0);
    for (char c : t) cnt[c - 'A']++;
    int done = 0, total = t.size(), time = 0;
    while (done < total) {
        int pick = -1;
        for (int i = 0; i < 26; i++)
            if (cnt[i] > 0 && cool[i] == 0 &&
                (pick == -1 || cnt[i] > cnt[pick])) pick = i;
        time++;
        for (int i = 0; i < 26; i++) if (cool[i] > 0) cool[i]--;
        if (pick != -1) { cnt[pick]--; cool[pick] = n; done++; }
    }
    return time;
}`,
          go: `func leastInterval(t []byte, n int) int {
    cnt := make([]int, 26)
    cool := make([]int, 26)
    for _, c := range t { cnt[c-'A']++ }
    done, total, time := 0, len(t), 0
    for done < total {
        pick := -1
        for i := 0; i < 26; i++ {
            if cnt[i] > 0 && cool[i] == 0 && (pick == -1 || cnt[i] > cnt[pick]) {
                pick = i
            }
        }
        time++
        for i := 0; i < 26; i++ { if cool[i] > 0 { cool[i]-- } }
        if pick != -1 { cnt[pick]--; cool[pick] = n; done++ }
    }
    return time
}`,
          python: `def leastInterval(t, n):
    cnt = [0] * 26
    cool = [0] * 26
    for c in t: cnt[ord(c) - ord('A')] += 1
    done, total, time = 0, len(t), 0
    while done < total:
        pick = -1
        for i in range(26):
            if cnt[i] > 0 and cool[i] == 0 and (pick == -1 or cnt[i] > cnt[pick]):
                pick = i
        time += 1
        for i in range(26):
            if cool[i] > 0: cool[i] -= 1
        if pick != -1:
            cnt[pick] -= 1
            cool[pick] = n
            done += 1
    return time`,
          java: `public int leastInterval(char[] t, int n) {
    int[] cnt = new int[26], cool = new int[26];
    for (char c : t) cnt[c - 'A']++;
    int done = 0, total = t.length, time = 0;
    while (done < total) {
        int pick = -1;
        for (int i = 0; i < 26; i++)
            if (cnt[i] > 0 && cool[i] == 0 && (pick == -1 || cnt[i] > cnt[pick])) pick = i;
        time++;
        for (int i = 0; i < 26; i++) if (cool[i] > 0) cool[i]--;
        if (pick != -1) { cnt[pick]--; cool[pick] = n; done++; }
    }
    return time;
}`,
        },
      },
      { type: "h3", title: "Optimal — O(n) Math Formula" },
      {
        type: "p",
        text: "Max frequency ও সেই frequency কত ধরনের task আছে গণনা করো। Formula: max(total_tasks, (max_freq - 1) × (n + 1) + count_of_max_freq)। প্রথম অংশ idle ছাড়া, দ্বিতীয় অংশ idle সহ minimum schedule।",
      },
      {
        type: "multi-code",
        filename: "task_scheduler_optimal",
        codeSamples: {
          cpp: `int leastInterval(vector<char>& t, int n) {
    vector<int> cnt(26, 0);
    for (char c : t) cnt[c - 'A']++;
    int maxF = *max_element(cnt.begin(), cnt.end());
    int maxCount = 0;
    for (int x : cnt) if (x == maxF) maxCount++;
    return max((int)t.size(), (maxF - 1) * (n + 1) + maxCount);
}`,
          go: `func leastInterval(t []byte, n int) int {
    cnt := make([]int, 26)
    for _, c := range t { cnt[c-'A']++ }
    maxF := 0
    for _, x := range cnt { if x > maxF { maxF = x } }
    maxCount := 0
    for _, x := range cnt { if x == maxF { maxCount++ } }
    cand := (maxF - 1) * (n + 1) + maxCount
    if len(t) > cand { return len(t) }
    return cand
}`,
          python: `def leastInterval(t, n):
    from collections import Counter
    cnt = Counter(t)
    maxF = max(cnt.values())
    maxCount = sum(1 for v in cnt.values() if v == maxF)
    return max(len(t), (maxF - 1) * (n + 1) + maxCount)`,
          java: `public int leastInterval(char[] t, int n) {
    int[] cnt = new int[26];
    for (char c : t) cnt[c - 'A']++;
    int maxF = 0, maxCount = 0;
    for (int x : cnt) maxF = Math.max(maxF, x);
    for (int x : cnt) if (x == maxF) maxCount++;
    int cand = (maxF - 1) * (n + 1) + maxCount;
    return Math.max(t.length, cand);
}`,
        },
      },
      { type: "h3", title: "Alternative — Max-Heap + Queue O(n × 26)" },
      {
        type: "p",
        text: "সবচেয়ে frequent task max-heap থেকে বের করো, n+1 cycle পর্যন্ত process করো, idle slot না ভরলে সেটি cooldown queue-তে রাখো। Heap খালি না হওয়া পর্যন্ত repeat করো। Simulation-এর চেয়ে efficient কিন্তু formula-র চেয়ে slow।",
      },
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute Simulation — Time: O(total_time × 26), Space: O(1)। total_time অনেক বড় হতে পারে।",
          "Optimal Math — Time: O(n), Space: O(1)। Frequency count + formula, একদম optimal।",
          "Heap + Queue — Time: O(n log 26) ≈ O(n), Space: O(26)। ভাল কিন্তু formula-র চেয়ে slow।",
          "Key: যদি pure math formula derive করা যায়, simulation এড়িয়ে যাও।",
        ],
      },

      { type: "h2", id: "p5", title: "Problem 5 — Find Median from Data Stream" },
      {
        type: "p",
        text: "একটি class design করো যা running stream থেকে number add করে এবং সবসময় current median return করে। Even count হলে দুটি middle-এর average, odd count হলে middle টা। Example: addNum(1), addNum(2) → median = 1.5, addNum(3) → median = 2।",
      },
      {
        type: "p",
        text: "Key insight — median বলতে বুঝায় sorted data-কে দুই ভাগে ভাগ করা। বাম অর্ধেক max-heap (যাতে max সহজে পাওয়া যায়), ডান অর্ধেক min-heap (যাতে min সহজে পাওয়া যায়)। দুই heap-এর size balance রাখলে median হলো (left.top + right.top) / 2 অথবা যে heap বড় তার top। এটা 'Two Heaps' pattern — interview-এ very common।",
      },
      { type: "h3", title: "Brute Force — O(n log n) per addNum" },
      {
        type: "p",
        text: "প্রত্যেক addNum-এ list-এ insert করে sort করো। findMedian-এ সরাসরি middle element return করো। Simple কিন্তু large stream-এ অসহ্য — n add হলে O(n² log n) total।",
      },
      {
        type: "multi-code",
        filename: "median_stream_brute",
        codeSamples: {
          cpp: `class MedianFinder {
    vector<int> v;
public:
    void addNum(int num) {
        v.push_back(num);
        sort(v.begin(), v.end());
    }
    double findMedian() {
        int n = v.size();
        if (n % 2) return v[n/2];
        return (v[n/2 - 1] + v[n/2]) / 2.0;
    }
};`,
          go: `type MedianFinder struct { v []int }
func Constructor() MedianFinder { return MedianFinder{} }
func (mf *MedianFinder) AddNum(num int) {
    mf.v = append(mf.v, num)
    sort.Ints(mf.v)
}
func (mf *MedianFinder) FindMedian() float64 {
    n := len(mf.v)
    if n % 2 == 1 { return float64(mf.v[n/2]) }
    return float64(mf.v[n/2-1]+mf.v[n/2]) / 2.0
}`,
          python: `class MedianFinder:
    def __init__(self):
        self.v = []
    def addNum(self, num):
        self.v.append(num)
        self.v.sort()
    def findMedian(self):
        n = len(self.v)
        if n % 2 == 1:
            return self.v[n // 2]
        return (self.v[n//2 - 1] + self.v[n//2]) / 2.0`,
          java: `class MedianFinder {
    List<Integer> v;
    public MedianFinder() { v = new ArrayList<>(); }
    public void addNum(int num) {
        v.add(num);
        Collections.sort(v);
    }
    public double findMedian() {
        int n = v.size();
        if (n % 2 == 1) return v.get(n/2);
        return (v.get(n/2-1) + v.get(n/2)) / 2.0;
    }
}`,
        },
      },
      { type: "h3", title: "Optimal — O(log n) per addNum with Two Heaps" },
      {
        type: "p",
        text: "Max-heap 'left' (lower half) ও min-heap 'right' (upper half) রাখো। নতুন element যোগ করার সময়: প্রথমে left-এ push করো, তারপর left-এর max কে right-এ move করো। যদি right বড় হয়ে যায়, একটি right-এর min কে left-এ move করো। এতে left.size সবসময় right.size বা right.size + 1 হবে। Median = left বড় হলে left.top, সমান হলে average।",
      },
      {
        type: "multi-code",
        filename: "median_stream_optimal",
        codeSamples: {
          cpp: `class MedianFinder {
    priority_queue<int> left;                              // max-heap
    priority_queue<int, vector<int>, greater<int>> right;  // min-heap
public:
    void addNum(int num) {
        left.push(num);
        right.push(left.top()); left.pop();
        if (right.size() > left.size()) {
            left.push(right.top()); right.pop();
        }
    }
    double findMedian() {
        if (left.size() > right.size()) return left.top();
        return (left.top() + right.top()) / 2.0;
    }
};`,
          go: `type MedianFinder struct {
    left  *MaxHeapI  // max-heap (lower half)
    right *IntHeap   // min-heap (upper half)
}
func Constructor() MedianFinder {
    return MedianFinder{&MaxHeapI{}, &IntHeap{}}
}
func (mf *MedianFinder) AddNum(num int) {
    heap.Push(mf.left, num)
    heap.Push(mf.right, heap.Pop(mf.left).(int))
    if mf.right.Len() > mf.left.Len() {
        heap.Push(mf.left, heap.Pop(mf.right).(int))
    }
}
func (mf *MedianFinder) FindMedian() float64 {
    if mf.left.Len() > mf.right.Len() {
        return float64((*mf.left)[0])
    }
    return float64((*mf.left)[0] + (*mf.right)[0]) / 2.0
}`,
          python: `import heapq
class MedianFinder:
    def __init__(self):
        self.left = []   # max-heap via negation (lower half)
        self.right = []  # min-heap (upper half)
    def addNum(self, num):
        heapq.heappush(self.left, -num)
        heapq.heappush(self.right, -heapq.heappop(self.left))
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))
    def findMedian(self):
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2.0`,
          java: `class MedianFinder {
    PriorityQueue<Integer> left;   // max-heap (lower half)
    PriorityQueue<Integer> right;  // min-heap (upper half)
    public MedianFinder() {
        left = new PriorityQueue<>(Collections.reverseOrder());
        right = new PriorityQueue<>();
    }
    public void addNum(int num) {
        left.offer(num);
        right.offer(left.poll());
        if (right.size() > left.size()) left.offer(right.poll());
    }
    public double findMedian() {
        if (left.size() > right.size()) return left.peek();
        return (left.peek() + right.peek()) / 2.0;
    }
}`,
        },
      },
      { type: "h3", title: "Complexity Comparison" },
      {
        type: "list",
        items: [
          "Brute — Time: O(n log n) per add, O(1) median। n add হলে O(n² log n) total।",
          "Optimal Two Heaps — Time: O(log n) per add, O(1) median। Order of magnitude বেশি fast।",
          "Space: O(n) for both — সব element store করতেই হয়।",
          "Key: median মানে দুই ভাগ — lower half max-heap, upper half min-heap। এটাই 'Two Heaps' pattern।",
        ],
      },

      { type: "h2", id: "summary", title: "Chapter Summary" },
      {
        type: "list",
        items: [
          "Kth Largest in Stream — min-heap of size k, O(log k) per add। 'top k' pattern-এর মূল।",
          "Last Stone Weight — max-heap, দুটি max extract ও push diff। O(n log n)।",
          "K Closest Points — max-heap of size k (opposite heap pattern), O(n log k)।",
          "Task Scheduler — math formula (max_freq - 1) × (n + 1) + count_of_max_freq, O(n)।",
          "Find Median — two heaps (lower max + upper min), O(log n) per add। 'Two Heaps' pattern।",
          "Core pattern: 'top k' চাইলে opposite heap of size k। Median/stream চাইলে two heaps balance। এটাই heap-এর মূল mantra।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: পরের topic হলো Graphs — nodes ও edges দিয়ে connected structure, BFS/DFS/Union-Find/Dijkstra।",
      },
    ],
  },


  // ---- Graphs ----
  {
    id: "dsa-graphs",
    subject: "dsa",
    title: "Graphs",
    bangla: "গ্রাফ",
    difficulty: "Hard",
    est: "3 hr",
    summary: "Graph হলো nodes (vertices) ও edges দিয়ে connected structure।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      { type: "p", text: "Graph হলো nodes (vertices) ও edges দিয়ে connected একটি structure। Tree-এর মতো, কিন্তু cycle থাকতে পারে এবং প্রতিটি node-এর যেকোনো সংখ্যক neighbor থাকতে পারে। Real-life thinking — Google Maps! শহর হলো nodes, রাস্তা হলো edges। Shortest path খুঁজতে BFS/DFS বা Dijkstra use করো।" },
      { type: "callout", calloutTone: "tip", text: "Tip: পরের topic হলো 1-D Dynamic Programming — subproblems solve করে memoize করা।" }
    ],
  },

  // ---- 1-D Dynamic Programming ----
  {
    id: "dsa-1d-dp",
    subject: "dsa",
    title: "1-D Dynamic Programming",
    bangla: "ওয়ান-ডি ডায়নামিক প্রোগ্রামিং",
    difficulty: "Hard",
    est: "3 hr",
    summary: "1-D DP-তে 1D array দিয়ে subproblems memoize করা হয়।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      { type: "p", text: "Dynamic Programming হলো এমন একটি technique যেখানে complex problem-কে ছোট subproblems-এ ভাগ করে, প্রতিটি subproblem একবার solve করে ফলাফল store (memoize) করা হয়। Real-life thinking — Fibonacci! fib(n) = fib(n-1) + fib(n-2)। বারবার একই subproblem solve না করে store করে রাখো।" },
      { type: "callout", calloutTone: "tip", text: "Tip: পরের topic হলো Intervals — overlapping ও merging interval problems।" }
    ],
  },

  // ---- Intervals ----
  {
    id: "dsa-intervals",
    subject: "dsa",
    title: "Intervals",
    bangla: "ইন্টারভালস",
    difficulty: "Medium",
    est: "1.5 hr",
    summary: "Interval problems-এ start ও end time দিয়ে overlap check করা হয়।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      { type: "p", text: "Interval হলো একটি [start, end] pair। Common operations: merge overlapping intervals, insert new interval, find meeting rooms। Real-life thinking — calendar scheduling! প্রতিটি meeting একটি interval। Overlap হলে conflict।" },
      { type: "callout", calloutTone: "tip", text: "Tip: পরের topic হলো Greedy — locally optimal choice দিয়ে globally optimal solution।" }
    ],
  },

  // ---- Greedy ----
  {
    id: "dsa-greedy",
    subject: "dsa",
    title: "Greedy",
    bangla: "গ্রিডি",
    difficulty: "Medium",
    est: "2 hr",
    summary: "Greedy algorithm প্রতিটি step-এ locally optimal choice করে।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      { type: "p", text: "Greedy algorithm প্রতিটি step-এ সবচেয়ে ভালো বলে মনে হওয়া choice করে, আশা করে যে এটি globally optimal হবে। সব problem-এ কাজ করে না, কিন্তু যেখানে কাজ করে সেখানে খুব efficient। Real-life thinking — পকেটে যত বড় কয়েন আছে সেটাই আগে দাও (coin change)।" },
      { type: "callout", calloutTone: "tip", text: "Tip: পরের topic হলো Advanced Graphs — Union-Find, Dijkstra, ও topological sort।" }
    ],
  },

  // ---- Advanced Graphs ----
  {
    id: "dsa-advanced-graphs",
    subject: "dsa",
    title: "Advanced Graphs",
    bangla: "অ্যাডভান্সড গ্রাফস",
    difficulty: "Hard",
    est: "2.5 hr",
    summary: "Advanced graph algorithms — Union-Find, Dijkstra, topological sort।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      { type: "p", text: "Advanced graph algorithms include Union-Find (disjoint set), Dijkstra's shortest path, ও topological sort। Real-life thinking — network routing! Shortest path খুঁজে বের করো (Dijkstra), cycle detect করো (Union-Find), task scheduling order বের করো (topological sort)।" },
      { type: "callout", calloutTone: "tip", text: "Tip: পরের topic হলো 2-D Dynamic Programming — 2D table দিয়ে DP।" }
    ],
  },

  // ---- 2-D Dynamic Programming ----
  {
    id: "dsa-2d-dp",
    subject: "dsa",
    title: "2-D Dynamic Programming",
    bangla: "টু-ডি ডায়নামিক প্রোগ্রামিং",
    difficulty: "Hard",
    est: "3 hr",
    summary: "2-D DP-তে 2D table দিয়ে subproblems memoize করা হয়।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      { type: "p", text: "2-D DP-তে subproblems একটি 2D grid-এ represent করা হয়। সাধারণত path counting, string matching, বা grid problems-এ use হয়। Real-life thinking — chess! প্রতিটি position থেকে কতভাবে goal-এ যাওয়া যায়? DP table দিয়ে প্রতিটি cell-এর answer store করো।" },
      { type: "callout", calloutTone: "tip", text: "Tip: পরের topic হলো Bit Manipulation — bitwise operations দিয়ে efficient computation।" }
    ],
  },

  // ---- Bit Manipulation ----
  {
    id: "dsa-bit-manipulation",
    subject: "dsa",
    title: "Bit Manipulation",
    bangla: "বিট ম্যানিপুলেশন",
    difficulty: "Medium",
    est: "1.5 hr",
    summary: "Bit manipulation-এ bitwise operations দিয়ে efficient computation করা হয়।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      { type: "p", text: "Bit manipulation হলো bitwise operations (AND, OR, XOR, shift) ব্যবহার করে দ্রুত computation। এটি O(1)-এ অনেক কাজ করতে পারে যেমন: কোনো number power of 2 কিনা, single number find (XOR), বা bit counting। Real-life thinking — switchboard! প্রতিটি switch একটি bit। On/off দিয়ে 32টি switch একটি integer-এ represent করা যায়।" },
      { type: "callout", calloutTone: "tip", text: "Tip: শেষ topic হলো Math & Geometry — mathematical ও geometric problems।" }
    ],
  },

  // ---- Math & Geometry ----
  {
    id: "dsa-math-geometry",
    subject: "dsa",
    title: "Math & Geometry",
    bangla: "ম্যাথ ও জিওমেট্রি",
    difficulty: "Medium",
    est: "2 hr",
    summary: "Math & Geometry problems-এ mathematical formulas ও coordinate geometry use করা হয়।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      { type: "p", text: "Math & Geometry problems include prime numbers, GCD/LCM, coordinate geometry, ও matrix operations। Real-life thinking — GPS coordinates! দুটি point-এর মধ্যে distance, area of polygon, বা rotation matrix — সবই math ও geometry।" },
      { type: "callout", calloutTone: "tip", text: "Tip: এই NeetCode roadmap-এর সব ১৮টি topic complete! এখন practice করো এবং patterns recognize করতে শেখো।" }
    ],
  }
];
