import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import imageio.v2 as imageio
import os

class MergeSort:
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
        self._merge_sort_recursive(0, len(self.data) - 1, visualize)

    def _merge_sort_recursive(self, left, right, visualize):
        if left < right:
            mid = (left + right) // 2
            
            self._merge_sort_recursive(left, mid, visualize)
            self._merge_sort_recursive(mid + 1, right, visualize)
            
            self._merge(left, mid, right, visualize)

    def _merge(self, left, mid, right, visualize):
        left_part = self.data[left:mid + 1]
        right_part = self.data[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(left_part) and j < len(right_part):
            if visualize:
                self._take_snapshot(active_range=(left, right), current_idx=k)
            
            if left_part[i] <= right_part[j]:
                self.data[k] = left_part[i]
                i += 1
            else:
                self.data[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            self.data[k] = left_part[i]
            i += 1
            k += 1
        while j < len(right_part):
            self.data[k] = right_part[j]
            j += 1
            k += 1
            
        if visualize:
            self._take_snapshot(active_range=(left, right), settled=True)

    def _take_snapshot(self, active_range=(None, None), current_idx=None, settled=False):
        plt.figure(figsize=(8, 5))
        
        colors = []
        l, r = active_range
        for idx in range(len(self.data)):
            if l is not None and r is not None and l <= idx <= r:
                if idx == current_idx:
                    colors.append('orange')
                elif settled:
                    colors.append('green')
                else:
                    colors.append('skyblue')
            else:
                colors.append('lightgray')
        
        plt.bar(range(len(self.data)), self.data, color=colors)
        
        legend_elements = [
            mpatches.Patch(color='skyblue', label='Merging group'),
            mpatches.Patch(color='orange', label='Current index'),
            mpatches.Patch(color='green', label='Merged'),
            mpatches.Patch(color='lightgray', label='Waiting')
        ]
        
        plt.legend(handles=legend_elements, loc='upper right')
        plt.title("Merge Sort: Combining Sub-arrays")
        
        file_path = os.path.join(self.temp_dir, f"merge_{len(self.frames)}.png")
        
        plt.savefig(file_path)
        plt.close()
        self.frames.append(file_path)

    def save_video(self, output_name="merge_sort.mp4", fps=3):
        if not self.frames:
            print("There are no frames to create a video.")
            return

        with imageio.get_writer(output_name, fps=fps) as writer:
            for filepath in self.frames:
                image = imageio.imread(filepath)
                writer.append_data(image)
        
        print(f"Video saved as {output_name}")
    def save_snapshot(self, filename="merge_sort_snapshot.png"):
        if self.frames:
            latest_frame = self.frames[-1]
            if os.path.exists(filename):
                os.remove(filename)
            os.rename(latest_frame, filename)
            print(f"Latest snapshot saved as: {filename}")
        else:
            print("No snapshots available to save.")