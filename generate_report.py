import plotly.express as px
import pandas 
import numpy as np
from questionnaire_data_model import Answerset, Answer, Person, Organization, Question, FocusArea, Study, MaturityScore
import questionnaire_processing_functions as qpf
from capability_model import c_0
import plotly.graph_objects as go

presetStudyID = 'int-net-test' # this will have to be passed as a variable in the function call
raw_data = 'int_net_questionnaire.xlsx' # this will have to be passed as a variable in the function call
plotKind = ['maturity_avg'] # this will have to be passed as a variable in the function call

# organize questionnaire data conform data model
questionnaire_data = qpf.parse_questionnaire_data(raw_data, presetStudyID)


# take questionaire data and maturity assessment and combine questionaire answers to assign maturity scores
# to each of the capabilities
report_data = qpf.createReportData(questionnaire_data, c_0)

# create different kinds of plots of the maturity scores

lvl_0_maturity_figure = qpf.lvl0_maturity_plot(report_data, plotKind)
lvl_0_maturity_figure.show()

level_1_maturity_figure = qpf.lvl1_maturity_plot(report_data, plotKind )
level_1_maturity_figure.show()

level_2_maturity_figure = qpf.lvl2_maturity_plot(report_data, plotKind)
level_2_maturity_figure.show()

for lvl2 in report_data.hasSubCapability :
    perCapabilityfigure = qpf.per_lvl2_maturity_plot(lvl2, plotKind)
    perCapabilityfigure.show()












    


















