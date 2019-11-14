import os
import time

files = []
print('fireflies cathed :')
for r, d, f in os.walk('fireflies'):
    for file in f:
        f_path = os.path.join(r, file)
        with open(f_path) as f_file:
            content = f_file.read()
            print('{} said: {}'.format(file, content))
        
        time.sleep(1)
