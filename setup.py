from setuptools import setup, find_packages

setup(
    name='pip-size',
    version='0.1.0',
    author='rexyqywe',
    project_address='https://github.com/rexyqywe/pip_size',
    description='Show installed pip packages size',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pip-size = pip_size.cli:main',
        ],
    },
    python_requires='>=3.6',
)


'''
Use pip-size instead pip list in windows  
go to the download path and type "pip install ."     
type "pip-size" in your terminal    
        
        
delete file:  
pip uninstall pip-size  -"y"        
python setup.py clean --all


'''