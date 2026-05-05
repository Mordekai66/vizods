import matplotlib.pyplot as plt
import networkx as nx
import os
import imageio.v2 as imageio

class Dijkstra:
    def __init__(self):
        self.graph = nx.Graph()
        self.frames = []
        self.temp_dir = ".temp"
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
        else:
            for f in os.listdir(self.temp_dir):
                os.remove(os.path.join(self.temp_dir, f))

    def add_edge(self, u, v, weight):
        self.graph.add_edge(u, v, weight=weight)

    def visualize_search(self, start_node, target_node=None):
        distances = {node: float('infinity') for node in self.graph.nodes()}
        distances[start_node] = 0
        visited = set()
        pq = [(0, start_node)]
        parent = {node: None for node in self.graph.nodes()}

        while pq:
            pq.sort()
            current_distance, u = pq.pop(0)

            if u in visited:
                continue
            visited.add(u)

            self._take_snapshot(
                visited=visited, 
                current_node=u, 
                distances=distances,
                message=f"Exploring Node: {u}"
            )

            if u == target_node:
                break

            for v, weight_data in self.graph[u].items():
                weight = weight_data['weight']
                distance = current_distance + weight

                if distance < distances[v]:
                    distances[v] = distance
                    parent[v] = u
                    pq.append((distance, v))
                    self._take_snapshot(
                        visited=visited,
                        current_node=v,
                        edge_highlight=(u, v),
                        distances=distances,
                        message=f"Updating distance of {v} to {distance}"
                    )

        if target_node and distances[target_node] != float('infinity'):
            path = []
            curr = target_node
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            self._take_snapshot(visited=visited, final_path=path, message="Shortest Path Found!")

    def _take_snapshot(self, visited=None, current_node=None, edge_highlight=None, final_path=None, distances=None, message=""):
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(self.graph, seed=42) # توزيعه ثابتة للعقد

        nx.draw_networkx_nodes(self.graph, pos, node_color='skyblue', node_size=800)
        
        if visited:
            nx.draw_networkx_nodes(self.graph, pos, nodelist=list(visited), node_color='lightgreen', node_size=800)
        
        if current_node:
            nx.draw_networkx_nodes(self.graph, pos, nodelist=[current_node], node_color='orange', node_size=1000)

        if final_path:
            path_edges = list(zip(final_path, final_path[1:]))
            nx.draw_networkx_nodes(self.graph, pos, nodelist=final_path, node_color='red', node_size=1000)
            nx.draw_networkx_edges(self.graph, pos, edgelist=path_edges, edge_color='red', width=3)

        nx.draw_networkx_edges(self.graph, pos, edge_color='gray', alpha=0.5)
        if edge_highlight:
            nx.draw_networkx_edges(self.graph, pos, edgelist=[edge_highlight], edge_color='orange', width=2)
        
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        
        if distances:
            node_labels = {n: f"{n}\n({d if d != float('inf') else '∞'})" for n, d in distances.items()}
            nx.draw_networkx_labels(self.graph, pos, labels=node_labels, font_size=10)
        else:
            nx.draw_networkx_labels(self.graph, pos)

        plt.title(f"Dijkstra Algorithm: {message}")
        
        filename = os.path.join(self.temp_dir, f"dij_{len(self.frames)}.png")
        plt.savefig(filename)
        plt.close()
        self.frames.append(filename)

    def save_video(self, output_name="dijkstra_path.mp4", fps=1):
        with imageio.get_writer(output_name, fps=fps) as writer:
            for filename in self.frames:
                image = imageio.imread(filename)
                writer.append_data(image)
        print(f"✅ Dijkstra video saved as: {output_name}")
        
    def save_snapshot(self, filename="dijkstra_snapshot.png"):
        if self.frames:
            latest_frame = self.frames[-1]
            image = imageio.imread(latest_frame)
            imageio.imwrite(filename, image)
            print(f"✅ Latest snapshot saved as: {filename}")
        else:
            print("⚠️ No snapshots available to save.")
    
    def save_gif(self, output_name="dijkstra_path.gif", fps=1):
        if not self.frames:
            print("⚠️ No frames to create GIF.")
            return
        with imageio.get_writer(output_name, mode='I', fps=fps) as writer:
            for filename in self.frames:
                image = imageio.imread(filename)
                writer.append_data(image)
        print(f"✅ Dijkstra GIF saved as: {output_name}")