# EminentReportingTool
tool for generating reports out of eminent questionnaire data


## Functions

This package contains several functions that each perform different functions in managing eminent data. 

There are two important input artifacts that these functions use:
- export of the EUSurvey responses in XML
- a spreadsheet with the capability and maturity model.\


## IMM_to_ld()

the IMM_to_ld function takes as input:
- input_spreadsheet : string, the path to the spreadsheet containing the capability model and the maturity model
- namespace : string, the namespace within which the maturity model will need to be defined
- output_rdf : string, the path to which the rdf representation needs to be written

output:
- rdf graph object containing the tripples describing the maturity model


The function assumes the spreadsheet has a format similar to that found in ```./tests/EminentV2.1.xlsx```. It contains a list of characteristics, that are associated with their maturity level, the dimension they describe, the leevel 2 capability they belong to and the level 1 capability they belong to and then generates the tripples for each of those resources

## survey_to_ld()

This function takes as input:
- input_xml = str,  path to the survey export of the EUSurvey responses in XML
- version_number= str,  the new version number of the survey
- output_rdf= str, the path to which the rdf representation needs to be written
- serialization = 'ttl', the way the graph should be serialized, default is 'ttl' (see rdflib documentation for other options)\

output:
- rdf graph object containing the tripples describing the questionnaire and which question measures which dimension in the IMM


This function takes the survey as input and generates an rdf graph that contains the questions and their relationships to the maturity model. Only use this function when a change has been made to the survey and a new version needs to be generated