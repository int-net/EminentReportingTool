import xml.etree.ElementTree as ET
import xml.etree.ElementTree as ET
from rdflib import Graph, Namespace, URIRef, Literal, BNode
from rdflib.namespace import FOAF, DCTERMS, DCAT, PROV, OWL, RDFS, RDF, XMLNS, SKOS, SOSA, ORG, SSN

from pydantic import BaseModel



class Dimension(BaseModel) :
    id : str
    label : str

def classify_characteristic(description = str):
    description = description.lower()

    capablities = [
        'Community Growth',
        'Knowledge Retentionn',
        'Diversity of Perspectives',
        'Integration Profile Establishment',
        'Standardization',
        'Compliance Testing',
        'User Base Growth',
        'Operational Alignment',
        'Tool, Product and Reference Implementation Development',
        'Market Creation'
    ]

    capability_key_map = {
        'Community Growth' : '1.1',
        'Knowledge Retentionn': '1.2',
        'Diversity of Perspectives' : '1.3',
        'Integration Profile Establishment': '2.1' ,
        'Standardization' : '2.2',
        'Compliance Testing': '2.3',
        'User Base Growth': '3.1',
        'Operational Alignment': '3.2',
        'Tool, Product and Reference Implementation Development': '3.3',
        'Market Creation' : '3.4'

    }

    dimensions = [
        'Process',
        'People and Organization',
        'Information',
        'Resources'
    ]

    dimension_telltales ={
        'process' : 'Process',
        'organization' : 'People and Organization',
        'Community meembers' : 'People and Organization',

    }

    dimension_key_map= {
        'Process' : 'p',
        'People and Organization' : "o",
        'Information': 'i',
        'Resources': 'r'
    }
    

    for c in capablities :
        for d in dimensions :
            if d.lower() in description and c.lower() in description:
                dim = Dimension(
                    id= capability_key_map[c] + '.' + dimension_key_map[d],
                    label= d
                )
                #print(dim.id)
                return dim
            else : return []





def survey_to_rdf(input_xml = str, version_number= str, output_rdf= str, serialization = 'ttl') :
    # Read the XML content from a file
    with open(input_xml, "r") as file:
        xml_content = file.read()
    # Parse the XML content
    root = ET.fromstring(xml_content)

    graph = Graph()
    emar_ns= Namespace("http://eminent.intnet.eu/maturity_assessment_results#")
    ema_ns = Namespace("http://eminent.intnet.eu/maturity_assessment#")
    emm_ns = Namespace("http://eminent.intnet.eu/maturity_model#")
    sgam_ns = Namespace("http://eminent.intnet.eu/sgam#")
    graph.bind("emar", emar_ns)
    graph.bind("ema", ema_ns)
    graph.bind("emm", emm_ns)
    graph.bind("sgam", sgam_ns)

    # these are questiona about the respondent, these should be ignored for this function as they are metadata and
    # handled separately
    whoAreYouQuestionIDs = [
        "a086bcf9-c9c9-8b58-a15a-0ab224d76de3",
        "0eb59ebe-5ffe-f965-78ca-852a40dc5ad7",
        "51194433-574f-111a-7b94-7f048ef4dd79",
        "0de32b34-c527-19d4-f6ca-76af0cd7b88b",
        "91cc8bfe-ee6e-c7e9-3462-b49021778bdc",
        "17d78fb6-586e-21f1-a958-93af40ed9c88",
        "9666d660-00fd-1a81-d1f7-717d39c6f5d7",
        "6d4606c8-31b7-5c8f-4463-5be353ea4f64",
        "b1acefb8-c977-c91a-b82c-6bee6a82a34d",
        "32457cf6-2f78-5a25-7691-cad210b83222", 
        "384d5d53-9820-c0d1-a1cb-e6960e158527"
    ]

    # instantiate questionnaireversion objects, it is assumed they are all versions of Eminent
    surveys= root.findall(".//Survey")
    for s in surveys :
        survey_uid = s.get('uid') # uuid of the survey
        survey_uri = ema_ns[survey_uid]
        survey_id = s.get('id') # eusurvey;s internal ID for the survey
        survey_name = s.get('alias') # the name of the survey
        graph.add((survey_uri, RDF.type, ema_ns.QuestionnaireVersion))
        graph.add((survey_uri, SKOS.prefLabel, Literal(survey_name)))
        graph.add((survey_uri, DCTERMS.identifier, Literal(survey_id)))
    # graph.add((survey_uri, DCAT.version, Literal('1.0.0')))
        graph.add((survey_uri, DCTERMS.isVersionOf, ema_ns.Eminent))
        graph.add((survey_uri, OWL.versionInfo, Literal(version_number)))

        questions = s.findall(".//Question")

        for q in questions :
            if q.get('type') != 'Line' and q.get('id') not in whoAreYouQuestionIDs:
                question_id= q.get('id')
                question_uri = ema_ns[question_id]
                question_identifier = q.text[:5] # used for dcterms identifier
                question_phrasing = Literal(q.text, datatype=RDF.HTML)
                question_type = Literal(q.get('type'), lang='en')
                dimension_uri = emm_ns[question_identifier]

                graph.add((question_uri, RDF.type, ema_ns.Question))
                graph.add((question_uri, DCTERMS.identifier, Literal(question_identifier)))
                graph.add((question_uri, ema_ns.phrasing, Literal(question_phrasing)))
                graph.add((question_uri, DCTERMS.isPartOf, survey_uri))
                graph.add((question_uri, ema_ns.question_type, question_type))
                graph.add((question_uri, ema_ns.measures, dimension_uri))
                


        ChoiceAnswers = root.findall("./Survey//Answer")

        # choice answers are actualy characteristics
        for ca in ChoiceAnswers :
            if len(ca.text)>19: # this is a hack to avoid the choice answers for section 1

                characteristic_id= ca.get('id')
                characteristic_uri= ema_ns[characteristic_id]
                characteristic_description = ca.text
                # related_dimension= classify_characteristic(ca.text)
                # print(related_dimension.id) #use the text to classify to which dimension it belongs
                # dimension_uri= emm_ns[related_dimension.id]
                graph.add((characteristic_uri, RDF.type, emm_ns.Characteristic))
                graph.add((characteristic_uri, SKOS.definition, Literal(characteristic_description)))
                #graph.add((characteristic_uri, DCTERMS.identifier, )))
                #graph.add((characteristic_uri, SSN.isPropertyOf, dimension_uri))

                

    graph.serialize(destination= output_rdf, format=serialization)

