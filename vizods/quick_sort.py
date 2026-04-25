import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import imageio.v2 as imageio
import os

class QuickSort:
    def __init__(self, data):
        self.data = data
        self.frames = []
        self.temp_dir = ".temp"
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)

    def sort(self, visualize=True):
        self._quick_sort_recursive(0, len(self.data) - 1, visualize)

    def _quick_sort_recursive(self, low, high, visualize):
        if low < high:
            pivot_index = self._partition(low, high, visualize)
            
            self._quick_sort_recursive(low, pivot_index - 1, visualize)
            self._quick_sort_recursive(pivot_index + 1, high, visualize)

    def _partition(self, low, high, visualize):
        pivot = self.data[high]
        i = low - 1
        
        for j in range(low, high):
            if visualize:
                self._take_snapshot(pivot_idx=high, curr_idx=j, left_ptr=i, low=low, high=high)
            
            if self.data[j] <= pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]
        
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        
        if visualize:
            self._take_snapshot(pivot_idx=i+1, low=low, high=high, settled=True)
            
        return i + 1

    def _take_snapshot(self, pivot_idx=None, curr_idx=None, left_ptr=None, low=None, high=None, settled=False):
        plt.figure(figsize=(8, 5))
        
        colors = []
        for k in range(len(self.data)):
            if k == pivot_idx:
                colors.append('purple')
            elif low is not None and high is not None and low <= k <= high:
                if k == curr_idx:
                    colors.append('orange')
                else:
                    colors.append('skyblue')
            else:
                colors.append('lightgray')
        
        plt.bar(range(len(self.data)), self.data, color=colors)
        
        legend_patches = [
            mpatches.Patch(color='purple', label='Pivot'),
            mpatches.Patch(color='orange', label='Current Element'),
            mpatches.Patch(color='skyblue', label='Partitioned Range'),
            mpatches.Patch(color='lightgray', label='Inactive Elements')]
        
        plt.legend(handles=legend_patches, loc='upper right')
        plt.title(f"Quick Sort: Partitioning around Pivot")
        
        file_path = os.path.join(self.temp_dir, f"frame_{len(self.frames)}.png")
        
        plt.savefig(file_path)
        plt.close()
        self.frames.append(file_path)

    def save_video(self, output_name="quick_sort.mp4", fps=5):
        if not self.frames:
            print("There are no frames to create a video.")
            return

        with imageio.get_writer(output_name, fps=fps) as writer:
            for filepath in self.frames:
                image = imageio.imread(filepath)
                writer.append_data(image)
                os.remove(filepath)
        
        print(f"Video saved as {output_name}")