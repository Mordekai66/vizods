import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import imageio
import os

class BubbleSort:
    def __init__(self, data):
        self.data = data
        self.frames = []
        self.temp_dir = ".temp"
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)

    def sort(self, visualize=True):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                
                if visualize:
                    self._take_snapshot(highlight=(j, j+1), sorted_count=i)
            if visualize:
                self._take_snapshot(sorted_count=i + 1)

    def _take_snapshot(self, message, highlight=(None, None), sorted_count=0):
        plt.figure(figsize=(6, 4))
        n = len(self.data)
        
        colors = []
        for k in range(n):
            if k >= n - sorted_count:
                colors.append('green')
            elif highlight[0] is not None and k in highlight:
                colors.append('orange')
            else:
                colors.append('skyblue')
                
        plt.bar(range(n), self.data, color=colors)
        
        legend_elements = [
            mpatches.Patch(color='orange', label='Comparing'),
            mpatches.Patch(color='skyblue', label='Unsorted'),
            mpatches.Patch(color='green', label='Sorted')
        ]
        
        plt.legend(handles=legend_elements, loc='upper right')
        plt.title("Bubble Sort Process")
        filename = os.path.join(self.temp_dir, f"temp_{len(self.frames)}.png")
        plt.savefig(filename)
        plt.close()
        self.frames.append(filename)

    def save_video(self, output_name="bubble_sort.mp4", fps=5):
        with imageio.get_writer(output_name, fps=fps) as writer:
            for filename in self.frames:
                image = imageio.imread(filename)
                writer.append_data(image)
                os.remove(filename)
        print(f"Video saved as {output_name}")

    def save_snapshot(self, filename="final_state.png"):
        plt.bar(range(len(self.data)), self.data, color='green')
        plt.title("Final Sorted State")
        plt.savefig(filename)
        plt.close()
        print(f"Snapshot saved as {filename}")