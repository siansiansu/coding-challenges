# LeetCode-Problems
[![codecov](https://codecov.io/gh/siansiansu/leetcode-problems/branch/master/graph/badge.svg)](https://codecov.io/gh/siansiansu/leetcode-problems) [![CircleCI](https://circleci.com/gh/siansiansu/leetcode-problems.svg?style=svg)](https://circleci.com/gh/siansiansu/leetcode-problems) [![codebeat badge](https://codebeat.co/badges/9a121f43-0c3c-4200-8d91-04dad0cdaa97)](https://codebeat.co/projects/github-com-siansiansu-leetcode-problems-master) ![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg) 

## Coding Challenges Websites
- [Leetcode](https://leetcode.com) - The World's Leading Online Programming Learning Platform.

- [LintCode](https://www.lintcode.com/) - Coding interview questions online training system.

- [Coderbyte](https://coderbyte.com/) - The #1 Website for Coding Challenges.

- [CodeSignal](https://codesignal.com/) - A skills-based assessment platform operated by American company BrainFights.

- [Codility](https://www.codility.com/) - Tech Recruiting Platform, Online Code Testing.

- [CodinGame](https://www.codingame.com/start) - The new way to improve your programming skills while having fun and getting noticed.

- [Codewars](https://www.codewars.com/) - Train with Programming Challenges/Kata.

- [CodeChef](https://www.codechef.com/) - A competitive programming website.

- [Codeforces](http://codeforces.com/) - Programming competitions and contests, programming community.
- 
- [HackerEarth](https://www.hackerearth.com/) - Hackathons, Innovation Management, and Technical Recruitment Software And Helps Companies Fast-track Their Growth.

- [HackerRank](https://www.hackerrank.com/) - Practice coding, prepare for interviews, and get hired.

- [TopCoder](https://www.topcoder.com/challenges/) - Design & Build High-Quality Software with Crowdsourcing.

- [Python Tutor](http://www.pythontutor.com/visualize.html#mode=edit) - Visualize Python, Java, JavaScript, C, C++, Ruby code execution.

- [GeeksforGeeks](https://www.geeksforgeeks.org/) - A computer science portal for geeks.


## Data Structure
### Array 陣列

由相同類型的元素 (element) 的集合所組成的資料結構，分配一塊連續的記憶體來儲存。利用元素的索引 (index) 可以計算出該元素對應的儲存位址。

- Features
  - 只要利用 index 即可在O(1)時間對 Array 的資料做存取。
  - 較Linked list 為節省記憶體空間：因為 Linked list 需要多一個 pointer 來記錄下一個 node 的記憶體位置。
  - 新增/刪除資料很麻煩。
  - 若資料數量時常在改變，要時常調整矩陣的大小，會花費 O(N) 的時間在搬動資料。

- Types
  - One-dimensional arrays
  - Multidimensional arrays
  - Dope vectors
  - Row- and column-major order
  - Dynamic Array: 根據資料數量，調整陣列大小。
  - Non-linear formulas

### List (Linked List) 串列

使用 node (節點) 來記錄、表示、儲存資料 (data)，並利用每個 node 中的 pointer 指向下一個 node，藉此將多個 node 串連起來，形成 Linked list，並以 NULL 來代表 Linked list 的終點。

- Operations
  - Length 
  - Concatenate
  - Invert
  
- Features
  - 各 node 不一定要佔用連續的記憶體空間。
  - 各 node 的 data type 不一定要相同。
  - 新增 / 刪除資料較 Array 簡單。
  - Linked list 的資料數量可以是動態的，不像 Array 會有 resize 的問題。
  - 沒有 index。
  - 需要額外的記憶體空間來儲存 pointer。

- Types
  - Singly Linked List 單向連結串列
  - Doubly Linked List 雙向連結串列
  - Circular List 環狀連結串列
  - XOR Linked List 互斥或連結串列。
  - Dancing Links 舞蹈鏈。
  - Unrolled Linked List 鬆散鏈表。
  
### Queue 佇列

具有 FIFO (First-In-First-Out) 的資料結構，如同排隊買車票的隊伍即可視為 Queue，先進入隊伍的人，可以優先離開隊伍，走向售票窗口買票，而後到的人，就需要等隊伍前面的人都買完票後才能買。

- Operations
  - Push: 把資料從 Queue 的末端放進 Queue，並更新成新的 back。
  - Pop: 把 front 所指向的資料從 Queue 中移除，並更新 front。
  - getFront: 回傳 front 所指向的資料。
  - getBack: 回傳 back 所指向的資料。
  - IsEmpty: 確認 Queue 裡是否有資料。
  - getSize: 回傳 Queue 裡的資料個數。

- Types
  - Circular Queue 環型佇列。
  - Double-ends Queues 雙佇列。
    - Input Restricted Deque 輸入限制性雙佇列。
    - Output Restricted Deque 輸出限制性雙佇列。
  - Priority Queue 優先權佇列。
    - Max-Priority Queue: 讀取資料時，都拿到「權重最大」的資料。
    - Min-Priority Queue: 讀取資料時，都拿到「權重最小」的資料。
    - Single-End Priority Queue (SEPQ): 只能取得「最大」或是「最小」權重的資料。
    - Double-End Priority Queue (DEPQ): 可以同時取得「權重最大」以及「權重最小」的資料。

### Stack 

具有 LOFP (Last-In-First-Out) 的資料結構，可以想像成一種裝資料的容器，最後進入 Stack 的資料會最先被取出，最早進入 Stack 的資料則最晚被取出。

- Operations
  - push
  - top()
  - pop()
  - is-empty()
  - is-full()
  - get-size()

## Algorithm Design
- Incremental Method
- Memoization
- Enumeration
- Iterative Method
- Recursive Method
- Greedy Method
- Divide and Conquer
- Scaling Algorithm
- External Memory Algorithm
- Parallel Algorithm 
- Randomized Algorithm




## Algorithms

### Strings
- Knuth–Morris–Pratt (KMP) Algorithm
- Levenshtein Distance - 兩個字串之間，由一個轉換成另外一個所花費的最少編輯次數。
- Manacher
- Minimum cost to construct a string
- Rabin–Karp Algorithm


### sorts
- Bogo Sort
- Buddle Sort