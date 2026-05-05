import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import imageio.v2 as imageio
import os

class SelectionSort:
    def __init__(self, data):
        self.data = data
        self.frames = []
        self.temp_dir = ".temp"
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
        else:
            for file in os.listdir(self.temp_dir):
                os.remove(os.path.join(self.temp_dir, file))

    def sort(self, visualize=True):
        n = len(self.data)
        for i in range(n):
            min_idx = i
            
            for j in range(i + 1, n):
                if visualize:
                    self._take_snapshot(current_min=min_idx, comparing=j, sorted_limit=i)
                
                if self.data[j] < self.data[min_idx]:
                    min_idx = j
            
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
            
            if visualize:
                self._take_snapshot(sorted_limit=i+1)

    def _take_snapshot(self, current_min=None, comparing=None, sorted_limit=0):
        plt.figure(figsize=(8, 5))
        
        colors = []
        for k in range(len(self.data)):
            if k < sorted_limit:
                colors.append('green')
            elif k == current_min:
                colors.append('red')
            elif k == comparing:
                colors.append('orange')
            else:
                colors.append('skyblue')
        
        plt.bar(range(len(self.data)), self.data, color=colors)
        
        legend_elements = [
        mpatches.Patch(color='red', label='Current Minimum'),
        mpatches.Patch(color='orange', label='Scanning Element'),
        mpatches.Patch(color='skyblue', label='Remaining Unsorted'),
        mpatches.Patch(color='green', label='Sorted')]
        
        plt.legend(handles=legend_elements, loc='upper right')
        plt.title(f"Selection Sort: Finding Minimum for Position {sorted_limit}")
        
        file_path = os.path.join(self.temp_dir, f"frame_{len(self.frames)}.png")
        
        plt.savefig(file_path)
        plt.close()
        self.frames.append(file_path)

    def save_video(self, output_name="selection_sort.mp4", fps=3):
        if not self.frames:
            print("❌ Frames not found! Make sure to run sort() first.")
            return

        with imageio.get_writer(output_name, fps=fps) as writer:
            for filepath in self.frames:
                image = imageio.imread(filepath)
                writer.append_data(image)
        
        print(f"Video saved as {output_name}")
        
    def save_gif(self, output_name="selection_sort.gif", fps=3):
        if not self.frames:
            print("❌ Frames not found! Make sure to run sort() first.")
            return

        with imageio.get_writer(output_name, mode='I', fps=fps) as writer:
            for filepath in self.frames:
                image = imageio.imread(filepath)
                writer.append_data(image)
        
        print(f"GIF saved as {output_name}")

    def save_snapshot(self, filename="final_state.png"):
        plt.bar(range(len(self.data)), self.data, color='green')
        plt.title("Final Sorted State")
        plt.savefig(filename)
        plt.close()
        print(f"Snapshot saved as {filename}")