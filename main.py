import os
import sys

def system_type():
    if sys.platform == "Liunx":
        os.system('nohub python3 mysite\manage.py runserver')
    else:
        os.system('python mysite\manage.py runserver')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    system_type()

