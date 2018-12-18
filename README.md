# Log Munger

## Description

Bespoke data merging utility, designed to combine data from the following two sources:

  1. CloudWatch logs written by the Service Finder Service
  
  2. Splunk logs produced by the DoS search backend
  
The CloudWatch files are expected to be in flat text format, the Splunk logs to be in CSV. The 
output of this script will be CSV written to stdout.
