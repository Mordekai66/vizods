import matplotlib.pyplot as plt
import networkx as nx
import os
import imageio.v2 as imageio

class InsertState:
    ROOT = "root"
    LEFT = "left"
    RIGHT = "right"
    DUPLICATE = "duplicate"

class BST:
    def __init__(self):
        self.tree_data = {}
        self.root = None
        self.frames = []
        self.temp_dir = ".temp"
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
        else:            
            for f in os.listdir(self.temp_dir):
                os.remove(os.path.join(self.temp_dir, f))

    def insert(self, value):
        if self.root is None:
            self.root = value
            self._take_snapshot(active_node=value, message=f"{InsertState.ROOT}: {value}")
            return
        
        state = self._insert_iterative(value)
        
        if state == InsertState.DUPLICATE:
            print(f"Value {value} already exists in the tree.")
        else:
            self._take_snapshot(active_node=value, message=f"{state}: {value}")

    def _insert_iterative(self, value):
        current = self.root
        
        while True:
            self.tree_data.setdefault(current, {'left': None, 'right': None})
            
            if value == current:
                return InsertState.DUPLICATE
            
            elif value < current:
                if self.tree_data[current]['left'] is None:
                    self.tree_data[current]['left'] = value
                    return InsertState.LEFT
                current = self.tree_data[current]['left']
            
            else:
                if self.tree_data[current]['right'] is None:
                    self.tree_data[current]['right'] = value
                    return InsertState.RIGHT
                current = self.tree_data[current]['right']

    def search(self, value):
        current = self.root
        
        while current is not None:
            self._take_snapshot(active_node=current, message=f"search at {current}")
            
            if value == current:
                self._take_snapshot(active_node=current, message=f"found: {value}")
                return True
            
            elif value < current:
                current = self.tree_data.get(current, {}).get('left')
            else:
                current = self.tree_data.get(current, {}).get('right')
        
        self._take_snapshot(active_node=None, message=f"not found: {value}")
        return False

    def delete(self, value):
        # Note: This implementation only handles leaf node deletion for simplicity
        parent = None
        current = self.root

        while current and current != value:
            parent = current
            if value < current:
                current = self.tree_data.get(current, {}).get('left')
            else:
                current = self.tree_data.get(current, {}).get('right')

        if current is None:
            print(f"Value {value} not found")
            return

        # CASE 1: Leaf
        if self.tree_data.get(current, {}).get('left') is None and self.tree_data.get(current, {}).get('right') is None:
            if parent is None:
                self.root = None
            else:
                if self.tree_data[parent]['left'] == current:
                    self.tree_data[parent]['left'] = None
                else:
                    self.tree_data[parent]['right'] = None
            
            self.tree_data.pop(current, None)
            self._take_snapshot(active_node=value, message=f"deleting: {value}")

    def _take_snapshot(self, active_node=None, message=""):
        plt.figure(figsize=(10, 7))
        G = nx.DiGraph()
        
        all_nodes = set()
        if self.root is not None:
            all_nodes.add(self.root)
        for parent, children in self.tree_data.items():
            all_nodes.add(parent)
            if children['left'] is not None:
                all_nodes.add(children['left'])
            if children['right'] is not None:
                all_nodes.add(children['right'])
        
        G.add_nodes_from(all_nodes)

        for parent, children in self.tree_data.items():
            if children['left'] is not None:
                G.add_edge(parent, children['left'])
            if children['right'] is not None:
                G.add_edge(parent, children['right'])
        
        pos = self._hierarchy_pos(G, self.root) if self.root is not None else {}
        
        node_list = list(G.nodes())
        node_colors = ['orange' if n == active_node else 'skyblue' for n in node_list]
        
        nx.draw(G, pos, with_labels=True, node_size=1500, node_color=node_colors, edge_color='gray', arrows=True, font_weight='bold', arrowsize=15)
        
        plt.title(f"vizods BST: {message}", fontsize=14)
        plt.figtext(0.5, 0.02, "Skyblue: Node | Orange: Last Action", ha="center")
        
        filename = os.path.join(self.temp_dir, f"bst_{len(self.frames)}.png")
        plt.savefig(filename)
        plt.close()
        self.frames.append(filename)

    def _hierarchy_pos(self, G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
        def _pos(node, left, right, vert_loc, xcenter, pos=None):
            if pos is None:
                pos = {node: (xcenter, vert_loc)}
            else:
                pos[node] = (xcenter, vert_loc)
            
            neighbors = list(G.neighbors(node))
            if neighbors:
                dx = (right - left) / 2.
                left_child = [n for n in neighbors if n < node]
                right_child = [n for n in neighbors if n > node]
                
                if left_child:
                    _pos(left_child[0], left, xcenter, vert_loc - vert_gap, xcenter - dx, pos)
                if right_child:
                    _pos(right_child[0], xcenter, right, vert_loc - vert_gap, xcenter + dx, pos)
            return pos

        return _pos(root, 0, 1, vert_loc, xcenter)

    def save_snapshot(self, filename="bst_snapshot.png"):
        if not self.frames:
            print("No frames to save!")
            return
        latest_frame = self.frames[-1]
        if os.path.exists(latest_frame):
            if os.path.exists(filename):
                os.remove(filename)
            os.rename(latest_frame, filename)
            print(f"Latest BST snapshot saved as: {filename}")
        else:
            print("Latest frame not found! Or file with the same name already exists.")

    def save_video(self, output_name="bst_animation.mp4", fps=1):
        if not self.frames:
            print("No frames to save!")
            return
        with imageio.get_writer(output_name, fps=fps) as writer:
            for filename in self.frames:
                image = imageio.imread(filename)
                writer.append_data(image)
        print(f"BST Visualization saved as: {output_name}")
    
    def save_gif(self, output_name="bst_animation.gif", fps=1):
        if not self.frames:
            print("No frames to save!")
            return
        with imageio.get_writer(output_name, mode='I', fps=fps) as writer:
            for filename in self.frames:
                image = imageio.imread(filename)
                writer.append_data(image)
        print(f"BST Visualization saved as: {output_name}")