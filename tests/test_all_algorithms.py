import os
import sys
import shutil
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from vizods.binary_search import BinarySearch
from vizods.bst import BST
from vizods.bubble_sort import BubbleSort
from vizods.dijkstra import Dijkstra
from vizods.insertion_sort import InsertionSort
from vizods.linear_search import LinearSearch
from vizods.linked_list import LinkedList
from vizods.merge_sort import MergeSort
from vizods.queue import Queue
from vizods.quick_sort import QuickSort
from vizods.selection_sort import SelectionSort
from vizods.stack import Stack

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

def print_success(msg):
    print(f"{Colors.GREEN}✓ {msg}{Colors.RESET}")

def print_error(msg):
    print(f"{Colors.RED}✗ {msg}{Colors.RESET}")

def print_info(msg):
    print(f"{Colors.BLUE}▶ {msg}{Colors.RESET}")

def print_warning(msg):
    print(f"{Colors.YELLOW}⚠ {msg}{Colors.RESET}")

def cleanup_temp_dirs():
    temp_dirs = [".temp", "__pycache__"]
    for temp_dir in temp_dirs:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, ignore_errors=True)
            print_info(f"Cleaned up: {temp_dir}")

def test_binary_search():
    print_info("Testing Binary Search...")
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90] # يجب أن تكون مرتبة
    bs = BinarySearch(data)
    
    assert bs.search(30) != -1, "Should find 30"
    assert bs.search(100) == -1, "Should not find 100"
    
    bs.save_video("output/binary_search.mp4", fps=2)
    print_success("Binary Search tests passed!")

def test_linear_search():
    print_info("Testing Linear Search...")
    data = [10, 50, 30, 70, 80, 60, 20, 90, 40]
    ls = LinearSearch(data)
    
    # حالة البحث عن عنصر موجود
    assert ls.search(70) == True, "Should find 70"
    # حالة البحث عن عنصر غير موجود
    assert ls.search(100) == False, "Should not find 100"
    
    ls.save_video("output/linear_search.mp4", fps=2)
    print_success("Linear Search tests passed!")

def test_bst():
    print_info("Testing Binary Search Tree (BST)...")
    
    bst = BST()
    
    test_values = [50, 30, 70, 20, 40, 60, 80]
    for val in test_values:
        bst.insert(val)
    
    assert bst.root == 50, "Root should be 50"
    
    assert bst.search(40) == True, "Search for 40 should return True"
    assert bst.search(100) == False, "Search for 100 should return False"
    
    bst.delete(20)
    assert bst.search(20) == False, "20 should be deleted"
    
    bst.insert(50) 
    
    bst.save_video("output/bst_animation.mp4", fps=1)
    bst.save_snapshot("output/bst_snapshot.png")
    
    print_success("BST tests passed!")

def test_stack():
    print_info("Testing Stack...")
    
    stack = Stack()
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    assert stack.size() == 3, "Stack size should be 3"
    assert stack.peek() == 30, "Peek should return 30"
    
    popped = stack.pop()
    assert popped == 30, "Popped value should be 30"
    assert stack.size() == 2, "Stack size should be 2 after pop"
    
    assert stack.is_empty() == False, "Stack should not be empty"
    
    stack.pop()
    stack.pop()
    assert stack.is_empty() == True, "Stack should be empty"
    assert stack.pop() is None, "Pop on empty stack should return None"
    
    stack.save_video("output/stack.mp4", fps=2)
    stack.save_snapshot("output/stack_snapshot.png")
    
    print_success("Stack tests passed!")

def test_queue():
    print_info("Testing Queue...")
    
    queue = Queue()
    
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    
    assert queue.size() == 3, "Queue size should be 3"
    assert queue.front() == 10, "Front should be 10"
    assert queue.rear() == 30, "Rear should be 30"
    
    dequeued = queue.dequeue()
    assert dequeued == 10, "Dequeued value should be 10"
    assert queue.size() == 2, "Queue size should be 2"
    assert queue.front() == 20, "Front should now be 20"
    
    assert queue.is_empty() == False, "Queue should not be empty"
    
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty() == True, "Queue should be empty"
    assert queue.dequeue() is None, "Dequeue on empty queue should return None"
    assert queue.front() is None, "Front on empty queue should return None"
    
    queue.save_video("output/queue.mp4", fps=2)
    queue.save_snapshot("output/queue_snapshot.png")
    
    print_success("Queue tests passed!")

def test_linked_list():
    print_info("Testing Linked List...")
    
    ll = LinkedList()
    
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    
    assert len(ll.nodes) == 3, "Should have 3 nodes"
    
    ll.delete_node(20)
    assert 20 not in ll.nodes, "20 should be deleted"
    assert len(ll.nodes) == 2, "Should have 2 nodes after deletion"
    
    ll.delete_node(100)
    
    ll.save_video("output/linked_list.mp4", fps=2)
    ll.save_snapshot("output/linked_list_snapshot.png")
    
    print_success("Linked List tests passed!")

def test_bubble_sort():
    print_info("Testing Bubble Sort...")
    
    data = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(data)
    
    sorter = BubbleSort(data.copy())
    sorter.sort(visualize=True)
    
    assert sorter.data == expected, f"Bubble sort failed. Got {sorter.data}, expected {expected}"
    
    sorter.save_video("output/bubble_sort.mp4", fps=5)
    sorter.save_snapshot("output/bubble_sort_snapshot.png")
    
    print_success("Bubble Sort tests passed!")

