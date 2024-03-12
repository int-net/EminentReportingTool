import plotly.express as px
import pandas 
import numpy as np
# from questionnaire_data_model import Answerset, Answer, Person, Organization, Question, FocusArea, Study, MaturityScore
# import questionnaire_processing_functions as qpf

import compute_maturiy_scores as cms

import plotly.graph_objects as go

maturity_model='./tests/imm.ttl'
maturity_assessment = './tests/EminentQUestionnaire_1.0.0.ttl' # this will have to be passed as a variable in the function call
study = 'http://eminent.intnet.eu/maturity_assessment_results#cim-expert-group-2024'
responses = './tests/eminentresponses.ttl'
plotKind = 'maturity_avg' # this will have to be passed as a variable in the function call

figure= cms.compute_maturity_scores(maturity_model=maturity_model, 
                        maturity_assessment=maturity_assessment,
                        responses= responses,
                        study= study,
                        plot_kind=plotKind
                        )

#figure.show()


figure= cms.compute_maturity_scores(maturity_model=maturity_model, 
                        maturity_assessment=maturity_assessment,
                        responses= responses,
                        study= 'http://eminent.intnet.eu/maturity_assessment_results#SIF-2024',
                        plot_kind=plotKind
                        )

figure.savefig('./tests/maturity_score.png', pad_inches= 2)













    


















