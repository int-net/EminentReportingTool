import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from textwrap import wrap  # Import the textwrap module
import matplotlib


def subcapability_radar_plot(maturitydf: pd.DataFrame, plotKind: str, capability) :
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_theta_offset(np.pi / 2)  # Rotate plot so that the first axis is at the top


    # Example data (replace with your actual data)
    if str(capability) == 'http://eminent.intnet.eu/maturity_model#CommunityFacilitation' :
        labels_outer = ['Growth', 'Retention', 'Diversity']
        labels_inner = ['process', 'organization', 'information', 'resources',
                        'process', 'organization', 'information', 'resources',
                        'process', 'organization', 'information', 'resources']
    elif str(capability) == 'http://eminent.intnet.eu/maturity_model#TechnicalAgreements' :
        labels_outer = ['Profiles', 'Standardization', 'Testing']
        labels_inner = ['process', 'organization', 'information', 'resources',
                        'process', 'organization', 'information', 'resources',
                        'process', 'organization', 'information', 'resources']
    elif str(capability) == 'http://eminent.intnet.eu/maturity_model#Implementation' :
        labels_outer = ['Users', 'Alignment', 'Development', 'Market']
        labels_inner = ['process', 'organization', 'information', 'resources',
                        'process', 'organization', 'information', 'resources',
                        'process', 'organization', 'information', 'resources',
                        'process', 'organization', 'information', 'resources']
    else: print(capability +' : '+ 'http://eminent.intnet.eu/maturity_model#CommunityFacilitation')

    # labels_inner = maturitydf['dimension'].tolist()

    if plotKind == 'maturity_median':
        data = maturitydf['maturity_median'].tolist()
    elif plotKind == 'maturity_mode':
        data = maturitydf['maturity_mode'].tolist()
    elif plotKind == 'maturity_avg':
        data = maturitydf['maturity_avg'].tolist()

    # Create evenly spaced angles
    theta = np.linspace(0, 2 * np.pi, len(labels_inner), endpoint=False)
    gamma = np.linspace(0, 2 * np.pi, len(labels_outer), endpoint=False)
    gamma = [x+ np.pi/4 for x in gamma]

    

    # Wrap long labels into multiple lines
    labels_inner_wrapped = [label.replace(' ', '\n') for label in labels_inner]
    labels_outer_wrapped = [label.replace(' ', '\n') for label in labels_outer]

    # Plot data
    ax.plot(theta, data, marker='o', label='Data')
    ax.fill(theta, data, alpha=0.3)

    # Set axis limits to always show the full range from 0 to 5
    ax.set_ylim(0, 5)


    # Add labels
    ax.set_xticks(theta)
    ax.set_xticklabels(labels_inner_wrapped)  # Use the wrapped labels
    ax.set_rlabel_position(1)  # Move radial labels away from the center

    # Add outer labels with increased radial distance
    for angle, label in zip(gamma, labels_outer_wrapped):
        ax.text(angle, 8.5, label, ha='center', va='center')  # Adjust the radial distance (e.g., 1.2)

    # Customize the plot as needed (e.g., title, legend, etc.)
    fig.tight_layout(pad=2)
    matplotlib.rcParams.update({'font.size': 10})

    #plt.show()

    return fig
