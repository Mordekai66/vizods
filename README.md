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

[Installation](#-installation) • [Quick Start](#-quick-start) • [Documentation](#-api-documentation) • [Examples](#-examples) • [Contributing](#-contributing)

</div>

---

## 🌟 Overview

**vizods** is a powerful, intuitive Python library designed to bridge the gap between abstract code and visual understanding. Whether you're a **student** learning algorithms, an **educator** preparing materials, or a **developer** explaining concepts, `vizods` turns your data structures and algorithms into beautiful **MP4 animations** and **PNG snapshots** automatically.

> 💡 *"A picture is worth a thousand lines of code."*

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| 🎬 **Auto Animation** | Generate `.mp4` videos of algorithm execution step-by-step |
| 📸 **Snapshot Export** | Save final or intermediate states as `.png` images |
| 🌳 **Tree Visualization** | Hierarchical layouts for Binary Search Trees |
| 📊 **Sorting Animations** | Bar chart visualizations with color-coded states |
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
- **FFmpeg:** Required for `.mp4` rendering

#### Installing FFmpeg

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
- `imageio-ffmpeg >= 0.4.7`
- `networkx >= 2.8.0`
- `numpy >= 1.21.0`

---

## 🚀 Quick Start

```python
from vizods.bubble_sort import BubbleSort

# Create and visualize a sorting animation in 3 lines
sorter = BubbleSort([64, 25, 12, 22, 11])
sorter.sort()
sorter.save_video("my_first_animation.mp4")
```

That's it! 🎉 You now have a fully animated MP4 visualization.

---

## 📚 Supported Modules

| Category | Module | Class | Visual Style |
| :--- | :--- | :--- | :--- |
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

### 1️⃣ Sorting Algorithms

#### Bubble Sort
```python
from vizods.bubble_sort import BubbleSort

data = [64, 34, 25, 12, 22, 11, 90]
sorter = BubbleSort(data)
sorter.sort(visualize=True)
sorter.save_video("bubble_sort.mp4", fps=5)
sorter.save_snapshot("bubble_final.png")
```

#### Quick Sort
```python
from vizods.quick_sort import QuickSort

sorter = QuickSort([10, 80, 30, 90, 40, 50, 70])
sorter.sort()
sorter.save_video("quick_sort.mp4", fps=5)
```

#### Merge Sort
```python
from vizods.merge_sort import MergeSort

sorter = MergeSort([38, 27, 43, 3, 9, 82, 10])
sorter.sort()
sorter.save_video("merge_sort.mp4", fps=3)
```

#### Insertion Sort
```python
from vizods.insertion_sort import InsertionSort

sorter = InsertionSort([5, 2, 4, 6, 1, 3])
sorter.sort()
sorter.save_video("insertion_sort.mp4", fps=4)
```

#### Selection Sort
```python
from vizods.selection_sort import SelectionSort

sorter = SelectionSort([29, 10, 14, 37, 13])
sorter.sort()
sorter.save_video("selection_sort.mp4", fps=3)
```

---

### 2️⃣ Binary Search Tree (BST)

```python
from vizods.bst import BST

tree = BST()

# Insert nodes
for value in [50, 30, 70, 20, 40, 60, 80]:
    tree.insert(value)

# Search a value
tree.search(40)

# Delete a leaf node
tree.delete(20)

# Save outputs
tree.save_video("tree_operations.mp4", fps=1)
tree.save_snapshot("final_tree.png")
```

---

### 3️⃣ Linked List

```python
from vizods.linked_list import LinkedList

ll = LinkedList()

# Add nodes
for value in [10, 20, 30, 40, 50]:
    ll.add_node(value)

# Delete a node
ll.delete_node(30)

# Save animation
ll.save_video("linked_list.mp4", fps=2)
```

---

### 4️⃣ Dijkstra's Shortest Path

```python
from vizods.dijkstra import Dijkstra

graph = Dijkstra()

# Build a weighted graph
edges = [
    ('A', 'B', 4), ('A', 'C', 2),
    ('B', 'C', 1), ('B', 'D', 5),
    ('C', 'D', 8), ('C', 'E', 10),
    ('D', 'E', 2)
]
for u, v, w in edges:
    graph.add_edge(u, v, w)

# Visualize shortest path
graph.visualize_search(start_node='A', target_node='E')
graph.save_video("dijkstra_path.mp4", fps=1)
```

### 5️⃣ Stack (LIFO)

```python
from vizods.stack import Stack

stack = Stack()

# Push elements
for value in [10, 20, 30, 40, 50]:
    stack.push(value)

# Peek and pop
stack.peek()
stack.pop()
stack.pop()

# Save outputs
stack.save_video("stack_demo.mp4", fps=2)
stack.save_snapshot("stack_final.png")
```

### 6️⃣ Queue (FIFO)

```python
from vizods.queue import Queue

queue = Queue()

# Enqueue elements
for value in [10, 20, 30, 40, 50]:
    queue.enqueue(value)

# Inspect front and rear
queue.front()
queue.rear()

# Dequeue elements
queue.dequeue()
queue.dequeue()

# Save outputs
queue.save_video("queue_demo.mp4", fps=2)
queue.save_snapshot("queue_final.png")
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

### 🔹 Sorting Classes (`BubbleSort`, `QuickSort`, `MergeSort`, `InsertionSort`, `SelectionSort`)

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `__init__(data)` | `data: list` | Initialize with a list of numbers |
| `sort(visualize=True)` | `visualize: bool` | Run sort & capture frames |
| `save_video(output_name, fps)` | `output_name: str`, `fps: int` | Export animation as MP4 |
| `save_snapshot(filename)` | `filename: str` | Save final state as PNG |

---

### 🔹 `BST` (Binary Search Tree)

| Method | Description |
| :--- | :--- |
| `insert(value)` | Insert a new node into the tree |
| `search(value)` | Search for a value, animating the traversal |
| `delete(value)` | Delete a leaf node *(leaf-only support)* |
| `save_video(output_name, fps)` | Export full operations as MP4 |
| `save_snapshot(filename)` | Save current tree state as PNG |

---

### 🔹 `LinkedList`

| Method | Description |
| :--- | :--- |
| `add_node(value)` | Append a node to the list |
| `delete_node(value)` | Remove a specific node |
| `save_video(output_name, fps)` | Export operations animation as MP4 |

---

### 🔹 `Dijkstra`

| Method | Description |
| :--- | :--- |
| `add_edge(u, v, weight)` | Add a weighted edge |
| `visualize_search(start_node, target_node)` | Run & animate Dijkstra's algorithm |
| `save_video(output_name, fps)` | Export pathfinding animation as MP4 |

---

## 🎓 Use Cases

- 🏫 **Education:** Teach algorithms in classrooms with engaging visuals
- 📹 **Content Creation:** Produce YouTube tutorials and online courses
- 📝 **Documentation:** Embed animations in blogs, articles, and books
- 🎤 **Presentations:** Make technical talks more interactive
- 🧪 **Debugging:** Visually inspect algorithm behavior

---

## 🛠️ Project Structure

```
vizods/
├── .github/
│   └── .workflows/
│       └── pypi.yml
├── output/ # Samples
│   ├── bst_animation.mp4
│   ├── bst_snapshot.png
│   ├── bubble_sort_snapshot.png
│   ├── bubble_sort.mp4
│   ├── ...
│   ├── ...
│   ├── ...
│   └── stack.mp4
├── tests/
│   └── test_all_algorithms.py
├── vizods/
│   ├── __init__.py
│   ├── bst.py
│   ├── bubble_sort.py
│   ├── dijkstra.py
│   ├── insertion_sort.py
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
- [ImageIO](https://imageio.readthedocs.io/) — for video encoding
- All contributors and users of this library ❤️

---

<div align="center">

**Developed with ❤️ by [Mordekai66](https://github.com/Mordekai66)**

*If this project helped you, consider giving it a ⭐ on GitHub!*

</div>
