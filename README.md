# vizods
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Visualizer](https://img.shields.io/badge/Visualization-Supported-orange.svg)]()
[![Last Commit](https://img.shields.io/github/last-commit/Mordekai66/vizods)]()
[![Repo Size](https://img.shields.io/github/repo-size/Mordekai66/vizods)]()

**vizods** is a powerful Python library that bridges the gap between abstract code and visual understanding. Transform your algorithms and data structures into high-quality `.mp4` animations and `.png` snapshots with a single line of code.

---

## Key Features
* **Intuitive Visualization:** Automatically generate animations for sorting, trees, and graphs.
* **Smart Structure Support:** Specialized layouts for Linked Lists and Binary Search Trees.
* **Pathfinding Tracing:** Step-by-step visualization of Dijkstra’s algorithm with weight tracking.
* **Customizable:** Add your own logic and let `vizods` handle the rendering.

---

## Installation

```bash
pip install vizods
```
*Note: Ensure you have `ffmpeg` installed for video rendering.*

---

## Usage Examples

### 1. Binary Search Tree (BST)
```python
from vizods.bst import BST

tree = BST()
for val in [50, 30, 70, 20, 40]:
    tree.insert(val)

tree.save_video("tree_growth.mp4")
tree.save_snapshot("final_tree.png")
```

### 2. Dijkstra's Algorithm
```python
from vizods.dijkstra import Dijkstra

graph = Dijkstra()
graph.add_edge('A', 'B', 4)
graph.add_edge('B', 'C', 2)
graph.visualize_search(start_node='A', target_node='C')
graph.save_video("pathfinding.mp4")
```

---

## Supported Modules

| Category | Modules | Visual Style |
| :--- | :--- | :--- |
| **Sorting** | Bubble, Quick, Merge, Insertion, Selection | Bar Charts |
| **Data Structures** | Linked List, BST | Nodes & Pointers |
| **Pathfinding** | Dijkstra | Weighted Graphs |

---

## Visualization Standards
* 🟢 **Green:** Sorted / Visited Node.
* 🟠 **Orange:** Active / Currently Processing.
* 🔴 **Red:** Shortest Path / Deleting Node.
* 🔵 **Skyblue:** Standard Node / Unvisited.

---

## Contributing
Contributions are what make the open-source community an amazing place to learn! 
1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/NewAlgo`).
3. Commit your Changes.
4. Push to the Branch.
5. Open a Pull Request.

---

## License
Distributed under the MIT License. See `LICENSE` for more information.

**Developed with ❤️ by Mordekai66**