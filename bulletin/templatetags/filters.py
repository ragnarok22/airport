from django.template import Library

register = Library()

images = [
    'jpg',
    'jpeg',
    'png',
]

document = [
    'odt',
    'doc',
    'docx',
]

gif = [
    'gif',
    'ico',
]

ppt = [
    'ppt',
    'pptx',
    'odp',
]

pdf = [
    'pdf',
]

rar = [
    '7z',
    'gz',
    'tar',
    'tar.7z',
    'tar.gz',
    'zip',
    'rar',
]

EXTENSION = [images, document, gif, ppt, pdf, rar]


@register.filter(name='check_extension')
def check_extension(file: str):
    def dictionary_generator():
        dic = {}
        ext = ['image.png', 'word.png', 'gif.png', 'ppt.jpeg', 'pdf.png', 'rar.jpeg']
        iterator = 0
        for i in EXTENSION:
            for j in i:
                dic[j] = ext[iterator]
            iterator += 1
        return dic

    flag = None
    dictionary = dictionary_generator()
    for ext in EXTENSION:
        for e in ext:
            if file.endswith(e):
                flag = e
                break
    if flag:
        return dictionary[flag]
    return 'unknown.png'
