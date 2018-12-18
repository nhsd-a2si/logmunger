# Log Munger

## Description

Bespoke data merging utility, designed to combine data from the following two sources:

  1. CloudWatch logs written by the Service Finder Service
  
  2. Splunk logs produced by the DoS search backend
  
The CloudWatch files are expected to be in flat text format, the Splunk logs to be in CSV. The 
output of this script will be CSV written to stdout.

## Dependencies

You will need Python 3 on your machine:

```
$ python3 -V
Python 3.4.0
```
Lucky you.

## Usage

Command line syntax is as follows:

```
$ ./logmunger.py --sfslog=SFS_LOG_FILE.txt --doslog=DOS_LOG_FILE.csv
```

Output is written to stdout. If you want that in a file then just direct the output there like this:

```
$ ./logmunger.py --sfslog=SFS_LOG_FILE.txt --doslog=DOS_LOG_FILE.csv > MYAWESOMEOUTPUT.csv
```

## Maintenance

### Running tests

Run the unit test suite either using Make:
```
$ make test
```
or by direct command line:
```
$ python3 -m unittest
```
