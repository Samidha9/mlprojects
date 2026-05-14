from setuptools import find_packages, setup
setup(
    name ='ML Project',
    version = 0.01,
    author = 'Samidha',
    author_email = 'samidhabhosale7@gmail.com',
    packages = find_packages(),
    install_requires= ['pandas', 'numpy', 'matplotlib', 'seaborn']
)