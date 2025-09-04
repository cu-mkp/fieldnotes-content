from subprocess import run
from os import chdir, walk, getcwd
from os.path import join, isdir
import sys

DATA_DIR = join(getcwd(), ".pandoc")

TEMPLATES = {
    'semester': 'semester.html',
    'fieldnote_semester': 'fieldnote-semester.html',
    'fieldnote_student': 'fieldnote-student.html',
    'annotation_semester': 'annotation-semester.html',
    'annotation_student': 'annotation-student.html',
    'profiles': 'profiles.html',
    'home': 'home.html'
    }

SEMESTERS = ['fa14', 'sp15', 'fa15', 'sp16', 'fa16', 'sp17', 'sp17dh', 'fa17']

def pandoc(template):
    cmd = ["pandoc", "-s", "-o" "index.html",
           "--data-dir", DATA_DIR,
           "--template", TEMPLATES[template],
           "index.md"]

    process = run(cmd)

    if process.stdout is not None:
        print(process.stdout)

    if process.returncode != 0:
        print("Directory: " + getcwd())
        print(' '.join(process.args))
        if process.stderr is not None:
            print(process.stderr)

def get_dirs():
    # Returns list of directories in current directories (not recursive)
    return next(walk('.'))[1]

def home():
    pandoc('home')
    for sem in SEMESTERS:
        semester(sem)

def semester(semester):
    chdir(semester)
    pandoc('semester')
    fieldnote_semester()
    annotation_semester()
    profiles()
    chdir('..')

def fieldnote_semester():
    chdir('fld')
    pandoc('fieldnote_semester')
    for student in get_dirs():
        fieldnote_student(student)
    chdir('..')

def fieldnote_student(student):
    chdir(student)
    pandoc('fieldnote_student')
    chdir('..')

def annotation_semester():
    if not isdir('ann'):
        return
    chdir('ann')
    pandoc('annotation_semester')
    for student in get_dirs():
        annotation_student(student)
    chdir('..')

def annotation_student(student):
    chdir(student)
    pandoc('annotation_student')
    chdir('..')

def profiles():
    chdir('profiles')
    pandoc('profiles')
    chdir('..')

def main():
    if len(sys.argv) == 2 and sys.argv[1]:
        chdir(sys.argv[1])
    home()
    chdir('..')

if __name__ == "__main__":
    main()