survey_to_rdf(input_xml="./tests/EUSurveyTestData.xml", version_number='1.0.0', serialization= 'ttl', output_rdf='./tests/EminentQUestionnaire_1.0.0.ttl')


def inrich_questionaire(input_xml= str, output_rdf=str) :
    return output_rdf


graph = Graph()

with open('./tests/EUSurveyTestData.xml', "r") as file:
    xml_content = file.read()

# Parse the XML content
root = ET.fromstring(xml_content)


emar_ns= Namespace("http://eminent.intnet.eu/maturity_assessment_results#")
ema_ns = Namespace("http://eminent.intnet.eu/maturity_assessment#")
emm_ns = Namespace("http://eminent.intnet.eu/maturity_model#")
sgam_ns = Namespace("http://eminent.intnet.eu/sgam#")
graph.bind("emar", emar_ns)
graph.bind("ema", ema_ns)
graph.bind("emm", emm_ns)
graph.bind("sgam", sgam_ns)

# these are questiona about the respondent, these should be ignored for this function as they are metadata and
# handled separately
whoAreYouQuestionIDs = [
    "a086bcf9-c9c9-8b58-a15a-0ab224d76de3",
    "0eb59ebe-5ffe-f965-78ca-852a40dc5ad7",
    "51194433-574f-111a-7b94-7f048ef4dd79",
    "0de32b34-c527-19d4-f6ca-76af0cd7b88b",
    "91cc8bfe-ee6e-c7e9-3462-b49021778bdc",
    "17d78fb6-586e-21f1-a958-93af40ed9c88",
    "9666d660-00fd-1a81-d1f7-717d39c6f5d7",
    "6d4606c8-31b7-5c8f-4463-5be353ea4f64",
    "b1acefb8-c977-c91a-b82c-6bee6a82a34d",
    "32457cf6-2f78-5a25-7691-cad210b83222", 
    "384d5d53-9820-c0d1-a1cb-e6960e158527"
]

# instantiate questionnaireversion objects, it is assumed they are all versions of Eminent
surveys= root.findall(".//Survey")
for s in surveys :
    survey_uid = s.get('uid') # uuid of the survey
    survey_uri = ema_ns[survey_uid]
    survey_id = s.get('id') # eusurvey;s internal ID for the survey
    survey_name = s.get('alias') # the name of the survey
    graph.add((survey_uri, RDF.type, ema_ns.QuestionnaireVersion))
    graph.add((survey_uri, SKOS.prefLabel, Literal(survey_name)))
    graph.add((survey_uri, DCTERMS.identifier, Literal(survey_id)))
# graph.add((survey_uri, DCAT.version, Literal('1.0.0')))
    graph.add((survey_uri, DCTERMS.isVersionOf, ema_ns.Eminent))

    questions = s.findall(".//Question")

    for q in questions :
        if q.get('type') != 'Line' and q.get('id') not in whoAreYouQuestionIDs:
            question_id= q.get('id')
            question_uri = ema_ns[question_id]
            question_identifier = q.text[:5] # used for dcterms identifier
            question_phrasing = Literal(q.text, datatype=RDF.HTML)
            question_type = Literal(q.get('type'), lang='en')
            dimension_uri = emm_ns[question_identifier]

            graph.add((question_uri, RDF.type, ema_ns.Question))
            graph.add((question_uri, DCTERMS.identifier, Literal(question_identifier)))
            graph.add((question_uri, ema_ns.phrasing, Literal(question_phrasing)))
            graph.add((question_uri, DCTERMS.isPartOf, survey_uri))
            graph.add((question_uri, ema_ns.question_type, question_type))
            graph.add((question_uri, ema_ns.measures, dimension_uri))
            graph.add((dimension_uri, RDF.type, emm_ns.Dimension))
            graph.add((dimension_uri, DCTERMS.identifier, Literal(question_identifier))) #dimensions and questions should share ID
            
            ChoiceAnswers = root.findall("./Survey//Answer")

    # choice answers are actualy characteristics
    for ca in ChoiceAnswers :
        if len(ca.text)>19: # this is a hack to avoid the choice answers for section 1

            characteristic_id= ca.get('id')
            characteristic_uri= ema_ns[characteristic_id]
            characteristic_description = ca.text
            # related_dimension= classify_characteristic(ca.text)
            # print(related_dimension.id) #use the text to classify to which dimension it belongs
            # dimension_uri= emm_ns[related_dimension.id]
            graph.add((characteristic_uri, RDF.type, emm_ns.Characteristic))
            graph.add((characteristic_uri, SKOS.definition, Literal(characteristic_description)))
            #graph.add((characteristic_uri, DCTERMS.identifier, )))
            #graph.add((characteristic_uri, SSN.isPropertyOf, dimension_uri))




graph.serialize(destination='./tests/EminentQuestionnaireEnrichment.ttl', format='ttl')
