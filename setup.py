from setuptools import setup

setup(
  name = 'pdftablr',
  packages = ['pdftablr'],
  scripts = ['pdftable'],
  version = '0.1.0',
  description = "Python3 implementation of Kyle Cronan's pdftable module, with unit tests",
  long_description = """
  This is a Python 3 module and command line utility that analyzes XML output from the
    program `pdftohtml` in order to extract tables from PDF files and output the data as CSV.
    
    For example:
    
        pdftohtml -xml -stdout file.pdf | pdftable -f file%d.csv
    
    See also `pdftable -h` and http://sourceforge.net/projects/pdftable
    
    Original author: (c) 2009 Kyle Cronan <kyle@pbx.org>
    
    This Python 3 implementation: (c) 2017 Phil Gooch
    
    As per Kyle's code, this version is licensed under GPLv3. See LICENSE file.
    
    # Installation
    
    Install `pdftohtml` via `poppler-utils` (Linux) or `poppler` (Mac OSX)
    
    Then install the module
    
        python setup.py install
        
    or
        pip install pdftablr
        
    ## Command line usage
    
        pdftohtml -xml -stdout file.pdf | pdftable -f file%d.csv
        
    ## Module usage
        
        from pdftablr.table_extractor import Extractor
    
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
    
  """,
  license = 'GPLv3',
  author = 'Phil Gooch and Kyle Cronan',
  author_email = 'philgooch@users.noreply.github.com',
  url = 'https://github.com/philgooch/pdftable',
  download_url = 'https://github.com/philgooch/pdftable/archive/v0.1.0.tar.gz',
  keywords = ['python3', 'pdf', 'table-extraction', 'tables', 'information-extraction'],
  classifiers = ["License :: OSI Approved :: GNU General Public License (GPL)",
                 "Natural Language :: English",
                 "Operating System :: OS Independent",
                 "Programming Language :: Python",
                 "Topic :: Office/Business",
                 "Topic :: Software Development :: Libraries",
                 "Topic :: Text Processing",
                 ],
  zip_safe=False,
)
