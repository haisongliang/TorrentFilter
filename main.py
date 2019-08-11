import  torrent_parser as tp
import os
import shutil

def get_size(info):
    if 'files' in info:
        length = 0

        for item in info['files']:
            length += item['length']
        return length
    else:
        return info['length']

root = r'C:\Users\haisong\AppData\Local\qBittorrent\BT_backup'
keyword = 'm-team'
target_dir = r"D:\torrents"

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

for dirpath, dirnames, filenames in os.walk(root):
    for filepath in filenames:
        fullpath = os.path.join(dirpath, filepath)
        ext = os.path.splitext(fullpath)[1]
        if ext == '.torrent':

            data = tp.parse_torrent_file(fullpath)
            tracker = data['announce']
            if tracker.find(keyword) >= 0 and get_size(data['info']) < 100 * 1024 * 1024:
                print(fullpath, data['info']['name'])
                shutil.copy(fullpath, os.path.join(target_dir, filepath))
