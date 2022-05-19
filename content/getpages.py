from os import chdir, walk, getcwd
from os.path import join, isdir
import sys

SEMESTERS = ['fa14', 'sp15', 'fa15', 'sp16', 'fa16', 'sp17', 'sp17dh', 'fa17']

def formatpage(url, title):
    return '  - title: "' + title + '"\n    link: "' + url + '"\n    desc: ""\n'

def get_dirs():
    # Returns list of directories in current directories (not recursive)
    return next(walk('.'))[1]

def get_pages():
    return next(walk('.'))[2]

def home():
    pages = [formatpage('fa14/index.html', 'Fall 2014'),
             formatpage('sp15/index.html', 'Spring 2015'),
             formatpage('fa15/index.html', 'Fall 2015'),
             formatpage('sp16/index.html', 'Spring 2016'),
             formatpage('fa16/index.html', 'Fall 2016'),
             formatpage('sp17/index.html', 'Spring 2017'),
             formatpage('sp17dh/index.html', 'Spring 2017 Digital Humanities'),
             formatpage('fa17/index.html', 'Fall 2017')
             ]
    with open('pages.md', 'w') as fp:
        fp.write(''.join(pages))
    #print(pages)
    for sem in SEMESTERS:
        semester(sem)

def semester(semester):
    chdir(semester)
    pages = [
            formatpage('ann/index.html', 'Annotations'),
            formatpage('fld/index.html', 'Field Notes'),
            formatpage('profiles/index.html', 'Profiles')
            ]
    with open('pages.md', 'w') as fp:
        fp.write(''.join(pages))
    fieldnote_semester()
    annotation_semester()
    profiles()
    chdir('..')

def fieldnote_semester():
    chdir('fld')

    pages = []
    for student in get_dirs():
        url = join(student, 'index.html')
        parts = student.split('_')
        title = parts[1].capitalize()+ ' '  + parts[0].capitalize()
        pages.append(formatpage(url, title))
    with open('pages.md', 'w') as fp:
        fp.write(''.join(pages))

    for student in get_dirs():
        fieldnote_student(student)
    chdir('..')

def fieldnote_student(student):
    chdir(student)

    pages = []
    for project in get_pages():
        title = ' '.join(list(map(lambda x: x.capitalize(), project.split('.')[0].split('_')[-1].split('-'))))
        pages.append(formatpage(project, title))
    with open('pages.md', 'w') as fp:
        fp.write(''.join(pages))

    chdir('..')

def annotation_semester():
    if not isdir('ann'):
        return
    chdir('ann')

    pages = []
    for project in get_dirs():
        url = join(project, 'index.html')
        parts = project.split('_')
        students = list(map(lambda x: x.capitalize(), parts[1].split('+')))
        project_name = ' '.join(list(map(lambda x: x.capitalize(), parts[0].split('-'))))

        title = ', '.join(students) + ': ' + project_name
        pages.append(formatpage(url, title))
    with open('pages.md', 'w') as fp:
        fp.write(''.join(pages))

    for student in get_dirs():
        annotation_student(student)
    chdir('..')

def annotation_student(student):
    chdir(student)

    pages = []
    for project in get_pages():
        title = ' '.join(list(map(lambda x: x.capitalize(), project.split('.')[0].split('_')[-1].split('-'))))
        pages.append(formatpage(project, title))
    with open('pages.md', 'w') as fp:
        fp.write(''.join(pages))

    chdir('..')

def profiles():
    chdir('profiles')

    pages = []
    for person in get_pages():
        parts = person.split('.')[0].split('_')
        if len(parts) < 3:
            continue
        title = parts[-1].capitalize() + ' ' + parts[-2].capitalize()
        pages.append(formatpage(person, title))
    with open('pages.md', 'w') as fp:
        fp.write(''.join(pages))

    chdir('..')

def main():
    if len(sys.argv) == 2 and sys.argv[1]:
        chdir(sys.argv[1])
    home()
    chdir('..')

if __name__ == "__main__":
    main()