def test_insertion_sort():
    print_info("Testing Insertion Sort...")
    
    data = [12, 11, 13, 5, 6]
    expected = sorted(data)
    
    sorter = InsertionSort(data.copy())
    sorter.sort(visualize=True)
    
    assert sorter.data == expected, f"Insertion sort failed. Got {sorter.data}, expected {expected}"
    
    sorter.save_video("output/insertion_sort.mp4", fps=4)
    sorter.save_snapshot("output/insertion_sort_snapshot.png")
    
    print_success("Insertion Sort tests passed!")

def test_selection_sort():
    print_info("Testing Selection Sort...")
    
    data = [64, 25, 12, 22, 11]
    expected = sorted(data)
    
    sorter = SelectionSort(data.copy())
    sorter.sort(visualize=True)
    
    assert sorter.data == expected, f"Selection sort failed. Got {sorter.data}, expected {expected}"
    
    sorter.save_video("output/selection_sort.mp4", fps=3)
    sorter.save_snapshot("output/selection_sort_snapshot.png")
    
    print_success("Selection Sort tests passed!")

def test_merge_sort():
    print_info("Testing Merge Sort...")
    
    data = [38, 27, 43, 3, 9, 82, 10]
    expected = sorted(data)
    
    sorter = MergeSort(data.copy())
    sorter.sort(visualize=True)
    
    assert sorter.data == expected, f"Merge sort failed. Got {sorter.data}, expected {expected}"
    
    sorter.save_video("output/merge_sort.mp4", fps=3)
    sorter.save_snapshot("output/merge_sort_snapshot.png")
    
    print_success("Merge Sort tests passed!")

def test_quick_sort():
    print_info("Testing Quick Sort...")
    
    data = [10, 7, 8, 9, 1, 5]
    expected = sorted(data)
    
    sorter = QuickSort(data.copy())
    sorter.sort(visualize=True)
    
    assert sorter.data == expected, f"Quick sort failed. Got {sorter.data}, expected {expected}"
    
    sorter.save_video("output/quick_sort.mp4", fps=5)
    sorter.save_snapshot("output/quick_sort_snapshot.png")
    
    print_success("Quick Sort tests passed!")

def test_dijkstra():
    print_info("Testing Dijkstra's Algorithm...")
    
    dijkstra = Dijkstra()
    
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2),
        ('D', 'F', 6),
        ('E', 'F', 3)
    ]
    
    for u, v, w in edges:
        dijkstra.add_edge(u, v, w)
    
    dijkstra.visualize_search('A', 'F')
    
    dijkstra.save_video("output/dijkstra_path.mp4", fps=1)
    dijkstra.save_snapshot("output/dijkstra_snapshot.png")
    
    print_success("Dijkstra's Algorithm tests passed!")

def test_edge_cases():
    print_info("Testing edge cases...")
    
    bst = BST()
    assert bst.search(10) == False, "Empty BST search should return False"
    bst.delete(10)

    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.delete(10)
    
    stack = Stack()
    assert stack.pop() is None
    assert stack.peek() is None
    
    queue = Queue()
    assert queue.dequeue() is None
    assert queue.front() is None
    assert queue.rear() is None
    
    empty_sorter = BubbleSort([])
    empty_sorter.sort(visualize=True)
    assert empty_sorter.data == [], "Empty array sort should work"
    
    single_sorter = QuickSort([42])
    single_sorter.sort(visualize=True)
    assert single_sorter.data == [42], "Single element sort should work"
    
    sorted_data = [1, 2, 3, 4, 5]
    sorter = InsertionSort(sorted_data.copy())
    sorter.sort(visualize=True)
    assert sorter.data == sorted_data, "Already sorted array should remain sorted"
    
    reversed_data = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    sorter2 = SelectionSort(reversed_data.copy())
    sorter2.sort(visualize=True)
    assert sorter2.data == expected, "Reversed array should be sorted correctly"
    
    print_success("Edge cases tests passed!")

def main():
    print(f"\n{Colors.BLUE}{'='*60}{Colors.RESET}")
    print(f"{Colors.BLUE}     STARTING COMPREHENSIVE TESTS FOR ALL ALGORITHMS{Colors.RESET}")
    print(f"{Colors.BLUE}{'='*60}{Colors.RESET}\n")
    
    os.makedirs("output", exist_ok=True)
    
    tests = [
        ("Linear Search", test_linear_search),
        ("Binary Search", test_binary_search),
        ("Binary Search Tree", test_bst),
        ("Stack", test_stack),
        ("Queue", test_queue),
        ("Linked List", test_linked_list),
        ("Bubble Sort", test_bubble_sort),
        ("Insertion Sort", test_insertion_sort),
        ("Selection Sort", test_selection_sort),
        ("Merge Sort", test_merge_sort),
        ("Quick Sort", test_quick_sort),
        ("Dijkstra's Algorithm", test_dijkstra),
        ("Edge Cases", test_edge_cases),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            print_error(f"{test_name}: {e}")
            failed += 1
        except Exception as e:
            print_error(f"{test_name}: Unexpected error - {e}")
            failed += 1
        print() 
    
    print(f"{Colors.BLUE}{'='*60}{Colors.RESET}")
    print(f"{Colors.BLUE}                 TEST RESULTS SUMMARY{Colors.RESET}")
    print(f"{Colors.BLUE}{'='*60}{Colors.RESET}")
    print(f"{Colors.GREEN}✓ Passed: {passed}{Colors.RESET}")
    print(f"{Colors.RED}✗ Failed: {failed}{Colors.RESET}")
    print(f"{Colors.BLUE}{'='*60}{Colors.RESET}\n")
    
    answer = input("Delete temporary directories? (y/n): ")
    if answer.lower() == 'y':
        cleanup_temp_dirs()
    
    print(f"\n{Colors.BLUE}All output files saved in 'output/' directory{Colors.RESET}\n")
    
    return failed == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)