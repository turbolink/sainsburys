# Sainbury's Test

### Assumptions:
* CSV files could be processed individually by given file name or all CSV files in a directory by given directory name
* The output of the program is expected to be a specifically formatted text displayed in a console
* Unit and Behave tests are not considered rigorous and represent a possible project configuration

### Project setup
The program was tested with Python 2.7

Create your virtual environment and install dependencies:
```
cd {your_workfolder}
git clone https://github.com/turbolink/sainsburys.git
virtualenv {virtualenv_name}
source {virtualenv_name}/bin/activate
cd sainburys
pip install -r requirements.txt
``` 

### How to run the program
```
cd {your_workfloder}/sainburys/src
python runner.py
```

### How to run unit tests
```
cd {your_workfolder}/sainburys/src
python -m unittest test.unit.test_runner
```

### How to run Behave tests
```
cd {your_workfolder}/sainburys/src
behave test/bdd/features/processor.feature
```