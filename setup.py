from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')
    return requirements

requirements = read_requirements()

setup(
    name='makePDF',  # Replace 'your-cli-tool' with the name of your CLI tool
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'makePDF=main:main',
        ],
    },
    author='Christopher Bannon',
    author_email='cbannon@berkeley.edu',
    description='Simple CLI tool to convert images in a directory to a PDF',
    url='https://github.com/Cbannon35/makePDF',
    install_requires=requirements,  # List dependencies if any
)