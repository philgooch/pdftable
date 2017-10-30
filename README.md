# PDF Tablr

Version: 0.1.0  [![Build Status](https://travis-ci.org/philgooch/pdftable.svg)](https://travis-ci.org/philgooch/pdftable.svg)


This is a Python 3 module and command line utility that analyzes XML output from the
program `pdftohtml` in order to extract tables from PDF files and output the data as CSV.

For example:

    pdftohtml -xml -stdout file.pdf | pdftable -f file%d.csv


See also `pdftable -h` and http://sourceforge.net/projects/pdftable

Original author: Kyle Cronan <kyle@pbx.org>

This Python 3 implementation: Phil Gooch <philgooch@users.noreply.github.com>

As per Kyle's code, this version is licensed under GPLv3. See LICENSE file.

# Installation

Install `pdftohtml` via `poppler-utils` (Linux) or `poppler` (Mac OSX)

Then install the module

    python setup.py install
    
## Command line usage

    pdftohtml -xml -stdout file.pdf | pdftable -f file%d.csv
    
## Module usage
    
    from pdftablr import table_extractor

    # XML file created from pdftohtml
    input_path = '/path/to/file.xml'
    
    # Output CSV file
    output_path = '/path/to/output.csv'
    
    with open(output_path, 'w') as output_file:
        table_extractor = Extractor(output_file=output_file)
    
        with open(input_path) as f:
            table_extractor.read_file(f)
        
        tables = table_extractor.extract()
        for table in tables:
            table.output(writer=None)