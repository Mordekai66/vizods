# vizods
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Visualizer](https://img.shields.io/badge/Visualization-Supported-orange.svg)]()
[![Last Commit](https://img.shields.io/github/last-commit/Mordekai66/vizods)]()
[![Repo Size](https://img.shields.io/github/repo-size/Mordekai66/vizods)]()

**vizods** is a comprehensive Python library that combines robust Data Structures and Algorithms with built-in visualization tools. It allows developers and students to not only execute code but also **see** how data transforms in real-time through images and videos.

---

## Key Features
* **Built-in Visualization:** Generate `.png` snapshots or `.mp4` videos of algorithm execution.
* **Educational Legends:** Every visual output includes a color-coded legend and status messages.
* **Clean API:** Intuitive syntax designed for both production and learning.
* **Extensible Architecture:** Easily add new algorithms by inheriting from our base visualizer classes.

---

## Installation

```bash
pip install vizods
```
*Note: Ensure you have `ffmpeg` installed on your system for video rendering.*

---

## Quick Start: Bubble Sort Visualization

```python
from vizods.bubble_sort import BubbleSort

# Initialize with data
data = [64, 34, 25, 12, 22, 11, 90]
sorter = BubbleSort(data)

# Run algorithm with visualization enabled
sorter.sort()

# Export results
sorter.save_snapshot("final_result.png")
sorter.save_video("bubble_sort_demo.mp4", fps=5)
```

---

## Supported Modules

### 1. Sorting Algorithms
| Algorithm | Status | Visualization |
| :--- | :---: | :---: |
| Bubble Sort | ✅ | Bar Chart + Legend |
| Selection Sort | ✅ | Bar Chart + Legend |
| Insertion Sort | ✅ | Bar Chart + Legend |
| Quick Sort | ✅ | Pivot Tracking |
| Merge Sort | ✅ | Sub-array Merging |

### 2. Data Structures (Coming Soon)
* **Linked Lists:** Animated pointer manipulation and node traversal.
* **Binary Trees:** Visual tree rebalancing (AVL/BST).
* **Graphs:** Pathfinding visualization (Dijkstra, BFS, DFS).

### 3. Pathfinding
* **A* Search:** Grid-based visualization.
* **Dijkstra:** Weighted graph traversal animations.

---

## Visualization Standards
To ensure a consistent learning experience, vizods follows a strict color-coding system:
* 🟢 **Green:** Sorted / Finalized / Target Reached.
* 🟠 **Orange:** Currently being processed / Compared.
* 🔴 **Red:** Highlighted element / Error / Key being moved.
* 🟣 **Purple:** Pivot point (for Divide & Conquer).
* ⚪ **Gray:** Inactive / Out of scope.

---

## Contributing
We welcome contributions! If you'd like to add a new algorithm or improve a visualizer:
1. Fork the Project.
2. Create your Feature Branch.
3. Commit your Changes.
4. Push to the Branch.
5. Open a Pull Request.

---

## License
Distributed under the MIT License. See `LICENSE` for more information.

---
**Developed with ❤️ for the Developer Community.**
