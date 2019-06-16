from setuptools import setup, find_packages


with open("requirements.txt") as f:
    dependencies = f.readlines()

setup(
    name="whentfis",
    packages=find_packages(),
    include_package_data=True,
    test_suite="whentfis.tests",
    python_requires='>=3',
    url="",
    entry_points={
        'console_scripts':
        ['whentfis=whentfis.scripts.whentfis:main'],
    },
    version="0.1",
    author="Laurence Warne",
    license="MIT",
    install_requires=dependencies,
    zip_safe=False
)
