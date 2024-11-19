# Sagittal Average

This is a very simple example package used as part of the UCL
[Research Software Engineering with Python](development.rc.ucl.ac.uk/training/engineering) course.

## Installation

Browse to the directory where this file lives, and run:
```bash
pip install .
```
That command will download any dependencies we have


## Usage
    
Invoke the tool with `sagittal_average_run <input_file_Dir>` or use it on your own library:

```python
from sagittal_average import sagittal_brain

sagittal_brain.run_averages("input_file.csv", "ouput_file.csv")
```
