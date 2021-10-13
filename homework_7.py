import os
import shutil

# Задание 1
pattern = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for root, folders in pattern.items():
    if os.path.exists(root):
        print(root, 'такая папка уже существует')
    else:
        for folder in folders:
            cur_dir = os.path.join(root, folder)
            os.makedirs(cur_dir)
# Задание 3
my_dir = 'task3'
if not os.path.exists(my_dir):
    os.mkdir(my_dir)

folder = r'my_project'
files = []


for r, d, f in os.walk(folder):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))
for path in files:
    folder = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    save_path = os.path.join(folder, os.path.basename(path))
    shutil.copy(path, save_path)

# Задание 4
files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append(os.stat(file_path).st_size)
max_size = max(files)
i = 1
out_dict = {}
for _ in range(len(str(max_size))):
    i *= 10
    out_dict[i] = 0
for file in files:
        out_dict[10 ** len(str(file))] += 1
print(out_dict)