from generate_report import generate_report
from responses_to_ld import answerset_to_rdf
from rdflib import Graph, Namespace, URIRef, Literal, BNode

# this function performs the whole process from importing the xml response
# to adding the results to the responses rdf graph and generating the report

def import_write_results_generate_reports(input_xml: str, 
                                          output_rdf : str,
                                          maturity_model: str,
                                          maturity_assessment : str, 
                                          study: URIRef, 
                                          community: str,
                                          responses : str, 
                                          output_directory: str,
                                          input_rdf: str= None,
                                          serialization: str='ttl',
                                          plot_kind: str = 'maturity_avg') :
    
    answerset_to_rdf(input_xml= input_xml, 
                     input_rdf= input_rdf,
                     output_rdf= output_rdf,
                     serialization = serialization)
    
    generate_report(maturity_model= maturity_model ,
                    maturity_assessment =maturity_assessment, 
                    study= study, 
                    community= community,
                    responses = responses, 
                    plot_kind= plot_kind, 
                    output_directory= output_directory)
    
import_write_results_generate_reports(
    input_xml= 'tests/ENERSHARE-2025/Content_Export_Eminent_ES-2025.xml',
    # input_rdf= '/home/joep/Documents/uuidea/git/EminentResultsDatabase/EminentResponses/EminentResponses.ttl',
    output_rdf= 'tests/ENERSHARE-2025/EminentResponses.ttl',
    serialization= 'ttl',
    maturity_model='tests/imm.ttl',
    maturity_assessment='tests/EminentQUestionnaire_1.1.0.ttl',
    study=  URIRef('http://eminent.intnet.eu/maturity_assessment_results#ES-2025'), 
    community= "ENERSHARE",
    responses= '/home/joep/Documents/uuidea/git/EminentResultsDatabase/EminentResponses/EminentResponses.ttl', 
    output_directory="tests/ENERSHARE-2025/"

)