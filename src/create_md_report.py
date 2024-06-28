from mdutils.mdutils import MdUtils
from mdutils import Html
import pandas as pd

def crete_md_report (study= str, 
                     output_dir= str, 
                     community= str,
                     maturity_df = pd.DataFrame,
                     community_df= pd.DataFrame,
                     agreements_df= pd.DataFrame,
                     implementation_df= pd.DataFrame) :
    study_name =str(study).split("#",1)[1]

    mdFile = MdUtils(file_name= output_dir+study_name+'_Maturity_Report', title= 'Results of the '+study_name+' maturity assessment')


    #########################################
    ############ Introduction ###############
    #########################################

    mdFile.new_paragraph("This report and its' contents were partially generated by the [EMINENT reporting tool](https://www.github.com/int-net/EminentReportingTool). "
                         "This tool has been developed as part of the int:net project. This work has received funding "
                         "from the European Union’s Horizon Europe research and innovation programme under grant "
                         "agreement N°101070086 (int:net).")
    
    mdFile.new_paragraph("This report is publisded under the [CC-BY-ND](https://www.creativecommons.org/cc-by-nd) license.")

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


    #########################################
    ############ Appendix A ###############
    #########################################

    mdFile.new_header(level = 1, title= "Appendix A: All results")

    mdFile.new_paragraph("This appendix contains all data analysis results from the maturity assessment in tabular from."
                         "as such, it goes beyounf the average score that has been used for the spider diagrams in"
                         "the main report. We find that the full analysis can give aditional insight into the degree"
                         "of consensus about the maturity of the interoperability community as reported by the respondents."
                         "Furthremore, this section goes a little deeper into the data quality of the data "
                         "that was used to create the report.")
    
    ##### descrtibing the the data
    mdFile.new_header(level = 2, title= "Describing the data in this appendix and guidance on how to interpret it")  

    mdFile.new_paragraph("This section describes the data that is presented below, what the different collumns mean, "
                         "and gives some guidance on how to interpret the data and look for (potentially) relevant patterns.")

    mdFile.new_paragraph("The data is presented across 4 tables, corresponding to the 4 spider diagrams included in"
                         " the main report. Each table has 7 collumns:")
    
    collumns = [
        "capability: The capability to which the scores apply. (only used in the first table)"
        "dimension: The combination of capability and dimension to which the scores apply. (only used used in the last 3 tables)",
        "maturity_avg: The mean maturity score based on the respnents' answers. Excluding the 'unsure' responses.",
        "maturity_median: The median maturity score, meaning 50 % of respondents selected an equal or lower score and 50 % selected an equal or higher score. Excluding the 'unsure' responses.",
        "maturity_mode: The maturity score that was selected the most by the respondents. Excluding the 'unsure' responses.",
        "number_of_answers: The number of people who responded to this question. If this number does not match the total number of respondents, this not all te data could be interpreted correctly.",
        "stddev: The standard deviation of the respondens' answers. Excluding the 'unsure' responses.",
        "number_of_unsure: The number of times respndents selected the 'unsure' option. "
    ]

    mdFile.new_paragraph("As a final note, all values have been rounded to 1 digit behind the decimal.")
    mdFile.new_list(collumns)

    mdFile.new_paragraph("When analysing the data, there are a couple of things a reader can look for to make sense of "
                         "the data. First and foremost, the reader should keep in mind that EMINENT is a tool for"
                         " learning, and not for judgement. To this end there is limited value to looking at the average score"
                         " to see if it is low or high. This only becomes a relevant excersize when one does a maturity tracking excersize and"
                         " wishes to see if there has been improvement.")
    
    mdFile.new_paragraph("During the tests that were executed as part of the int:net project, some best/good practices "
                         "were developed as to how to go about interpreting the data and developing a narrative that is meaningfule"
                         " to the interoperability community when it comes to finding area's to prioritize for improvement.")
    
    mdFile.new_paragraph("As mentioned before, it isn't particularly valuable to look at the value of particular scores, but it has "
                         "proven valuable to discuss particulartly high scores (compared to other scores) as well as particularly "
                         "low scores (again, compared to other scores). Looking for the high scores can help a community identify -or validate- its "
                         "strengths. First of all, these should be celebrated, but furthermore it can help to discuss what is going well in those area's and why."
                         " This can help the commuity formulate success stories as well as serve as inspiration for improvement in other areas."
                         " Identifying lower scores can help communities identify area's for growth and improvement. It should be noted though "
                         "that not every 'lower than average' score should immediately lead to action. Sometimes a low score comes about"
                         "simply because that area of interoperability is not very relevant (yet). For example, a newly formed community, "
                         "That is in the process of formulating the first version of the problem statement (profile establishment) or writing "
                         "their first standards, might not have a high score in testing yet. At this stage putting in a lot of effort to "
                         "become more mature at testing is simply not fruitful: you need to have a standard, and reference implementations "
                         "before there is anything to test in the first place. In this phase, it is probably better to put effort in becoming"
                         "more mature in those areas of interoperability that the community is corrently working on but strugling with."
                         " So when looking for area's of improvement, lower scores can be "
                         "an indicator, but finding the area's of improvement that need to be prioritized can only happen in discussion with"
                         " the community.")
    
    mdFile.new_paragraph("While the maturity_avg score is used within the report for the spider diagrams, it was found that, in adition "
                         "the maturity_mode (the most frequently selected answer), as well as the number_of_unsure and the stddev values"
                         "give important extra context.")
    
    mdFile.new_paragraph("A high stddev score indicates that there is disagreemnt among the respondents as to the performance of the "
                         "interoperability community in that particular capability/dimension combination. What is a high score? "
                         "Well, given that the possible range of values is between 0 and 5, a stddev of 2.5 would mean half the respondents"
                         " thinks the maturity is 0 and the other half thinks it is 5. So as a rule of thumb, a stddev <1 suggests a high degree "
                         "of consensus. A stddev between 1 and 1.5 indicates some disagreement and a stddev >1.5 suggests a high degree of "
                         "disagreement amongst respondents. In these situations it might be beneficial to organize a conversation with the respondents"
                         " to identify the origin of the disagreement. While respondents are encouraged to select 'unsure'  if they do not know "
                         " the answer, it is still possible that some respondents are close to that subject and select a different answer "
                         "than those who are more distant from it. ")
    
    mdFile.new_paragraph("When the stddev is high, it can be worht while to take the maturity_mode score into consideration "
                         "as another proxy for the actual score, since it is the answer that is most frequently selected.")
    
    mdFile.new_paragraph("Finally, the number_of_unsure values can give some insight into the degree to which members of the community are "
                         "aware of the efforts that the community makes within certain capabilities/dimensions. It is important to remember"
                         " that respondents are encouraged to select 'unsure' if they do not know the answer. This way, we can be more confident "
                         "that those who did select an answer, know what they are talking about and can speak from experience."
                         "In large communitities where different members specialize and focus their efforts on different "
                         "aspects of interoperability, it can be expected that not everyone is aware of everything that is happening. "
                         "For instance, it is very plausible - and potentially unproblematic- that a testing expert answers 'unsure' to some or all of the questions "
                         "about 'Userbase Growth'. In a smaller community, however, one would expect to see very few 'unsure' responses. "
                         "In general, when respondents have selected 'unsure' frequently, it is worthwhile for the community leadership to explore "
                         "improvements for the communication and knowledge exchange within the community.")
    
    mdFile.new_header(level=2, title="Maturity scores aggregated to the capability level")

    print_maturity_df= maturity_df.round(1)
    mdFile.write(print_maturity_df.to_markdown(index=False))


    mdFile.new_header(level=2, title="Maturity scores for Community Facilitation, aggregated to the dimension level" )
    
    print_community_df= community_df.round(1)
    mdFile.write(print_community_df.to_markdown(index=False))
    

    mdFile.new_header(level=2, title="Maturity scores for Technical Agreements, aggregated to the dimension level" )
    print_agreements_df= agreements_df.round(1)
    mdFile.write(print_agreements_df.to_markdown(index=False))


    mdFile.new_header(level=2, title="Maturity scores for Facilitating Implementation, aggregated to the dimension level" )
    
    print_implementation_df= implementation_df.round(1)
    mdFile.write(print_implementation_df.to_markdown(index=False))


    mdFile.new_table_of_contents(table_title='Contents', depth=2)
    mdFile.create_md_file()


# crete_md_report(study='http://eminent.intnet.eu/maturity_assessment_results#cim-expert-group-2024',
#                 output_dir='./tests/cim/', community= 'cim-expert-group')