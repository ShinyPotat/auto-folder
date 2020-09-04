import os, sys, getopt, json

class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

try:
    with open('./extensions.json') as f:
        extensions = json.load(f)
except FileNotFoundError:
    print(bcolors.FAIL + 'Error: extensions.json file must be in the same folder than auto-folder.py' + bcolors.ENDC)
    sys.exit(2)

folders = list(extensions.keys())
folders.append('other')

def main(argv):

    #Comprobar los valores introducidos por los usuarios
    if len(argv) == 0 or len(argv) > 2 or argv[0].startswith('-')==False:
        print(bcolors.FAIL + '<Syntax error>: ' + bcolors.ENDC + 'auto-folder.py -p <path>')
        sys.exit(2) 

    try:
      opts, args = getopt.getopt(argv,"hp:")
    except getopt.GetoptError:
        print(bcolors.FAIL + '<Syntax error>: ' + bcolors.ENDC + 'auto-folder.py -p <path>')
        sys.exit(2)

    #Comprobar el flag que se ha usado
    for opt, arg in opts:
        if opt == '-h':
            print('auto-folder.py -p <path>')
            sys.exit()
        elif opt in ("-p", "--path"):
            path = arg

    # Crear las carpetas si no existen
    for folder in folders:
        if(os.path.isdir(os.path.join(path, folder))==False):
            os.mkdir(os.path.join(path, folder))
            print('folder ' + bcolors.OKGREEN + folder + bcolors.ENDC + ' created')

    while True:

        #Listado de archivos
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
