import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import imageio.v2 as imageio
import os

class Queue:
    def __init__(self):
        self.data = []
        self.frames = []
        self.temp_dir = ".temp"
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
        else:
            for f in os.listdir(self.temp_dir):
                os.remove(os.path.join(self.temp_dir, f))

    def enqueue(self, value):
        self.data.append(value)
        self._take_snapshot(active_idx=len(self.data) - 1, 
                            message=f"Enqueued: {value}", 
                            color='orange')

    def dequeue(self):
        if not self.data:
            self._take_snapshot(message="Dequeue failed: Queue is empty!")
            print("Queue is empty. Nothing to dequeue.")
            return None
        
        value = self.data[0]
        self._take_snapshot(active_idx=0, 
                            message=f"Dequeuing: {value}", 
                            color='red')
        
        self.data.pop(0)
        self._take_snapshot(message=f"Dequeued: {value}")
        return value

    def front(self):
        if not self.data:
            self._take_snapshot(message="Front failed: Queue is empty!")
            print("Queue is empty. No front element.")
            return None
        
        value = self.data[0]
        self._take_snapshot(active_idx=0, 
                            message=f"Front: {value}", 
                            color='purple')
        return value

    def rear(self):
        if not self.data:
            self._take_snapshot(message="Rear failed: Queue is empty!")
            print("Queue is empty. No rear element.")
            return None
        
        value = self.data[-1]
        self._take_snapshot(active_idx=len(self.data) - 1, 
                            message=f"Rear: {value}", 
                            color='purple')
        return value

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def _take_snapshot(self, active_idx=None, message="", color='orange'):
        plt.figure(figsize=(10, 4))
        
        n = len(self.data)
        
        if n == 0:
            plt.text(0.5, 0.5, "Empty Queue", ha='center', va='center',
                     fontsize=20, color='gray',
                     transform=plt.gca().transAxes)
            plt.xlim(0, 1)
            plt.ylim(0, 1)
        else:
            colors = []
            for k in range(n):
                if k == active_idx:
                    colors.append(color)
                elif k == 0:
                    colors.append('lightgreen')
                elif k == n - 1:
                    colors.append('skyblue')
                else:
                    colors.append('lightgray')
            
            x_positions = list(range(n))
            plt.bar(x_positions, [1] * n, color=colors,
                    edgecolor='black', width=0.8)
            
            for i, val in enumerate(self.data):
                plt.text(i, 0.5, str(val), ha='center', va='center',
                         fontsize=14, fontweight='bold')
            
            plt.annotate('FRONT', xy=(0, 1.05), xytext=(0, 1.35),
                         fontsize=11, fontweight='bold', color='darkgreen',
                         arrowprops=dict(arrowstyle='->', color='darkgreen'),
                         ha='center')
            
            plt.annotate('REAR', xy=(n - 1, 1.05), xytext=(n - 1, 1.35),
                         fontsize=11, fontweight='bold', color='darkblue',
                         arrowprops=dict(arrowstyle='->', color='darkblue'),
                         ha='center')
            
            plt.xlim(-0.7, max(n, 1) - 0.3)
            plt.ylim(0, 1.6)
        
        plt.yticks([])
        plt.xlabel("Queue Order (FIFO)")
        
        legend_elements = [
            mpatches.Patch(color='orange', label='Enqueueing'),
            mpatches.Patch(color='red', label='Dequeueing'),
            mpatches.Patch(color='purple', label='Inspecting'),
            mpatches.Patch(color='lightgreen', label='Front Element'),
            mpatches.Patch(color='skyblue', label='Rear Element'),
            mpatches.Patch(color='lightgray', label='Stored Elements')
        ]
        
        plt.legend(handles=legend_elements, loc='upper left',
                   bbox_to_anchor=(1.01, 1.0), fontsize=9)
        plt.title(f"Queue: {message}", fontsize=13)
        plt.tight_layout()
        
        file_path = os.path.join(self.temp_dir, f"queue_{len(self.frames)}.png")
        plt.savefig(file_path)
        plt.close()
        self.frames.append(file_path)

    def save_video(self, output_name="queue.mp4", fps=2):
        if not self.frames:
            print("There are no frames to create a video.")
            return

        with imageio.get_writer(output_name, fps=fps) as writer:
            for filepath in self.frames:
                image = imageio.imread(filepath)
                writer.append_data(image)
        
        print(f"Video saved as {output_name}")
    
    def save_gif(self, output_name="queue.gif", fps=2):
        if not self.frames:
            print("There are no frames to create a GIF.")
            return

        with imageio.get_writer(output_name, mode='I', fps=fps) as writer:
            for filepath in self.frames:
                image = imageio.imread(filepath)
                writer.append_data(image)
        
        print(f"GIF saved as {output_name}")

    def save_snapshot(self, filename="queue_final.png"):
        if not self.frames:
            print("No frames to save!")
            return
        
        latest_frame = self.frames[-1]
        if os.path.exists(latest_frame):
            if os.path.exists(filename):
                os.remove(filename)
            os.rename(latest_frame, filename)
            self.frames.pop()
            print(f"Latest queue snapshot saved as: {filename}")
        else:
            print("Latest frame not found!")