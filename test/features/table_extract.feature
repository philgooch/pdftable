Feature: Extraction tables from pdftohtml XML output


  Scenario: I want to extract tables from pdftohtml
    Given I am using the Table Extractor
    When I am processing the file "test/fixtures/3.xml"
    Then The output should match the expected CSV data:
    """
     , , ,Men    ,Women
     ,,,,
    Force to stop or start the load  , ,20 kg    ,15 kg
     ,,,
    Sustained force to keep the load in motion   , ,10 kg      ,7 kg
     ,,,
    """

    When I am processing the file "test/fixtures/0.xml"
    Then The output should match the expected CSV data:
    """
    ,,2010,,,2009
    Land and,,,Land and,,
    buildings,Other,Total,buildings,Other,Total
    ,£m,£m,£m,£m,£m,£m
    No later than 1 year,5.4,1.4,6.8,5.2,1.2,6.4
    Later than 1 year and no later than 5 years,14.5,2.4,16.9,16.4,1.6,18.0
    Later than 5 years,30.1,-,30.1,3.2,-,3.2
    ,50.0,3.8,53.8,24.8,2.8,27.6
    as follows:,,,,,,
    Land and buildings,,,,,,
    ,,,,,2010,2009
    ,,,,,£m,£m
    No later than 1 year,,,,,0.5,0.9
    Later than 1 year and no later than 5 years,,,,,1.9,2.3
    Later than 5 years,,,,,0.2,0.7
    ,,,,,2.6,3.9
    11. Finance income and costs ,,,,,,
    ,,,,,2010,2009
    ,,,,,£m,£m
    Bank interest receivable on cash and short term deposits,,,,,0.1,0.1
    Finance income,,,,,0.1,0.1
    Net pension scheme interest cost less return on pension scheme assets (see Note 8 and Note 24bii),,,,,(5.6),(5.4)
    Finance expense,,,,,(5.6),(5.4)
    """
