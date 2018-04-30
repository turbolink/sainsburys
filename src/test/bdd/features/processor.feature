Feature: Test Processor

  @test
  Scenario: Process a single CSV file
    Given I provide Processor with a file name ../csv_files/1.csv
    Then I run the process
    And I receive the result list of length 2

  @test
  Scenario: Process a directory with CSV files
    Given I provide Processor with a directory name ../csv_files
    Then I run the process
    And I receive the result list of length 6