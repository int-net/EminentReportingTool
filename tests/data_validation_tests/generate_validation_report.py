from rdflib import Graph, Namespace, URIRef, Literal, BNode
from rdflib.namespace import FOAF, DCTERMS, DCAT, PROV, OWL, RDFS, RDF, XMLNS, SKOS, SOSA, ORG, SSN
import pandas as pd
from pyshacl import validate

def validate_response_data (maturity_model= str,maturity_assessment =str,  
                    responses = str, validation_shapes= str):
    g = Graph()
    g.parse(maturity_model)
    g.parse(maturity_assessment)
    g.parse(responses)

    validation_graph = Graph()
    validation_graph.parse(validation_shapes)
    
    r = validate(g,
        shacl_graph = validation_graph,
        inference = 'rdfs',
        abort_on_first = False,
        allow_infos = False,
        allow_warnings = False,
        meta_shacl = False,
        advanced = False,
        js = False,
        debug = False
        )

    conforms, results_graph, results_text = r
    # print(conforms)
    # print(results_text)

    # write a query that finds the missing questions or dimenisons
    count_number_of_answersets_query = """select (Count(distinct(?answerset)) as ?count) {{
        ?answerset a ema:AnswerSet .
    }}
    
    """
    count_number_of_answersets = g.query(count_number_of_answersets_query)
  
    for a in count_number_of_answersets :
        print(a['count'])

    count_number_of_answers_query = """ select ?answerset ?survey (count(distinct(?answer)) as ?numberOfAnswers) where {
        ?answerset a ema:AnswerSet . 
        ?answerset dcterms:isPartOf ?survey .
        ?answer dcterms:isPartOf ?answerset . 
    }
    group by ?answerset
    """
    number_of_answers = g.query(count_number_of_answers_query)
    # for b in number_of_answers :
    #     print(f"{b.answerset} | {b.survey} | {b['numberOfAnswers']}")

    find_missing_questions_query = """ select ?answerset ?Question ?id {{
        ?answerset a ema:AnswerSet .
        
        {?Question a ema:Question .}
        MINUS 
        {?answerset ^dcterms:isPartOf/sosa:usedProcedure ?Question .}

        ?Question dcterms:identifier ?id .
    }}

    """
    missing_questions = g.query(find_missing_questions_query)

    for r in missing_questions:
        print(r.answerset)
        print(r.id)

maturity_model='./tests/imm.ttl'
maturity_assessment = './tests/EminentQUestionnaire_1.1.0.ttl' # this will have to be passed as a variable in the function call
responses = './tests/eminentresponses.ttl'
validation_shapes = './tests/data_validation_tests/shapes/DatavalidationShapes.ttl'

validate_response_data(maturity_model=maturity_model, 
                        maturity_assessment=maturity_assessment,
                        responses= responses,
                        validation_shapes= validation_shapes,
                        )

