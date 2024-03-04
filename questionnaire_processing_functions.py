from answer_to_score import maturity_score_map
import pandas
from questionnaire_data_model import Answerset, Answer, Person, Organization, Question, FocusArea, Study, MaturityScore, Level0Capability, Level1Capability, Level2Capability
import statistics
import plotly.express as px
import plotly.graph_objects as go


# function that takes a string value of a multiple choice question and turns it into
# the corresponding score using maturity_score_map
def answer_to_score(strAnswer):
    strAnswer= strAnswer.rstrip(
          
    )
    if strAnswer in maturity_score_map:
        score = maturity_score_map[strAnswer]
    elif strAnswer == 'Unsure':
        score = "Unsure"
    else :
        score = 'Unknown'    
    
    return score

## function that takes excel dump of questionnaire answers (ms forms) and pareses and enriches it

def parse_questionnaire_data(file, presetStudyID) :
   

    raw_data = pandas.read_excel(file)
    raw_data = raw_data.replace('\n','')
    questionnaire_dataframe = pandas.DataFrame(raw_data)

    # store question phrases for later
    questionList = questionnaire_dataframe.columns

    # change labels from question phrasing to collumn number starting at 1

    questionnaire_dataframe.columns = range(1, len(questionnaire_dataframe.columns)+1) 

    # print(questionnaire_dataframe[10][1]) # row starts at zero


    # Parse the data and construct the model
    ## instantiate study

    thisStudy = Study(studyID= presetStudyID)
    answersets  = []

    # loop oover answersets and 
    for index, row in questionnaire_dataframe.iterrows() :
        testid= row[16]
        if testid == thisStudy.studyID :

            thisAnswerSet= Answerset(
                id= str(row[1]),
                resultTime= row[3],
                wasQuotedFrom= Person(
                    AreaOfExpertise= FocusArea(
                        inZone= [row[7]],
                        inDomain=[row[8]],
                        onLayer=[row[9]]
                        ),
                    actedOnBehalfOf= Organization(
                        size= row[11], 
                        description= row[10],
                        AreaOfExpertise= FocusArea(
                            inZone = [row[13]],
                            inDomain= [row[14]],
                            onLayer= [row[15]]
                            )
                        )
                    ),
                hasPart = [

                    ############################################
                    ####### Community growth ###################
                    ############################################

                        Answer(
                            hasSimpleAnswer = answer_to_score(row[17]),
                            usedProcedure= Question(
                                phrasing= str(questionList[16]),
                                questionID = '1.1.p'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[18]),
                            usedProcedure= Question(
                                phrasing= str(questionList[17]),
                                questionID = '1.1.o'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[19]),
                            usedProcedure= Question(
                                phrasing= str(questionList[18]),
                                questionID = '1.1.i'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[20]),
                            usedProcedure= Question(
                                phrasing= str(questionList[19]),
                                questionID = '1.1.r'
                            )
                        ),

                    ############################################
                    ####### knwoledge retention ################
                    ############################################

                        Answer(
                            hasSimpleAnswer = answer_to_score(row[21]),
                            usedProcedure= Question(
                                phrasing= str(questionList[20]),
                                questionID = '1.2.p'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[22]),
                            usedProcedure= Question(
                                phrasing= str(questionList[21]),
                                questionID = '1.2.o'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[23]),
                            usedProcedure= Question(
                                phrasing= str(questionList[22]),
                                questionID = '1.2.i'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[24]),
                            usedProcedure= Question(
                                phrasing= str(questionList[23]),
                                questionID = '1.2.r'
                            )
                        ),

                    ############################################
                    ####### Diversity of Perspectives ##########
                    ############################################

                        Answer(
                            hasSimpleAnswer = answer_to_score(row[25]),
                            usedProcedure= Question(
                                phrasing= str(questionList[24]),
                                questionID = '1.3.p'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[26]),
                            usedProcedure= Question(
                                phrasing= str(questionList[25]),
                                questionID = '1.3.o'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[27]),
                            usedProcedure= Question(
                                phrasing= str(questionList[26]),
                                questionID = '1.3.i'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[28]),
                            usedProcedure= Question(
                                phrasing= str(questionList[27]),
                                questionID = '1.3.r'
                            )
                        ),
                    ####################################################
                    ####### Integration Profile Establishment ##########
                    ####################################################

                        Answer(
                            hasSimpleAnswer = answer_to_score(row[29]),
                            usedProcedure= Question(
                                phrasing= str(questionList[28]),
                                questionID = '2.1.p'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[30]),
                            usedProcedure= Question(
                                phrasing= str(questionList[29]),
                                questionID = '2.1.o'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[31]),
                            usedProcedure= Question(
                                phrasing= str(questionList[30]),
                                questionID = '2.1.i'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[32]),
                            usedProcedure= Question(
                                phrasing= str(questionList[31]),
                                questionID = '2.1.r'
                            )
                        ),
                    ####################################################
                    ####### Standardizatiom ##########
                    ####################################################

                        Answer(
                            hasSimpleAnswer = answer_to_score(row[33]),
                            usedProcedure= Question(
                                phrasing= str(questionList[32]),
                                questionID = '2.2.p'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[34]),
                            usedProcedure= Question(
                                phrasing= str(questionList[33]),
                                questionID = '2.2.o'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[35]),
                            usedProcedure= Question(
                                phrasing= str(questionList[34]),
                                questionID = '2.2.i'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[36]),
                            usedProcedure= Question(
                                phrasing= str(questionList[35]),
                                questionID = '2.2.r'
                            )
                        ), 
                    #####################################
                    ####### Compliance Testing ##########
                    #####################################

                        Answer(
                            hasSimpleAnswer = answer_to_score(row[37]),
                            usedProcedure= Question(
                                phrasing= str(questionList[36]),
                                questionID = '2.3.p'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[38]),
                            usedProcedure= Question(
                                phrasing= str(questionList[37]),
                                questionID = '2.3.o'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[39]),
                            usedProcedure= Question(
                                phrasing= str(questionList[38]),
                                questionID = '2.3.i'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[40]),
                            usedProcedure= Question(
                                phrasing= str(questionList[39]),
                                questionID = '2.3.r'
                            )
                        ),
                    ###################################
                    ####### User Base Growth ##########
                    ###################################

                        Answer(
                            hasSimpleAnswer = answer_to_score(row[41]),
                            usedProcedure= Question(
                                phrasing= str(questionList[40]),
                                questionID = '3.1.p'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[42]),
                            usedProcedure= Question(
                                phrasing= str(questionList[41]),
                                questionID = '3.1.o'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[43]),
                            usedProcedure= Question(
                                phrasing= str(questionList[42]),
                                questionID = '3.1.i'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[44]),
                            usedProcedure= Question(
                                phrasing= str(questionList[43]),
                                questionID = '3.1.r'
                            )
                        ),      
                    #########################################
                    ####### Operational Allignment ##########
                    #########################################

                        Answer(
                            hasSimpleAnswer = answer_to_score(row[45]),
                            usedProcedure= Question(
                                phrasing= str(questionList[44]),
                                questionID = '3.2.p'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[46]),
                            usedProcedure= Question(
                                phrasing= str(questionList[45]),
                                questionID = '3.2.o'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[47]),
                            usedProcedure= Question(
                                phrasing= str(questionList[46]),
                                questionID = '3.2.i'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[48]),
                            usedProcedure= Question(
                                phrasing= str(questionList[47]),
                                questionID = '3.2.r'
                            )
                        ), 
                    #########################################################################
                    ####### Tool, Product and Reference Implementation Development ##########
                    #########################################################################

                        Answer(
                            hasSimpleAnswer = answer_to_score(row[49]),
                            usedProcedure= Question(
                                phrasing= str(questionList[48]),
                                questionID = '3.3.p'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[50]),
                            usedProcedure= Question(
                                phrasing= str(questionList[49]),
                                questionID = '3.3.o'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[51]),
                            usedProcedure= Question(
                                phrasing= str(questionList[50]),
                                questionID = '3.3.i'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[52]),
                            usedProcedure= Question(
                                phrasing= str(questionList[51]),
                                questionID = '3.3.r'
                            )
                        ),

                    ##################################
                    ####### Market Creation ##########
                    ##################################

                        Answer(
                            hasSimpleAnswer = answer_to_score(row[53]),
                            usedProcedure= Question(
                                phrasing= str(questionList[52]),
                                questionID = '3.4.p'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[54]),
                            usedProcedure= Question(
                                phrasing= str(questionList[53]),
                                questionID = '3.4.o'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[55]),
                            usedProcedure= Question(
                                phrasing= str(questionList[54]),
                                questionID = '3.4.i'
                            )
                        ),
                        Answer(
                            hasSimpleAnswer = answer_to_score(row[56]),
                            usedProcedure= Question(
                                phrasing= str(questionList[55]),
                                questionID = '3.4.r'
                            )
                        )                                                                                     
                        
                    ]    
            )

            answersets.append(thisAnswerSet)
    

    thisStudy.hasPart = answersets

    return thisStudy
    

