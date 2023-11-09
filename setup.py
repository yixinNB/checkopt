from setuptools import setup
from setuptools import find_packages

VERSION = '1.0.0'

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='checkopt',
    version=VERSION,
    description='✨A powerful tool to replace getopt✨',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='y',
    # author_email='gward@python.net',
    url='https://github.com/yixinNB/checkopt',
    packages=find_packages(exclude=['test']),
    project_urls={
        "Documentation": "https://github.com/yixinNB/checkopt",
        "Code": "https://github.com/yixinNB/checkopt",
        "Issue tracker": "https://github.com/yixinNB/checkopt/issues",
    }
)
