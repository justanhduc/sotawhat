from distutils.core import setup
import os


AUTHOR = 'huyenchip'
MAJOR = 0
MINOR = 1
MICRO = '0'
VERSION = '%d.%d.%s' % (MAJOR, MINOR, MICRO)


def setup_package():
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

    setup(
        name='sotawhat',
        version=VERSION,
        description='A script to search for SOTA papers on Arxiv.',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://huyenchip.com/2018/10/04/sotawhat.html',
        author=AUTHOR,
        author_email='chip@huyenchip.com',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: MIT License',
            'Operating System :: Microsoft :: Windows :: Windows 10',
            'Programming Language :: Python :: 3 :: Only',
            'Programming Language :: Python :: 3.5'
        ],
        platforms=['Windows', 'Linux'],
        py_modules=['sotawhat'],
        install_requires=['nltk', 'pyspellchecker']
    )


if __name__ == '__main__':
    setup_package()
