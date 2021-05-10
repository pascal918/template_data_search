

from setuptools import setup, find_packages


install_requires = [
    "numpy~=1.20.2",
    "tensorflow~=2.4.1",
    "matplotlib~=3.4.1",
    "pandas~=1.2.4", 
    "sklearn",
    "scipy~=1.6.3",
    "seaborn~=0.11.1", 
    "ipython~=7.23.0",
    "notebook~=6.3.0",
    "Werkzeug~=1.0.1",


]


setup(
    name="basic",
    version="0.0.1",
    groupid="free.basic",
    description="test",
    author="kzhang",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8'
    ],
    install_requires=install_requires,
    packages=find_packages("src"),
    zip_safe=False,

    package_dir={"": "src"},
)


