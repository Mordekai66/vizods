import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx
import os
import imageio.v2 as imageio

class LinkedList:
    def __init__(self):
        self.nodes = []
        self.frames = []
        self.temp_dir = ".temp"
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
        else:            
            for file in os.listdir(self.temp_dir):
                os.remove(os.path.join(self.temp_dir, file))

    def add_node(self, value):
        self.nodes.append(value)
        self._take_snapshot(active_node=len(self.nodes)-1, message=f"Added node: {value}")

    def delete_node(self, value):
        if value in self.nodes:
            idx = self.nodes.index(value)
            self._take_snapshot(active_node=idx, message=f"Deleting node: {value}", color='red')
            self.nodes.remove(value)
            self._take_snapshot(message=f"Node {value} removed.")

    def _take_snapshot(self, active_node=None, message="", color='orange'):
        plt.figure(figsize=(10, 4))
        G = nx.DiGraph()

        labels = {}
        node_colors = []
        
        for i, val in enumerate(self.nodes):
            G.add_node(i)
            labels[i] = str(val)
            
            if i == active_node:
                node_colors.append(color)
            else:
                node_colors.append('skyblue')
            
            if i > 0:
                G.add_edge(i-1, i)

        pos = {i: (i, 0) for i in range(len(self.nodes))}
        
        nx.draw(G, pos, with_labels=True, labels=labels, node_size=2000, 
                node_color=node_colors, edge_color='gray', arrows=True, 
                arrowsize=20, font_weight='bold')

        plt.title(f"Linked List: {message}")
        
        legend_elements = [
            mpatches.Patch(color='skyblue', label='Node'),
            mpatches.Patch(color='orange', label='Active/New'),
            mpatches.Patch(color='red', label='Deleting')
        ]
        plt.legend(handles=legend_elements, loc='upper right')

        filename = os.path.join(self.temp_dir, f"linked_list_{len(self.frames)}.png")
        plt.savefig(filename)
        plt.close()
        self.frames.append(filename)

    def save_video(self, output_name="linked_list.mp4", fps=2):
        with imageio.get_writer(output_name, fps=fps) as writer:
            for filename in self.frames:
                image = imageio.imread(filename)
                writer.append_data(image)
        print(f"Linked List video saved: {output_name}")
        
    def save_gif(self, output_name="linked_list.gif", fps=2):
        if not self.frames:
            print("No frames to create GIF.")
            return
        with imageio.get_writer(output_name, mode='I', fps=fps) as writer:
            for filename in self.frames:
                image = imageio.imread(filename)
                writer.append_data(image)
        print(f"Linked List GIF saved: {output_name}")
        
    def save_snapshot(self, filename="linked_list_snapshot.png"):
        if self.frames:
            latest_frame = self.frames[-1]
            if os.path.exists(filename):
                os.remove(filename)
            os.rename(latest_frame, filename)
            print(f"Latest snapshot saved as: {filename}")
        else:
            print("No snapshots available to save.")