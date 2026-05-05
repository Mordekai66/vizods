<div align="center">

# 🎨 vizods

### *Visualize Data Structures & Algorithms with Python*

[![PyPI Version](https://img.shields.io/pypi/v/vizods?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/vizods/)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/vizods?period=total&units=INTERNATIONAL_SYSTEM&left_color=GRAY&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/vizods)
[![Downloads](https://img.shields.io/pypi/dm/vizods?color=brightgreen&logo=pypi&logoColor=white)](https://pypi.org/project/vizods/)
[![GitHub Stars](https://img.shields.io/github/stars/Mordekai66/vizods?style=social)](https://github.com/Mordekai66/vizods)
[![GitHub Issues](https://img.shields.io/github/issues/Mordekai66/vizods)](https://github.com/Mordekai66/vizods/issues)
[![Last Commit](https://img.shields.io/github/last-commit/Mordekai66/vizods?color=orange)](https://github.com/Mordekai66/vizods/commits/main)
[![Repo Size](https://img.shields.io/github/repo-size/Mordekai66/vizods?color=purple)](https://github.com/Mordekai66/vizods)
[![Code Style](https://img.shields.io/badge/code%20style-PEP8-green.svg)](https://peps.python.org/pep-0008/)

**Transform abstract algorithms into stunning animated visualizations with a single line of code.**

[Installation](#-installation) • [Quick Start](#-quick-start) • [See It in Action](#see-it-in-action) • [Documentation](#-api-documentation) • [Examples](#-examples) • [Contributing](#-contributing)

</div>

---

## 🌟 Overview

**vizods** is a powerful, intuitive Python library designed to bridge the gap between abstract code and visual understanding. Whether you're a **student** learning algorithms, an **educator** preparing materials, or a **developer** explaining concepts, `vizods` turns your data structures and algorithms into beautiful **MP4 videos**, **GIF animations**, and **PNG snapshots** automatically.

> 💡 *"A picture is worth a thousand lines of code."*

---

## See It in Action

**Bubble Sort in motion (GIF):**

<img width="600" height="400" alt="bubble_sort" src="https://github.com/user-attachments/assets/96a4db75-f65c-4fa7-bb29-406c3da556a5" />

*(Generate your own with `sorter.save_gif("bubble_sort.gif", fps=5)`)*

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| 🎬 **Auto Animation (MP4)** | Generate `.mp4` videos of algorithm execution step-by-step |
| 🌀 **GIF Export** | Create lightweight `.gif` animations—perfect for READMEs, docs, and notebooks |
| 📸 **Snapshot Export** | Save final or intermediate states as `.png` images |
| 🌳 **Tree Visualization** | Hierarchical layouts for Binary Search Trees |
| 📊 **Sorting Animations** | Bar chart visualizations with color-coded states |
| 🔍 **Search Animations**  | Dynamic highlighting of search ranges and target matching |
| 🗺️ **Graph Pathfinding** | Step-by-step Dijkstra's algorithm tracing with weights |
| 🔗 **Linked Lists** | Pointer-based node visualization |
| 🎨 **Color-Coded States** | Universal color scheme for clarity |
| ⚡ **Zero Configuration** | Works out of the box — just `pip install` and run |

---

## 📦 Installation

Install **vizods** directly from PyPI:

```bash
pip install vizods
```

### Prerequisites

- **Python:** 3.8 or higher
- **FFmpeg (optional):** Required *only* for `.mp4` rendering. **GIF export works without FFmpeg.**

#### Installing FFmpeg (for MP4)

<details>
<summary><b>🪟 Windows</b></summary>

```bash
# Using Chocolatey
choco install ffmpeg

# Or download from https://ffmpeg.org/download.html
```
</details>

<details>
<summary><b>🍎 macOS</b></summary>

```bash
brew install ffmpeg
```
</details>

<details>
<summary><b>🐧 Linux (Ubuntu/Debian)</b></summary>

```bash
sudo apt update && sudo apt install ffmpeg
```
</details>

### Dependencies

`vizods` automatically installs:
- `matplotlib >= 3.5.0`
- `imageio >= 2.20.0`
- `imageio-ffmpeg >= 0.4.7` *(only needed for MP4)*
- `networkx >= 2.8.0`
- `numpy >= 1.21.0`

---

## 🚀 Quick Start

```python
from vizods.bubble_sort import BubbleSort

# Create and visualize a sorting animation in 3 lines
sorter = BubbleSort([64, 25, 12, 22, 11])
sorter.sort()

# Export your animation (choose one or both!)
sorter.save_gif("my_first_animation.gif", fps=5)   # ✅ No FFmpeg needed
sorter.save_video("my_first_animation.mp4", fps=5) # Requires FFmpeg
```

That's it! 🎉 You now have a fully animated visualization.

---

## 📚 Supported Modules

| Category | Module | Class | Visual Style |
| :--- | :--- | :--- | :--- |
| **Searching** | `linear_search` | `LinearSearch` | 🔍 Highlighted Bars |
| | `binary_search` | `BinarySearch` | 📉 Range Reduction |
| **Sorting** | `bubble_sort` | `BubbleSort` | 📊 Bar Chart |
| | `insertion_sort` | `InsertionSort` | 📊 Bar Chart |
| | `selection_sort` | `SelectionSort` | 📊 Bar Chart |
| | `merge_sort` | `MergeSort` | 📊 Bar Chart |
| | `quick_sort` | `QuickSort` | 📊 Bar Chart |
| **Data Structures** | `linked_list` | `LinkedList` | 🔗 Nodes & Pointers |
| | `bst` | `BST` | 🌳 Hierarchical Tree |
| | `stack` | `Stack` | 📚 Vertical Bar Stack |
| | `queue` | `Queue` | ➡️ Horizontal Bar Queue |
| **Graph Algorithms** | `dijkstra` | `Dijkstra` | 🗺️ Weighted Graph |

---

## 🎯 Examples

### 1️⃣ Searching Algorithms

#### Linear Search
```python
from vizods.linear_search import LinearSearch

data = [10, 50, 30, 70, 80, 60, 20, 90, 40]
ls = LinearSearch(data)
ls.search(70)

ls.save_gif("linear_search.gif", fps=2)
ls.save_video("linear_search.mp4", fps=2)
```

#### Binary Search
```python
from vizods.binary_search import BinarySearch

# Binary search requires a sorted array
data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
bs = BinarySearch(data)
bs.search(70)

bs.save_gif("binary_search.gif", fps=2)
bs.save_video("binary_search.mp4", fps=2)
```

---

### 2️⃣ Sorting Algorithms

#### Bubble Sort
```python
from vizods.bubble_sort import BubbleSort

data = [64, 34, 25, 12, 22, 11, 90]
sorter = BubbleSort(data)
sorter.sort(visualize=True)

sorter.save_gif("bubble_sort.gif", fps=5)
sorter.save_video("bubble_sort.mp4", fps=5)
```

#### Insertion Sort
```python
from vizods.insertion_sort import InsertionSort

sorter = InsertionSort([12, 11, 13, 5, 6])
sorter.sort()

sorter.save_gif("insertion_sort.gif", fps=4)
sorter.save_video("insertion_sort.mp4", fps=4)
```

#### Selection Sort
```python
from vizods.selection_sort import SelectionSort

sorter = SelectionSort([64, 25, 12, 22, 11])
sorter.sort()

sorter.save_gif("selection_sort.gif", fps=3)
sorter.save_video("selection_sort.mp4", fps=3)
```

#### Merge Sort
```python
from vizods.merge_sort import MergeSort

sorter = MergeSort([38, 27, 43, 3, 9, 82, 10])
sorter.sort()

sorter.save_gif("merge_sort.gif", fps=3)
sorter.save_video("merge_sort.mp4", fps=3)
```

#### Quick Sort
```python
from vizods.quick_sort import QuickSort

sorter = QuickSort([10, 7, 8, 9, 1, 5])
sorter.sort()

sorter.save_gif("quick_sort.gif", fps=5)
sorter.save_video("quick_sort.mp4", fps=5)
```

---

### 3️⃣ Data Structures

#### Linked List
```python
from vizods.linked_list import LinkedList

ll = LinkedList()
for value in [10, 20, 30, 40, 50]:
    ll.add_node(value)

ll.delete_node(30)

ll.save_gif("linked_list.gif", fps=2)
ll.save_video("linked_list.mp4", fps=2)
```

#### Binary Search Tree (BST)
```python
from vizods.bst import BST

tree = BST()
for value in [50, 30, 70, 20, 40, 60, 80]:
    tree.insert(value)

tree.search(40)
tree.delete(20)

tree.save_gif("bst_animation.gif", fps=1)
tree.save_video("bst_animation.mp4", fps=1)
```

#### Stack (LIFO)
```python
from vizods.stack import Stack

stack = Stack()
for value in [10, 20, 30]:
    stack.push(value)

stack.pop()

stack.save_gif("stack.gif", fps=2)
stack.save_video("stack.mp4", fps=2)
```

#### Queue (FIFO)
```python
from vizods.queue import Queue

queue = Queue()
for value in [10, 20, 30]:
    queue.enqueue(value)

queue.dequeue()

queue.save_gif("queue.gif", fps=2)
queue.save_video("queue.mp4", fps=2)
```

---

### 4️⃣ Graph Algorithms

#### Dijkstra's Shortest Path
```python
from vizods.dijkstra import Dijkstra

graph = Dijkstra()
edges = [
    ('A', 'B', 4), ('A', 'C', 2),
    ('B', 'C', 1), ('B', 'D', 5),
    ('C', 'D', 8), ('D', 'E', 2)
]
for u, v, w in edges:
    graph.add_edge(u, v, w)

graph.visualize_search(start_node='A', target_node='E')

graph.save_gif("dijkstra_path.gif", fps=1)
graph.save_video("dijkstra_path.mp4", fps=1)
```

---

## 🎨 Visualization Color Standards

`vizods` uses a consistent color language across all visualizations:

| Color | Meaning |
| :---: | :--- |
| 🟢 **Green** | Sorted / Visited / Completed |
| 🟠 **Orange** | Active / Currently Processing |
| 🔴 **Red** | Critical / Deleting / Shortest Path |
| 🔵 **Skyblue** | Standard / Unprocessed |
| 🟣 **Purple** | Pivot (Quick Sort) |
| ⚪ **Lightgray** | Inactive / Waiting |

---

## 📖 API Documentation

### 🔹 Searching Classes (`LinearSearch`, `BinarySearch`)

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `__init__(data)` | `data: list` | Initialize with a list of numbers |
| `search(target)` | `target: int/float` | Start the search process and capture frames |
| `save_gif(output_name, fps)` | `output_name: str`, `fps: int` | Export search animation as **GIF** (no FFmpeg required) |
| `save_video(output_name, fps)` | `output_name: str`, `fps: int` | Export search animation as **MP4** (requires FFmpeg) |
| `save_snapshot(filename)` | Save the current tree structure as **PNG** |

---

### 🔹 Sorting Classes (`BubbleSort`, `QuickSort`, `MergeSort`, `InsertionSort`, `SelectionSort`)

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `__init__(data)` | `data: list` | Initialize with a list of numbers |
| `sort(visualize=True)` | `visualize: bool` | Run the sorting algorithm & capture frames |
| `save_gif(output_name, fps)` | `output_name: str`, `fps: int` | Export sorting animation as **GIF** |
| `save_video(output_name, fps)` | `output_name: str`, `fps: int` | Export sorting animation as **MP4** |
| `save_snapshot(filename)` | `filename: str` | Save the final sorted state as **PNG** |

---

### 🔹 `Stack` (LIFO)

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `push(value)` | `value` | Add an element to the top of the stack |
| `pop()` | - | Remove and return the top element |
| `peek()` | - | View the top element without removing it |
| `is_empty()` | - | Check if the stack is empty |
| `save_gif(output_name, fps)` | `output_name: str`, `fps: int` | Export stack operations as **GIF** |
| `save_video(output_name, fps)` | `output_name: str`, `fps: int` | Export stack operations as **MP4** |
| `save_snapshot(filename)` | `filename: str` | Save a snapshot of the current stack state |

---

### 🔹 `Queue` (FIFO)

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `enqueue(value)` | `value` | Add an element to the end of the queue |
| `dequeue()` | - | Remove and return the front element |
| `front()` | - | View the first element in the queue |
| `rear()` | - | View the last element in the queue |
| `save_gif(output_name, fps)` | `output_name: str`, `fps: int` | Export queue operations as **GIF** |
| `save_video(output_name, fps)` | `output_name: str`, `fps: int` | Export queue operations as **MP4** |
| `save_snapshot(filename)` | `filename: str` | Save a snapshot of the current queue state |

---

### 🔹 `BST` (Binary Search Tree)

| Method | Description |
| :--- | :--- |
| `insert(value)` | Insert a new node into the tree |
| `search(value)` | Search for a value, animating the traversal path |
| `delete(value)` | Delete a node *(currently supports leaf nodes)* |
| `save_gif(output_name, fps)` | Export full tree operations as **GIF** |
| `save_video(output_name, fps)` | Export full tree operations as **MP4** |
| `save_snapshot(filename)` | Save the current tree structure as **PNG** |

---

### 🔹 `LinkedList`

| Method | Description |
| :--- | :--- |
| `add_node(value)` | Append a new node to the end of the list |
| `delete_node(value)` | Remove a specific node from the list |
| `save_gif(output_name, fps)` | Export pointer/node operations as **GIF** |
| `save_video(output_name, fps)` | Export pointer/node operations as **MP4** |
| `save_snapshot(filename)` | Save the current tree structure as **PNG** |

---

### 🔹 `Dijkstra`

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `add_edge(u, v, weight)` | `u, v: nodes`, `weight: int` | Add a weighted edge between two nodes |
| `visualize_search(start, target)` | `start, target: nodes` | Run and animate the shortest pathfinding process |
| `save_gif(output_name, fps)` | `output_name: str`, `fps: int` | Export pathfinding animation as **GIF** |
| `save_video(output_name, fps)` | `output_name: str`, `fps: int` | Export pathfinding animation as **MP4** |
| `save_snapshot(filename)` | Save the current tree structure as **PNG** |

---

## 🎓 Use Cases

- 🏫 **Education:** Teach algorithms in classrooms with engaging visuals (GIFs embed perfectly in slides & LMS pages)
- 📹 **Content Creation:** Produce YouTube tutorials and online courses
- 📝 **Documentation:** Embed GIFs in blogs, GitHub READMEs, articles, and books
- 🎤 **Presentations:** Make technical talks more interactive—no video player needed
- 🧪 **Debugging:** Visually inspect algorithm behavior frame-by-frame

---

## 🛠️ Project Structure

```
vizods/
├── .github/
│   └── .workflows/
│       └── pypi.yml
├── output/ # Sample outputs (MP4, GIF, PNG)
│   ├── bst_animation.mp4
│   ├── bst_animation.gif
│   ├── bst_snapshot.png
│   ├── bubble_sort.mp4
│   ├── bubble_sort.gif
│   ├── bubble_sort_snapshot.png
│   ├── ...
│   └── stack.gif
├── tests/
│   └── test_all_algorithms.py
├── vizods/
│   ├── __init__.py
│   ├── binary_search.py
│   ├── bst.py
│   ├── bubble_sort.py
│   ├── dijkstra.py
│   ├── insertion_sort.py
│   ├── linear_search.py
│   ├── linked_list.py
│   ├── merge_sort.py
│   ├── queue.py
│   ├── quick_sort.py 
│   ├── selection_sort.py
│   └── stack.py
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

---

## 🤝 Contributing

Contributions make the open-source community such an amazing place to learn and grow. **Any contributions are greatly appreciated!**

1. **Fork** the project
2. **Create** your feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

Please make sure to update tests as appropriate and follow the [PEP 8](https://peps.python.org/pep-0008/) style guide.

---

## 🐛 Reporting Bugs

Found a bug? Please [open an issue](https://github.com/Mordekai66/vizods/issues) with:
- A clear description
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version)

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

## 👨‍💻 Author

**Abdelrahman Ali** ([@Mordekai66](https://github.com/Mordekai66))

📧 abdelrahman.ali.dev@gmail.com

---

## 🌟 Show Your Support

If you find `vizods` helpful:
- ⭐ **Star** this repository
- 🍴 **Fork** it for your projects
- 📢 **Share** it with fellow developers
- 💬 **Tweet** about it

---

## 🙏 Acknowledgements

- [Matplotlib](https://matplotlib.org/) — for plotting
- [NetworkX](https://networkx.org/) — for graph structures
- [ImageIO](https://imageio.readthedocs.io/) — for video/GIF encoding
- All contributors and users of this library ❤️

---

<div align="center">

**Developed with ❤️ by [Mordekai66](https://github.com/Mordekai66)**

*If this project helped you, consider giving it a ⭐ on GitHub!*

</div>
