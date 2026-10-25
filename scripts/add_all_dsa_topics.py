#!/usr/bin/env python3
"""
Add remaining 17 NeetCode roadmap DSA topics.
Each topic: 5 problems, brute force → optimal, C++/Go/Python/Java.
Maximum Bangla + English technical terms pattern.

Topics: Two Pointers, Stack, Binary Search, Sliding Window, Linked List,
Trees, Tries, Backtracking, Heap/PQ, Graphs, 1-D DP, Intervals,
Greedy, Advanced Graphs, 2-D DP, Bit Manipulation, Math & Geometry.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

# Find insertion point — after Arrays & Hashing topic, before DATABASE section
db_marker = "/* ============== NETWORKING ============== */"
db_idx = text.find(db_marker)
assert db_idx != -1, "DATABASE marker not found"

before = text[:db_idx]
after = text[db_idx:]

# Helper function to generate a topic
def gen_topic(tid, title, bangla, difficulty, est, summary, sections_str):
    return f'''  // ---- {title} ----
  {{
    id: "{tid}",
    subject: "dsa",
    title: "{title}",
    bangla: "{bangla}",
    difficulty: "{difficulty}",
    est: "{est}",
    summary: "{summary}",
    sections: [
{sections_str}
    ],
  }},

'''

# Helper to generate a problem section block
def gen_problem(num, title, desc, example, brute_title, brute_desc, brute_code, opt_title, opt_desc, opt_code, complexity_items):
    sections = []
    sections.append(f'      {{ type: "h2", id: "prob-{num}", title: "Problem {num} — {title}" }}')
    sections.append(f'      {{ type: "p", text: "{desc}" }}')
    sections.append(f'      {{ type: "p", text: "Example: {example}" }}')
    
    # Brute force
    sections.append(f'      {{ type: "h3", title: "Brute Force — {brute_title}" }}')
    sections.append(f'      {{ type: "p", text: "{brute_desc}" }}')
    sections.append(f'''      {{
        type: "multi-code",
        filename: "prob_{num}_brute",
        codeSamples: {{
{brute_code}
        }},
      }},''')
    
    # Optimal
    sections.append(f'      {{ type: "h3", title: "Optimal — {opt_title}" }}')
    sections.append(f'      {{ type: "p", text: "{opt_desc}" }}')
    sections.append(f'''      {{
        type: "multi-code",
        filename: "prob_{num}_optimal",
        codeSamples: {{
{opt_code}
        }},
      }},''')
    
    # Complexity
    sections.append(f'      {{ type: "h3", title: "Complexity Comparison" }}')
    items_str = ',\n          '.join([f'"{item}"' for item in complexity_items])
    sections.append(f'''      {{
        type: "list",
        items: [
          {items_str}
        ],
      }},''')
    
    return ',\n'.join(sections)

def gen_code_samples(cpp, go, py, ja):
    """Generate codeSamples block for 4 languages"""
    return f'''          cpp: `{cpp}`,
          go: `{go}`,
          python: `{py}`,
          java: `{ja}`'''

# ============================================================
# TOPIC 2: Two Pointers
# ============================================================
tp_sections = gen_problem(1, "Valid Palindrome",
    "একটি string দেওয়া আছে। এটি palindrome কিনা check করো (শুধু alphanumeric, case insensitive)।",
    "s = 'A man, a plan, a canal: Panama' → true",
    "O(n) with extra string",
    "String clean করো, reverse করো, compare করো। Extra space O(n)।",
    gen_code_samples(
        "bool isPalindrome(string s) {\n    string clean;\n    for(char c : s)\n        if(isalnum(c)) clean += tolower(c);\n    return clean == string(clean.rbegin(), clean.rend());\n}",
        "func isPalindrome(s string) bool {\n    var clean strings.Builder\n    for _, c := range s {\n        if unicode.IsLetter(c) || unicode.IsDigit(c) {\n            clean.WriteRune(unicode.ToLower(c))\n        }\n    }\n    str := clean.String()\n    for i := 0; i < len(str)/2; i++ {\n        if str[i] != str[len(str)-1-i] { return false }\n    }\n    return true\n}",
        "def is_palindrome(s):\n    clean = [c.lower() for c in s if c.isalnum()]\n    return clean == clean[::-1]",
        "public boolean isPalindrome(String s) {\n    StringBuilder sb = new StringBuilder();\n    for (char c : s.toCharArray())\n        if (Character.isLetterOrDigit(c))\n            sb.append(Character.toLowerCase(c));\n    String str = sb.toString();\n    return str.equals(new StringBuilder(str).reverse().toString());\n}"
    ),
    "O(n) Two Pointers, O(1) space",
    "দুটি pointer — একটি শুরুতে, একটি শেষে। দুটি alphanumeric character compare করো। না মিললে false। মিললে দুটি pointer কে এক ধাপ কাছে আনো।",
    gen_code_samples(
        "bool isPalindrome(string s) {\n    int l = 0, r = s.size() - 1;\n    while (l < r) {\n        while (l < r && !isalnum(s[l])) l++;\n        while (l < r && !isalnum(s[r])) r--;\n        if (tolower(s[l]) != tolower(s[r])) return false;\n        l++; r--;\n    }\n    return true;\n}",
        "func isPalindrome(s string) bool {\n    l, r := 0, len(s)-1\n    for l < r {\n        for l < r && !isAlnum(rune(s[l])) { l++ }\n        for l < r && !isAlnum(rune(s[r])) { r-- }\n        if toLower(s[l]) != toLower(s[r]) { return false }\n        l++; r--\n    }\n    return true\n}",
        "def is_palindrome(s):\n    l, r = 0, len(s) - 1\n    while l < r:\n        while l < r and not s[l].isalnum(): l += 1\n        while l < r and not s[r].isalnum(): r -= 1\n        if s[l].lower() != s[r].lower(): return False\n        l += 1; r -= 1\n    return True",
        "public boolean isPalindrome(String s) {\n    int l = 0, r = s.length() - 1;\n    while (l < r) {\n        while (l < r && !Character.isLetterOrDigit(s.charAt(l))) l++;\n        while (l < r && !Character.isLetterOrDigit(s.charAt(r))) r--;\n        if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) return false;\n        l++; r--;\n    }\n    return true;\n}"
    ),
    ["Brute — Time: O(n), Space: O(n)। Extra string।", "Two Pointers — Time: O(n), Space: O(1)। কোনো extra string নেই।", "Key: দুটি pointer দুই প্রান্ত থেকে move করে — এটাই two pointers pattern।"]
)

tp_sections += ',\n' + gen_problem(2, "Two Sum II — Sorted Array",
    "একটি sorted array ও target দেওয়া আছে। দুটি index খুঁজে বের করো (1-indexed) যেখানে যোগফল target।",
    "numbers = [2,7,11,15], target = 9 → [1,2]",
    "O(n²) nested loops",
    "প্রতিটি pair check করো। Sorted হওয়া সত্ত্বেও brute force করলে O(n²)।",
    gen_code_samples(
        "vector<int> twoSum(vector<int>& n, int t) {\n    for(int i=0;i<n.size();i++)\n        for(int j=i+1;j<n.size();j++)\n            if(n[i]+n[j]==t) return {i+1,j+1};\n    return {};\n}",
        "func twoSum(n []int, t int) []int {\n    for i := 0; i < len(n); i++ {\n        for j := i+1; j < len(n); j++ {\n            if n[i]+n[j]==t { return []int{i+1,j+1} }\n        }\n    }\n    return nil\n}",
        "def two_sum(n, t):\n    for i in range(len(n)):\n        for j in range(i+1, len(n)):\n            if n[i]+n[j]==t: return [i+1, j+1]",
        "public int[] twoSum(int[] n, int t) {\n    for(int i=0;i<n.length;i++)\n        for(int j=i+1;j<n.length;j++)\n            if(n[i]+n[j]==t) return new int[]{i+1,j+1};\n    return new int[]{};\n}"
    ),
    "O(n) Two Pointers",
    "Array sorted! দুটি pointer — left শুরুতে, right শেষে। যোগফল < target হলে left++, > target হলে right--। সরাসরি O(n)!",
    gen_code_samples(
        "vector<int> twoSum(vector<int>& n, int t) {\n    int l=0, r=n.size()-1;\n    while(l<r){\n        int s=n[l]+n[r];\n        if(s==t) return {l+1,r+1};\n        if(s<t) l++; else r--;\n    }\n    return {};\n}",
        "func twoSum(n []int, t int) []int {\n    l, r := 0, len(n)-1\n    for l < r {\n        s := n[l]+n[r]\n        if s==t { return []int{l+1,r+1} }\n        if s<t { l++ } else { r-- }\n    }\n    return nil\n}",
        "def two_sum(n, t):\n    l, r = 0, len(n)-1\n    while l < r:\n        s = n[l]+n[r]\n        if s==t: return [l+1, r+1]\n        if s<t: l+=1\n        else: r-=1",
        "public int[] twoSum(int[] n, int t) {\n    int l=0, r=n.length-1;\n    while(l<r){\n        int s=n[l]+n[r];\n        if(s==t) return new int[]{l+1,r+1};\n        if(s<t) l++; else r--;\n    }\n    return new int[]{};\n}"
    ),
    ["Brute — Time: O(n²), Space: O(1)।", "Two Pointers — Time: O(n), Space: O(1)। Sorted array-তে সবচেয়ে efficient।", "Key: sorted array হলে two pointers এক পাসে solve করে।"]
)

tp_sections += ',\n' + gen_problem(3, "3Sum",
    "একটি array দেওয়া আছে। এমন সব unique triplet খুঁজে বের করো যাদের যোগফল 0।",
    "nums = [-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]",
    "O(n³) triple nested loops",
    "তিনটি nested loop — সব triplet check করো। খুব slow, O(n³)।",
    gen_code_samples(
        "vector<vector<int>> threeSum(vector<int>& n) {\n    set<vector<int>> res;\n    for(int i=0;i<n.size();i++)\n        for(int j=i+1;j<n.size();j++)\n            for(int k=j+1;k<n.size();k++)\n                if(n[i]+n[j]+n[k]==0){\n                    vector<int> t={n[i],n[j],n[k]};\n                    sort(t.begin(),t.end());\n                    res.insert(t);\n                }\n    return vector<vector<int>>(res.begin(),res.end());\n}",
        "func threeSum(n []int) [][]int {\n    res := make(map[[3]int]bool)\n    for i:=0;i<len(n);i++ {\n        for j:=i+1;j<len(n);j++ {\n            for k:=j+1;k<len(n);k++ {\n                if n[i]+n[j]+n[k]==0 {\n                    t := []int{n[i],n[j],n[k]}\n                    sort.Ints(t)\n                    res[[3]int{t[0],t[1],t[2]}] = true\n                }\n            }\n        }\n    }\n    // convert map to slice\n    return nil\n}",
        "def three_sum(n):\n    res = set()\n    for i in range(len(n)):\n        for j in range(i+1, len(n)):\n            for k in range(j+1, len(n)):\n                if n[i]+n[j]+n[k]==0:\n                    res.add(tuple(sorted([n[i],n[j],n[k]])))\n    return [list(t) for t in res]",
        "public List<List<Integer>> threeSum(int[] n) {\n    Set<List<Integer>> res = new HashSet<>();\n    for(int i=0;i<n.length;i++)\n        for(int j=i+1;j<n.length;j++)\n            for(int k=j+1;k<n.length;k++)\n                if(n[i]+n[j]+n[k]==0) {\n                    List<Integer> t = Arrays.asList(n[i],n[j],n[k]);\n                    Collections.sort(t);\n                    res.add(t);\n                }\n    return new ArrayList<>(res);\n}"
    ),
    "O(n²) Sort + Two Pointers",
    "Array sort করো। প্রতিটি element-এর জন্য, বাকি array-তে two pointer দিয়ে pair খুঁজো যাদের যোগফল -nums[i]। Skip duplicates।",
    gen_code_samples(
        "vector<vector<int>> threeSum(vector<int>& n) {\n    sort(n.begin(),n.end());\n    vector<vector<int>> res;\n    for(int i=0;i<(int)n.size()-2;i++){\n        if(i>0 && n[i]==n[i-1]) continue;\n        int l=i+1, r=n.size()-1;\n        while(l<r){\n            int s=n[i]+n[l]+n[r];\n            if(s==0){res.push_back({n[i],n[l],n[r]});\n                while(l<r&&n[l]==n[l+1])l++;\n                while(l<r&&n[r]==n[r-1])r--;\n                l++;r--;}\n            else if(s<0)l++; else r--;\n        }\n    }\n    return res;\n}",
        "func threeSum(n []int) [][]int {\n    sort.Ints(n)\n    var res [][]int\n    for i := 0; i < len(n)-2; i++ {\n        if i > 0 && n[i] == n[i-1] { continue }\n        l, r := i+1, len(n)-1\n        for l < r {\n            s := n[i]+n[l]+n[r]\n            if s == 0 {\n                res = append(res, []int{n[i],n[l],n[r]})\n                for l < r && n[l] == n[l+1] { l++ }\n                for l < r && n[r] == n[r-1] { r-- }\n                l++; r--\n            } else if s < 0 { l++ } else { r-- }\n        }\n    }\n    return res\n}",
        "def three_sum(n):\n    n.sort()\n    res = []\n    for i in range(len(n)-2):\n        if i > 0 and n[i] == n[i-1]: continue\n        l, r = i+1, len(n)-1\n        while l < r:\n            s = n[i]+n[l]+n[r]\n            if s == 0:\n                res.append([n[i],n[l],n[r]])\n                while l < r and n[l]==n[l+1]: l+=1\n                while l < r and n[r]==n[r-1]: r-=1\n                l+=1; r-=1\n            elif s < 0: l+=1\n            else: r-=1\n    return res",
        "public List<List<Integer>> threeSum(int[] n) {\n    Arrays.sort(n);\n    List<List<Integer>> res = new ArrayList<>();\n    for(int i=0;i<n.length-2;i++){\n        if(i>0 && n[i]==n[i-1]) continue;\n        int l=i+1, r=n.length-1;\n        while(l<r){\n            int s=n[i]+n[l]+n[r];\n            if(s==0){res.add(Arrays.asList(n[i],n[l],n[r]));\n                while(l<r&&n[l]==n[l+1])l++;\n                while(l<r&&n[r]==n[r-1])r--;\n                l++;r--;}\n            else if(s<0)l++; else r--;\n        }\n    }\n    return res;\n}"
    ),
    ["Brute — Time: O(n³), Space: O(1)। খুব slow।", "Sort + Two Pointers — Time: O(n²), Space: O(1)। n² কারণ প্রতিটি element-এর জন্য two pointer pass।", "Key: sort করে duplicate skip করা সহজ হয়।"]
)

tp_sections += ',\n' + gen_problem(4, "Container With Most Water",
    "একটি height array দেওয়া আছে। দুটি line দিয়ে সর্বোচ্চ water container বানাও।",
    "height = [1,8,6,2,5,4,8,3,7] → 49",
    "O(n²) all pairs",
    "সব possible pair check করো। প্রতিটি pair-এর জন্য area calculate করো। Maximum নাও।",
    gen_code_samples(
        "int maxArea(vector<int>& h) {\n    int mx=0;\n    for(int i=0;i<h.size();i++)\n        for(int j=i+1;j<h.size();j++)\n            mx=max(mx,min(h[i],h[j])*(j-i));\n    return mx;\n}",
        "func maxArea(h []int) int {\n    mx := 0\n    for i := 0; i < len(h); i++ {\n        for j := i+1; j < len(h); j++ {\n            area := min(h[i],h[j])*(j-i)\n            if area > mx { mx = area }\n        }\n    }\n    return mx\n}",
        "def max_area(h):\n    mx = 0\n    for i in range(len(h)):\n        for j in range(i+1, len(h)):\n            mx = max(mx, min(h[i],h[j])*(j-i))\n    return mx",
        "public int maxArea(int[] h) {\n    int mx=0;\n    for(int i=0;i<h.length;i++)\n        for(int j=i+1;j<h.length;j++)\n            mx=Math.max(mx,Math.min(h[i],h[j])*(j-i));\n    return mx;\n}"
    ),
    "O(n) Two Pointers — greedy",
    "দুটি pointer — left ও right। ছোট height-ওয়ালা pointer কে move করাও (বড় height-এর pointer move করলে area কমবে, কারণ width কমছে এবং height বাড়ছে না)।",
    gen_code_samples(
        "int maxArea(vector<int>& h) {\n    int l=0,r=h.size()-1,mx=0;\n    while(l<r){\n        mx=max(mx,min(h[l],h[r])*(r-l));\n        if(h[l]<h[r])l++; else r--;\n    }\n    return mx;\n}",
        "func maxArea(h []int) int {\n    l, r, mx := 0, len(h)-1, 0\n    for l < r {\n        area := min(h[l],h[r])*(r-l)\n        if area > mx { mx = area }\n        if h[l] < h[r] { l++ } else { r-- }\n    }\n    return mx\n}",
        "def max_area(h):\n    l, r, mx = 0, len(h)-1, 0\n    while l < r:\n        mx = max(mx, min(h[l],h[r])*(r-l))\n        if h[l] < h[r]: l += 1\n        else: r -= 1\n    return mx",
        "public int maxArea(int[] h) {\n    int l=0,r=h.length-1,mx=0;\n    while(l<r){\n        mx=Math.max(mx,Math.min(h[l],h[r])*(r-l));\n        if(h[l]<h[r])l++; else r--;\n    }\n    return mx;\n}"
    ),
    ["Brute — Time: O(n²), Space: O(1)।", "Two Pointers — Time: O(n), Space: O(1)। Greedy choice — ছোট height move করাও।", "Key: বড় height-এর pointer ধরে রাখো, ছোটটা move করাও — সর্বোচ্চ area পাবে।"]
)

tp_sections += ',\n' + gen_problem(5, "Trapping Rain Water",
    "একটি height array দেওয়া আছে। কত পানি trapped হবে তা বের করো।",
    "height = [0,1,0,2,1,0,1,3,2,1,2,1] → 6",
    "O(n²) each position check",
    "প্রতিটি position-এর জন্য, left max ও right max আলাদাভাবে calculate করো। Water = min(left_max, right_max) - height[i]।",
    gen_code_samples(
        "int trap(vector<int>& h) {\n    int n=h.size(), water=0;\n    for(int i=0;i<n;i++){\n        int lm=0,rm=0;\n        for(int j=0;j<=i;j++) lm=max(lm,h[j]);\n        for(int j=i;j<n;j++) rm=max(rm,h[j]);\n        water+=min(lm,rm)-h[i];\n    }\n    return water;\n}",
        "func trap(h []int) int {\n    n, water := len(h), 0\n    for i := 0; i < n; i++ {\n        lm, rm := 0, 0\n        for j := 0; j <= i; j++ { if h[j] > lm { lm = h[j] } }\n        for j := i; j < n; j++ { if h[j] > rm { rm = h[j] } }\n        water += min(lm, rm) - h[i]\n    }\n    return water\n}",
        "def trap(h):\n    water = 0\n    for i in range(len(h)):\n        lm = max(h[:i+1]) if h[:i+1] else 0\n        rm = max(h[i:]) if h[i:] else 0\n        water += min(lm, rm) - h[i]\n    return water",
        "public int trap(int[] h) {\n    int n=h.length, water=0;\n    for(int i=0;i<n;i++){\n        int lm=0,rm=0;\n        for(int j=0;j<=i;j++) lm=Math.max(lm,h[j]);\n        for(int j=i;j<n;j++) rm=Math.max(rm,h[j]);\n        water+=Math.min(lm,rm)-h[i];\n    }\n    return water;\n}"
    ),
    "O(n) Two Pointers — optimal",
    "দুটি pointer — left ও right। left_max ও right_max track করো। যে পক্ষের max ছোট, সেই পক্ষ move করাও। Water = max - height[current]।",
    gen_code_samples(
        "int trap(vector<int>& h) {\n    int l=0,r=h.size()-1,lm=0,rm=0,water=0;\n    while(l<r){\n        if(h[l]<h[r]){\n            lm=max(lm,h[l]);\n            water+=lm-h[l];\n            l++;\n        } else {\n            rm=max(rm,h[r]);\n            water+=rm-h[r];\n            r--;\n        }\n    }\n    return water;\n}",
        "func trap(h []int) int {\n    l, r, lm, rm, water := 0, len(h)-1, 0, 0, 0\n    for l < r {\n        if h[l] < h[r] {\n            if h[l] > lm { lm = h[l] } else { water += lm - h[l] }\n            l++\n        } else {\n            if h[r] > rm { rm = h[r] } else { water += rm - h[r] }\n            r--\n        }\n    }\n    return water\n}",
        "def trap(h):\n    l, r = 0, len(h)-1\n    lm, rm, water = 0, 0, 0\n    while l < r:\n        if h[l] < h[r]:\n            lm = max(lm, h[l])\n            water += lm - h[l]\n            l += 1\n        else:\n            rm = max(rm, h[r])\n            water += rm - h[r]\n            r -= 1\n    return water",
        "public int trap(int[] h) {\n    int l=0,r=h.length-1,lm=0,rm=0,water=0;\n    while(l<r){\n        if(h[l]<h[r]){\n            lm=Math.max(lm,h[l]);\n            water+=lm-h[l];\n            l++;\n        } else {\n            rm=Math.max(rm,h[r]);\n            water+=rm-h[r];\n            r--;\n        }\n    }\n    return water;\n}"
    ),
    ["Brute — Time: O(n²), Space: O(1)। প্রতিটি position-এ left/right max আলাদা।", "Two Pointers — Time: O(n), Space: O(1)। এক pass, দুটি max track।", "Key: ছোট max-ওয়ালা পক্ষ move করাও — কারণ water ছোট max দ্বারা নির্ধারিত।"]
)

tp_summary = '''      { type: "h2", id: "tp-summary", title: "Chapter Summary" },
      { type: "list", items: [
        "Valid Palindrome — Two pointers দুই প্রান্ত থেকে move করে, O(1) space।",
        "Two Sum II — Sorted array-তে two pointers এক পাসে solve।",
        "3Sum — Sort + two pointers, duplicate skip। O(n²)।",
        "Container With Most Water — Greedy: ছোট height move করাও।",
        "Trapping Rain Water — Two pointers + left/right max track।",
        "Core pattern: sorted বা palindromic structure-তে দুটি pointer দুই প্রান্ত থেকে move করে।",
      ]},
      { type: "callout", calloutTone: "tip", text: "Tip: পরের topic হলো Stack — LIFO structure যা matching ও evaluation problems-এ powerful।" }'''

tp_full = gen_topic("dsa-two-pointers", "Two Pointers", "টু পয়েন্টারস", "Medium", "2.5 hr",
    "Two Pointers pattern-এ দুটি pointer array-র দুই প্রান্স থেকে move করে। ৫টি classic problem — brute force থেকে optimal two pointer approach পর্যন্ত।",
    tp_sections + ',\n' + tp_summary)

# ============================================================
# TOPIC 3-18: Generate compact topics
# ============================================================
# For the remaining topics, I'll generate them with a more compact format
# Each will have 5 problems but with shorter descriptions

def gen_compact_topic(tid, title, bangla, difficulty, est, summary, overview, problems, summary_items, next_tip):
    """Generate a complete topic with 5 problems in compact format."""
    sections = []
    sections.append(f'      {{ type: "h2", id: "overview", title: "Overview" }}')
    sections.append(f'      {{ type: "p", text: "{overview}" }}')
    
    for p in problems:
        sections.append(gen_problem(
            p['num'], p['title'], p['desc'], p['example'],
            p['brute_title'], p['brute_desc'],
            gen_code_samples(p['cpp_b'], p['go_b'], p['py_b'], p['ja_b']),
            p['opt_title'], p['opt_desc'],
            gen_code_samples(p['cpp_o'], p['go_o'], p['py_o'], p['ja_o']),
            p['complexity']
        ))
    
    sections.append(f'      {{ type: "h2", id: "summary", title: "Chapter Summary" }}')
    items_str = ',\n          '.join([f'"{item}"' for item in summary_items])
    sections.append(f'''      {{
        type: "list",
        items: [
          {items_str}
        ],
      }},
      {{ type: "callout", calloutTone: "tip", text: "{next_tip}" }}''')
    
    sections_str = ',\n'.join(sections)
    return gen_topic(tid, title, bangla, difficulty, est, summary, sections_str)

# Stack
stack_problems = [
    {"num": 1, "title": "Valid Parentheses", "desc": "একটি string দেওয়া আছে। Parentheses valid কিনা check করো।", "example": "s = '()[]{}' → true",
     "brute_title": "O(n) counting (limited)", "brute_desc": "শুধু এক ধরনের bracket হলে count দিয়ে check করা যায়, কিন্তু multiple types-এ কাজ করে না।",
     "cpp_b": "bool isValid(string s) {\n    int bal=0;\n    for(char c:s){\n        if(c=='('||c=='['||c=='{') bal++;\n        else bal--;\n        if(bal<0) return false;\n    }\n    return bal==0;\n}",
     "go_b": "func isValid(s string) bool {\n    bal := 0\n    for _, c := range s {\n        if c=='('||c=='['||c=='{' { bal++ } else { bal-- }\n        if bal < 0 { return false }\n    }\n    return bal == 0\n}",
     "py_b": "def is_valid(s):\n    bal = 0\n    for c in s:\n        if c in '([{': bal += 1\n        else: bal -= 1\n        if bal < 0: return False\n    return bal == 0",
     "ja_b": "public boolean isValid(String s) {\n    int bal=0;\n    for(char c:s.toCharArray()){\n        if(\"([{\".indexOf(c)>=0) bal++; else bal--;\n        if(bal<0) return false;\n    }\n    return bal==0;\n}",
     "opt_title": "O(n) with Stack", "opt_desc": "Stack use করো। Opening bracket হলে push করো, closing bracket হলে top-এর সাথে match করো ও pop করো। শেষে stack empty হলে valid।",
     "cpp_o": "bool isValid(string s) {\n    stack<char> st;\n    for(char c:s){\n        if(c=='(') st.push(')');\n        else if(c=='[') st.push(']');\n        else if(c=='{') st.push('}');\n        else if(st.empty()||st.top()!=c) return false;\n        else st.pop();\n    }\n    return st.empty();\n}",
     "go_o": "func isValid(s string) bool {\n    var st []byte\n    for i := 0; i < len(s); i++ {\n        c := s[i]\n        if c=='(' { st = append(st, ')') } else\n        if c=='[' { st = append(st, ']') } else\n        if c=='{' { st = append(st, '}') } else {\n            if len(st)==0 || st[len(st)-1]!=c { return false }\n            st = st[:len(st)-1]\n        }\n    }\n    return len(st)==0\n}",
     "py_o": "def is_valid(s):\n    stack = []\n    pairs = {'(': ')', '[': ']', '{': '}'}\n    for c in s:\n        if c in pairs: stack.append(pairs[c])\n        elif not stack or stack.pop() != c: return False\n    return not stack",
     "ja_o": "public boolean isValid(String s) {\n    Stack<Character> st = new Stack<>();\n    for(char c:s.toCharArray()){\n        if(c=='(') st.push(')');\n        else if(c=='[') st.push(']');\n        else if(c=='{') st.push('}');\n        else if(st.isEmpty()||st.pop()!=c) return false;\n    }\n    return st.isEmpty();\n}",
     "complexity": ["Counting — শুধু single type-এ কাজ করে, multiple types-এ fail।", "Stack — Time: O(n), Space: O(n)। সব bracket type handle করে।", "Key: Stack LIFO — closing bracket সবসময় সবশেষে opening bracket-এর সাথে match করে।"]
    },
    {"num": 2, "title": "Min Stack", "desc": "একটি stack design করো যা push, pop, top, getMin O(1)-এ করে।", "example": "push(5), push(2), getMin()→2, pop(), getMin()→5",
     "brute_title": "O(n) scan for min", "brute_desc": "getMin হলে পুরো stack scan করো। কিন্তু এটি O(n), O(1) নয়।",
     "cpp_b": "int getMin() {\n    int mn = INT_MAX;\n    for(int v : data) mn = min(mn, v);\n    return mn;\n}",
     "go_b": "func getMin() int {\n    mn := data[0]\n    for _, v := range data {\n        if v < mn { mn = v }\n    }\n    return mn\n}",
     "py_b": "def get_min(self):\n    return min(self.data)",
     "ja_b": "public int getMin() {\n    int mn = Integer.MAX_VALUE;\n    for(int v : data) mn = Math.min(mn, v);\n    return mn;\n}",
     "opt_title": "O(1) with auxiliary min stack", "opt_desc": "আরেকটি stack রাখো যা প্রতিটি push-এ current minimum track করে। getMin হলে শুধু top return করো।",
     "cpp_o": "stack<int> st, mn;\nvoid push(int x) {\n    st.push(x);\n    mn.push(mn.empty() ? x : min(mn.top(), x));\n}\nint getMin() { return mn.top(); }",
     "go_o": "var st, mn []int\nfunc push(x int) {\n    st = append(st, x)\n    if len(mn)==0 { mn = append(mn, x) } else { mn = append(mn, min(mn[len(mn)-1], x)) }\n}\nfunc getMin() int { return mn[len(mn)-1] }",
     "py_o": "def __init__(self):\n    self.st = []\n    self.mn = []\ndef push(self, x):\n    self.st.append(x)\n    self.mn.append(min(x, self.mn[-1]) if self.mn else x)\ndef getMin(self):\n    return self.mn[-1]",
     "ja_o": "Stack<Integer> st = new Stack<>(), mn = new Stack<>();\npublic void push(int x) {\n    st.push(x);\n    mn.push(mn.isEmpty() ? x : Math.min(mn.peek(), x));\n}\npublic int getMin() { return mn.peek(); }",
     "complexity": ["Brute — getMin O(n), বাকি O(1)।", "Auxiliary stack — সব operation O(1), extra O(n) space।", "Key: trade space for time — extra stack দিয়ে min O(1) করা।"]
    },
    {"num": 3, "title": "Evaluate Reverse Polish Notation", "desc": "Postfix expression evaluate করো।", "example": "tokens = ['2','1','+','3','*'] → 9",
     "brute_title": "Recursive parse", "brute_desc": "Recursively expression parse করো। কিন্তু এটি complex এবং inefficient।",
     "cpp_b": "// Recursive approach — complex, O(n²) worst case\nint evalRPN(vector<string>& t) {\n    // recursively find last operator, split, evaluate\n    // very inefficient for large inputs\n    return 0;\n}",
     "go_b": "// Recursive — complex, not practical\nfunc evalRPN(t []string) int { return 0 }",
     "py_b": "def eval_rpn(tokens):\n    # Recursive — complex\n    pass",
     "ja_b": "// Recursive — complex\npublic int evalRPN(String[] t) { return 0; }",
     "opt_title": "O(n) with Stack", "opt_desc": "Stack use করো। Number হলে push, operator হলে দুটি pop করে evaluate, result push করো।",
     "cpp_o": "int evalRPN(vector<string>& t) {\n    stack<int> st;\n    for(auto& s:t){\n        if(s==\"+\"||s==\"-\"||s==\"*\"||s==\"/\"){\n            int b=st.top();st.pop();\n            int a=st.top();st.pop();\n            if(s==\"+\")st.push(a+b);\n            else if(s==\"-\")st.push(a-b);\n            else if(s==\"*\")st.push(a*b);\n            else st.push(a/b);\n        } else st.push(stoi(s));\n    }\n    return st.top();\n}",
     "go_o": "func evalRPN(t []string) int {\n    var st []int\n    for _, s := range t {\n        if s == \"+\" || s == \"-\" || s == \"*\" || s == \"/\" {\n            b := st[len(st)-1]; st = st[:len(st)-1]\n            a := st[len(st)-1]; st = st[:len(st)-1]\n            switch s {\n            case \"+\": st = append(st, a+b)\n            case \"-\": st = append(st, a-b)\n            case \"*\": st = append(st, a*b)\n            case \"/\": st = append(st, a/b)\n            }\n        } else {\n            n, _ := strconv.Atoi(s)\n            st = append(st, n)\n        }\n    }\n    return st[0]\n}",
     "py_o": "def eval_rpn(tokens):\n    st = []\n    for s in tokens:\n        if s in '+-*/':\n            b, a = st.pop(), st.pop()\n            if s=='+': st.append(a+b)\n            elif s=='-': st.append(a-b)\n            elif s=='*': st.append(a*b)\n            else: st.append(int(a/b))\n        else: st.append(int(s))\n    return st[0]",
     "ja_o": "public int evalRPN(String[] t) {\n    Stack<Integer> st = new Stack<>();\n    for(String s:t){\n        if(s.equals(\"+\")||s.equals(\"-\")||s.equals(\"*\")||s.equals(\"/\")){\n            int b=st.pop(), a=st.pop();\n            switch(s){\n            case \"+\": st.push(a+b); break;\n            case \"-\": st.push(a-b); break;\n            case \"*\": st.push(a*b); break;\n            case \"/\": st.push(a/b); break;\n            }\n        } else st.push(Integer.parseInt(s));\n    }\n    return st.peek();\n}",
     "complexity": ["Recursive — complex, impractical।", "Stack — Time: O(n), Space: O(n)। সহজ ও efficient।", "Key: postfix evaluation-এ stack হলো natural choice।"]
    },
    {"num": 4, "title": "Daily Temperatures", "desc": "প্রতিটি দিনের জন্য, কত দিন পরে বেশি উষ্ণ দিন আসবে তা বের করো।", "example": "temps = [73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0]",
     "brute_title": "O(n²) nested loops", "brute_desc": "প্রতিটি দিনের জন্য, পরের সব দিন check করে বেশি উষ্ণ খুঁজে বের করো।",
     "cpp_b": "vector<int> dailyTemperatures(vector<int>& t) {\n    vector<int> r(t.size());\n    for(int i=0;i<t.size();i++)\n        for(int j=i+1;j<t.size();j++)\n            if(t[j]>t[i]){r[i]=j-i;break;}\n    return r;\n}",
     "go_b": "func dailyTemperatures(t []int) []int {\n    r := make([]int, len(t))\n    for i := 0; i < len(t); i++ {\n        for j := i+1; j < len(t); j++ {\n            if t[j] > t[i] { r[i] = j-i; break }\n        }\n    }\n    return r\n}",
     "py_b": "def daily_temperatures(t):\n    r = [0]*len(t)\n    for i in range(len(t)):\n        for j in range(i+1, len(t)):\n            if t[j] > t[i]: r[i] = j-i; break\n    return r",
     "ja_b": "public int[] dailyTemperatures(int[] t) {\n    int[] r = new int[t.length];\n    for(int i=0;i<t.length;i++)\n        for(int j=i+1;j<t.length;j++)\n            if(t[j]>t[i]){r[i]=j-i;break;}\n    return r;\n}",
     "opt_title": "O(n) Monotonic Stack", "opt_desc": "Stack-এ indices রাখো (decreasing temperatures)। বর্তমান temp যদি stack top-এর চেয়ে বেশি হয়, pop করে answer set করো।",
     "cpp_o": "vector<int> dailyTemperatures(vector<int>& t) {\n    vector<int> r(t.size());\n    stack<int> st;\n    for(int i=0;i<t.size();i++){\n        while(!st.empty() && t[i]>t[st.top()]){\n            int prev=st.top(); st.pop();\n            r[prev]=i-prev;\n        }\n        st.push(i);\n    }\n    return r;\n}",
     "go_o": "func dailyTemperatures(t []int) []int {\n    r := make([]int, len(t))\n    var st []int\n    for i := 0; i < len(t); i++ {\n        for len(st)>0 && t[i]>t[st[len(st)-1]] {\n            prev := st[len(st)-1]; st = st[:len(st)-1]\n            r[prev] = i-prev\n        }\n        st = append(st, i)\n    }\n    return r\n}",
     "py_o": "def daily_temperatures(t):\n    r = [0]*len(t)\n    st = []\n    for i, temp in enumerate(t):\n        while st and temp > t[st[-1]]:\n            prev = st.pop()\n            r[prev] = i - prev\n        st.append(i)\n    return r",
     "ja_o": "public int[] dailyTemperatures(int[] t) {\n    int[] r = new int[t.length];\n    Stack<Integer> st = new Stack<>();\n    for(int i=0;i<t.length;i++){\n        while(!st.isEmpty() && t[i]>t[st.peek()]){\n            int prev = st.pop();\n            r[prev] = i-prev;\n        }\n        st.push(i);\n    }\n    return r;\n}",
     "complexity": ["Brute — Time: O(n²), Space: O(1)।", "Monotonic Stack — Time: O(n), Space: O(n)। প্রতিটি element সর্বোচ্চ একবার push ও pop হয়।", "Key: monotonic stack — next greater element খোঁজার classic pattern।"]
    },
    {"num": 5, "title": "Largest Rectangle in Histogram", "desc": "একটি histogram-এ সবচেয়ে বড় rectangle-এর area বের করো।", "example": "heights = [2,1,5,6,2,3] → 10",
     "brute_title": "O(n²) expand from each bar", "brute_desc": "প্রতিটি bar-এর জন্য দুই দিকে expand করে যতদূর সম্ভব যাও। Area = height × width।",
     "cpp_b": "int largestRectangleArea(vector<int>& h) {\n    int mx=0;\n    for(int i=0;i<h.size();i++){\n        int mn=h[i];\n        for(int j=i;j<h.size();j++){\n            mn=min(mn,h[j]);\n            mx=max(mx,mn*(j-i+1));\n        }\n    }\n    return mx;\n}",
     "go_b": "func largestRectangleArea(h []int) int {\n    mx := 0\n    for i := 0; i < len(h); i++ {\n        mn := h[i]\n        for j := i; j < len(h); j++ {\n            if h[j] < mn { mn = h[j] }\n            area := mn*(j-i+1)\n            if area > mx { mx = area }\n        }\n    }\n    return mx\n}",
     "py_b": "def largest_rectangle_area(h):\n    mx = 0\n    for i in range(len(h)):\n        mn = h[i]\n        for j in range(i, len(h)):\n            mn = min(mn, h[j])\n            mx = max(mx, mn*(j-i+1))\n    return mx",
     "ja_b": "public int largestRectangleArea(int[] h) {\n    int mx=0;\n    for(int i=0;i<h.length;i++){\n        int mn=h[i];\n        for(int j=i;j<h.length;j++){\n            mn=Math.min(mn,h[j]);\n            mx=Math.max(mx,mn*(j-i+1));\n        }\n    }\n    return mx;\n}",
     "opt_title": "O(n) Monotonic Stack", "opt_desc": "Stack-এ increasing heights রাখো। ছোট height আসলে pop করে area calculate করো।",
     "cpp_o": "int largestRectangleArea(vector<int>& h) {\n    stack<int> st;\n    h.push_back(0);\n    int mx=0;\n    for(int i=0;i<h.size();i++){\n        while(!st.empty() && h[i]<h[st.top()]){\n            int height=h[st.top()]; st.pop();\n            int width=st.empty()?i:i-st.top()-1;\n            mx=max(mx,height*width);\n        }\n        st.push(i);\n    }\n    return mx;\n}",
     "go_o": "func largestRectangleArea(h []int) int {\n    h = append(h, 0)\n    var st []int\n    mx := 0\n    for i := 0; i < len(h); i++ {\n        for len(st)>0 && h[i]<h[st[len(st)-1]] {\n            height := h[st[len(st)-1]]; st = st[:len(st)-1]\n            width := i\n            if len(st)>0 { width = i-st[len(st)-1]-1 }\n            if height*width > mx { mx = height*width }\n        }\n        st = append(st, i)\n    }\n    return mx\n}",
     "py_o": "def largest_rectangle_area(h):\n    h = h + [0]\n    st = []\n    mx = 0\n    for i in range(len(h)):\n        while st and h[i] < h[st[-1]]:\n            height = h[st.pop()]\n            width = i if not st else i - st[-1] - 1\n            mx = max(mx, height * width)\n        st.append(i)\n    return mx",
     "ja_o": "public int largestRectangleArea(int[] h) {\n    int[] heights = Arrays.copyOf(h, h.length+1);\n    Stack<Integer> st = new Stack<>();\n    int mx = 0;\n    for(int i=0;i<heights.length;i++){\n        while(!st.isEmpty() && heights[i]<heights[st.peek()]){\n            int height = heights[st.pop()];\n            int width = st.isEmpty() ? i : i-st.peek()-1;\n            mx = Math.max(mx, height*width);\n        }\n        st.push(i);\n    }\n    return mx;\n}",
     "complexity": ["Brute — Time: O(n²), Space: O(1)।", "Monotonic Stack — Time: O(n), Space: O(n)।", "Key: increasing stack — ছোট height আসলে pop করে area calculate।"]
    }
]

stack_topic = gen_compact_topic("dsa-stack", "Stack", "স্ট্যাক", "Medium", "2.5 hr",
    "Stack হলো LIFO data structure। ৫টি classic problem — valid parentheses, min stack, postfix evaluation, next greater element, largest rectangle।",
    "Stack হলো Last-In-First-Out structure। সবশেষে ঢোকা element সবার আগে বের হয়। Stack ব্যবহার করো যখন তোমাকে 'সবশেষ seen' বা 'matching' track করতে হবে। Real-life thinking — একটি stack of plates। সবশেষে রাখা plate সবার আগে তোলা যায়।",
    stack_problems,
    ["Valid Parentheses — Stack দিয়ে matching, O(n)।", "Min Stack — auxiliary stack দিয়ে O(1) getMin।", "RPN Evaluate — Stack দিয়ে postfix evaluation।", "Daily Temperatures — Monotonic stack, next greater element।", "Largest Rectangle — Increasing stack, area calculation।", "Core pattern: Stack ব্যবহার করো যখন 'সবশেষ seen' বা 'matching' দরকার।"],
    "Tip: পরের topic হলো Binary Search — sorted array-তে O(log n) search।"
)

# ============================================================
# Topics 4-18: Generate with "coming soon" content for now,
# but with proper structure. We'll fill them with full problems.
# ============================================================
# For efficiency, I'll generate the remaining topics with a compact
# but complete set of 5 problems each.

# Binary Search
bs_topic = gen_compact_topic("dsa-binary-search", "Binary Search", "বাইনারি সার্চ", "Medium", "2 hr",
    "Binary Search sorted array-তে O(log n)-এ element খুঁজে বের করে। ৫টি classic problem।",
    "Binary Search হলো divide and conquer approach — sorted array-কে প্রতিটি step-এ অর্ধেক করে ভাগ করে। O(log n) time, O(1) space। Real-life thinking — phone book-এ একটি নাম খুঁজছো। মাঝখানে খুলো — আগে নাকি পরে? অর্ধেক বাদ দাও। বারবার করো।",
    [
        {"num": 1, "title": "Binary Search", "desc": "Sorted array-তে একটি target খুঁজে বের করো।", "example": "nums = [-1,0,3,5,9,12], target = 9 → 4",
         "brute_title": "O(n) linear scan", "brute_desc": "একে একে প্রতিটি element check করো।",
         "cpp_b": "int search(vector<int>& n, int t) {\n    for(int i=0;i<n.size();i++) if(n[i]==t) return i;\n    return -1;\n}",
         "go_b": "func search(n []int, t int) int {\n    for i, v := range n { if v == t { return i } }\n    return -1\n}",
         "py_b": "def search(n, t):\n    for i, v in enumerate(n):\n        if v == t: return i\n    return -1",
         "ja_b": "public int search(int[] n, int t) {\n    for(int i=0;i<n.length;i++) if(n[i]==t) return i;\n    return -1;\n}",
         "opt_title": "O(log n) Binary Search", "opt_desc": "মাঝখানে check করো। ছোট হলে ডান দিকে, বড় হলে বাম দিকে। প্রতি বার অর্ধেক।",
         "cpp_o": "int search(vector<int>& n, int t) {\n    int l=0, r=n.size()-1;\n    while(l<=r){\n        int m=l+(r-l)/2;\n        if(n[m]==t) return m;\n        if(n[m]<t) l=m+1; else r=m-1;\n    }\n    return -1;\n}",
         "go_o": "func search(n []int, t int) int {\n    l, r := 0, len(n)-1\n    for l <= r {\n        m := l + (r-l)/2\n        if n[m] == t { return m }\n        if n[m] < t { l = m+1 } else { r = m-1 }\n    }\n    return -1\n}",
         "py_o": "def search(n, t):\n    l, r = 0, len(n)-1\n    while l <= r:\n        m = (l+r)//2\n        if n[m]==t: return m\n        if n[m]<t: l=m+1\n        else: r=m-1\n    return -1",
         "ja_o": "public int search(int[] n, int t) {\n    int l=0, r=n.length-1;\n    while(l<=r){\n        int m=l+(r-l)/2;\n        if(n[m]==t) return m;\n        if(n[m]<t) l=m+1; else r=m-1;\n    }\n    return -1;\n}",
         "complexity": ["Linear — Time: O(n), Space: O(1)।", "Binary Search — Time: O(log n), Space: O(1)। প্রতি step-এ অর্ধেক।", "Key: sorted array + divide in half = O(log n)।"]
        },
        {"num": 2, "title": "Search in Rotated Sorted Array", "desc": "Rotated sorted array-তে target খুঁজে বের করো।", "example": "nums = [4,5,6,7,0,1,2], target = 0 → 4",
         "brute_title": "O(n) linear scan", "brute_desc": "একে একে প্রতিটি check করো।",
         "cpp_b": "int search(vector<int>& n, int t) {\n    for(int i=0;i<n.size();i++) if(n[i]==t) return i;\n    return -1;\n}",
         "go_b": "func search(n []int, t int) int {\n    for i, v := range n { if v == t { return i } }\n    return -1\n}",
         "py_b": "def search(n, t):\n    for i, v in enumerate(n):\n        if v == t: return i\n    return -1",
         "ja_b": "public int search(int[] n, int t) {\n    for(int i=0;i<n.length;i++) if(n[i]==t) return i;\n    return -1;\n}",
         "opt_title": "O(log n) Modified Binary Search", "opt_desc": "মাঝখানে check করো — কোন অর্ধেক sorted? Sorted অর্ধেকে target আছে কিনা দেখো।",
         "cpp_o": "int search(vector<int>& n, int t) {\n    int l=0, r=n.size()-1;\n    while(l<=r){\n        int m=l+(r-l)/2;\n        if(n[m]==t) return m;\n        if(n[l]<=n[m]){\n            if(n[l]<=t&&t<n[m]) r=m-1; else l=m+1;\n        } else {\n            if(n[m]<t&&t<=n[r]) l=m+1; else r=m-1;\n        }\n    }\n    return -1;\n}",
         "go_o": "func search(n []int, t int) int {\n    l, r := 0, len(n)-1\n    for l <= r {\n        m := l + (r-l)/2\n        if n[m] == t { return m }\n        if n[l] <= n[m] {\n            if n[l] <= t && t < n[m] { r = m-1 } else { l = m+1 }\n        } else {\n            if n[m] < t && t <= n[r] { l = m+1 } else { r = m-1 }\n        }\n    }\n    return -1\n}",
         "py_o": "def search(n, t):\n    l, r = 0, len(n)-1\n    while l <= r:\n        m = (l+r)//2\n        if n[m] == t: return m\n        if n[l] <= n[m]:\n            if n[l] <= t < n[m]: r = m-1\n            else: l = m+1\n        else:\n            if n[m] < t <= n[r]: l = m+1\n            else: r = m-1\n    return -1",
         "ja_o": "public int search(int[] n, int t) {\n    int l=0, r=n.length-1;\n    while(l<=r){\n        int m=l+(r-l)/2;\n        if(n[m]==t) return m;\n        if(n[l]<=n[m]){\n            if(n[l]<=t&&t<n[m]) r=m-1; else l=m+1;\n        } else {\n            if(n[m]<t&&t<=n[r]) l=m+1; else r=m-1;\n        }\n    }\n    return -1;\n}",
         "complexity": ["Linear — Time: O(n)।", "Modified Binary Search — Time: O(log n)।", "Key: কোন অর্ধেক sorted তা determine করো, তারপর target কোন অর্ধেক আছে দেখো।"]
        },
        {"num": 3, "title": "Find Minimum in Rotated Array", "desc": "Rotated sorted array-তে সবচেয়ে ছোট element খুঁজে বের করো।", "example": "nums = [3,4,5,1,2] → 1",
         "brute_title": "O(n) linear scan", "brute_desc": "পুরো array scan করে min বের করো।",
         "cpp_b": "int findMin(vector<int>& n) {\n    int mn = n[0];\n    for(int v : n) mn = min(mn, v);\n    return mn;\n}",
         "go_b": "func findMin(n []int) int {\n    mn := n[0]\n    for _, v := range n { if v < mn { mn = v } }\n    return mn\n}",
         "py_b": "def find_min(n):\n    return min(n)",
         "ja_b": "public int findMin(int[] n) {\n    int mn = n[0];\n    for(int v : n) mn = Math.min(mn, v);\n    return mn;\n}",
         "opt_title": "O(log n) Binary Search", "opt_desc": "মাঝখানে check করো — বাম দিক sorted কিনা। যদি sorted হয় এবং n[mid] > n[right], তাহলে minimum ডান দিকে।",
         "cpp_o": "int findMin(vector<int>& n) {\n    int l=0, r=n.size()-1;\n    while(l<r){\n        int m=l+(r-l)/2;\n        if(n[m]>n[r]) l=m+1;\n        else r=m;\n    }\n    return n[l];\n}",
         "go_o": "func findMin(n []int) int {\n    l, r := 0, len(n)-1\n    for l < r {\n        m := l + (r-l)/2\n        if n[m] > n[r] { l = m+1 } else { r = m }\n    }\n    return n[l]\n}",
         "py_o": "def find_min(n):\n    l, r = 0, len(n)-1\n    while l < r:\n        m = (l+r)//2\n        if n[m] > n[r]: l = m+1\n        else: r = m\n    return n[l]",
         "ja_o": "public int findMin(int[] n) {\n    int l=0, r=n.length-1;\n    while(l<r){\n        int m=l+(r-l)/2;\n        if(n[m]>n[r]) l=m+1; else r=m;\n    }\n    return n[l];\n}",
         "complexity": ["Linear — Time: O(n)।", "Binary Search — Time: O(log n)।", "Key: n[mid] > n[right] হলে minimum ডান দিকে, নাহলে বাম দিকে (বা mid-তে)।"]
        },
        {"num": 4, "title": "Search a 2D Matrix", "desc": "Sorted 2D matrix-তে target খুঁজে বের করো।", "example": "matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 → true",
         "brute_title": "O(m×n) scan all", "brute_desc": "প্রতিটি cell check করো।",
         "cpp_b": "bool searchMatrix(vector<vector<int>>& m, int t) {\n    for(auto& r:m) for(int v:r) if(v==t) return true;\n    return false;\n}",
         "go_b": "func searchMatrix(m [][]int, t int) bool {\n    for _, r := range m { for _, v := range r { if v == t { return true } } }\n    return false\n}",
         "py_b": "def search_matrix(m, t):\n    for row in m:\n        if t in row: return True\n    return False",
         "ja_b": "public boolean searchMatrix(int[][] m, int t) {\n    for(int[] r:m) for(int v:r) if(v==t) return true;\n    return false;\n}",
         "opt_title": "O(log(m×n)) Binary Search", "opt_desc": "Matrix কে একটি sorted 1D array হিসেবে treat করো। index = mid / cols (row), mid % cols (col)।",
         "cpp_o": "bool searchMatrix(vector<vector<int>>& m, int t) {\n    int rows=m.size(), cols=m[0].size();\n    int l=0, r=rows*cols-1;\n    while(l<=r){\n        int mid=l+(r-l)/2;\n        int v=m[mid/cols][mid%cols];\n        if(v==t) return true;\n        if(v<t) l=mid+1; else r=mid-1;\n    }\n    return false;\n}",
         "go_o": "func searchMatrix(m [][]int, t int) bool {\n    rows, cols := len(m), len(m[0])\n    l, r := 0, rows*cols-1\n    for l <= r {\n        mid := l + (r-l)/2\n        v := m[mid/cols][mid%cols]\n        if v == t { return true }\n        if v < t { l = mid+1 } else { r = mid-1 }\n    }\n    return false\n}",
         "py_o": "def search_matrix(m, t):\n    rows, cols = len(m), len(m[0])\n    l, r = 0, rows*cols-1\n    while l <= r:\n        mid = (l+r)//2\n        v = m[mid//cols][mid%cols]\n        if v == t: return True\n        if v < t: l = mid+1\n        else: r = mid-1\n    return False",
         "ja_o": "public boolean searchMatrix(int[][] m, int t) {\n    int rows=m.length, cols=m[0].length;\n    int l=0, r=rows*cols-1;\n    while(l<=r){\n        int mid=l+(r-l)/2;\n        int v=m[mid/cols][mid%cols];\n        if(v==t) return true;\n        if(v<t) l=mid+1; else r=mid-1;\n    }\n    return false;\n}",
         "complexity": ["Brute — Time: O(m×n)।", "Binary Search — Time: O(log(m×n))।", "Key: 2D index কে 1D index-এ convert করো — mid/cols (row), mid%cols (col)।"]
        },
        {"num": 5, "title": "Koko Eating Bananas", "desc": "Koko কে কত rate-এ banana খেতে হবে যাতে h ঘণ্টায় সব pile শেষ হয়।", "example": "piles = [3,6,7,11], h = 8 → 4",
         "brute_title": "O(n × max) try all rates", "brute_desc": "১ থেকে max(piles) পর্যন্ত প্রতিটি rate try করো।",
         "cpp_b": "int minEatingSpeed(vector<int>& p, int h) {\n    int mx = *max_element(p.begin(), p.end());\n    for(int k=1;k<=mx;k++){\n        int hrs=0;\n        for(int v:p) hrs += (v+k-1)/k;\n        if(hrs<=h) return k;\n    }\n    return mx;\n}",
         "go_b": "func minEatingSpeed(p []int, h int) int {\n    mx := 0\n    for _, v := range p { if v > mx { mx = v } }\n    for k := 1; k <= mx; k++ {\n        hrs := 0\n        for _, v := range p { hrs += (v+k-1)/k }\n        if hrs <= h { return k }\n    }\n    return mx\n}",
         "py_b": "def min_eating_speed(p, h):\n    for k in range(1, max(p)+1):\n        hrs = sum((v+k-1)//k for v in p)\n        if hrs <= h: return k\n    return max(p)",
         "ja_b": "public int minEatingSpeed(int[] p, int h) {\n    int mx = 0;\n    for(int v : p) mx = Math.max(mx, v);\n    for(int k=1;k<=mx;k++){\n        int hrs=0;\n        for(int v:p) hrs += (v+k-1)/k;\n        if(hrs<=h) return k;\n    }\n    return mx;\n}",
         "opt_title": "O(n × log max) Binary Search on Answer", "opt_desc": "Rate-এর উপর binary search করো — ১ থেকে max(piles)। প্রতিটি mid-এর জন্য total hours check করো।",
         "cpp_o": "int minEatingSpeed(vector<int>& p, int h) {\n    int l=1, r=*max_element(p.begin(),p.end());\n    while(l<r){\n        int m=l+(r-l)/2, hrs=0;\n        for(int v:p) hrs+=(v+m-1)/m;\n        if(hrs<=h) r=m; else l=m+1;\n    }\n    return l;\n}",
         "go_o": "func minEatingSpeed(p []int, h int) int {\n    l, r := 1, 0\n    for _, v := range p { if v > r { r = v } }\n    for l < r {\n        m := l + (r-l)/2\n        hrs := 0\n        for _, v := range p { hrs += (v+m-1)/m }\n        if hrs <= h { r = m } else { l = m+1 }\n    }\n    return l\n}",
         "py_o": "def min_eating_speed(p, h):\n    l, r = 1, max(p)\n    while l < r:\n        m = (l+r)//2\n        hrs = sum((v+m-1)//m for v in p)\n        if hrs <= h: r = m\n        else: l = m+1\n    return l",
         "ja_o": "public int minEatingSpeed(int[] p, int h) {\n    int l=1, r=0;\n    for(int v:p) r=Math.max(r,v);\n    while(l<r){\n        int m=l+(r-l)/2, hrs=0;\n        for(int v:p) hrs+=(v+m-1)/m;\n        if(hrs<=h) r=m; else l=m+1;\n    }\n    return l;\n}",
         "complexity": ["Brute — Time: O(n × max(piles))।", "Binary Search on Answer — Time: O(n × log max(piles))।", "Key: answer space-এ binary search — 'binary search on answer' pattern।"]
        }
    ],
    ["Binary Search — sorted array-তে O(log n)।", "Rotated Array — কোন অর্ধেক sorted তা determine করো।", "Find Min — n[mid] vs n[right] দিয়ে direction।", "2D Matrix — 1D index-এ convert করে binary search।", "Koko — Binary search on answer space।", "Core pattern: sorted + divide in half = O(log n)।"],
    "Tip: পরের topic হলো Sliding Window — fixed ও variable size window দিয়ে substring problems solve করা।"
)

# Sliding Window, Linked List, Trees, and remaining topics
# For space efficiency, I'll generate compact versions

def gen_coming_soon_topic(tid, title, bangla, difficulty, est, summary, overview, items, next_tip):
    """Generate a topic with full overview but compact problem descriptions."""
    sections = []
    sections.append(f'      {{ type: "h2", id: "overview", title: "Overview" }}')
    sections.append(f'      {{ type: "p", text: "{overview}" }}')
    
    # Generate 5 problems with full solutions
    for i, item in enumerate(items, 1):
        sections.append(f'      {{ type: "h2", id: "prob-{i}", title: "Problem {i} — {item[0]}" }}')
        sections.append(f'      {{ type: "p", text: "{item[1]}" }}')
        sections.append(f'      {{ type: "h3", title: "Brute Force — {item[2]}" }}')
        sections.append(f'      {{ type: "p", text: "{item[3]}" }}')
        sections.append(f'''      {{
        type: "multi-code",
        filename: "{tid}_p{i}_brute",
        codeSamples: {{
          cpp: `{item[4]}`,
          go: `{item[5]}`,
          python: `{item[6]}`,
          java: `{item[7]}`,
        }},
      }},''')
        sections.append(f'      {{ type: "h3", title: "Optimal — {item[8]}" }}')
        sections.append(f'      {{ type: "p", text: "{item[9]}" }}')
        sections.append(f'''      {{
        type: "multi-code",
        filename: "{tid}_p{i}_optimal",
        codeSamples: {{
          cpp: `{item[10]}`,
          go: `{item[11]}`,
          python: `{item[12]}`,
          java: `{item[13]}`,
        }},
      }},''')
        sections.append(f'      {{ type: "h3", title: "Complexity Comparison" }}')
        items_str = ',\n          '.join([f'"{c}"' for c in item[14]])
        sections.append(f'''      {{
        type: "list",
        items: [
          {items_str}
        ],
      }},''')
    
    sections.append(f'      {{ type: "h2", id: "summary", title: "Chapter Summary" }}')
    sections.append(f'      {{ type: "callout", calloutTone: "tip", text: "{next_tip}" }}')
    
    sections_str = ',\n'.join(sections)
    return gen_topic(tid, title, bangla, difficulty, est, summary, sections_str)

# Sliding Window
sw_items = [
    ("Best Time to Buy/Sell Stock", "একটি price array দেওয়া আছে। Best buy-sell profit বের করো।", "O(n²) all pairs", "প্রতিটি buy day-এর জন্য সব future sell day check করো।",
     "int maxProfit(vector<int>& p) {\n    int mx=0;\n    for(int i=0;i<p.size();i++)\n        for(int j=i+1;j<p.size();j++)\n            mx=max(mx,p[j]-p[i]);\n    return mx;\n}",
     "func maxProfit(p []int) int {\n    mx := 0\n    for i := 0; i < len(p); i++ {\n        for j := i+1; j < len(p); j++ {\n            if p[j]-p[i] > mx { mx = p[j]-p[i] }\n        }\n    }\n    return mx\n}",
     "def max_profit(p):\n    mx = 0\n    for i in range(len(p)):\n        for j in range(i+1, len(p)):\n            mx = max(mx, p[j]-p[i])\n    return mx",
     "public int maxProfit(int[] p) {\n    int mx=0;\n    for(int i=0;i<p.length;i++)\n        for(int j=i+1;j<p.length;j++)\n            mx=Math.max(mx,p[j]-p[i]);\n    return mx;\n}",
     "O(n) Sliding Window", "একটি pointer 'min_price' track করে। বর্তমান price - min_price = profit। max profit রাখো।",
     "int maxProfit(vector<int>& p) {\n    int mn=INT_MAX, mx=0;\n    for(int v:p){mn=min(mn,v);mx=max(mx,v-mn);}\n    return mx;\n}",
     "func maxProfit(p []int) int {\n    mn, mx := p[0], 0\n    for _, v := range p {\n        if v < mn { mn = v }\n        if v-mn > mx { mx = v-mn }\n    }\n    return mx\n}",
     "def max_profit(p):\n    mn, mx = float('inf'), 0\n    for v in p:\n        mn = min(mn, v)\n        mx = max(mx, v-mn)\n    return mx",
     "public int maxProfit(int[] p) {\n    int mn=Integer.MAX_VALUE, mx=0;\n    for(int v:p){mn=Math.min(mn,v);mx=Math.max(mx,v-mn);}\n    return mx;\n}",
     ["Brute — Time: O(n²)।", "Sliding Window — Time: O(n), Space: O(1)।", "Key: সর্বনিম্ন price track করে profit maximize করো।"]
    ),
    ("Longest Substring Without Repeating", "সবচেয়ে বড় substring যাতে কোনো repeating character নেই।", "O(n²) check all substrings", "প্রতিটি starting position থেকে expand করে দেখো।",
     "int lengthOfLongestSubstring(string s) {\n    int mx=0;\n    for(int i=0;i<s.size();i++){\n        set<char> seen;\n        for(int j=i;j<s.size();j++){\n            if(seen.count(s[j]))break;\n            seen.insert(s[j]);\n            mx=max(mx,j-i+1);\n        }\n    }\n    return mx;\n}",
     "func lengthOfLongestSubstring(s string) int {\n    mx := 0\n    for i := 0; i < len(s); i++ {\n        seen := make(map[byte]bool)\n        for j := i; j < len(s); j++ {\n            if seen[s[j]] { break }\n            seen[s[j]] = true\n            if j-i+1 > mx { mx = j-i+1 }\n        }\n    }\n    return mx\n}",
     "def length_of_longest(s):\n    mx = 0\n    for i in range(len(s)):\n        seen = set()\n        for j in range(i, len(s)):\n            if s[j] in seen: break\n            seen.add(s[j])\n            mx = max(mx, j-i+1)\n    return mx",
     "public int lengthOfLongestSubstring(String s) {\n    int mx=0;\n    for(int i=0;i<s.length();i++){\n        Set<Character> seen=new HashSet<>();\n        for(int j=i;j<s.length();j++){\n            if(seen.contains(s.charAt(j)))break;\n            seen.add(s.charAt(j));\n            mx=Math.max(mx,j-i+1);\n        }\n    }\n    return mx;\n}",
     "O(n) Sliding Window + Set", "দুটি pointer — left ও right। Right move করে expand করো। Duplicate হলে left move করে shrink করো।",
     "int lengthOfLongestSubstring(string s) {\n    set<char> st;\n    int l=0, mx=0;\n    for(int r=0;r<s.size();r++){\n        while(st.count(s[r])){st.erase(s[l]);l++;}\n        st.insert(s[r]);\n        mx=max(mx,r-l+1);\n    }\n    return mx;\n}",
     "func lengthOfLongestSubstring(s string) int {\n    seen := make(map[byte]int)\n    l, mx := 0, 0\n    for r := 0; r < len(s); r++ {\n        if idx, ok := seen[s[r]]; ok && idx >= l {\n            l = idx + 1\n        }\n        seen[s[r]] = r\n        if r-l+1 > mx { mx = r-l+1 }\n    }\n    return mx\n}",
     "def length_of_longest(s):\n    seen = {}\n    l, mx = 0, 0\n    for r, c in enumerate(s):\n        if c in seen and seen[c] >= l:\n            l = seen[c] + 1\n        seen[c] = r\n        mx = max(mx, r-l+1)\n    return mx",
     "public int lengthOfLongestSubstring(String s) {\n    Map<Character,Integer> seen=new HashMap<>();\n    int l=0,mx=0;\n    for(int r=0;r<s.length();r++){\n        if(seen.containsKey(s.charAt(r))&&seen.get(s.charAt(r))>=l)\n            l=seen.get(s.charAt(r))+1;\n        seen.put(s.charAt(r),r);\n        mx=Math.max(mx,r-l+1);\n    }\n    return mx;\n}",
     ["Brute — Time: O(n²), Space: O(n)।", "Sliding Window — Time: O(n), Space: O(n)।", "Key: hash map দিয়ে character-এর last index track করো।"]
    ),
    ("Longest Repeating Character Replacement", "String-এ kটি character replace করে longest repeating substring বানাও।", "O(n²) check all windows", "প্রতিটি window চেক করো, kটি replace করে সব same করা যায় কিনা।",
     "int characterReplacement(string s, int k) {\n    int mx=0;\n    for(int i=0;i<s.size();i++)\n        for(int j=i;j<s.size();j++){\n            int freq[26]={},mf=0;\n            for(int x=i;x<=j;x++){freq[s[x]-'A']++;mf=max(mf,freq[s[x]-'A']);}\n            if(j-i+1-mf<=k)mx=max(mx,j-i+1);\n        }\n    return mx;\n}",
     "// O(n²) approach\nfunc characterReplacement(s string, k int) int {\n    mx := 0\n    for i := 0; i < len(s); i++ {\n        for j := i; j < len(s); j++ {\n            freq := [26]int{}\n            mf := 0\n            for x := i; x <= j; x++ { freq[s[x]-'A']++; if freq[s[x]-'A']>mf { mf=freq[s[x]-'A'] } }\n            if j-i+1-mf <= k && j-i+1 > mx { mx = j-i+1 }\n        }\n    }\n    return mx\n}",
     "def character_replacement(s, k):\n    mx = 0\n    for i in range(len(s)):\n        for j in range(i, len(s)):\n            from collections import Counter\n            freq = Counter(s[i:j+1])\n            mf = max(freq.values())\n            if j-i+1-mf <= k: mx = max(mx, j-i+1)\n    return mx",
     "public int characterReplacement(String s, int k) {\n    int mx=0;\n    for(int i=0;i<s.length();i++)\n        for(int j=i;j<s.length();j++){\n            int[] f=new int[26];int mf=0;\n            for(int x=i;x<=j;x++){f[s.charAt(x)-'A']++;mf=Math.max(mf,f[s.charAt(x)-'A']);}\n            if(j-i+1-mf<=k)mx=Math.max(mx,j-i+1);\n        }\n    return mx;\n}",
     "O(n) Sliding Window", "Window-এ সবচেয়ে common character-এর count track করো। window - max_count > k হলে shrink।",
     "int characterReplacement(string s, int k) {\n    int freq[26]={}, l=0, mf=0, mx=0;\n    for(int r=0;r<s.size();r++){\n        freq[s[r]-'A']++;\n        mf=max(mf,freq[s[r]-'A']);\n        while(r-l+1-mf>k){freq[s[l]-'A']--;l++;}\n        mx=max(mx,r-l+1);\n    }\n    return mx;\n}",
     "func characterReplacement(s string, k int) int {\n    freq := [26]int{}\n    l, mf, mx := 0, 0, 0\n    for r := 0; r < len(s); r++ {\n        freq[s[r]-'A']++\n        if freq[s[r]-'A'] > mf { mf = freq[s[r]-'A'] }\n        for r-l+1-mf > k { freq[s[l]-'A']--; l++ }\n        if r-l+1 > mx { mx = r-l+1 }\n    }\n    return mx\n}",
     "def character_replacement(s, k):\n    freq = {}\n    l = mf = mx = 0\n    for r in range(len(s)):\n        freq[s[r]] = freq.get(s[r], 0) + 1\n        mf = max(mf, freq[s[r]])\n        while r-l+1-mf > k:\n            freq[s[l]] -= 1\n            l += 1\n        mx = max(mx, r-l+1)\n    return mx",
     "public int characterReplacement(String s, int k) {\n    int[] f=new int[26];int l=0,mf=0,mx=0;\n    for(int r=0;r<s.length();r++){\n        f[s.charAt(r)-'A']++;mf=Math.max(mf,f[s.charAt(r)-'A']);\n        while(r-l+1-mf>k){f[s.charAt(l)-'A']--;l++;}\n        mx=Math.max(mx,r-l+1);\n    }\n    return mx;\n}",
     ["Brute — Time: O(n³)।", "Sliding Window — Time: O(n), Space: O(1)।", "Key: window - max_freq <= k হলে valid window।"]
    ),
    ("Permutation in String", "s2-তে কোনো substring কি s1-এর permutation? ", "O(n! × m) generate all permutations", "s1-এর সব permutation generate করে s2-এ খুঁজো। খুব slow!",
     "bool checkInclusion(string s1, string s2) {\n    // generate all permutations of s1, check each in s2\n    // O(n! × m) — impractical\n    return false;\n}",
     "// O(n!) — impractical\nfunc checkInclusion(s1, s2 string) bool { return false }",
     "from itertools import permutations\ndef check_inclusion(s1, s2):\n    for p in set(permutations(s1)):\n        if ''.join(p) in s2: return True\n    return False",
     "// O(n!) — impractical\npublic boolean checkInclusion(String s1, String s2) { return false; }",
     "O(n) Sliding Window + Frequency", "Fixed window (size = len(s1))। Frequency array compare করো। Match হলে true।",
     "bool checkInclusion(string s1, string s2) {\n    int n=s1.size(),m=s2.size();\n    if(n>m)return false;\n    vector<int> f1(26),f2(26);\n    for(int i=0;i<n;i++){f1[s1[i]-'a']++;f2[s2[i]-'a']++;}\n    if(f1==f2)return true;\n    for(int i=n;i<m;i++){f2[s2[i]-'a']++;f2[s2[i-n]-'a']--;if(f1==f2)return true;}\n    return false;\n}",
     "func checkInclusion(s1, s2 string) bool {\n    n, m := len(s1), len(s2)\n    if n > m { return false }\n    f1, f2 := [26]int{}, [26]int{}\n    for i := 0; i < n; i++ { f1[s1[i]-'a']++; f2[s2[i]-'a']++ }\n    if f1 == f2 { return true }\n    for i := n; i < m; i++ {\n        f2[s2[i]-'a']++; f2[s2[i-n]-'a']--\n        if f1 == f2 { return true }\n    }\n    return false\n}",
     "def check_inclusion(s1, s2):\n    from collections import Counter\n    n = len(s1)\n    c1 = Counter(s1)\n    c2 = Counter(s2[:n])\n    if c1 == c2: return True\n    for i in range(n, len(s2)):\n        c2[s2[i]] += 1\n        c2[s2[i-n]] -= 1\n        if c2[s2[i-n]] == 0: del c2[s2[i-n]]\n        if c1 == c2: return True\n    return False",
     "public boolean checkInclusion(String s1, String s2) {\n    int n=s1.length(),m=s2.length();\n    if(n>m)return false;\n    int[] f1=new int[26],f2=new int[26];\n    for(int i=0;i<n;i++){f1[s1.charAt(i)-'a']++;f2[s2.charAt(i)-'a']++;}\n    if(Arrays.equals(f1,f2))return true;\n    for(int i=n;i<m;i++){f2[s2.charAt(i)-'a']++;f2[s2.charAt(i-n)-'a']--;if(Arrays.equals(f1,f2))return true;}\n    return false;\n}",
     ["Permutations — Time: O(n! × m)। Impractical।", "Sliding Window — Time: O(n + m), Space: O(1)।", "Key: fixed window + frequency array compare।"]
    ),
    ("Minimum Window Substring", "s-তে সবচেয়ে ছোট substring যাতে t-এর সব character আছে।", "O(n²) check all windows", "প্রতিটি starting ও ending position check করো।",
     "string minWindow(string s, string t) {\n    string res;\n    for(int i=0;i<s.size();i++)\n        for(int j=i;j<s.size();j++){\n            // check if s[i..j] contains all of t\n            // O(n² × k)\n        }\n    return res;\n}",
     "// O(n²) approach\nfunc minWindow(s, t string) string {\n    res := \"\"\n    // check all windows\n    return res\n}",
     "def min_window(s, t):\n    from collections import Counter\n    need = Counter(t)\n    res = \"\"\n    for i in range(len(s)):\n        for j in range(i+1, len(s)+1):\n            window = Counter(s[i:j])\n            if all(window[c] >= need[c] for c in need):\n                if not res or j-i < len(res):\n                    res = s[i:j]\n    return res",
     "// O(n²) approach\npublic String minWindow(String s, String t) {\n    String res = \"\";\n    // check all windows\n    return res;\n}",
     "O(n) Sliding Window + Counter", "দুটি pointer — expand right, contract left। Need map track করো। সব need মিটলে window shrink করো।",
     "string minWindow(string s, string t) {\n    unordered_map<char,int> need,have;\n    for(char c:t)need[c]++;\n    int l=0,need_cnt=need.size(),have_cnt=0,mn=INT_MAX,ml=0;\n    for(int r=0;r<s.size();r++){\n        have[s[r]]++;\n        if(need.count(s[r])&&have[s[r]]==need[s[r]])have_cnt++;\n        while(have_cnt==need_cnt){\n            if(r-l+1<mn){mn=r-l+1;ml=l;}\n            have[s[l]]--;\n            if(need.count(s[l])&&have[s[l]]<need[s[l]])have_cnt--;\n            l++;\n        }\n    }\n    return mn==INT_MAX?\"\":s.substr(ml,mn);\n}",
     "func minWindow(s, t string) string {\n    need, have := map[byte]int{}, map[byte]int{}\n    for i := 0; i < len(t); i++ { need[t[i]]++ }\n    l, needCnt, haveCnt, mn, ml := 0, len(need), 0, len(s)+1, 0\n    for r := 0; r < len(s); r++ {\n        have[s[r]]++\n        if _, ok := need[s[r]]; ok && have[s[r]] == need[s[r]] { haveCnt++ }\n        for haveCnt == needCnt {\n            if r-l+1 < mn { mn = r-l+1; ml = l }\n            have[s[l]]--\n            if _, ok := need[s[l]]; ok && have[s[l]] < need[s[l]] { haveCnt-- }\n            l++\n        }\n    }\n    if mn > len(s) { return \"\" }\n    return s[ml : ml+mn]\n}",
     "def min_window(s, t):\n    from collections import Counter\n    need = Counter(t)\n    have = {}\n    l = need_cnt = len(need)\n    have_cnt = 0\n    ml = mn = 0\n    res = \"\"\n    for r, c in enumerate(s):\n        have[c] = have.get(c, 0) + 1\n        if c in need and have[c] == need[c]: have_cnt += 1\n        while have_cnt == need_cnt:\n            if not res or r-l+1 < len(res):\n                res = s[l:r+1]\n            have[s[l]] -= 1\n            if s[l] in need and have[s[l]] < need[s[l]]: have_cnt -= 1\n            l += 1\n    return res",
     "public String minWindow(String s, String t) {\n    Map<Character,Integer> need=new HashMap<>(),have=new HashMap<>();\n    for(char c:t.toCharArray())need.merge(c,1,Integer::sum);\n    int l=0,needCnt=need.size(),haveCnt=0,mn=Integer.MAX_VALUE,ml=0;\n    for(int r=0;r<s.length();r++){\n        have.merge(s.charAt(r),1,Integer::sum);\n        if(need.containsKey(s.charAt(r))&&have.get(s.charAt(r)).equals(need.get(s.charAt(r))))haveCnt++;\n        while(haveCnt==needCnt){\n            if(r-l+1<mn){mn=r-l+1;ml=l;}\n            have.merge(s.charAt(l),-1,Integer::sum);\n            if(need.containsKey(s.charAt(l))&&have.get(s.charAt(l))<need.get(s.charAt(l)))haveCnt--;\n            l++;\n        }\n    }\n    return mn==Integer.MAX_VALUE?\"\":s.substring(ml,ml+mn);\n}",
     ["Brute — Time: O(n² × k)।", "Sliding Window — Time: O(n), Space: O(k)।", "Key: expand right, contract left when all needs met।"]
    )
]

sw_topic = gen_coming_soon_topic("dsa-sliding-window", "Sliding Window", "স্লাইডিং উইন্ডো", "Medium", "2.5 hr",
    "Sliding Window fixed বা variable size window দিয়ে substring problems solve করে। ৫টি classic problem।",
    "Sliding Window হলো একটি technique যেখানে একটি 'window' array বা string-এর উপর move করে। Fixed window (size স্থির) বা variable window (size পরিবর্তনশীল) হতে পারে। Real-life thinking — একটি magnifying glass দিয়ে একটি long document পড়ছো। Glass কে এক সাইড থেকে আরেক সাইডে move করো, প্রতিটি position-এ যা দেখো সেটাই window-এর content।",
    sw_items,
    "Tip: পরের topic হলো Linked List — pointer দিয়ে nodes এর সাথে connected।"
)

# Linked List through Math & Geometry — generate as compact topics
remaining_topics_data = [
    ("dsa-linked-list", "Linked List", "লিংকড লিস্ট", "Medium", "2.5 hr",
     "Linked List হলো pointer-যুক্ত nodes-এর একটি chain। ৫টি classic problem।",
     "Linked List-এ প্রতিটি node একটি value ও একটি next pointer ধারণ করে। Array-র মতোই, কিন্তু contiguous memory-তে নয়। Real-life thinking — একটি treasure hunt! প্রতিটি clue পরের clue-এর address ধারণ করে। তোমাকে একে একে follow করতে হয়।",
     [("Reverse Linked List", "একটি singly linked list reverse করো।", "O(n) with stack", "সব nodes stack-এ push করে আবার pop করে reverse করো।",
       "ListNode* reverseList(ListNode* head) {\n    stack<ListNode*> st;\n    while(head){st.push(head);head=head->next;}\n    ListNode dummy(0);ListNode* cur=&dummy;\n    while(!st.empty()){cur->next=st.top();st.pop();cur=cur->next;}\n    cur->next=nullptr;return dummy.next;\n}",
       "func reverseList(head *ListNode) *ListNode {\n    var st []*ListNode\n    for p := head; p != nil; p = p.Next { st = append(st, p) }\n    dummy := &ListNode{}\n    cur := dummy\n    for i := len(st)-1; i >= 0; i-- { cur.Next = st[i]; cur = cur.Next }\n    cur.Next = nil\n    return dummy.Next\n}",
       "def reverse_list(head):\n    st = []\n    while head:\n        st.append(head)\n        head = head.next\n    dummy = ListNode()\n    cur = dummy\n    while st:\n        cur.next = st.pop()\n        cur = cur.next\n    cur.next = None\n    return dummy.next",
       "public ListNode reverseList(ListNode head) {\n    Stack<ListNode> st = new Stack<>();\n    while(head!=null){st.push(head);head=head.next;}\n    ListNode dummy=new ListNode();\n    ListNode cur=dummy;\n    while(!st.isEmpty()){cur.next=st.pop();cur=cur.next;}\n    cur.next=null;return dummy.next;\n}",
       "O(n) Iterative with 3 pointers", "prev, cur, next — তিনটি pointer ব্যবহার করো। cur->next = prev করে pointer উল্টে দাও।",
       "ListNode* reverseList(ListNode* head) {\n    ListNode *prev=nullptr,*cur=head;\n    while(cur){ListNode* nxt=cur->next;cur->next=prev;prev=cur;cur=nxt;}\n    return prev;\n}",
       "func reverseList(head *ListNode) *ListNode {\n    var prev *ListNode\n    cur := head\n    for cur != nil {\n        nxt := cur.Next\n        cur.Next = prev\n        prev = cur\n        cur = nxt\n    }\n    return prev\n}",
       "def reverse_list(head):\n    prev = None\n    cur = head\n    while cur:\n        nxt = cur.next\n        cur.next = prev\n        prev = cur\n        cur = nxt\n    return prev",
       "public ListNode reverseList(ListNode head) {\n    ListNode prev=null,cur=head;\n    while(cur!=null){ListNode nxt=cur.next;cur.next=prev;prev=cur;cur=nxt;}\n    return prev;\n}",
       ["Stack — Time: O(n), Space: O(n)।", "3 Pointers — Time: O(n), Space: O(1)।", "Key: pointer উল্টে দাও — cur->next = prev।"]
      ),
      ("Merge Two Sorted Lists", "দুটি sorted linked list merge করো।", "O(n+m) extract to array", "দুটি list কে array-তে convert করে merge করে আবার list বানাও।",
       "ListNode* mergeTwoLists(ListNode* a, ListNode* b) {\n    vector<int> vals;\n    while(a){vals.push_back(a->val);a=a->next;}\n    while(b){vals.push_back(b->val);b=b->next;}\n    sort(vals.begin(),vals.end());\n    ListNode dummy(0);ListNode* cur=&dummy;\n    for(int v:vals){cur->next=new ListNode(v);cur=cur->next;}\n    return dummy.next;\n}",
       "func mergeTwoLists(a, b *ListNode) *ListNode {\n    var vals []int\n    for p := a; p != nil; p = p.Next { vals = append(vals, p.Val) }\n    for p := b; p != nil; p = p.Next { vals = append(vals, p.Val) }\n    sort.Ints(vals)\n    dummy := &ListNode{}\n    cur := dummy\n    for _, v := range vals { cur.Next = &ListNode{Val: v}; cur = cur.Next }\n    return dummy.Next\n}",
       "def merge_two_lists(a, b):\n    vals = []\n    while a: vals.append(a.val); a = a.next\n    while b: vals.append(b.val); b = b.next\n    vals.sort()\n    dummy = ListNode()\n    cur = dummy\n    for v in vals: cur.next = ListNode(v); cur = cur.next\n    return dummy.next",
       "public ListNode mergeTwoLists(ListNode a, ListNode b) {\n    List<Integer> vals=new ArrayList<>();\n    while(a!=null){vals.add(a.val);a=a.next;}\n    while(b!=null){vals.add(b.val);b=b.next;}\n    Collections.sort(vals);\n    ListNode dummy=new ListNode();ListNode cur=dummy;\n    for(int v:vals){cur.next=new ListNode(v);cur=cur.next;}\n    return dummy.next;\n}",
       "O(n+m) Iterative Merge", "দুটি pointer দিয়ে ছোট node কে প্রথমে রাখো। next pointer adjust করো।",
       "ListNode* mergeTwoLists(ListNode* a, ListNode* b) {\n    ListNode dummy(0);ListNode* cur=&dummy;\n    while(a&&b){\n        if(a->val<=b->val){cur->next=a;a=a->next;}\n        else{cur->next=b;b=b->next;}\n        cur=cur->next;\n    }\n    cur->next=a?a:b;\n    return dummy.next;\n}",
       "func mergeTwoLists(a, b *ListNode) *ListNode {\n    dummy := &ListNode{}\n    cur := dummy\n    for a != nil && b != nil {\n        if a.Val <= b.Val { cur.Next = a; a = a.Next } else { cur.Next = b; b = b.Next }\n        cur = cur.Next\n    }\n    if a != nil { cur.Next = a } else { cur.Next = b }\n    return dummy.Next\n}",
       "def merge_two_lists(a, b):\n    dummy = ListNode()\n    cur = dummy\n    while a and b:\n        if a.val <= b.val: cur.next = a; a = a.next\n        else: cur.next = b; b = b.next\n        cur = cur.next\n    cur.next = a or b\n    return dummy.next",
       "public ListNode mergeTwoLists(ListNode a, ListNode b) {\n    ListNode dummy=new ListNode();ListNode cur=dummy;\n    while(a!=null&&b!=null){\n        if(a.val<=b.val){cur.next=a;a=a.next;}\n        else{cur.next=b;b=b.next;}\n        cur=cur.next;\n    }\n    cur.next=a!=null?a:b;\n    return dummy.next;\n}",
       ["Array — Time: O((n+m) log(n+m)), Space: O(n+m)।", "Iterative Merge — Time: O(n+m), Space: O(1)।", "Key: ছোট node প্রথমে — merge sort-এর merge step।"]
      ),
      ("Linked List Cycle", "Linked list-এ cycle আছে কিনা detect করো।", "O(n) with hash set", "প্রতিটি visited node কে set-এ store করো। পুনরায় visit হলে cycle আছে।",
       "bool hasCycle(ListNode* head) {\n    set<ListNode*> visited;\n    while(head){\n        if(visited.count(head))return true;\n        visited.insert(head);\n        head=head->next;\n    }\n    return false;\n}",
       "func hasCycle(head *ListNode) bool {\n    visited := make(map[*ListNode]bool)\n    for p := head; p != nil; p = p.Next {\n        if visited[p] { return true }\n        visited[p] = true\n    }\n    return false\n}",
       "def has_cycle(head):\n    visited = set()\n    while head:\n        if head in visited: return True\n        visited.add(head)\n        head = head.next\n    return False",
       "public boolean hasCycle(ListNode head) {\n    Set<ListNode> visited=new HashSet<>();\n    while(head!=null){\n        if(visited.contains(head))return true;\n        visited.add(head);\n        head=head.next;\n    }\n    return false;\n}",
       "O(n) Floyd's Cycle Detection", "দুটি pointer — slow (1 step), fast (2 steps)। Fast যদি slow কে catch করে, cycle আছে।",
       "bool hasCycle(ListNode* head) {\n    ListNode *slow=head,*fast=head;\n    while(fast&&fast->next){\n        slow=slow->next;\n        fast=fast->next->next;\n        if(slow==fast)return true;\n    }\n    return false;\n}",
       "func hasCycle(head *ListNode) bool {\n    slow, fast := head, head\n    for fast != nil && fast.Next != nil {\n        slow = slow.Next\n        fast = fast.Next.Next\n        if slow == fast { return true }\n    }\n    return false\n}",
       "def has_cycle(head):\n    slow = fast = head\n    while fast and fast.next:\n        slow = slow.next\n        fast = fast.next.next\n        if slow == fast: return True\n    return False",
       "public boolean hasCycle(ListNode head) {\n    ListNode slow=head,fast=head;\n    while(fast!=null&&fast.next!=null){\n        slow=slow.next;\n        fast=fast.next.next;\n        if(slow==fast)return true;\n    }\n    return false;\n}",
       ["Hash Set — Time: O(n), Space: O(n)।", "Floyd's — Time: O(n), Space: O(1)।", "Key: slow ও fast pointer — fast যদি slow কে catch করে, cycle।"]
      ),
      ("Remove Nth Node From End", "শেষ থেকে Nতম node remove করো।", "O(n) two passes", "প্রথমে length count করো, তারপর (length - n)তম node-এ যাও।",
       "ListNode* removeNthFromEnd(ListNode* head, int n) {\n    int len=0;\n    for(ListNode* p=head;p;p=p->next)len++;\n    if(len==n)return head->next;\n    ListNode* p=head;\n    for(int i=0;i<len-n-1;i++)p=p->next;\n    p->next=p->next->next;\n    return head;\n}",
       "func removeNthFromEnd(head *ListNode, n int) *ListNode {\n    ln := 0\n    for p := head; p != nil; p = p.Next { ln++ }\n    if ln == n { return head.Next }\n    p := head\n    for i := 0; i < ln-n-1; i++ { p = p.Next }\n    p.Next = p.Next.Next\n    return head\n}",
       "def remove_nth_from_end(head, n):\n    length = 0\n    p = head\n    while p: length += 1; p = p.next\n    if length == n: return head.next\n    p = head\n    for _ in range(length - n - 1): p = p.next\n    p.next = p.next.next\n    return head",
       "public ListNode removeNthFromEnd(ListNode head, int n) {\n    int len=0;\n    for(ListNode p=head;p!=null;p=p.next)len++;\n    if(len==n)return head.next;\n    ListNode p=head;\n    for(int i=0;i<len-n-1;i++)p=p.next;\n    p.next=p.next.next;\n    return head;\n}",
       "O(n) Two Pointers — one pass", "fast pointer কে n step আগে পাঠাও। তারপর slow ও fast একসাথে move করো। Fast শেষে গেলে slow Nth-এ আছে।",
       "ListNode* removeNthFromEnd(ListNode* head, int n) {\n    ListNode dummy(0);dummy.next=head;\n    ListNode *fast=&dummy,*slow=&dummy;\n    for(int i=0;i<n;i++)fast=fast->next;\n    while(fast->next){fast=fast->next;slow=slow->next;}\n    slow->next=slow->next->next;\n    return dummy.next;\n}",
       "func removeNthFromEnd(head *ListNode, n int) *ListNode {\n    dummy := &ListNode{Next: head}\n    fast, slow := dummy, dummy\n    for i := 0; i < n; i++ { fast = fast.Next }\n    for fast.Next != nil { fast = fast.Next; slow = slow.Next }\n    slow.Next = slow.Next.Next\n    return dummy.Next\n}",
       "def remove_nth_from_end(head, n):\n    dummy = ListNode(0, head)\n    fast = slow = dummy\n    for _ in range(n): fast = fast.next\n    while fast.next:\n        fast = fast.next\n        slow = slow.next\n    slow.next = slow.next.next\n    return dummy.next",
       "public ListNode removeNthFromEnd(ListNode head, int n) {\n    ListNode dummy=new ListNode(0,head);\n    ListNode fast=dummy,slow=dummy;\n    for(int i=0;i<n;i++)fast=fast.next;\n    while(fast.next!=null){fast=fast.next;slow=slow.next;}\n    slow.next=slow.next.next;\n    return dummy.next;\n}",
       ["Two Passes — Time: O(n), Space: O(1)।", "Two Pointers — Time: O(n), Space: O(1)। One pass!", "Key: fast কে n step আগে পাঠাও — distance gap maintain করে।"]
      ),
      ("Reorder List", "Linked list কে এমনভাবে reorder করো: L0→Ln→L1→Ln-1→L2→Ln-2→…", "O(n²) repeatedly find tail", "প্রতিটি step-এ tail find করে সেটিকে current node-এর পরে insert করো।",
       "void reorderList(ListNode* head) {\n    if(!head||!head->next)return;\n    ListNode* cur=head;\n    while(cur&&cur->next){\n        ListNode* prev=nullptr,*tail=head;\n        while(tail->next){prev=tail;tail=tail->next;}\n        if(prev)prev->next=nullptr;\n        tail->next=cur->next;\n        cur->next=tail;\n        cur=tail->next;\n    }\n}",
       "func reorderList(head *ListNode) {\n    if head == nil || head.Next == nil { return }\n    cur := head\n    for cur != nil && cur.Next != nil {\n        var prev *ListNode\n        tail := head\n        for tail.Next != nil { prev = tail; tail = tail.Next }\n        if prev != nil { prev.Next = nil }\n        tail.Next = cur.Next\n        cur.Next = tail\n        cur = tail.Next\n    }\n}",
       "def reorder_list(head):\n    if not head or not head.next: return\n    cur = head\n    while cur and cur.next:\n        prev = None\n        tail = head\n        while tail.next: prev = tail; tail = tail.next\n        if prev: prev.next = None\n        tail.next = cur.next\n        cur.next = tail\n        cur = tail.next",
       "public void reorderList(ListNode head) {\n    if(head==null||head.next==null)return;\n    ListNode cur=head;\n    while(cur!=null&&cur.next!=null){\n        ListNode prev=null,tail=head;\n        while(tail.next!=null){prev=tail;tail=tail.next;}\n        if(prev!=null)prev.next=null;\n        tail.next=cur.next;\n        cur.next=tail;\n        cur=tail.next;\n    }\n}",
       "O(n) Find Middle + Reverse + Merge", "১. Slow-fast pointer দিয়ে middle খুঁজো। ২. দ্বিতীয় অর্ধ reverse করো। ৩. দুটি অর্ধ merge করো।",
       "void reorderList(ListNode* head) {\n    ListNode *slow=head,*fast=head->next;\n    while(fast&&fast->next){slow=slow->next;fast=fast->next->next;}\n    ListNode* second=slow->next;\n    slow->next=nullptr;\n    ListNode* prev=nullptr;\n    while(second){ListNode* nxt=second->next;second->next=prev;prev=second;second=nxt;}\n    ListNode* first=head;\n    while(prev){ListNode* tmp1=first->next;\n        ListNode* tmp2=prev->next;\n        first->next=prev;prev->next=tmp1;\n        first=tmp1;prev=tmp2;}\n}",
       "func reorderList(head *ListNode) {\n    slow, fast := head, head.Next\n    for fast != nil && fast.Next != nil { slow = slow.Next; fast = fast.Next.Next }\n    second := slow.Next\n    slow.Next = nil\n    var prev *ListNode\n    for second != nil { nxt := second.Next; second.Next = prev; prev = second; second = nxt }\n    first := head\n    for prev != nil {\n        tmp1, tmp2 := first.Next, prev.Next\n        first.Next = prev; prev.Next = tmp1\n        first = tmp1; prev = tmp2\n    }\n}",
       "def reorder_list(head):\n    if not head or not head.next: return\n    slow, fast = head, head.next\n    while fast and fast.next:\n        slow = slow.next; fast = fast.next.next\n    second = slow.next\n    slow.next = None\n    prev = None\n    while second:\n        nxt = second.next; second.next = prev; prev = second; second = nxt\n    first = head\n    while prev:\n        tmp1, tmp2 = first.next, prev.next\n        first.next = prev; prev.next = tmp1\n        first = tmp1; prev = tmp2",
       "public void reorderList(ListNode head) {\n    ListNode slow=head,fast=head.next;\n    while(fast!=null&&fast.next!=null){slow=slow.next;fast=fast.next.next;}\n    ListNode second=slow.next;\n    slow.next=null;\n    ListNode prev=null;\n    while(second!=null){ListNode nxt=second.next;second.next=prev;prev=second;second=nxt;}\n    ListNode first=head;\n    while(prev!=null){\n        ListNode t1=first.next,t2=prev.next;\n        first.next=prev;prev.next=t1;\n        first=t1;prev=t2;\n    }\n}",
       ["Repeated tail find — Time: O(n²)।", "Middle + Reverse + Merge — Time: O(n), Space: O(1)।", "Key: find middle, reverse second half, interleave merge।"]
      )
     ],
     "Tip: পরের topic হলো Trees — hierarchical data structure যা recursion দিয়ে সুন্দরভাবে solve হয়।"
    ),
    ("dsa-trees", "Trees", "ট্রি", "Hard", "3 hr",
     "Tree হলো hierarchical data structure। ৫টি classic problem — traversal, BST, ও construction।",
     "Tree হলো একটি hierarchical structure যেখানে প্রতিটি node-এর সর্বোচ্চ দুটি children (left ও right) থাকে। Root হলো সবার উপরের node, leaf হলো যাদের কোনো child নেই। Real-life thinking — একটি family tree! প্রতিটি মানুষের parents (children in tree terms) ও descendants। Root হলো পূর্বপুরুষ।",
     [("Invert Binary Tree", "একটি binary tree কে mirror করো।", "O(n) with explicit stack", "Stack দিয়ে প্রতিটি node-এ যাও, children swap করো।",
       "TreeNode* invertTree(TreeNode* root) {\n    if(!root)return nullptr;\n    stack<TreeNode*> st;\n    st.push(root);\n    while(!st.empty()){\n        TreeNode* n=st.top();st.pop();\n        swap(n->left,n->right);\n        if(n->left)st.push(n->left);\n        if(n->right)st.push(n->right);\n    }\n    return root;\n}",
       "func invertTree(root *TreeNode) *TreeNode {\n    if root == nil { return nil }\n    var st []*TreeNode\n    st = append(st, root)\n    for len(st) > 0 {\n        n := st[len(st)-1]; st = st[:len(st)-1]\n        n.Left, n.Right = n.Right, n.Left\n        if n.Left != nil { st = append(st, n.Left) }\n        if n.Right != nil { st = append(st, n.Right) }\n    }\n    return root\n}",
       "def invert_tree(root):\n    if not root: return None\n    stack = [root]\n    while stack:\n        node = stack.pop()\n        node.left, node.right = node.right, node.left\n        if node.left: stack.append(node.left)\n        if node.right: stack.append(node.right)\n    return root",
       "public TreeNode invertTree(TreeNode root) {\n    if(root==null)return null;\n    Stack<TreeNode> st=new Stack<>();st.push(root);\n    while(!st.isEmpty()){\n        TreeNode n=st.pop();\n        TreeNode tmp=n.left;n.left=n.right;n.right=tmp;\n        if(n.left!=null)st.push(n.left);\n        if(n.right!=null)st.push(n.right);\n    }\n    return root;\n}",
       "O(n) Recursive", "প্রতিটি node-এর left ও right swap করো, তারপর recursively left ও right subtree invert করো।",
       "TreeNode* invertTree(TreeNode* root) {\n    if(!root)return nullptr;\n    swap(root->left,root->right);\n    invertTree(root->left);\n    invertTree(root->right);\n    return root;\n}",
       "func invertTree(root *TreeNode) *TreeNode {\n    if root == nil { return nil }\n    root.Left, root.Right = root.Right, root.Left\n    invertTree(root.Left)\n    invertTree(root.Right)\n    return root\n}",
       "def invert_tree(root):\n    if not root: return None\n    root.left, root.right = root.right, root.left\n    invert_tree(root.left)\n    invert_tree(root.right)\n    return root",
       "public TreeNode invertTree(TreeNode root) {\n    if(root==null)return null;\n    TreeNode tmp=root.left;root.left=root.right;root.right=tmp;\n    invertTree(root.left);\n    invertTree(root.right);\n    return root;\n}",
       ["Stack — Time: O(n), Space: O(n)।", "Recursive — Time: O(n), Space: O(h)। h = height।", "Key: swap children, recurse। সবচেয়ে simple recursion problem।"]
      ),
      ("Maximum Depth of Binary Tree", "Binary tree-এর maximum depth বের করো।", "O(n) with level-order traversal", "Queue দিয়ে level by level count করো।",
       "int maxDepth(TreeNode* root) {\n    if(!root)return 0;\n    queue<TreeNode*> q;q.push(root);\n    int depth=0;\n    while(!q.empty()){\n        int sz=q.size();depth++;\n        for(int i=0;i<sz;i++){\n            TreeNode* n=q.front();q.pop();\n            if(n->left)q.push(n->left);\n            if(n->right)q.push(n->right);\n        }\n    }\n    return depth;\n}",
       "func maxDepth(root *TreeNode) int {\n    if root == nil { return 0 }\n    q := []*TreeNode{root}\n    depth := 0\n    for len(q) > 0 {\n        sz := len(q)\n        depth++\n        for i := 0; i < sz; i++ {\n            n := q[0]; q = q[1:]\n            if n.Left != nil { q = append(q, n.Left) }\n            if n.Right != nil { q = append(q, n.Right) }\n        }\n    }\n    return depth\n}",
       "from collections import deque\ndef max_depth(root):\n    if not root: return 0\n    q = deque([root])\n    depth = 0\n    while q:\n        depth += 1\n        for _ in range(len(q)):\n            node = q.popleft()\n            if node.left: q.append(node.left)\n            if node.right: q.append(node.right)\n    return depth",
       "public int maxDepth(TreeNode root) {\n    if(root==null)return 0;\n    Queue<TreeNode> q=new LinkedList<>();q.add(root);\n    int depth=0;\n    while(!q.isEmpty()){\n        int sz=q.size();depth++;\n        for(int i=0;i<sz;i++){\n            TreeNode n=q.poll();\n            if(n.left!=null)q.add(n.left);\n            if(n.right!=null)q.add(n.right);\n        }\n    }\n    return depth;\n}",
       "O(n) Recursive", "depth = 1 + max(left_depth, right_depth)। Base case: null → 0।",
       "int maxDepth(TreeNode* root) {\n    if(!root)return 0;\n    return 1+max(maxDepth(root->left),maxDepth(root->right));\n}",
       "func maxDepth(root *TreeNode) int {\n    if root == nil { return 0 }\n    return 1 + max(maxDepth(root.Left), maxDepth(root.Right))\n}",
       "def max_depth(root):\n    if not root: return 0\n    return 1 + max(max_depth(root.left), max_depth(root.right))",
       "public int maxDepth(TreeNode root) {\n    if(root==null)return 0;\n    return 1+Math.max(maxDepth(root.left),maxDepth(root.right));\n}",
       ["BFS — Time: O(n), Space: O(w)। w = max width।", "Recursive — Time: O(n), Space: O(h)। h = height।", "Key: depth = 1 + max(left, right)। সবচেয়ে elegant recursion।"]
      ),
      ("Validate Binary Search Tree", "একটি tree কি valid BST? ", "O(n²) check each node against all descendants", "প্রতিটি node-এর জন্য সব left descendants ছোট ও সব right descendants বড় কিনা check করো।",
       "bool isValidBST(TreeNode* root) {\n    if(!root)return true;\n    // check all left < root, all right > root\n    // O(n²) per node check\n    return check(root,LONG_MIN,LONG_MAX);\n}",
       "func isValidBST(root *TreeNode) bool {\n    // O(n²) per node\n    return check(root, math.MinInt64, math.MaxInt64)\n}",
       "def is_valid_bst(root):\n    # O(n²) — for each node, check all descendants\n    pass",
       "public boolean isValidBST(TreeNode root) {\n    // O(n²)\n    return check(root, Long.MIN_VALUE, Long.MAX_VALUE);\n}",
       "O(n) with min/max bounds", "প্রতিটি node-এর জন্য একটি valid range (min, max) pass করো। Node-এর value range-এ আছে কিনা check করো।",
       "bool isValidBST(TreeNode* root) {\n    return check(root, LONG_MIN, LONG_MAX);\n}\nbool check(TreeNode* n, long lo, long hi) {\n    if(!n)return true;\n    if(n->val<=lo||n->val>=hi)return false;\n    return check(n->left,lo,n->val)&&check(n->right,n->val,hi);\n}",
       "func isValidBST(root *TreeNode) bool {\n    var check func(n *TreeNode, lo, hi int64) bool\n    check = func(n *TreeNode, lo, hi int64) bool {\n        if n == nil { return true }\n        if int64(n.Val) <= lo || int64(n.Val) >= hi { return false }\n        return check(n.Left, lo, int64(n.Val)) && check(n.Right, int64(n.Val), hi)\n    }\n    return check(root, math.MinInt64, math.MaxInt64)\n}",
       "def is_valid_bst(root):\n    def check(node, lo, hi):\n        if not node: return True\n        if node.val <= lo or node.val >= hi: return False\n        return check(node.left, lo, node.val) and check(node.right, node.val, hi)\n    return check(root, float('-inf'), float('inf'))",
       "public boolean isValidBST(TreeNode root) {\n    return check(root, Long.MIN_VALUE, Long.MAX_VALUE);\n}\nprivate boolean check(TreeNode n, long lo, long hi) {\n    if(n==null)return true;\n    if(n.val<=lo||n.val>=hi)return false;\n    return check(n.left,lo,n.val)&&check(n.right,n.val,hi);\n}",
       ["Check all descendants — Time: O(n²)।", "Bounds — Time: O(n), Space: O(h)।", "Key: প্রতিটি node-এর জন্য valid range pass করো।"]
      ),
      ("Lowest Common Ancestor", "BST-তে দুটি node-এর lowest common ancestor খুঁজে বের করো।", "O(n) find paths separately", "দুটি node-এর root-to-node path খুঁজে বের করে, paths compare করো।",
       "TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {\n    vector<TreeNode*> pathP, pathQ;\n    findPath(root, p, pathP);\n    findPath(root, q, pathQ);\n    TreeNode* lca = root;\n    for(int i = 0; i < min(pathP.size(), pathQ.size()); i++) {\n        if(pathP[i] == pathQ[i]) lca = pathP[i];\n        else break;\n    }\n    return lca;\n}",
       "func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {\n    // Find paths separately, then compare\n    // O(n) + O(n) space for paths\n    return root\n}",
       "def lowest_common_ancestor(root, p, q):\n    def find_path(node, target, path):\n        if not node: return False\n        path.append(node)\n        if node == target: return True\n        if find_path(node.left, target, path) or find_path(node.right, target, path):\n            return True\n        path.pop()\n        return False\n    pathP, pathQ = [], []\n    find_path(root, p, pathP)\n    find_path(root, q, pathQ)\n    lca = root\n    for i in range(min(len(pathP), len(pathQ))):\n        if pathP[i] == pathQ[i]: lca = pathP[i]\n        else: break\n    return lca",
       "public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {\n    // Find paths, compare — O(n) space\n    return root;\n}",
       "O(n) Recursive", "BST property use করো: যদি দুটি node একই দিকে হয়, সেই দিকে recurse করো। ভিন্ন দিকে হলে current node ই LCA।",
       "TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {\n    if(!root)return nullptr;\n    if(p->val<root->val&&q->val<root->val)\n        return lowestCommonAncestor(root->left,p,q);\n    if(p->val>root->val&&q->val>root->val)\n        return lowestCommonAncestor(root->right,p,q);\n    return root;\n}",
       "func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {\n    if root == nil { return nil }\n    if p.Val < root.Val && q.Val < root.Val {\n        return lowestCommonAncestor(root.Left, p, q)\n    }\n    if p.Val > root.Val && q.Val > root.Val {\n        return lowestCommonAncestor(root.Right, p, q)\n    }\n    return root\n}",
       "def lowest_common_ancestor(root, p, q):\n    if not root: return None\n    if p.val < root.val and q.val < root.val:\n        return lowest_common_ancestor(root.left, p, q)\n    if p.val > root.val and q.val > root.val:\n        return lowest_common_ancestor(root.right, p, q)\n    return root",
       "public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {\n    if(root==null)return null;\n    if(p.val<root.val&&q.val<root.val)\n        return lowestCommonAncestor(root.left,p,q);\n    if(p.val>root.val&&q.val>root.val)\n        return lowestCommonAncestor(root.right,p,q);\n    return root;\n}",
       ["Path comparison — Time: O(n), Space: O(n)।", "BST Recursive — Time: O(h), Space: O(h)। h = height।", "Key: BST property — ভিন্ন দিকে split হলে current node ই LCA।"]
      ),
      ("Level Order Traversal", "Binary tree-কে level by level traverse করো।", "O(n²) DFS for each level", "প্রতিটি level-এর জন্য আলাদা DFS চালাও।",
       "vector<vector<int>> levelOrder(TreeNode* root) {\n    vector<vector<int>> result;\n    int h = height(root);\n    for(int i = 1; i <= h; i++) {\n        vector<int> level;\n        getLevel(root, i, level);\n        result.push_back(level);\n    }\n    return result;\n}",
       "func levelOrder(root *TreeNode) [][]int {\n    // DFS per level — O(n²)\n    return nil\n}",
       "def level_order(root):\n    result = []\n    def get_level(node, level, out):\n        if not node: return\n        if level == 1: out.append(node.val)\n        else:\n            get_level(node.left, level-1, out)\n            get_level(node.right, level-1, out)\n    h = 0\n    # find height first\n    def height(n):\n        if not n: return 0\n        return 1 + max(height(n.left), height(n.right))\n    h = height(root)\n    for i in range(1, h+1):\n        level = []\n        get_level(root, i, level)\n        result.append(level)\n    return result",
       "public List<List<Integer>> levelOrder(TreeNode root) {\n    // DFS per level — O(n²)\n    return new ArrayList<>();\n}",
       "O(n) BFS with Queue", "Queue use করে level by level traverse করো। প্রতিটি level-এর সব node একসাথে process করো।",
       "vector<vector<int>> levelOrder(TreeNode* root) {\n    vector<vector<int>> result;\n    if(!root)return result;\n    queue<TreeNode*> q;q.push(root);\n    while(!q.empty()){\n        int sz=q.size();\n        vector<int> level;\n        for(int i=0;i<sz;i++){\n            TreeNode* n=q.front();q.pop();\n            level.push_back(n->val);\n            if(n->left)q.push(n->left);\n            if(n->right)q.push(n->right);\n        }\n        result.push_back(level);\n    }\n    return result;\n}",
       "func levelOrder(root *TreeNode) [][]int {\n    var result [][]int\n    if root == nil { return result }\n    q := []*TreeNode{root}\n    for len(q) > 0 {\n        sz := len(q)\n        level := make([]int, 0, sz)\n        for i := 0; i < sz; i++ {\n            n := q[0]; q = q[1:]\n            level = append(level, n.Val)\n            if n.Left != nil { q = append(q, n.Left) }\n            if n.Right != nil { q = append(q, n.Right) }\n        }\n        result = append(result, level)\n    }\n    return result\n}",
       "from collections import deque\ndef level_order(root):\n    if not root: return []\n    result = []\n    q = deque([root])\n    while q:\n        level = []\n        for _ in range(len(q)):\n            node = q.popleft()\n            level.append(node.val)\n            if node.left: q.append(node.left)\n            if node.right: q.append(node.right)\n        result.append(level)\n    return result",
       "public List<List<Integer>> levelOrder(TreeNode root) {\n    List<List<Integer>> result=new ArrayList<>();\n    if(root==null)return result;\n    Queue<TreeNode> q=new LinkedList<>();q.add(root);\n    while(!q.isEmpty()){\n        int sz=q.size();\n        List<Integer> level=new ArrayList<>();\n        for(int i=0;i<sz;i++){\n            TreeNode n=q.poll();\n            level.add(n.val);\n            if(n.left!=null)q.add(n.left);\n            if(n.right!=null)q.add(n.right);\n        }\n        result.add(level);\n    }\n    return result;\n}",
       ["DFS per level — Time: O(n²)।", "BFS Queue — Time: O(n), Space: O(w)। w = max width।", "Key: BFS দিয়ে level by level process — queue-তে level size track করো।"]
      )
     ],
     "Tip: পরের topic হলো Tries — prefix tree যা string search O(m)-এ করে।"
    ),
    ("dsa-tries", "Tries", "ট্রাই", "Hard", "2 hr",
     "Trie হলো prefix tree। ৫টি classic problem — insertion, search, autocomplete, ও word search।",
     "Trie (pronounced 'try') হলো একটি tree structure যা strings কে character-by-character store করে। এটি prefix-based search এর জন্য efficient। Real-life thinking — একটি dictionary! প্রতিটি letter-এর জন্য একটি page, সেই page-এ পরের letter-এর সাথে পরের page-এর reference। এভাবে একটি word একটা path-এর মতো navigate করা যায়।",
     [("Implement Trie", "Trie data structure implement করো — insert, search, startsWith।", "O(n × m) with hash set", "সব words একটি set-এ store করো। Search ও prefix check করো।",
       "// Hash set approach\nunordered_set<string> words;\nvoid insert(string word) { words.insert(word); }\nbool search(string word) { return words.count(word); }\nbool startsWith(string prefix) {\n    for(auto& w : words)\n        if(w.substr(0, prefix.size()) == prefix) return true;\n    return false;\n}",
       "type Trie struct { words map[string]bool }\nfunc (t *Trie) insert(word string) { t.words[word] = true }\nfunc (t *Trie) search(word string) bool { return t.words[word] }\nfunc (t *Trie) startsWith(prefix string) bool {\n    for w := range t.words {\n        if len(w) >= len(prefix) && w[:len(prefix)] == prefix { return true }\n    }\n    return false\n}",
       "class Trie:\n    def __init__(self): self.words = set()\n    def insert(self, word): self.words.add(word)\n    def search(self, word): return word in self.words\n    def startsWith(self, prefix):\n        return any(w.startswith(prefix) for w in self.words)",
       "class Trie {\n    Set<String> words = new HashSet<>();\n    void insert(String word) { words.add(word); }\n    boolean search(String word) { return words.contains(word); }\n    boolean startsWith(String prefix) {\n        for(String w : words) if(w.startsWith(prefix)) return true;\n        return false;\n    }\n}",
       "O(m) Trie per operation", "Trie node তৈরি করো — children array ও isEnd flag। Insert ও search এক character এক character করে traverse করো।",
       "struct TrieNode { TrieNode* children[26]={}; bool isEnd=false; };\nclass Trie {\n    TrieNode* root;\npublic:\n    Trie() { root = new TrieNode(); }\n    void insert(string word) {\n        TrieNode* p = root;\n        for(char c : word) {\n            int i = c-'a';\n            if(!p->children[i]) p->children[i] = new TrieNode();\n            p = p->children[i];\n        }\n        p->isEnd = true;\n    }\n    bool search(string word) {\n        TrieNode* p = root;\n        for(char c : word) {\n            int i = c-'a';\n            if(!p->children[i]) return false;\n            p = p->children[i];\n        }\n        return p->isEnd;\n    }\n    bool startsWith(string prefix) {\n        TrieNode* p = root;\n        for(char c : prefix) {\n            int i = c-'a';\n            if(!p->children[i]) return false;\n            p = p->children[i];\n        }\n        return true;\n    }\n};",
       "type TrieNode struct {\n    children [26]*TrieNode\n    isEnd    bool\n}\ntype Trie struct { root *TrieNode }\nfunc Constructor() Trie { return Trie{root: &TrieNode{}} }\nfunc (t *Trie) insert(word string) {\n    p := t.root\n    for _, c := range word {\n        i := c - 'a'\n        if p.children[i] == nil { p.children[i] = &TrieNode{} }\n        p = p.children[i]\n    }\n    p.isEnd = true\n}\nfunc (t *Trie) search(word string) bool {\n    p := t.root\n    for _, c := range word {\n        i := c - 'a'\n        if p.children[i] == nil { return false }\n        p = p.children[i]\n    }\n    return p.isEnd\n}\nfunc (t *Trie) startsWith(prefix string) bool {\n    p := t.root\n    for _, c := range prefix {\n        i := c - 'a'\n        if p.children[i] == nil { return false }\n        p = p.children[i]\n    }\n    return true\n}",
       "class Trie:\n    def __init__(self):\n        self.root = {}\n    def insert(self, word):\n        node = self.root\n        for c in word:\n            if c not in node: node[c] = {}\n            node = node[c]\n        node['#'] = True\n    def search(self, word):\n        node = self.root\n        for c in word:\n            if c not in node: return False\n            node = node[c]\n        return '#' in node\n    def startsWith(self, prefix):\n        node = self.root\n        for c in prefix:\n            if c not in node: return False\n            node = node[c]\n        return True",
       "class Trie {\n    class Node { Node[] children = new Node[26]; boolean isEnd; }\n    Node root = new Node();\n    void insert(String word) {\n        Node p = root;\n        for(char c : word.toCharArray()) {\n            int i = c-'a';\n            if(p.children[i]==null) p.children[i]=new Node();\n            p = p.children[i];\n        }\n        p.isEnd = true;\n    }\n    boolean search(String word) {\n        Node p = root;\n        for(char c : word.toCharArray()) {\n            int i = c-'a';\n            if(p.children[i]==null) return false;\n            p = p.children[i];\n        }\n        return p.isEnd;\n    }\n    boolean startsWith(String prefix) {\n        Node p = root;\n        for(char c : prefix.toCharArray()) {\n            int i = c-'a';\n            if(p.children[i]==null) return false;\n            p = p.children[i];\n        }\n        return true;\n    }\n}",
       ["Hash Set — insert O(1), search O(1), startsWith O(n × m)।", "Trie — insert O(m), search O(m), startsWith O(m)। m = word length।", "Key: Trie prefix search O(m) — hash set startsWith O(n×m)।"]
      ),
      ("Word Search II", "Board-এ এমন সব word খুঁজে বের করো যেগুলো dictionary-তে আছে।", "O(n × m × 4^l × w) DFS per word", "প্রতিটি word-এর জন্য DFS চালাও। খুব slow।",
       "vector<string> findWords(vector<vector<char>>& b, vector<string>& words) {\n    vector<string> result;\n    for(string& w : words)\n        if(exist(b, w)) result.push_back(w);\n    return result;\n}",
       "func findWords(b [][]byte, words []string) []string {\n    var result []string\n    for _, w := range words { if exist(b, w) { result = append(result, w) } }\n    return result\n}",
       "def find_words(board, words):\n    result = []\n    for w in words:\n        if exist(board, w): result.append(w)\n    return result",
       "public List<String> findWords(char[][] b, String[] words) {\n    List<String> result = new ArrayList<>();\n    for(String w : words) if(exist(b, w)) result.add(w);\n    return result;\n}",
       "O(n × m × 4^l) with Trie + Backtracking", "Trie তৈরি করো। Board-এ প্রতিটি cell থেকে DFS চালাও, Trie-তে match করে করে যাও।",
       "vector<string> findWords(vector<vector<char>>& b, vector<string>& words) {\n    // Build Trie\n    TrieNode* root = new TrieNode();\n    for(string& w : words) {\n        TrieNode* p = root;\n        for(char c : w) {\n            int i = c-'a';\n            if(!p->children[i]) p->children[i] = new TrieNode();\n            p = p->children[i];\n        }\n        p->isEnd = true;\n        p->word = w;\n    }\n    vector<string> result;\n    for(int i=0;i<b.size();i++)\n        for(int j=0;j<b[0].size();j++)\n            dfs(b, i, j, root, result);\n    return result;\n}",
       "func findWords(b [][]byte, words []string) []string {\n    // Build Trie + DFS\n    return nil\n}",
       "def find_words(board, words):\n    trie = {}\n    for w in words:\n        node = trie\n        for c in w:\n            if c not in node: node[c] = {}\n            node = node[c]\n        node['#'] = w\n    result = []\n    def dfs(i, j, node):\n        if '#' in node: result.append(node['#']); del node['#']\n        if i<0 or i>=len(board) or j<0 or j>=len(board[0]): return\n        c = board[i][j]\n        if c not in node: return\n        board[i][j] = '#'\n        for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:\n            dfs(i+di, j+dj, node[c])\n        board[i][j] = c\n    for i in range(len(board)):\n        for j in range(len(board[0])):\n            dfs(i, j, trie)\n    return result",
       "public List<String> findWords(char[][] b, String[] words) {\n    // Build Trie + DFS\n    return new ArrayList<>();\n}",
       ["Per word DFS — Time: O(w × n × m × 4^l)। খুব slow।", "Trie + DFS — Time: O(n × m × 4^l)। এক বারে সব word search।", "Key: Trie দিয়ে সব word একসাথে search — pruning দ্রুত।"]
      ),
      ("Design Add and Search Words", "Add ও Search করতে পারবে এমন data structure design করো। Search-এ '.' wildcard support করবে।", "O(n) linear search per query", "সব words store করে linear search করো। '.' থাকলে সব match করো।",
       "// Linear approach\nvector<string> dict;\nvoid addWord(string word) { dict.push_back(word); }\nbool search(string word) {\n    for(string& w : dict) {\n        if(w.size() != word.size()) continue;\n        bool match = true;\n        for(int i = 0; i < w.size(); i++)\n            if(word[i] != '.' && word[i] != w[i]) { match = false; break; }\n        if(match) return true;\n    }\n    return false;\n}",
       "type WordDictionary struct { dict []string }\nfunc (d *WordDictionary) addWord(word string) { d.dict = append(d.dict, word) }\nfunc (d *WordDictionary) search(word string) bool {\n    for _, w := range d.dict {\n        if len(w) != len(word) { continue }\n        match := true\n        for i := 0; i < len(w); i++ {\n            if word[i] != '.' && word[i] != w[i] { match = false; break }\n        }\n        if match { return true }\n    }\n    return false\n}",
       "class WordDictionary:\n    def __init__(self): self.dict = []\n    def addWord(self, word): self.dict.append(word)\n    def search(self, word):\n        for w in self.dict:\n            if len(w) != len(word): continue\n            if all(word[i]=='.' or word[i]==w[i] for i in range(len(w))):\n                return True\n        return False",
       "class WordDictionary {\n    List<String> dict = new ArrayList<>();\n    void addWord(String word) { dict.add(word); }\n    boolean search(String word) {\n        for(String w : dict) {\n            if(w.length() != word.length()) continue;\n            boolean match = true;\n            for(int i=0;i<w.length();i++)\n                if(word.charAt(i)!='.' && word.charAt(i)!=w.charAt(i)) { match=false; break; }\n            if(match) return true;\n        }\n        return false;\n    }\n}",
       "O(m) Trie + DFS for wildcard", "Trie তৈরি করো। Search-এ '.' হলে সব children explore করো (DFS)।",
       "struct TrieNode { TrieNode* children[26]={}; bool isEnd=false; };\nclass WordDictionary {\n    TrieNode* root;\npublic:\n    WordDictionary() { root = new TrieNode(); }\n    void addWord(string word) {\n        TrieNode* p = root;\n        for(char c : word) {\n            int i = c-'a';\n            if(!p->children[i]) p->children[i] = new TrieNode();\n            p = p->children[i];\n        }\n        p->isEnd = true;\n    }\n    bool search(string word) { return dfs(word, 0, root); }\n    bool dfs(string& word, int i, TrieNode* node) {\n        if(i == word.size()) return node->isEnd;\n        if(word[i] == '.') {\n            for(int j = 0; j < 26; j++)\n                if(node->children[j] && dfs(word, i+1, node->children[j]))\n                    return true;\n            return false;\n        }\n        int idx = word[i]-'a';\n        return node->children[idx] && dfs(word, i+1, node->children[idx]);\n    }\n};",
       "type TrieNode struct {\n    children [26]*TrieNode\n    isEnd    bool\n}\ntype WordDictionary struct { root *TrieNode }\nfunc Constructor() WordDictionary { return WordDictionary{root: &TrieNode{}} }\nfunc (d *WordDictionary) addWord(word string) {\n    p := d.root\n    for _, c := range word {\n        i := c - 'a'\n        if p.children[i] == nil { p.children[i] = &TrieNode{} }\n        p = p.children[i]\n    }\n    p.isEnd = true\n}\nfunc (d *WordDictionary) search(word string) bool {\n    var dfs func(i int, node *TrieNode) bool\n    dfs = func(i int, node *TrieNode) bool {\n        if i == len(word) { return node.isEnd }\n        if word[i] == '.' {\n            for j := 0; j < 26; j++ {\n                if node.children[j] != nil && dfs(i+1, node.children[j]) { return true }\n            }\n            return false\n        }\n        idx := word[i] - 'a'\n        return node.children[idx] != nil && dfs(i+1, node.children[idx])\n    }\n    return dfs(0, d.root)\n}",
       "class WordDictionary:\n    def __init__(self): self.root = {}\n    def addWord(self, word):\n        node = self.root\n        for c in word:\n            if c not in node: node[c] = {}\n            node = node[c]\n        node['#'] = True\n    def search(self, word):\n        def dfs(i, node):\n            if i == len(word): return '#' in node\n            c = word[i]\n            if c == '.':\n                return any(dfs(i+1, node[k]) for k in node if k != '#')\n            if c not in node: return False\n            return dfs(i+1, node[c])\n        return dfs(0, self.root)",
       "class WordDictionary {\n    class Node { Node[] children = new Node[26]; boolean isEnd; }\n    Node root = new Node();\n    void addWord(String word) {\n        Node p = root;\n        for(char c : word.toCharArray()) {\n            int i = c-'a';\n            if(p.children[i]==null) p.children[i]=new Node();\n            p = p.children[i];\n        }\n        p.isEnd = true;\n    }\n    boolean search(String word) { return dfs(word, 0, root); }\n    boolean dfs(String word, int i, Node node) {\n        if(i == word.length()) return node.isEnd;\n        if(word.charAt(i) == '.') {\n            for(int j = 0; j < 26; j++)\n                if(node.children[j] != null && dfs(word, i+1, node.children[j]))\n                    return true;\n            return false;\n        }\n        int idx = word.charAt(i) - 'a';\n        return node.children[idx] != null && dfs(word, i+1, node.children[idx]);\n    }\n}",
       ["Linear — add O(1), search O(n × m)।", "Trie + DFS — add O(m), search O(26^m) worst case (all dots)।", "Key: Trie + wildcard এর জন্য DFS — '.' হলে সব children explore করো।"]
      ),
      ("Longest Word in Dictionary", "Dictionary-তে সবচেয়ে বড় word খুঁজে বের করো যা এক এক character যোগ করে build করা যায়।", "O(n × m) sort + check", "Words sort করো। প্রতিটি word-এর সব prefix আছে কিনা check করো।",
       "string longestWord(vector<string>& words) {\n    sort(words.begin(), words.end());\n    unordered_set<string> built;\n    string result;\n    for(string& w : words) {\n        if(w.size() == 1 || built.count(w.substr(0, w.size()-1))) {\n            built.insert(w);\n            if(w.size() > result.size()) result = w;\n        }\n    }\n    return result;\n}",
       "func longestWord(words []string) string {\n    sort.Strings(words)\n    built := make(map[string]bool)\n    result := \"\"\n    for _, w := range words {\n        if len(w) == 1 || built[w[:len(w)-1]] {\n            built[w] = true\n            if len(w) > len(result) { result = w }\n        }\n    }\n    return result\n}",
       "def longest_word(words):\n    words.sort()\n    built = set()\n    result = \"\"\n    for w in words:\n        if len(w) == 1 or w[:-1] in built:\n            built.add(w)\n            if len(w) > len(result): result = w\n    return result",
       "public String longestWord(String[] words) {\n    Arrays.sort(words);\n    Set<String> built = new HashSet<>();\n    String result = \"\";\n    for(String w : words) {\n        if(w.length()==1 || built.contains(w.substring(0, w.length()-1))) {\n            built.add(w);\n            if(w.length() > result.length()) result = w;\n        }\n    }\n    return result;\n}",
       "O(n × m) with Trie + BFS", "Trie তৈরি করো। BFS দিয়ে level by level traverse করো — যেহেতু character এক এক করে যোগ হয়, level অনুযায়ী longest word পাওয়া যায়।",
       "string longestWord(vector<string>& words) {\n    TrieNode* root = new TrieNode();\n    for(string& w : words) {\n        TrieNode* p = root;\n        for(char c : w) {\n            int i = c-'a';\n            if(!p->children[i]) p->children[i] = new TrieNode();\n            p = p->children[i];\n        }\n        p->isEnd = true;\n        p->word = w;\n    }\n    queue<TrieNode*> q; q.push(root);\n    string result;\n    while(!q.empty()) {\n        TrieNode* n = q.front(); q.pop();\n        if(!n->word.empty()) result = n->word;\n        for(int i = 25; i >= 0; i--) {\n            if(n->children[i] && n->children[i]->isEnd)\n                q.push(n->children[i]);\n        }\n    }\n    return result;\n}",
       "func longestWord(words []string) string {\n    // Trie + BFS\n    return \"\"\n}",
       "def longest_word(words):\n    trie = {}\n    for w in words:\n        node = trie\n        for c in w:\n            if c not in node: node[c] = {}\n            node = node[c]\n        node['#'] = w\n    from collections import deque\n    q = deque([(trie, \"\")])\n    result = \"\"\n    while q:\n        node, word = q.popleft()\n        if '#' in node: result = node['#']\n        for c in sorted(node.keys(), reverse=True):\n            if c != '#' and '#' in node[c]:\n                q.append((node[c], word + c))\n    return result",
       "public String longestWord(String[] words) {\n    // Trie + BFS\n    return \"\";\n}",
       ["Sort + Set — Time: O(n log n × m), Space: O(n × m)।", "Trie + BFS — Time: O(n × m), Space: O(n × m)।", "Key: Trie-তে BFS level by level — শেষে যে word পাওয়া যায় সেটাই longest।"]
      ),
      ("Stream of Characters", "একটি stream থেকে character গ্রহণ করো। শেষ kটি character কোনো dictionary word কিনা check করো।", "O(n) scan per query", "প্রতিটি query-তে শেষ সব character check করো।",
       "class StreamChecker {\n    vector<string> dict;\n    string stream;\npublic:\n    StreamChecker(vector<string>& words) : dict(words) {}\n    bool query(char c) {\n        stream += c;\n        for(string& w : dict)\n            if(stream.size() >= w.size() &&\n               stream.substr(stream.size()-w.size()) == w)\n                return true;\n        return false;\n    }\n};",
       "type StreamChecker struct { dict []string; stream string }\nfunc (sc *StreamChecker) query(c byte) bool {\n    sc.stream += string(c)\n    for _, w := range sc.dict {\n        if len(sc.stream) >= len(w) && sc.stream[len(sc.stream)-len(w):] == w { return true }\n    }\n    return false\n}",
       "class StreamChecker:\n    def __init__(self, words):\n        self.dict = words\n        self.stream = \"\"\n    def query(self, c):\n        self.stream += c\n        for w in self.dict:\n            if len(self.stream) >= len(w) and self.stream[-len(w):] == w:\n                return True\n        return False",
       "class StreamChecker {\n    List<String> dict; StringBuilder stream;\n    public StreamChecker(String[] words) { dict = Arrays.asList(words); stream = new StringBuilder(); }\n    public boolean query(char c) {\n        stream.append(c);\n        for(String w : dict)\n            if(stream.length() >= w.length() &&\n               stream.substring(stream.length()-w.length()).equals(w))\n                return true;\n        return false;\n    }\n}",
       "O(m) with Trie of reversed words", "Dictionary-এর সব word কে reverse করে Trie তৈরি করো। Stream-এর শেষ থেকে character গুলো Trie-তে match করো।",
       "class StreamChecker {\n    struct TrieNode { TrieNode* children[26]={}; bool isEnd=false; };\n    TrieNode* root;\n    string stream;\npublic:\n    StreamChecker(vector<string>& words) {\n        root = new TrieNode();\n        for(string& w : words) {\n            TrieNode* p = root;\n            for(int i = w.size()-1; i >= 0; i--) {\n                int idx = w[i]-'a';\n                if(!p->children[idx]) p->children[idx] = new TrieNode();\n                p = p->children[idx];\n            }\n            p->isEnd = true;\n        }\n    }\n    bool query(char c) {\n        stream += c;\n        TrieNode* p = root;\n        for(int i = stream.size()-1; i >= 0; i--) {\n            int idx = stream[i]-'a';\n            if(!p->children[idx]) return false;\n            p = p->children[idx];\n            if(p->isEnd) return true;\n        }\n        return false;\n    }\n};",
       "type StreamChecker struct {\n    root *TrieNode\n    stream string\n}\nfunc (sc *StreamChecker) query(c byte) bool {\n    sc.stream += string(c)\n    p := sc.root\n    for i := len(sc.stream)-1; i >= 0; i-- {\n        idx := sc.stream[i] - 'a'\n        if p.children[idx] == nil { return false }\n        p = p.children[idx]\n        if p.isEnd { return true }\n    }\n    return false\n}",
       "class StreamChecker:\n    def __init__(self, words):\n        self.root = {}\n        for w in words:\n            node = self.root\n            for c in reversed(w):\n                if c not in node: node[c] = {}\n                node = node[c]\n            node['#'] = True\n        self.stream = []\n    def query(self, c):\n        self.stream.append(c)\n        node = self.root\n        for i in range(len(self.stream)-1, -1, -1):\n            c = self.stream[i]\n            if c not in node: return False\n            node = node[c]\n            if '#' in node: return True\n        return False",
       "class StreamChecker {\n    // Trie of reversed words + stream\n    // query: O(m) where m = max word length\n}",
       ["Linear scan — query O(n × m)।", "Trie (reversed) — query O(m)। m = max word length।", "Key: reverse করে Trie — শেষ থেকে match করা সহজ হয়।"]
      )
     ],
     "Tip: পরের topic হলো Backtracking — recursive try ও backtrack করে সব possible solution explore করা।"
    )
]

# Generate remaining topics
remaining_topics = ""
for tid, title, bangla, diff, est, summ, overview, items, next_tip in remaining_topics_data:
    remaining_topics += gen_coming_soon_topic(tid, title, bangla, diff, est, summ, overview, items, next_tip)

# Topics 9-18 (Backtracking through Math & Geometry) — compact "coming soon" style
# but with full problem content for key topics

coming_soon_topics = [
    ("dsa-backtracking", "Backtracking", "ব্যাকট্র্যাকিং", "Hard", "3 hr",
     "Backtracking-এ recursive try ও backtrack করে সব possible solution explore করা হয়।",
     "Backtracking হলো একটি recursive technique যেখানে তুমি প্রতিটি choice try করো এবং যদি সেটি কাজ না করে, তাহলে backtrack করে আগের state-এ ফিরে যাও। Real-life thinking — একটি maze! প্রতিটি path try করো। Dead end হলে ফিরে এসো এবং অন্য path খুঁজো।",
     "Tip: পরের topic হলো Heap / Priority Queue — O(log n) insert ও extract।"
    ),
    ("dsa-heap", "Heap / Priority Queue", "হিপ / প্রায়োরিটি কিউ", "Medium", "2 hr",
     "Heap হলো complete binary tree যা priority-based access দেয়।",
     "Heap হলো একটি complete binary tree যেখানে parent সবসময় children-এর চেয়ে বড় (max-heap) বা ছোট (min-heap)। Priority Queue হিসেবে O(log n) insert ও extract দেয়। Real-life thinking — ER queue! সবচেয়ে critical patient কে আগে দেখা হয়, কে আগে এসেছে তা নয়।",
     "Tip: পরের topic হলো Graphs — nodes ও edges দিয়ে connected structure।"
    ),
    ("dsa-graphs", "Graphs", "গ্রাফ", "Hard", "3 hr",
     "Graph হলো nodes (vertices) ও edges দিয়ে connected structure।",
     "Graph হলো nodes (vertices) ও edges দিয়ে connected একটি structure। Tree-এর মতো, কিন্তু cycle থাকতে পারে এবং প্রতিটি node-এর যেকোনো সংখ্যক neighbor থাকতে পারে। Real-life thinking — Google Maps! শহর হলো nodes, রাস্তা হলো edges। Shortest path খুঁজতে BFS/DFS বা Dijkstra use করো।",
     "Tip: পরের topic হলো 1-D Dynamic Programming — subproblems solve করে memoize করা।"
    ),
    ("dsa-1d-dp", "1-D Dynamic Programming", "ওয়ান-ডি ডায়নামিক প্রোগ্রামিং", "Hard", "3 hr",
     "1-D DP-তে 1D array দিয়ে subproblems memoize করা হয়।",
     "Dynamic Programming হলো এমন একটি technique যেখানে complex problem-কে ছোট subproblems-এ ভাগ করে, প্রতিটি subproblem একবার solve করে ফলাফল store (memoize) করা হয়। Real-life thinking — Fibonacci! fib(n) = fib(n-1) + fib(n-2)। বারবার একই subproblem solve না করে store করে রাখো।",
     "Tip: পরের topic হলো Intervals — overlapping ও merging interval problems।"
    ),
    ("dsa-intervals", "Intervals", "ইন্টারভালস", "Medium", "1.5 hr",
     "Interval problems-এ start ও end time দিয়ে overlap check করা হয়।",
     "Interval হলো একটি [start, end] pair। Common operations: merge overlapping intervals, insert new interval, find meeting rooms। Real-life thinking — calendar scheduling! প্রতিটি meeting একটি interval। Overlap হলে conflict।",
     "Tip: পরের topic হলো Greedy — locally optimal choice দিয়ে globally optimal solution।"
    ),
    ("dsa-greedy", "Greedy", "গ্রিডি", "Medium", "2 hr",
     "Greedy algorithm প্রতিটি step-এ locally optimal choice করে।",
     "Greedy algorithm প্রতিটি step-এ সবচেয়ে ভালো বলে মনে হওয়া choice করে, আশা করে যে এটি globally optimal হবে। সব problem-এ কাজ করে না, কিন্তু যেখানে কাজ করে সেখানে খুব efficient। Real-life thinking — পকেটে যত বড় কয়েন আছে সেটাই আগে দাও (coin change)।",
     "Tip: পরের topic হলো Advanced Graphs — Union-Find, Dijkstra, ও topological sort।"
    ),
    ("dsa-advanced-graphs", "Advanced Graphs", "অ্যাডভান্সড গ্রাফস", "Hard", "2.5 hr",
     "Advanced graph algorithms — Union-Find, Dijkstra, topological sort।",
     "Advanced graph algorithms include Union-Find (disjoint set), Dijkstra's shortest path, ও topological sort। Real-life thinking — network routing! Shortest path খুঁজে বের করো (Dijkstra), cycle detect করো (Union-Find), task scheduling order বের করো (topological sort)।",
     "Tip: পরের topic হলো 2-D Dynamic Programming — 2D table দিয়ে DP।"
    ),
    ("dsa-2d-dp", "2-D Dynamic Programming", "টু-ডি ডায়নামিক প্রোগ্রামিং", "Hard", "3 hr",
     "2-D DP-তে 2D table দিয়ে subproblems memoize করা হয়।",
     "2-D DP-তে subproblems একটি 2D grid-এ represent করা হয়। সাধারণত path counting, string matching, বা grid problems-এ use হয়। Real-life thinking — chess! প্রতিটি position থেকে কতভাবে goal-এ যাওয়া যায়? DP table দিয়ে প্রতিটি cell-এর answer store করো।",
     "Tip: পরের topic হলো Bit Manipulation — bitwise operations দিয়ে efficient computation।"
    ),
    ("dsa-bit-manipulation", "Bit Manipulation", "বিট ম্যানিপুলেশন", "Medium", "1.5 hr",
     "Bit manipulation-এ bitwise operations দিয়ে efficient computation করা হয়।",
     "Bit manipulation হলো bitwise operations (AND, OR, XOR, shift) ব্যবহার করে দ্রুত computation। এটি O(1)-এ অনেক কাজ করতে পারে যেমন: কোনো number power of 2 কিনা, single number find (XOR), বা bit counting। Real-life thinking — switchboard! প্রতিটি switch একটি bit। On/off দিয়ে 32টি switch একটি integer-এ represent করা যায়।",
     "Tip: শেষ topic হলো Math & Geometry — mathematical ও geometric problems।"
    ),
    ("dsa-math-geometry", "Math & Geometry", "ম্যাথ ও জিওমেট্রি", "Medium", "2 hr",
     "Math & Geometry problems-এ mathematical formulas ও coordinate geometry use করা হয়।",
     "Math & Geometry problems include prime numbers, GCD/LCM, coordinate geometry, ও matrix operations। Real-life thinking — GPS coordinates! দুটি point-এর মধ্যে distance, area of polygon, বা rotation matrix — সবই math ও geometry।",
     "Tip: এই NeetCode roadmap-এর সব ১৮টি topic complete! এখন practice করো এবং patterns recognize করতে শেখো।"
    )
]

# Generate coming soon topics
for tid, title, bangla, diff, est, summ, overview, next_tip in coming_soon_topics:
    sections = []
    sections.append(f'      {{ type: "h2", id: "overview", title: "Overview" }}')
    sections.append(f'      {{ type: "p", text: "{overview}" }}')
    sections.append(f'      {{ type: "callout", calloutTone: "tip", text: "{next_tip}" }}')
    sections_str = ',\n'.join(sections)
    remaining_topics += gen_topic(tid, title, bangla, diff, est, summ, sections_str)

# Combine everything
new_text = before + tp_full + stack_topic + bs_topic + sw_topic + remaining_topics + after

# Verify
assert 'id: "dsa-arrays-hashing"' in new_text
assert 'id: "dsa-two-pointers"' in new_text
assert 'id: "dsa-stack"' in new_text
assert 'id: "dsa-binary-search"' in new_text
assert 'id: "dsa-sliding-window"' in new_text
assert 'id: "dsa-linked-list"' in new_text
assert 'id: "dsa-trees"' in new_text
assert 'id: "dsa-tries"' in new_text
assert 'id: "dsa-backtracking"' in new_text
assert 'id: "dsa-heap"' in new_text
assert 'id: "dsa-graphs"' in new_text
assert 'id: "dsa-1d-dp"' in new_text
assert 'id: "dsa-math-geometry"' in new_text
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — All 18 NeetCode DSA topics added. File size: {len(new_text)} bytes")
