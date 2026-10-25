#!/usr/bin/env python3
"""
Rewrite Ch 04 (Process Synchronization) with MAXIMUM BANGLA + English technical terms.
"""
from pathlib import Path

CONTENT_FILE = Path("/home/z/my-project/src/lib/content.ts")
text = CONTENT_FILE.read_text()

ch4_marker_start = "// ---- Ch 04 - Process Synchronization ----"
ch5_marker_start = "// ---- Ch 05 - Deadlocks ----"

start_idx = text.find(ch4_marker_start)
assert start_idx != -1, "Ch 04 marker not found"
end_idx = text.find(ch5_marker_start, start_idx)
assert end_idx != -1, "Ch 05 marker not found"

before = text[:start_idx]
after = text[end_idx:]

NEW_CH4 = r'''// ---- Ch 04 - Process Synchronization ----
  {
    id: "os-sync",
    subject: "os",
    title: "Ch 04 — Process Synchronization",
    bangla: "প্রসেস সিঙ্ক্রোনাইজেশন",
    difficulty: "Hard",
    est: "2 hr",
    summary:
      "যখন অনেক processes বা threads একই shared data-তে concurrently access করে, ফলাফল unpredictable বা incorrect হতে পারে। Process synchronization নিশ্চিত করে যে cooperative processes controlled ভাবে execute হয়, race conditions prevent হয় এবং data integrity preserve হয়। এই chapter-এ classic problems, solutions, ও system-level tools আলোচনা করা হয়েছে।",
    sections: [
      { type: "h2", id: "critical-section", title: "Critical Section Problem" },
      {
        type: "p",
        text: "Critical section হলো code-এর এমন একটি segment যেটি shared variables বা resources access করে (যেমন একটি file, একটি global counter) যেগুলো একাধিক process বা thread একসাথে execute করতে পারবে না।",
      },
      {
        type: "p",
        text: "Critical section problem হলো এমন একটি protocol design করা যেটি নিশ্চিত করে যে যখন একটি process তার critical section-এর ভেতরে থাকে, তখন কোনো অন্য process একই shared resources access করে এমন তার নিজের critical section-এ প্রবেশ করতে পারবে না।",
      },
      { type: "h3", title: "Typical process-এর structure" },
      {
        type: "code",
        lang: "c",
        text: `do {
    // Entry section — critical section-এ ঢোকার permission request
    // Critical section — shared variables access
    // Exit section — permission release
    // Remainder section — non-critical কাজ
} while (true);`,
      },
      {
        type: "p",
        text: "Real-life thinking — একটি ATM machine (critical section)। এক সময়ে শুধু একজন ব্যক্তি use করতে পারে। Waiting করা people (processes) কে coordinate করতে হবে — যদি দুজন একসাথে use করতে চায়, system double-dispense cash করতে পারে বা balances corrupt করতে পারে।",
      },

      { type: "h2", id: "requirements", title: "Solution Requirements" },
      {
        type: "p",
        text: "Critical section problem-এর valid solution তিনটি condition satisfy করতে হবে:",
      },
      {
        type: "list",
        items: [
          "Mutual exclusion — যদি process Pᵢ তার critical section execute করে, কোনো অন্য process তার critical section-এ থাকতে পারবে না।",
          "Progress — যদি কোনো process critical section-এ না থাকে এবং কিছু processes enter করতে চায়, শুধু সেই processes গুলো যারা তাদের remainder section-এ নেই তারা participate করবে কে enter করবে সেটা decide করতে। Selection অসীমকাল পর্যন্ত postpone করা যাবে না।",
          "Bounded waiting — একটি process critical section-এ enter করার request করার পর, কতগুলো অন্য processes এই request grant হওয়ার আগে enter করতে পারবে তার একটি bound (limit) আছে। কোনো starvation থাকবে না।",
        ],
      },

      { type: "h2", id: "peterson", title: "Software Solution: Peterson's Algorithm" },
      {
        type: "p",
        text: "Peterson's algorithm (1981) হলো দুটি processes (P0 ও P1) এর জন্য একটি classic software-only solution যেটি তিনটি requirements সব satisfy করে। এটি hardware atomic operations ছাড়াই কাজ করে।",
      },
      { type: "h3", title: "Data structures" },
      {
        type: "list",
        items: [
          "int turn; — কার turn সেটা indicate করে।",
          "bool flag[2]; — প্রতিটি flag[i] indicate করে যে process i enter করতে ready।",
        ],
      },
      {
        type: "multi-code",
        filename: "peterson_algo",
        codeSamples: {
          cpp: `#include <iostream>
#include <thread>
#include <atomic>

std::atomic<int> turn{0};
std::atomic<bool> flag[2] = {false, false};
int counter = 0;  // shared resource

void worker(int i) {
    int j = 1 - i;
    for (int k = 0; k < 10000; k++) {
        flag[i] = true;          // I want to enter
        turn = j;                // courtesy: let other go first
        while (flag[j] && turn == j);  // busy wait
        // --- critical section ---
        counter++;
        // --- exit section ---
        flag[i] = false;
    }
}

int main() {
    std::thread t0(worker, 0), t1(worker, 1);
    t0.join(); t1.join();
    std::cout << "counter=" << counter << '\\n';  // 20000
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "sync"
    "sync/atomic"
)

var turn int32 = 0
var flag = [2]bool{false, false}
var counter int32 = 0

func worker(i int, wg *sync.WaitGroup) {
    defer wg.Done()
    j := 1 - i
    for k := 0; k < 10000; k++ {
        flag[i] = true
        atomic.StoreInt32(&turn, int32(j))
        for flag[j] && atomic.LoadInt32(&turn) == int32(j) {
            // busy wait
        }
        counter++
        flag[i] = false
    }
}

func main() {
    var wg sync.WaitGroup
    wg.Add(2)
    go worker(0, &wg)
    go worker(1, &wg)
    wg.Wait()
    fmt.Println("counter=", counter)  // 20000
}`,
          python: `import threading

turn = 0
flag = [False, False]
counter = 0
lock = threading.Lock()  # to safely update flag/turn (Peterson's classic assumes atomics)

def worker(i):
    global turn, flag, counter
    j = 1 - i
    for _ in range(10000):
        with lock:
            flag[i] = True
            turn = j
        while flag[j] and turn == j:
            pass  # busy wait
        # --- critical section ---
        counter += 1
        # --- exit ---
        with lock:
            flag[i] = False

ts = [threading.Thread(target=worker, args=(i,)) for i in range(2)]
for t in ts: t.start()
for t in ts: t.join()
print("counter=", counter)  # 20000 (GIL makes it sequential anyway)`,
          java: `import java.util.concurrent.atomic.*;

public class Peterson {
    static AtomicInteger turn = new AtomicInteger(0);
    static AtomicBoolean[] flag = {
        new AtomicBoolean(false), new AtomicBoolean(false)
    };
    static int counter = 0;

    static void worker(int i) {
        int j = 1 - i;
        for (int k = 0; k < 10000; k++) {
            flag[i].set(true);
            turn.set(j);
            while (flag[j].get() && turn.get() == j) {
                // busy wait
                Thread.yield();
            }
            counter++;  // critical section
            flag[i].set(false);
        }
    }

    public static void main(String[] args) throws InterruptedException {
        Thread t0 = new Thread(() -> worker(0));
        Thread t1 = new Thread(() -> worker(1));
        t0.start(); t1.start();
        t0.join(); t1.join();
        System.out.println("counter=" + counter);  // 20000
    }
}`,
        },
      },
      {
        type: "p",
        text: "Real-life thinking — দুজন মানুষ একটি single phone booth share করছে। প্রত্যেকে হাত তোলে (flag[i]=true) এবং politely বলে 'You go first' (turn = j)। যদি দুজনই হাত তোলে, যার turn সে (last spoken 'you first' অনুযায়ী) step back করে এবং অপরকে যেতে দেয়।",
      },
      {
        type: "callout",
        calloutTone: "info",
        text: "Note: Peterson's algorithm elegant কিন্তু modern CPU architectures-এ out-of-order execution এর কারণে কাজ করে না যতক্ষণ না memory barriers use করা হয়। এটি শুধু pedagogical classic হিসেবে থাকে।",
      },

      { type: "h2", id: "hardware", title: "Hardware Support: Test-and-Set ও Compare-and-Swap" },
      {
        type: "p",
        text: "Modern processors atomic hardware instructions provide করে যেগুলো একটি uninterruptible step-এ memory read, modify, ও write করে। এই instructions efficient synchronization primitives build করতে use হয়।",
      },

      { type: "h3", title: "Test-and-Set (TAS)" },
      {
        type: "p",
        text: "Atomically একটি memory location read করে এবং সেটিতে true (বা 1) write করে। এটি একটি single uninterruptible operation, তাই দুটি threads একসাথে TAS call করলে একটি পাবে old value false, অপরটি পাবে true।",
      },
      {
        type: "code",
        lang: "c",
        text: `bool test_and_set(bool *target) {
    bool old = *target;
    *target = true;
    return old;
}`,
      },
      {
        type: "p",
        text: "Mutual exclusion using TAS (shared variable lock = false initially): while (test_and_set(&lock)); // busy wait এর মাধ্যমে process lock acquire করার চেষ্টা করে। যেহেতু TAS atomic, একসাথে দুটি process lock acquire করতে পারবে না।",
      },

      { type: "h3", title: "Compare-and-Swap (CAS)" },
      {
        type: "p",
        text: "Atomically একটি variable-কে একটি given value-র সাথে compare করে; যদি equal হয়, সেটি একটি new value-র সাথে swap হয়। CAS modern lock-free programming-এ অত্যন্ত গুরুত্বপূর্ণ — এটি Java Atomic classes, Rust Arc/Mutex ইত্যাদির ভিত্তি।",
      },
      {
        type: "code",
        lang: "c",
        text: `int compare_and_swap(int *value, int expected, int new_value) {
    int old = *value;
    if (old == expected)
        *value = new_value;
    return old;
}`,
      },
      {
        type: "p",
        text: "Using CAS for mutual exclusion: while (compare_and_swap(&lock, 0, 1) != 0); // wait until lock 0 হয়। Real-life thinking — একটি restroom key। TAS হলো key available থাকলে grab করা এবং একই motion-এ সেটি 'taken' mark করা। CAS হলো বলা 'If key hook-এ আছে, নাও এবং একটা busy sign রেখে দাও; নাহলে কিছু করো না'।",
      },

      { type: "h2", id: "mutex-spinlock", title: "Mutex Locks ও Spinlocks" },
      {
        type: "p",
        text: "Mutex (MUTual EXclusion) হলো একটি simple locking mechanism যেটি acquire() ও release() operations support করে। দুটি প্রকার আছে — blocking mutex ও spinlock।",
      },
      {
        type: "list",
        items: [
          "Mutex lock (blocking) — thread lock acquire করতে না পারলে sleep হয়ে যায় (context switch)। Long critical sections-এর জন্য ভালো।",
          "Spinlock — thread lock acquire করতে না পারলে busy-wait (spin) করে একটি loop-এ, CPU consume করে। Short critical sections-এর জন্য ভালো (কোনো context-switch overhead নেই)।",
        ],
      },
      { type: "h3", title: "Mutex vs Spinlock — Comparison" },
      {
        type: "list",
        items: [
          "Waiting behaviour — Mutex: thread sleep হয়; Spinlock: thread spins (busy-wait)",
          "CPU usage during wait — Mutex: প্রায় zero; Spinlock: high (cycles waste)",
          "Context switch overhead — Mutex: yes (scheduler ও back); Spinlock: none",
          "Best when — Mutex: critical section long বা I/O involved; Spinlock: critical section very short",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — Mutex হলো meeting room-এর জন্য wait করা — আপনি আপনার office-এ যান (sleep) এবং free হলে notify পান। Spinlock হলো red light-এর জন্য wait করা — আপনি engine চালু রাখেন, steering wheel tap করতে থাকেন।",
      },

      { type: "h2", id: "mutex-demo", title: "Mutex Demo — Concurrent Counter" },
      {
        type: "p",
        text: "নিচে চারটি ভাষায় একটি concurrent counter দেখানো হলো যেখানে অনেক threads একসাথে একটি shared counter increment করে। Mutex ছাড়া race condition হবে এবং final value ভুল হবে। Mutex দিয়ে প্রতিটি increment atomic হয়।",
      },
      {
        type: "multi-code",
        filename: "mutex_counter",
        codeSamples: {
          cpp: `#include <iostream>
#include <thread>
#include <vector>
#include <mutex>

int counter = 0;
std::mutex m;

void bump(int n) {
    for (int i = 0; i < n; i++) {
        std::lock_guard<std::mutex> lk(m);   // RAII lock
        counter++;
    }
}

int main() {
    std::vector<std::thread> ts;
    for (int i = 0; i < 8; i++) ts.emplace_back(bump, 10000);
    for (auto& t : ts) t.join();
    std::cout << "counter=" << counter << '\\n';   // 80000
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "sync"
)

func main() {
    var counter int
    var mu sync.Mutex
    var wg sync.WaitGroup

    for i := 0; i < 8; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            for j := 0; j < 10000; j++ {
                mu.Lock()
                counter++
                mu.Unlock()
            }
        }()
    }
    wg.Wait()
    fmt.Println("counter=", counter)   // 80000
}`,
          python: `import threading

counter = 0
lock = threading.Lock()

def bump(n):
    global counter
    for _ in range(n):
        with lock:
            counter += 1

ts = [threading.Thread(target=bump, args=(10000,)) for _ in range(8)]
for t in ts: t.start()
for t in ts: t.join()
print("counter=", counter)   # 80000`,
          java: `public class MutexCounter {
    static int counter = 0;
    public static void main(String[] args) throws InterruptedException {
        Object lock = new Object();
        Thread[] ts = new Thread[8];
        for (int i = 0; i < 8; i++) {
            ts[i] = new Thread(() -> {
                for (int j = 0; j < 10000; j++) {
                    synchronized (lock) { counter++; }
                }
            });
            ts[i].start();
        }
        for (Thread t : ts) t.join();
        System.out.println("counter=" + counter);   // 80000
    }
}`,
        },
      },

      { type: "h2", id: "semaphores", title: "Semaphores" },
      {
        type: "p",
        text: "Semaphore হলো একটি integer variable যেটি initialization ছাড়া শুধু দুটি atomic operations দিয়ে access করা যায়: wait() (P, down, decrement ও নামেও পরিচিত) এবং signal() (V, up, increment)।",
      },
      { type: "h3", title: "Binary Semaphore" },
      {
        type: "p",
        text: "শুধু 0 ও 1 value নেয় — mutex lock-এর মতো behave করে। wait(S) যদি S > 0 হয় তাহলে decrement করে এবং proceed করে; নাহলে block/wait করে। signal(S) সবসময় S increment করে।",
      },
      { type: "h3", title: "Counting Semaphore" },
      {
        type: "p",
        text: "যেকোনো non-negative integer value নিতে পারে — available resources-এর সংখ্যা represent করে। wait(S) decrement করে; যদি S < 0 হয়ে যায় process block হয়। signal(S) increment করে; যদি blocked processes থাকে একজনকে wake করা হয়।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি parking garage with 50 spaces। একটি counter available spots দেখায়। wait() = car enters (counter--)। signal() = car leaves (counter++)। যদি counter 0 হয়ে যায়, cars-কে queue (block) করতে হয় বাইরে। উদাহরণ: তিনটি printers। Initialize semaphore printers = 3। প্রতিটি process printing-এর আগে wait(&printers), পরে signal(&printers) করে। চতুর্থ process block হবে যতক্ষণ না একটি printer free হয়।",
      },

      { type: "h2", id: "classical", title: "Classical Synchronization Problems" },
      {
        type: "p",
        text: "এই classic problems গুলো synchronization-এর challenges এবং semaphores, mutexes, monitors-এর use illustrate করে।",
      },

      { type: "h3", title: "1. Bounded Buffer (Producer-Consumer)" },
      {
        type: "p",
        text: "Problem — একটি fixed-size buffer। Producers তাতে data write করে; consumers data বের করে নেয়। Producer কে full buffer-এ write করতে পারবে না; consumer empty buffer থেকে read করতে পারবে না। দুটি producers (বা consumers) একসাথে buffer access করতে পারবে না।",
      },
      {
        type: "p",
        text: "Solution তিনটি semaphore use করে: mutex = 1 (buffer access protect করে), empty = n (empty slots সংখ্যা), full = 0 (filled slots সংখ্যা)। Producer প্রথমে wait(&empty) করে (empty slot আছে কিনা দেখে), তারপর wait(&mutex) করে, item add করে, signal(&mutex) ও signal(&full) করে। Consumer একইভাবে full থেকে empty-তে।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি pizza delivery counter (buffer)। Baker (producer) pizzas make করে shelf-এ রাখে। Cashier (consumer) customers-এর জন্য নেয়। Baker shelf full হলে থামে (empty=0)। Cashier shelf empty হলে wait করে (full=0)। একসাথে একজনই shelf touch করে (mutex)।",
      },
      {
        type: "multi-code",
        filename: "producer_consumer",
        codeSamples: {
          cpp: `#include <condition_variable>
#include <iostream>
#include <mutex>
#include <queue>
#include <thread>
#include <vector>

std::queue<int> buffer;
const int N = 5;
std::mutex m;
std::condition_variable notFull, notEmpty;

void producer(int id) {
    for (int i = 0; i < 10; i++) {
        std::unique_lock<std::mutex> lk(m);
        notFull.wait(lk, []{ return buffer.size() < N; });
        buffer.push(i);
        std::cout << "P" << id << " produced " << i << '\\n';
        notEmpty.notify_one();
    }
}

void consumer(int id) {
    for (int i = 0; i < 10; i++) {
        std::unique_lock<std::mutex> lk(m);
        notEmpty.wait(lk, []{ return !buffer.empty(); });
        int v = buffer.front(); buffer.pop();
        std::cout << "C" << id << " consumed " << v << '\\n';
        notFull.notify_one();
    }
}

int main() {
    std::thread p(producer, 1), c(consumer, 1);
    p.join(); c.join();
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "sync"
)

const N = 5

func main() {
    buffer := make(chan int, N)
    var wg sync.WaitGroup
    wg.Add(2)

    go func() {
        defer wg.Done()
        for i := 0; i < 10; i++ {
            buffer <- i
            fmt.Println("P1 produced", i)
        }
    }()

    go func() {
        defer wg.Done()
        for i := 0; i < 10; i++ {
            v := <-buffer
            fmt.Println("C1 consumed", v)
        }
    }()

    wg.Wait()
}`,
          python: `import threading
import queue

N = 5
buffer = queue.Queue(maxsize=N)

def producer():
    for i in range(10):
        buffer.put(i)  # blocks if full
        print(f"P1 produced {i}")

def consumer():
    for _ in range(10):
        v = buffer.get()  # blocks if empty
        print(f"C1 consumed {v}")

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start(); t2.start()
t1.join(); t2.join()`,
          java: `import java.util.concurrent.*;

public class ProducerConsumer {
    public static void main(String[] args) {
        BlockingQueue<Integer> buffer = new ArrayBlockingQueue<>(5);

        new Thread(() -> {
            try {
                for (int i = 0; i < 10; i++) {
                    buffer.put(i);
                    System.out.println("P1 produced " + i);
                }
            } catch (InterruptedException e) {}
        }).start();

        new Thread(() -> {
            try {
                for (int i = 0; i < 10; i++) {
                    int v = buffer.take();
                    System.out.println("C1 consumed " + v);
                }
            } catch (InterruptedException e) {}
        }).start();
    }
}`,
        },
      },

      { type: "h3", title: "2. Readers-Writers" },
      {
        type: "p",
        text: "Problem — একটি shared database। অনেক readers একসাথে read করতে পারে, কিন্তু একজন writer-কে exclusive access প্রয়োজন। দুটি variation আছে — First readers-writers problem (no reader starvation) যেখানে readers-এর priority এবং writers starve হতে পারে। Second readers-writers problem (writer priority) যেখানে writers-এর priority এবং readers starve হতে পারে।",
      },
      {
        type: "p",
        text: "Solution (first, with reader priority): তিনটি shared variables — rw_mutex = 1 (writer access), mutex = 1 (read_count protect করে), read_count = 0। Reader ঢোকার সময় mutex acquire করে read_count increment করে। যদি read_count == 1 হয় (first reader), rw_mutex acquire করে writers-কে lock করে। Last reader (read_count == 0) rw_mutex release করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি library book। অনেক মানুষ একই book একসাথে read করতে পারে (readers)। কিন্তু শুধু একজন মানুষ book update করতে পারবে (writer) — এবং update করার সময় কেউ half-written version read করবে না।",
      },

      { type: "h3", title: "3. Dining Philosophers" },
      {
        type: "p",
        text: "Problem — পাঁচজন philosopher একটি table-এ পাঁচটি chopstick (বা fork) সহ sit করে। প্রতিটি philosopher-কে eat করতে দুটি chopstick প্রয়োজন — left ও right। তারা think ও eat এর মধ্যে alternate করে। Challenge হলো deadlock ও starvation avoid করা।",
      },
      {
        type: "p",
        text: "Naïve solution deadlock হয় যদি সবাই একসাথে left chopstick pick up করে। Solution — একটি mutex use করে শুধু 4 philosophers-কে একসাথে table-এ allow করা। অথবা asymmetric (odd pick left then right, even pick right then left)। অথবা monitor use করা।",
      },
      {
        type: "p",
        text: "Real-life thinking — একদল বন্ধু একটি communal bowl of rice ও spoons share করছে। প্রত্যেকের serve করতে দুটি spoon প্রয়োজন। Coordination না থাকলে সবাই একটি spoon চিরকাল hold করে থাকবে (deadlock)।",
      },
      {
        type: "multi-code",
        filename: "dining_philosophers",
        codeSamples: {
          cpp: `#include <mutex>
#include <thread>
#include <vector>
#include <cstdio>

const int N = 5;
std::mutex chopsticks[N];
std::mutex table_mutex;  // prevent deadlock: allow only N-1 at table

void philosopher(int i) {
    int left = i;
    int right = (i + 1) % N;
    for (int meal = 0; meal < 3; meal++) {
        // think...
        {
            std::lock_guard<std::mutex> lk(table_mutex);
            std::lock(chopsticks[left], chopsticks[right]);
        }
        std::printf("P%d eating meal %d\\n", i, meal);
        chopsticks[left].unlock();
        chopsticks[right].unlock();
    }
}

int main() {
    std::vector<std::thread> ts;
    for (int i = 0; i < N; i++) ts.emplace_back(philosopher, i);
    for (auto& t : ts) t.join();
    return 0;
}`,
          go: `package main

import (
    "fmt"
    "sync"
)

const N = 5

func main() {
    var chopsticks [N]sync.Mutex
    var table sync.Mutex
    var wg sync.WaitGroup

    for i := 0; i < N; i++ {
        wg.Add(1)
        go func(i int) {
            defer wg.Done()
            left := i
            right := (i + 1) % N
            for meal := 0; meal < 3; meal++ {
                table.Lock()
                chopsticks[left].Lock()
                chopsticks[right].Lock()
                table.Unlock()
                fmt.Printf("P%d eating meal %d\\n", i, meal)
                chopsticks[right].Unlock()
                chopsticks[left].Unlock()
            }
        }(i)
    }
    wg.Wait()
}`,
          python: `import threading

N = 5
chopsticks = [threading.Lock() for _ in range(N)]
table = threading.Lock()  # prevent deadlock

def philosopher(i):
    left, right = i, (i + 1) % N
    for meal in range(3):
        with table:
            chopsticks[left].acquire()
            chopsticks[right].acquire()
        print(f"P{i} eating meal {meal}")
        chopsticks[right].release()
        chopsticks[left].release()

threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]
for t in threads: t.start()
for t in threads: t.join()`,
          java: `import java.util.concurrent.locks.*;

public class DiningPhilosophers {
    static final int N = 5;
    static ReentrantLock[] chopsticks = new ReentrantLock[N];
    static ReentrantLock table = new ReentrantLock();
    static {
        for (int i = 0; i < N; i++) chopsticks[i] = new ReentrantLock();
    }

    static void philosopher(int i) {
        int left = i, right = (i + 1) % N;
        for (int meal = 0; meal < 3; meal++) {
            table.lock();
            try {
                chopsticks[left].lock();
                chopsticks[right].lock();
            } finally { table.unlock(); }
            System.out.printf("P%d eating meal %d%n", i, meal);
            chopsticks[right].unlock();
            chopsticks[left].unlock();
        }
    }

    public static void main(String[] args) {
        Thread[] ts = new Thread[N];
        for (int i = 0; i < N; i++) {
            final int idx = i;
            ts[i] = new Thread(() -> philosopher(idx));
            ts[i].start();
        }
        for (Thread t : ts) {
            try { t.join(); } catch (InterruptedException e) {}
        }
    }
}`,
        },
      },

      { type: "h3", title: "4. Sleeping Barber" },
      {
        type: "p",
        text: "Problem — একটি barber shop একজন barber, একটি barber chair, এবং কিছু waiting chairs সহ। যদি কোনো customer না থাকে, barber sleep করে। একজন customer arrive করলে sleeping barber-কে wake করে। যদি barber busy হয়, customer একটি waiting chair-এ wait করে যদি available থাকে; নাহলে leave করে।",
      },
      {
        type: "p",
        text: "Solution তিনটি semaphores ও একটি integer use করে: customers = 0 (waiting customers), barber = 0 (barber ready), mutex = 1 (waiting count protect করে), waiting = 0 (number waiting), CHAIRS = 5। Barber wait(&customers) করে sleep করে। Customer arrive করলে waiting < CHAIRS হলে signal(&customers) করে barber-কে wake করে।",
      },
      {
        type: "p",
        text: "Real-life thinking — ঠিক সেই described barber shop, যেখানে barber customers-এর মধ্যে nap করে। এই problem real-world resource management (server pools, thread pools, message queues) simulate করে।",
      },

      { type: "h2", id: "monitors", title: "Monitors ও Condition Variables" },
      {
        type: "p",
        text: "Monitor হলো একটি high-level abstraction যেটি clean, structured ভাবে synchronization achieve করতে দেয়। এটি একটি programming language construct (যেমন Java, C#-এ) বা library concept (যেমন C-এ pthread_cond)।",
      },
      {
        type: "list",
        items: [
          "Monitor shared variables ও তাদের operations-কে encapsulate করে।",
          "একই সময়ে শুধু একটি thread monitor-এর ভেতরে active থাকতে পারে (automatic mutual exclusion)।",
          "Condition variables একটি thread-কে monitor-এর ভেতরে একটি নির্দিষ্ট condition true হওয়ার জন্য wait করতে দেয়, সাময়িকভাবে monitor lock release করে।",
        ],
      },
      { type: "h3", title: "Condition variable operations" },
      {
        type: "list",
        items: [
          "wait(cond, mutex) — mutex release করে, cond-এ block করে, signal হলে mutex re-acquire করে।",
          "signal(cond) — একজন waiting thread-কে wake করে (যদি থাকে)।",
          "broadcast(cond) — সব waiting threads-কে wake করে।",
        ],
      },
      {
        type: "p",
        text: "Real-life thinking — একটি restroom with একটি single key (monitor lock)। যদি restroom occupied হয়, আপনি একটি 'vacant' condition-এ wait করেন। Occupant leave করলে সে signal করে — একজন waiting person enter করে।",
      },

      { type: "h2", id: "pthreads", title: "Synchronization in POSIX Threads (Pthreads)" },
      {
        type: "p",
        text: "POSIX threads (pthreads) Unix-like systems-এ multithreading-এর জন্য একটি standard API provide করে। Common synchronization primitives হলো mutexes ও condition variables।",
      },
      { type: "h3", title: "Pthread Mutexes" },
      {
        type: "code",
        lang: "c",
        text: `#include <pthread.h>

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

// In threads
pthread_mutex_lock(&mutex);
// critical section
pthread_mutex_unlock(&mutex);`,
      },
      {
        type: "p",
        text: "pthread_mutex_trylock() non-blocking lock acquisition attempt করে — যদি lock available না হয় immediately return করে। এটি deadlock-free algorithms-এ useful।",
      },
      { type: "h3", title: "Pthread Condition Variables" },
      {
        type: "p",
        text: "Condition variables সবসময় একটি mutex-এর সাথে use হয়। একটি thread যে condition হবে সেটির জন্য wait করে। অন্য thread সেই condition true করে signal করে। সবসময় while loop use করতে হয় (if নয়) কারণ spurious wakeups হতে পারে।",
      },
      {
        type: "p",
        text: "Real-life thinking — একটি ticket booking system। Mutex double booking prevent করে। Condition variables একটি thread-কে seat available হওয়ার জন্য wait করতে দেয়।",
      },

      { type: "h2", id: "summary", title: "Summary" },
      {
        type: "list",
        items: [
          "Critical section — shared resources access করে এমন code segment যেটি mutually exclusive হতে হবে।",
          "Requirements — mutual exclusion, progress, bounded waiting।",
          "Peterson's algorithm — দুটি processes-এর জন্য software solution (pedagogical, practice-এ widely used নয়)।",
          "Hardware support — TAS, CAS atomic instructions যেগুলো lock implementation simplify করে।",
          "Mutex / Spinlock — Mutex block করে, spinlock busy-wait করে। Critical section-এর length অনুযায়ী choose করতে হবে।",
          "Semaphores — Counting semaphores resources manage করে; binary semaphores mutex-এর মতো কাজ করে।",
          "Classical problems — bounded buffer, readers-writers, dining philosophers, sleeping barber।",
          "Monitors — automatic mutual exclusion ও condition variables সহ language construct।",
          "Pthreads — Unix threading standard API with pthread_mutex ও pthread_cond।",
        ],
      },
      {
        type: "callout",
        calloutTone: "tip",
        text: "Tip: Process synchronization বোঝা correct concurrent programs লেখার জন্য crucial। পরের chapter deadlock নিয়ে আলোচনা করবে — কী হয় যখন synchronization ভুল হয়।",
      },
    ],
  },

'''

# I made a typo earlier in the script - let me check the first p section
# Actually the script content should be fine, let me proceed

new_text = before + NEW_CH4 + after

assert new_text.count('id: "os-') == 13
assert 'export const PROJECTS' in new_text
assert 'export const CHEATSHEETS' in new_text

CONTENT_FILE.write_text(new_text)
print(f"OK — Ch 04 rewritten with MAXIMUM BANGLA + English technical terms. File size: {len(new_text)} bytes")
