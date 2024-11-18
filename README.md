# Greetings!

This is a very simple file used as part of the UCL
[Research Software Engineering with Python](development.rc.ucl.ac.uk/training/engineering) course.

## Installation

```bash
pip install git+git://github.com/Jennivine/sagittal_average
```

## Usage
    
Invoke the tool with  or use it on your own library:

```python
from sagittal_average.sagittal_brain import run_averages
run_averages(file_input="brain_sample.csv",
             file_output="brain_average.csv")
```