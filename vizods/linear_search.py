import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import imageio.v2 as imageio
import os

class LinearSearch:
    def __init__(self, data):
        self.data = data
        self.frames = []
        self.temp_dir = ".temp"
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
        else:
            for file in os.listdir(self.temp_dir):
                os.remove(os.path.join(self.temp_dir, file))

    def search(self, target):
        n = len(self.data)
        found = False
        
        for i in range(n):
            self._take_snapshot(current_idx=i, target=target, message=f"Checking index {i}")
            
            if self.data[i] == target:
                self._take_snapshot(found_idx=i, target=target, message=f"Target {target} Found!")
                found = True
                break
        
        if not found:
            self._take_snapshot(target=target, message="Not Found")
        return found

    def _take_snapshot(self, current_idx=None, found_idx=None, target=None, message=""):
        plt.figure(figsize=(8, 5))
        colors = []
        for i in range(len(self.data)):
            if i == found_idx:
                colors.append('green')
            elif i == current_idx:
                colors.append('orange')
            else:
                colors.append('skyblue')
        
        plt.bar(range(len(self.data)), self.data, color=colors)
        plt.title(f"Linear Search: {message}")
        
        labels = [mpatches.Patch(color='orange', label='Current Check'),
                  mpatches.Patch(color='green', label='Match Found'),
                  mpatches.Patch(color='skyblue', label='Unchecked')]
        plt.legend(handles=labels)

        file_path = os.path.join(self.temp_dir, f"frame_{len(self.frames)}.png")
        plt.savefig(file_path)
        plt.close()
        self.frames.append(file_path)

    def save_video(self, output_name="linear_search.mp4", fps=2):
        with imageio.get_writer(output_name, fps=fps) as writer:
            for filepath in self.frames:
                writer.append_data(imageio.imread(filepath))
        print(f"Video saved: {output_name}")

    def save_snapshot(self, output_name="linear_search_snapshot.png"):
        if not self.frames:
            print("There are no frames to save.")
            return
        
        latest_frame = self.frames[-1]
        image = imageio.imread(latest_frame)
        imageio.imwrite(output_name, image)
        print(f"Snapshot saved as {output_name}")