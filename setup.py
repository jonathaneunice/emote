from setuptools import setup
from codecs import open

def lines(text):
    """
    Returns each non-blank line in text enclosed in a list.
    """
    return [l.strip() for l in text.strip().splitlines() if l.strip()]


setup(
    name='emote',
    version='0.1.0',
    author='Jonathan Eunice',
    author_email='jonathan.eunice@gmail.com',
    description='Copy emoticons or emoji to clipboard',
    long_description=open('README.rst', encoding='utf-8').read(),
    url='https://github.com/jonathaneunice/emote',
    install_requires=open('requirements.txt').read().splitlines(),
    tests_require=[],
    scripts=['emote'],
    zip_safe=False,
    keywords='emoticon emoji',
    classifiers=lines("""
        Development Status :: 4 - Beta
        Operating System :: OS Independent
        Environment :: Console
        License :: OSI Approved :: MIT License
        Programming Language :: Python
        Programming Language :: Python :: 3.6
        Programming Language :: Python :: 3.7
        Programming Language :: Python :: Implementation :: CPython
        Intended Audience :: End Users/Desktop
        Topic :: Internet
        Topic :: Text Processing
        Topic :: Utilities
    """)
)
