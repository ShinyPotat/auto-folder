import os, sys, getopt

class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

extensions = {
        "images": [
            'jpeg',
            'jpg',
            'png',
            'ico'
        ],
        "documents": [
            'txt',
            'doc',
            'docx',
            'pdf'
        ],
        "videos": [
            'mp4',
            'mkv',
            'gif'
        ],
        "music": [
            'mp3',
            'wav',
            'mpeg'
        ]
    }

folders = ['/images', '/documents', '/videos', '/music', '/other']

def main(argv):

    if len(argv) > 2 or argv[0].startswith('-')==False:
        print(bcolors.FAIL + '<Syntax error>: ' + bcolors.ENDC + 'auto-folder.py -p <path>')
        sys.exit(2) 

    try:
      opts, args = getopt.getopt(argv,"hp:",["path=",])
    except getopt.GetoptError:
        print(bcolors.FAIL + '<Syntax error>: ' + bcolors.ENDC + 'auto-folder.py -p <path>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('auto-folder.py -p <path>')
            sys.exit()
        elif opt in ("-p", "--path"):
            path = arg
        else:
            print(bcolors.FAIL + '<Syntax error>: ' + bcolors.ENDC + 'auto-folder.py -p <path>')
            sys.exit(2)

    for folder in folders:
        if(os.path.isdir(path + folder)==False):
            os.mkdir(path + folder)

    while True:

        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

        for file in files:

            file_split = file.split('.')
            file_extension = file_split[len(file_split)-1]
            
            for type in extensions:

                new_path = os.path.join(path, type)

                if file_extension in extensions.get(type):
                    os.rename(os.path.join(path, file), os.path.join(new_path, file))
                    print(bcolors.FAIL + file + bcolors.ENDC + ' moved to ' + bcolors.OKGREEN + type + bcolors.ENDC)
                    break
            
            if(os.path.isfile(os.path.join(path, file))):
                new_path = os.path.join(path, 'other')
                os.rename(os.path.join(path, file), os.path.join(new_path, file))
                print(bcolors.FAIL + file + bcolors.ENDC + ' moved to ' + bcolors.OKGREEN + 'other' + bcolors.ENDC)            

if __name__ == "__main__":
    main(sys.argv[1:])
