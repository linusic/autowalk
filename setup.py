from setuptools import setup

with open("autowalk/README.md", "r") as f:
    long_description = f.read()

setup(
    name='autowalk',
    version="1.2.0",
    author="linusic",
    author_email='cython_lin@cklin.top',
    description="Configurable tool of bulking build path for AutoJump and Ranger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/linusic/autowalk",
    
    license='MIT',
    classifiers=[ 
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
    entry_points={ 
        "console_scripts": [ 
            "aw=autowalk.main:main" 
        ]
    },
    py_modules=["main"],  
    python_requires='>=3.6',

    packages=(
        "autowalk",
        "autowalk.utils",
    ),

)
