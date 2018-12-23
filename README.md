# Log Munger

## Description

Bespoke data merging utility, designed to combine data from the following two sources:

  1. CloudWatch logs written by the Service Finder Service

  2. Splunk logs produced by the DoS search backend

The CloudWatch files are expected to be in flat text format, the Splunk logs to be in CSV.

The output of this script will be CSV written to stdout. The output is in the form of a complete
CSV file with header row and one row per original SFS log item. Where there was DoS data available
with a matching timestamp to an SFS log item, the SFS log data is augmented with that which was in 
the DoS record. If no matching DoS record was found, the SFS log item is still written out,
un-augmented.

*Note: The order of the log events written to the output is effectively random. That is to say:
they are not necessarily written in date/time order.*

## Caveat

SFS source records are matched with augmenting DoS records by means of their timestamps. Sadly the
DoS data does not contain fractional seconds: each row's timestamp is rounded to have .000000
as the fractional part. Therefore we strip the 1/1000 of a second granularity of the SFS records
before performing the matching. **[Note: we _strip_ rather than _round_.]**

Naturally this means that if two DoS records contain the same timestamp, the wrong one may get 
matched with the SFS record. There's no check for this. This was accepted by the commissioning
user as a known risk.

## Dependencies

You will need Python 3 on your machine:

```
$ python3 -V
Python 3.4.0
```
Lucky you.


## Installation

There are no installation steps - no package install, no setup. Just have the `./logmunger.py` 
file available as an executable file on your machine. (If you checked out this repo, it's already
got the +x bits set).

## Usage

Command line syntax is as follows:

```
$ ./logmunger.py --sfslog=SFS_LOG_FILE.txt --doslog=DOS_LOG_FILE.csv
```

Output is written to stdout. If you want that in a file then just direct the output there like this:

```
$ ./logmunger.py --sfslog=SFS_LOG_FILE.txt --doslog=DOS_LOG_FILE.csv > MYAWESOMEOUTPUT.csv
```

## Source file formats

In theory this should "just work" with data as supplied in the original work request. Naturally the
files need to be in the expected formats. There are as follows:

### SFS log file

This needs to be a plain text file. The line ending types don't matter - Windows and Linux are both
fine. For details of what the code expects, see the test fixture file [good_sfs_log.txt](tests/fixtures/good_sfs_log.txt).

The important points are: 

  1. Each data line begins with a date time value in the format of the example file

  2. Each data line contains a `payload={<blach blah blah>}` section as a JSON format string
     which contains the properties expected by the munger. See the [test_parse_sfs_line.py](tests/unit/test_parse_sfs_line.py)
     module for details.

### DoS log file

This needs to be a CSV file.  The line ending types don't matter - Windows and Linux are both fine.
For details of what the code expects, see the test fixture file [good_dos_log.csv](tests/fixtures/good_dos_log.csv).

The important points are: 

  1. The '_raw' section is ignored

  2. The columns match those expected by the munger. See the [test_parse_dos_row.py](tests/unit/test_parse_dos_row.py)
     module for details.

## Output file format

The output file is written to stdout so you can redirect it wherever you want. It's written with
Windows line endings `\r\n` although this should not be a problem when importing into Excel (or
similar) on a non-Windows machine.

For details of output format, see the [test_logmunger.py](tests/functional/test_logmunger.py)
module.

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
