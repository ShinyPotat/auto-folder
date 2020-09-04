import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

path = '.\\tests'

extensions = {
    "images": [
        'jpeg',
        'jpg',
        'png'
    ],
    "documents": [
        'txt',
        'doc',
        'docx',
        'pdf'
    ],
    "videos": [
        'mp4',
        'mkv'
    ],
    "music": [
        'mp3',
        'wav'
    ]
}

folders = ['/images', '/documents', '/videos', '/music']

for folder in folders:
    if(os.path.isdir(path + folder)==False):
        os.mkdir(path + folder)

while True:

    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    for file in files:

        file_extension = file.split('.')[1]
        
        for type in extensions:

            new_path = os.path.join(path, type)

            if file_extension in extensions.get(type):
                os.rename(os.path.join(path, file), os.path.join(new_path, file))
                print(bcolors.FAIL + os.path.join(path, file) + bcolors.ENDC + ' moved to ' + bcolors.OKGREEN + new_path + bcolors.ENDC)
                break
