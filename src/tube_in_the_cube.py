from rdflib import Graph, Namespace, URIRef, Literal, BNode
from rdflib.namespace import FOAF, DCTERMS, DCAT, PROV, OWL, RDFS, RDF, XMLNS, SKOS, SOSA, ORG, SSN
import pandas as pd


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

responses = './tests/eminentresponses.ttl'
g= Graph()
g.parse(responses)

emar_ns= Namespace("http://eminent.intnet.eu/maturity_assessment_results#")
ema_ns = Namespace("http://eminent.intnet.eu/maturity_assessment#")
emm_ns = Namespace("http://eminent.intnet.eu/maturity_model#")
sgam_ns = Namespace("http://eminent.intnet.eu/sgam#")
g.bind("emar", emar_ns)
g.bind("ema", ema_ns)
g.bind("emm", emm_ns)
g.bind("sgam", sgam_ns)



study = 'http://eminent.intnet.eu/maturity_assessment_results#cim-expert-group-2024'


# query to find all scores associated with a specific study and a specific capability and/ordimension
tube_in_the_tube_query = """select distinct ?answerset ?person ?domain ?zone ?layer where {{
    ?answerset dcterms:isPartOf ?study . 
    ?answerset prov:wasQuotedFrom ?person .
    ?person ema:areaOfExpertise/ema:inDomain ?domain .
    ?person ema:areaOfExpertise/ema:inZone ?zone .
    ?person ema:areaOfExpertise/ema:onLayer ?layer .
    
}}"""

tube= g.query(tube_in_the_tube_query, initBindings={'study': URIRef(study)})
tube_df = pd.DataFrame(dict(
    person=[],
    domain=[],
    zone= [],
    layer=[])
    )

for t in tube :
    print(print(f" {t.person} : {t.domain} : {t.zone} : {t.layer}"))
    tube_df.loc[len(tube_df.index)] = [t.person, 
                                            t.domain.split("#", 1)[1], 
                                            t.zone.split("#", 1)[1],
                                            t.layer.split("#", 1)[1]
                                            ] 
    
# Sample data (replace with your actual data)

df = pd.DataFrame(tube_df)

# Count occurrences of each combination of keywords
keyword_counts = df.groupby(['domain', 'zone', 'layer']).size().reset_index(name='Count')

# Create a 3D cube plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Extract axes data
x = keyword_counts['domain']
y = keyword_counts['zone']
z = keyword_counts['layer']
counts = keyword_counts['Count']

# Convert categorical labels to numeric indices
x_unique = x.unique()
y_unique = y.unique()
z_unique = z.unique()
x_indices = [x_unique.tolist().index(val) for val in x]
y_indices = [y_unique.tolist().index(val) for val in y]
z_indices = [z_unique.tolist().index(val) for val in z]

# Plot the cube
ax.bar3d(x_indices, y_indices, z_indices, dx=0.5, dy=0.5, dz=counts, shade=True, cmap='coolwarm')

# Customize labels
ax.set_xticks(range(len(x_unique)))
ax.set_xticklabels(x_unique, rotation=45)
ax.set_yticks(range(len(y_unique)))
ax.set_yticklabels(y_unique, rotation=45)
ax.set_zticks(range(len(z_unique)))
ax.set_zticklabels(z_unique)

ax.set_xlabel('domain')
ax.set_ylabel('zone')
ax.set_zlabel('layer')
ax.set_title('3D Cube Heatmap of Keyword Combinations')

# Show the plot
plt.show()
