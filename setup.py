from setuptools import setup, find_packages

VERSION = '1.0.0' 
DESCRIPTION = 'A pandas dataframe preprocessing python package'
LONG_DESCRIPTION = 'Contains utility functions that Is used in preprocessing stages of DL/ML implementation'

# Setting up
setup(
        name="little_data_preprocessor", 
        version=VERSION,
        author="Ameh Solomon Onyeke",
        author_email="amehsolomon46@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["pandas", "numpy"],
        
        keywords=['python', 'pandas', 'preprocessing'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)