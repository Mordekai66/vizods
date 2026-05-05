import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import imageio.v2 as imageio
import os

class BinarySearch:
    def __init__(self, data):
        self.data = sorted(data)
        self.frames = []
        self.temp_dir = ".temp"
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
        else:
            for file in os.listdir(self.temp_dir):
                os.remove(os.path.join(self.temp_dir, file))

    def search(self, target):
        low = 0
        high = len(self.data) - 1
        
        while low <= high:
            mid = (low + high) // 2
            self._take_snapshot(low, high, mid, target, f"Searching: Range [{low}-{high}]")

            if self.data[mid] == target:
                self._take_snapshot(low, high, mid, target, "Target Found!", found=True)
                return mid
            elif self.data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        self._take_snapshot(message="Target Not Found")
        return -1

    def _take_snapshot(self, low=None, high=None, mid=None, target=None, message="", found=False):
        plt.figure(figsize=(8, 5))
        colors = []
        for i in range(len(self.data)):
            if found and i == mid:
                colors.append('green')
            elif i == mid:
                colors.append('red')
            elif low is not None and high is not None and low <= i <= high:
                colors.append('orange')
            else:
                colors.append('lightgray')

        plt.bar(range(len(self.data)), self.data, color=colors)
        plt.title(f"Binary Search: {message}")
        
        legend = [mpatches.Patch(color='orange', label='Active Range'),
                  mpatches.Patch(color='red', label='Middle Element'),
                  mpatches.Patch(color='green', label='Target Found')]
        plt.legend(handles=legend)

        file_path = os.path.join(self.temp_dir, f"frame_{len(self.frames)}.png")
        plt.savefig(file_path)
        plt.close()
        self.frames.append(file_path)

    def save_video(self, output_name="binary_search.mp4", fps=2):
        with imageio.get_writer(output_name, fps=fps) as writer:
            for filepath in self.frames:
                writer.append_data(imageio.imread(filepath))
        print(f"Video saved: {output_name}")
    
    def save_gif(self, output_name="binary_search.gif", fps=2):
        with imageio.get_writer(output_name, mode='I', fps=fps) as writer:
            for filepath in self.frames:
                writer.append_data(imageio.imread(filepath))
        print(f"GIF saved: {output_name}")

    def save_snapshot(self, output_name="binary_search_snapshot.png"):
            if not self.frames:
                print("There are no frames to save.")
                return
            
            latest_frame = self.frames[-1]
            image = imageio.imread(latest_frame)
            imageio.imwrite(output_name, image)
            print(f"Snapshot saved as {output_name}")