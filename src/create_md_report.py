from mdutils.mdutils import MdUtils
from mdutils import Html

def crete_md_report (study= str, output_dir= str, community= str) :
    study_name =str(study).split("#",1)[1]

    mdFile = MdUtils(file_name= output_dir+study_name+'_Maturity_Report', title= 'Results of the '+study_name+' maturity assessment')


    #########################################
    ############ Introduction ###############
    #########################################

    mdFile.new_header(level=1, title ='Introduction')

    mdFile.new_paragraph("This report contains the result of the EMINENT Interoperability Maturty "
                         "Assessment that has been performed by members of the "+community+ " community. "
                         )
    
    mdFile.new_paragraph("The report is built up in the following way:")
    items = [
        "Respondent analysis: here the report discusses who has respondet to the questionnaire in terms of: ", 
        [
            "The area(s) of expertise of the respondents",
            "The area(s) of operation of the organizations the respondents represent."
        ],
        "Maturity Assessment: here the report discusses the maturity scores that "
        "follow from the responses that were received. This is done in 4 steps",
        [
            "First, the overal maturity scores for the 10 capabilities are discussed",
            "Then, for each of the 3 high level capabilities, the report will share"
             " the results down to the dimension level."
        ]
    ]
    mdFile.new_list(items=items)

    #########################################
    ############ Respondents ###############
    #########################################

    mdFile.new_header(level=1, title= "Respondent Analysis")

    mdFile.new_paragraph( "This section will give insights into who has responded to the questionnaire. "
                         "This will be done by looking at the area of expertise of the respondents, "
                         "as well as the area of operation of the organizations they represent. "
                         "Both the area of expertise and area of operation are expressed in terms of the the SGAM model")
    
    mdFile.new_header(level=2, title="Area of expertise of the respondents")

    mdFile.new_paragraph("Respondents were asked to indicate their area of expertise in terms of "
                         "the SGAM model. The results of the responses has been shown in the diagram below.")
    
    image_text= "Area of expertise of the respondents"
    path= study_name+"_respondents_tube_in_the_cube.png"

    mdFile.new_line(mdFile.new_inline_image(text=image_text, path=path))

    mdFile.new_header(level=2, title="Area of operation of organization")

    mdFile.new_paragraph("Respondents were asked to indicate their area of operation of the organization "
                         "they represent in terms of "
                         "the SGAM model. The results of the responses has been shown in the diagram below.")
    
    image_text= "Area of operation of the represented organizations"
    path= study_name+"_organizations_tube_in_the_cube.png"


    mdFile.new_line(mdFile.new_inline_image(text=image_text, path=path))

    #########################################
    ############ Maturity Assessmemt ###############
    #########################################
    mdFile.new_header(level=1, title= "Maturity Assessment")

    mdFile.new_paragraph("Respondents were asked to fill out a questionnaire in which each of the questions "
                         "targeted a different dimension of each of the 10 interoperability capabilities. "
                         "Respondents were asked to select the characteristic that best fit how they "
                         "experienced that dimension. The results were aggregated to dimension and "
                         "capability level. This section contains the aggregated result of that excersize.")

    mdFile.new_header(level = 2, title= "Overall Interoperability Maturity Assessment")

    mdFile.new_paragraph("This section discusses the overall picture that the maturity assessment has created "
                         "regarding the interoperabnility maturity of the "+community+" community. "
                         "The results can be found in the diagram below.")
    image_text= "overall Interoperability Maturity scores of the "+community+" community"
    path= study_name+".svg"
    mdFile.new_line(mdFile.new_inline_image(text=image_text, path=path))

    ########

    mdFile.new_header(level = 2, title= "In depth look at the maturity of the Community Facilitation Capability")

    mdFile.new_paragraph("This section discusses in more detail the maturity of the "+community+" community "
                         "with respect to the Community Facilitation Capability. The results can be found in the diagram below.")
    image_text= "Maturity scores in the Community Facilitation capability of the "+community+" community."
    path= study_name+"_CommunityFacilitation.svg"
    mdFile.new_line(mdFile.new_inline_image(text=image_text, path=path))

    ########

    mdFile.new_header(level = 2, title= "In depth look at the maturity of the Technical Agreements Capability")

    mdFile.new_paragraph("This section discusses in more detail the maturity of the "+community+" community "
                         "with respect to the Technical Agreements Capability. The results can be found in the diagram below.")
    image_text= "Maturity scores in the Technical Agreements capability of the "+community+" community."
    path= study_name+"_TechnicalAgreements.svg"
    mdFile.new_line(mdFile.new_inline_image(text=image_text, path=path))

      ########

    mdFile.new_header(level = 2, title= "In depth look at the maturity of the Implementation Capability")

    mdFile.new_paragraph("This section discusses in more detail the maturity of the "+community+" community "
                         "with respect to the Implementation Capability. The results can be found in the diagram below.")
    image_text= "Maturity scores in the Implementation  capability of the "+community+" community."
    path= study_name+"_Implementation.svg"
    mdFile.new_line(mdFile.new_inline_image(text=image_text, path=path))



    mdFile.new_table_of_contents(table_title='Contents', depth=2)
    mdFile.create_md_file()


crete_md_report(study='http://eminent.intnet.eu/maturity_assessment_results#SIF-2024',
                output_dir='./tests/sif/', community= 'SIF')