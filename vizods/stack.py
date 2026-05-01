import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import imageio.v2 as imageio
import os

class Stack:
    def __init__(self):
        self.data = []
        self.frames = []
        self.temp_dir = ".temp"
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
        else:
            for file in os.listdir(self.temp_dir):
                os.remove(os.path.join(self.temp_dir, file))

    def push(self, value):
        self.data.append(value)
        self._take_snapshot(active_idx=len(self.data) - 1, 
                            message=f"Pushed: {value}", 
                            color='orange')

    def pop(self):
        if not self.data:
            self._take_snapshot(message="Pop failed: Stack is empty!")
            print("Stack is empty. Nothing to pop.")
            return None
        
        value = self.data[-1]
        self._take_snapshot(active_idx=len(self.data) - 1, 
                            message=f"Popping: {value}", 
                            color='red')
        
        self.data.pop()
        self._take_snapshot(message=f"Popped: {value}")
        return value

    def peek(self):
        if not self.data:
            self._take_snapshot(message="Peek failed: Stack is empty!")
            print("Stack is empty. Nothing to peek.")
            return None
        
        value = self.data[-1]
        self._take_snapshot(active_idx=len(self.data) - 1, 
                            message=f"Peek (top): {value}", 
                            color='purple')
        return value

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def _take_snapshot(self, active_idx=None, message="", color='orange'):
        plt.figure(figsize=(8, 6))
        
        n = len(self.data)
        
        if n == 0:
            plt.text(0.5, 0.5, "Empty Stack", ha='center', va='center',
                     fontsize=20, color='gray',
                     transform=plt.gca().transAxes)
            plt.xlim(0, 1)
            plt.ylim(0, 1)
        else:
            colors = []
            for k in range(n):
                if k == active_idx:
                    colors.append(color)
                elif k == n - 1:
                    colors.append('skyblue')
                else:
                    colors.append('lightgray')
            
            y_positions = list(range(n))
            plt.barh(y_positions, [1] * n, color=colors, 
                     edgecolor='black', height=0.8)
            
            for i, val in enumerate(self.data):
                plt.text(0.5, i, str(val), ha='center', va='center',
                         fontsize=14, fontweight='bold')
            
            if n > 0:
                plt.annotate('TOP', xy=(1.05, n - 1), xytext=(1.3, n - 1),
                             fontsize=12, fontweight='bold', color='darkred',
                             arrowprops=dict(arrowstyle='->', color='darkred'),
                             va='center')
            
            plt.xlim(0, 2)
            plt.ylim(-0.5, max(n, 1) + 0.5)
        
        plt.xticks([])
        plt.ylabel("Stack Index (LIFO)")
        
        legend_elements = [
            mpatches.Patch(color='orange', label='Pushing'),
            mpatches.Patch(color='red', label='Popping'),
            mpatches.Patch(color='purple', label='Peeking'),
            mpatches.Patch(color='skyblue', label='Top Element'),
            mpatches.Patch(color='lightgray', label='Stored Elements')
        ]
        
        plt.legend(handles=legend_elements, loc='upper left',
                   bbox_to_anchor=(1.15, 1.0), fontsize=9)
        plt.title(f"Stack: {message}", fontsize=13)
        plt.tight_layout()
        
        file_path = os.path.join(self.temp_dir, f"stack_{len(self.frames)}.png")
        plt.savefig(file_path)
        plt.close()
        self.frames.append(file_path)

    def save_video(self, output_name="stack.mp4", fps=2):
        if not self.frames:
            print("There are no frames to create a video.")
            return

        with imageio.get_writer(output_name, fps=fps) as writer:
            for filepath in self.frames:
                image = imageio.imread(filepath)
                writer.append_data(image)
        
        print(f"Video saved as {output_name}")

    def save_snapshot(self, filename="stack_final.png"):
        if not self.frames:
            print("No frames to save!")
            return
        
        latest_frame = self.frames[-1]
        if os.path.exists(latest_frame):
            if os.path.exists(filename):
                os.remove(filename)
            os.rename(latest_frame, filename)
            self.frames.pop()
            print(f"Latest stack snapshot saved as: {filename}")
        else:
            print("Latest frame not found!")