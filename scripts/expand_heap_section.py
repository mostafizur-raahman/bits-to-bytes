#!/usr/bin/env python3
"""Expand the Heap / Priority Queue section in dsa.ts with 5 NeetCode problems."""

import re
from pathlib import Path

DSA_PATH = Path("/home/z/my-project/src/lib/content/dsa.ts")

# The new fully-expanded Heap / Priority Queue section
NEW_HEAP_SECTION = r'''  // ---- Heap / Priority Queue ----
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
'''

def main():
    content = DSA_PATH.read_text(encoding="utf-8")

    # The old (overview-only) Heap section to replace.
    old_heap = '''  // ---- Heap / Priority Queue ----
  {
    id: "dsa-heap",
    subject: "dsa",
    title: "Heap / Priority Queue",
    bangla: "হিপ / প্রায়োরিটি কিউ",
    difficulty: "Medium",
    est: "2 hr",
    summary: "Heap হলো complete binary tree যা priority-based access দেয়।",
    sections: [
      { type: "h2", id: "overview", title: "Overview" },
      { type: "p", text: "Heap হলো একটি complete binary tree যেখানে parent সবসময় children-এর চেয়ে বড় (max-heap) বা ছোট (min-heap)। Priority Queue হিসেবে O(log n) insert ও extract দেয়। Real-life thinking — ER queue! সবচেয়ে critical patient কে আগে দেখা হয়, কে আগে এসেছে তা নয়।" },
      { type: "callout", calloutTone: "tip", text: "Tip: পরের topic হলো Graphs — nodes ও edges দিয়ে connected structure।" }
    ],
  },'''

    if old_heap not in content:
        print("ERROR: Old Heap section not found exactly. Aborting.")
        # Try to find the section by ID for diagnostic
        m = re.search(r'// ---- Heap / Priority Queue ----.*?\n  \},', content, re.DOTALL)
        if m:
            print("Found Heap block. First 600 chars:")
            print(m.group(0)[:600])
        return 1

    new_content = content.replace(old_heap, NEW_HEAP_SECTION.rstrip() + "\n")
    DSA_PATH.write_text(new_content, encoding="utf-8")
    new_lines = new_content.count("\n")
    print(f"OK. New file line count: {new_lines}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