def raw_data_to_MaturityScore( raw_data : list):
    numericValues= [elm for elm in raw_data if isinstance(elm, int)]

    if len(numericValues) > 1 :
                    averageScore= statistics.mean(numericValues)
                    standardDeviation= statistics.stdev(numericValues)
                    medianScore= statistics.median(numericValues)
                    modeScore= statistics.mode(numericValues)
    elif len(numericValues) == 1 :
                    averageScore= numericValues[0]
                    standardDeviation= 'Not Enough Data'
                    medianScore= numericValues[0]
                    modeScore= numericValues[0]
    else :
                    averageScore= 'Not Enough Data'
                    standardDeviation= 'Not Enough Data'
                    medianScore= 'Not Enough Data'
                    modeScore= 'Not Enough Data'

    numberOfUnsure = len([elm for elm in raw_data if elm =='Unsure'])
    numberOfUnknown = len([elm for elm in raw_data if elm =='Unknown'])

    tempmaturityScore = MaturityScore(
                    raw_data = raw_data,
                    averageScore= averageScore,
                    standardDeviation= standardDeviation,
                    medianScore= medianScore,
                    modeScore= modeScore,
                    totalAnswers= len(raw_data),
                    numberOfUnsure= numberOfUnsure,
                    numberOfUnknown= numberOfUnknown
                )
    
    return tempmaturityScore
     

