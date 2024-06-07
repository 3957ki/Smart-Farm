import os
import random
# 주어진 디렉토리에 있는 항목들의 이름을 담고 있는 리스트를 반환합니다.
# 리스트는 임의의 순서대로 나열됩니다.
file_path = 'C:\\Users\\user\\Desktop\\강의\\종합설계\\imgs\\스킨답서스'
file_names = os.listdir(file_path)
random.shuffle(file_names)

i = 1
for name in file_names:
    src = os.path.join(file_path, name)
    dst = 'Scindapsus_' + str(i) + '.jpg'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1
