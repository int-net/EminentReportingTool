import plotly.express as px
import pandas 
import numpy as np
# from questionnaire_data_model import Answerset, Answer, Person, Organization, Question, FocusArea, Study, MaturityScore
# import questionnaire_processing_functions as qpf
import rdflib
import compute_maturiy_scores as cms

import generic_radar_plot as grp
import compute_lvl1_maturity_scores as l1cms

import plotly.graph_objects as go


def generate_report(maturity_model= str,maturity_assessment =str, study= rdflib.URIRef, responses = str, plot_kind= str, output_directory= str):
    # compute overall maturity scores
    overall_maturity_df = cms.compute_maturity_scores(maturity_model=maturity_model, 
                        maturity_assessment=maturity_assessment,
                        responses= responses,
                        study= study,
                        )
    
    # create and save plot

    overall_diagram = grp.generic_radar_plot(overall_maturity_df, plotKind= plotKind)
    filename = output_directory + str(study).split("#",1)[1]+'.svg'
    overall_diagram.savefig(filename, pad_inches= 2)

    l1cms.compute_lvl1_maturity_scores(maturity_model=maturity_model, 
                                       maturity_assessment=maturity_assessment, 
                                       study=study, 
                                       responses=responses, 
                                       plot_kind= plot_kind,
                                       output_folder=output_directory)








maturity_model='./tests/imm.ttl'
maturity_assessment = './tests/EminentQUestionnaire_1.0.0.ttl' # this will have to be passed as a variable in the function call
study = 'http://eminent.intnet.eu/maturity_assessment_results#cim-expert-group-2024'
responses = './tests/eminentresponses.ttl'
plotKind = 'maturity_avg' # this will have to be passed as a variable in the function call

generate_report(maturity_model=maturity_model, 
                        maturity_assessment=maturity_assessment,
                        responses= responses,
                        study= study,
                        plot_kind=plotKind,
                        output_directory= './tests/cim/'
                        )


generate_report(maturity_model=maturity_model, 
                        maturity_assessment=maturity_assessment,
                        responses= responses,
                        study= 'http://eminent.intnet.eu/maturity_assessment_results#SIF-2024',
                        plot_kind=plotKind,
                        output_directory= './tests/sif/'
                        )


