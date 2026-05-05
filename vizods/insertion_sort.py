import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import imageio.v2 as imageio
import os

class InsertionSort:
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
        
        for i in range(1, n):
            key = self.data[i]
            j = i - 1
            
            if visualize:
                self._take_snapshot(key_idx=i, comparing_idx=j, sorted_limit=i)

            while j >= 0 and self.data[j] > key:
                if visualize:
                    self._take_snapshot(key_idx=j+1, comparing_idx=j, sorted_limit=i)
                
                self.data[j + 1] = self.data[j]
                j -= 1
            
            self.data[j + 1] = key
            
            if visualize:
                self._take_snapshot(key_idx=j+1, sorted_limit=i+1)

    def _take_snapshot(self, key_idx=None, comparing_idx=None, sorted_limit=0):
        plt.figure(figsize=(8, 5))
        
        colors = []
        for k in range(len(self.data)):
            if k == key_idx:
                colors.append('red')
            elif k == comparing_idx:
                colors.append('orange')
            elif k < sorted_limit:
                colors.append('green')
            else:
                colors.append('skyblue')
        
        plt.bar(range(len(self.data)), self.data, color=colors)
        
        legend_elements = [
        mpatches.Patch(color='red', label='Key / Picked'),
        mpatches.Patch(color='orange', label='Comparing'),
        mpatches.Patch(color='skyblue', label='Unprocessed'),
        mpatches.Patch(color='green', label='Sorted Sub-array')]
        
        plt.legend(handles=legend_elements, loc='upper right')
        plt.title(f"Insertion Sort: Positioning Element {self.data[key_idx] if key_idx is not None else ''}")
        
        file_path = os.path.join(self.temp_dir, f"frame_{len(self.frames)}.png")
        
        plt.savefig(file_path)
        plt.close()
        self.frames.append(file_path)

    def save_video(self, output_name="insertion_sort.mp4", fps=4):
        if not self.frames:
            print("Make sure to call sort() with visualize=True before saving the video.")
            return

        with imageio.get_writer(output_name, fps=fps) as writer:
            for filepath in self.frames:
                image = imageio.imread(filepath)
                writer.append_data(image)
                
        print(f"Video saved as {output_name}")
    
    def save_gif(self, output_name="insertion_sort.gif", fps=4):
        if not self.frames:
            print("Make sure to call sort() with visualize=True before saving the GIF.")
            return

        with imageio.get_writer(output_name, mode='I', fps=fps) as writer:
            for filepath in self.frames:
                image = imageio.imread(filepath)
                writer.append_data(image)
                
        print(f"GIF saved as {output_name}")

    def save_snapshot(self, output_name="insertion_sort_final.png"):
        plt.figure(figsize=(8, 5))
        plt.bar(range(len(self.data)), self.data, color='green')
        plt.title("Insertion Sort: Final Sorted Array")
        plt.savefig(output_name)
        plt.close()
        print(f"Final snapshot saved as {output_name}")