from collections import defaultdict

class ResourceManager:
    r = defaultdict(int)

    def __add__(self, o):
        result_r = ResourceManager()
        for key in self.r.keys():
            result_r.r[key] += self.r[key] + o.r[key]
        return result_r

    def clean(self):
        to_delete = []
        for key in self.r.keys():
            if self.r[key] <= 0:
                to_delete.append(key)
        for key in to_delete:
            self.r.pop(key)

    def display(self):
        for key in sorted(self.r.keys()):
            print(f"{key}: {self.r[key]}")