# this function takes enriched questionnaire data in the form of a Study object and uses a template of a Level0Capability 
# and aggregates 
def createReportData(questionnaire_data : Study, c_0 : Level0Capability):
    for lvl1 in c_0.hasSubCapability :
        for lvl2 in lvl1.hasSubCapability :
            for dimension in lvl2.hasDimensions :
                dimension_name= dimension.name
                dimension_scores = []
                for answerset in questionnaire_data.hasPart :
                    for answer in answerset.hasPart :
                        if answer.usedProcedure.questionID == dimension_name :
                            dimension_scores.append(answer.hasSimpleAnswer)
                
            
                dimension.hasMaturityScore= raw_data_to_MaturityScore(dimension_scores)

    # aggregate dimension data to level2 capabilities            
    for l1 in c_0.hasSubCapability :
        for l2 in l1.hasSubCapability :
            cap2_raw_data= []
            for d in l2.hasDimensions :
                cap2_raw_data.extend(d.hasMaturityScore.raw_data)
            
            l2.hasMaturityScore = raw_data_to_MaturityScore(cap2_raw_data)

    
    for c in c_0.hasSubCapability :
        c_raw_data=[]
        for d in c.hasSubCapability :
              c_raw_data.extend(d.hasMaturityScore.raw_data)

        c.hasMaturityScore = raw_data_to_MaturityScore(c_raw_data)     


    interop_raw_data = []
    for cap in c_0.hasSubCapability :
          interop_raw_data.extend(cap.hasMaturityScore.raw_data)

    c_0.hasMaturityScore = raw_data_to_MaturityScore(interop_raw_data)

    return c_0


