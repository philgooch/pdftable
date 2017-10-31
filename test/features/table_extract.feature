Feature: Extraction tables from pdftohtml XML output


  Scenario: I want to extract tables from pdftohtml
    Given I am using the Table Extractor
    When I am processing the file "test/fixtures/3.xml"
    Then The output should match the contents of the file "test/fixtures/3.csv"

    When I am processing the file "test/fixtures/0.xml"
    Then The output should match the contents of the file "test/fixtures/0.csv"