def generic_radar_plot(maturitydf : pandas.DataFrame, plotKind : [] ) :
    categories = maturitydf['capability']

    fig = go.Figure()

    if 'maturity_median' in plotKind :
        fig.add_trace(go.Scatterpolar(
            r=maturitydf['maturity_median'],
            theta=categories,
            fill='toself',
            name='Median score',
            line=dict(color="#fede29")
        ))
    if 'maturity_mode' in plotKind :    
        fig.add_trace(go.Scatterpolar(
            r=maturitydf['maturity_mode'],
            theta=categories,
            fill='toself',
            name='mode score',
            line=dict(color="#f19b01")
    
        ))
    if 'maturity_avg' in plotKind :
        fig.add_trace(go.Scatterpolar(
            r=maturitydf['maturity_avg'],
            theta=categories,
            fill='toself',
            name='Average score',
            line=dict(color="#04abdc")
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0, 5]
            )),
        showlegend=True
    )

    return fig


def lvl0_maturity_plot(report_data : Level0Capability, plotKind= []):

    #innittiate maturity data frame
    maturitydf = pandas.DataFrame(dict(
        capability=[],
        maturity_avg=[],
        maturity_median= [],
        maturity_mode=[])
        )

    # for sc in report_data.hasSubCapability :
    #     maturitydf.loc[len(maturitydf.index)] = [sc.description, sc.hasMaturityScore.averageScore] 

    for sc in report_data.hasSubCapability :
            maturitydf.loc[len(maturitydf.index)] = [sc.description, 
                                                        sc.hasMaturityScore.averageScore, 
                                                        sc.hasMaturityScore.medianScore,
                                                        sc.hasMaturityScore.modeScore
                                                        ] 
   
    fig = generic_radar_plot(maturitydf, plotKind )

    return fig


def lvl1_maturity_plot(report_data : Level0Capability, plotKind= []):

    #innittiate maturity data frame
    maturitydf = pandas.DataFrame(dict(
        capability=[],
        maturity_avg=[],
        maturity_median= [],
        maturity_mode=[])
        )

    # for sc in report_data.hasSubCapability :
    #     maturitydf.loc[len(maturitydf.index)] = [sc.description, sc.hasMaturityScore.averageScore] 

    for sc in report_data.hasSubCapability :
        for sc2 in sc.hasSubCapability :
                maturitydf.loc[len(maturitydf.index)] = [sc2.description, 
                                                         sc2.hasMaturityScore.averageScore, 
                                                         sc2.hasMaturityScore.medianScore,
                                                         sc2.hasMaturityScore.modeScore
                                                         ] 

    fig = generic_radar_plot(maturitydf, plotKind)
    return fig



def lvl2_maturity_plot(report_data : Level0Capability, plotKind : []):

    #innittiate maturity data frame
    maturitydf = pandas.DataFrame(dict(
        capability=[],
        maturity_avg=[],
        maturity_median= [],
        maturity_mode=[])
        )

    # for sc in report_data.hasSubCapability :
    #     maturitydf.loc[len(maturitydf.index)] = [sc.description, sc.hasMaturityScore.averageScore] 

    for sc in report_data.hasSubCapability :
        for sc2 in sc.hasSubCapability :
            for d in sc2.hasDimensions:
                maturitydf.loc[len(maturitydf.index)] = [d.name, 
                                                         d.hasMaturityScore.averageScore, 
                                                         d.hasMaturityScore.medianScore,
                                                         d.hasMaturityScore.modeScore
                                                         ] 

    
    fig = generic_radar_plot(maturitydf, plotKind )

    return fig


def per_lvl2_maturity_plot(report_data : Level1Capability, plotKind : []):

    #innittiate maturity data frame
    maturitydf = pandas.DataFrame(dict(
        capability=[],
        maturity_avg=[],
        maturity_median= [],
        maturity_mode=[])
        )

    # for sc in report_data.hasSubCapability :
    #     maturitydf.loc[len(maturitydf.index)] = [sc.description, sc.hasMaturityScore.averageScore] 

    for sc2 in report_data.hasSubCapability :
            for d in sc2.hasDimensions:
                maturitydf.loc[len(maturitydf.index)] = [d.name, 
                                                         d.hasMaturityScore.averageScore, 
                                                         d.hasMaturityScore.medianScore,
                                                         d.hasMaturityScore.modeScore
                                                         ] 

    fig = generic_radar_plot(maturitydf, plotKind)

    return fig
