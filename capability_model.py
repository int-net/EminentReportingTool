from datetime import date, datetime, time, timedelta
from typing import List, Optional
from pydantic import BaseModel
from typing import Union
from questionnaire_data_model import Level1Capability, Level2Capability, Dimension, Level0Capability

# Community Facilitation
## Communty growth
d_1_1_p = Dimension(name= '1.1.p', description= 'process')
d_1_1_o = Dimension(name= '1.1.o', description= 'people and organization')
d_1_1_i = Dimension(name= '1.1.i', description= 'information')
d_1_1_r = Dimension(name= '1.1.r', description= 'resources')

c_1_1 = Level2Capability(name= 'c.1.1', 
                         description= "community growth",
                         hasDimensions= [
                             d_1_1_p,
                             d_1_1_o,
                             d_1_1_i,
                             d_1_1_r
                         ])

## knowledge retention
d_1_2_p = Dimension(name= '1.2.p', description= 'process')
d_1_2_o = Dimension(name= '1.2.o', description= 'people and organization')
d_1_2_i = Dimension(name= '1.2.i', description= 'information')
d_1_2_r = Dimension(name= '1.2.r', description= 'resources')

c_1_2 = Level2Capability(name= 'c.1.2', 
                         description= "knowledge retention",
                         hasDimensions= [
                             d_1_2_p,
                             d_1_2_o,
                             d_1_2_i,
                             d_1_2_r
                         ])


## Diversity of perspectives
d_1_3_p = Dimension(name= '1.3.p', description= 'process')
d_1_3_o = Dimension(name= '1.3.o', description= 'people and organization')
d_1_3_i = Dimension(name= '1.3.i', description= 'information')
d_1_3_r = Dimension(name= '1.3.r', description= 'resources')

c_1_3 = Level2Capability(name= 'c.1.1', 
                         description= "diversity of perspectives",
                         hasDimensions= [
                             d_1_3_p,
                             d_1_3_o,
                             d_1_3_i,
                             d_1_3_r
                         ])


## Comunity facilitation

c_1 = Level1Capability(
    name='c.1',
    description= 'community facilitation',
    hasSubCapability= [
        c_1_1,
        c_1_2,
        c_1_3
    ]
    )


# Technical Agreements
## integration profiles establishment
d_2_1_p = Dimension(name= '2.1.p', description= 'process')
d_2_1_o = Dimension(name= '2.1.o', description= 'people and organization')
d_2_1_i = Dimension(name= '2.1.i', description= 'information')
d_2_1_r = Dimension(name= '2.1.r', description= 'resources')

c_2_1 = Level2Capability(name= 'c.2.1', 
                         description= "integration profile establishment",
                         hasDimensions= [
                             d_2_1_p,
                             d_2_1_o,
                             d_2_1_i,
                             d_2_1_r
                         ])

## standardization

d_2_2_p = Dimension(name= '2.2.p', description= 'process')
d_2_2_o = Dimension(name= '2.2.o', description= 'people and organization')
d_2_2_i = Dimension(name= '2.2.i', description= 'information')
d_2_2_r = Dimension(name= '2.2.r', description= 'resources')

c_2_2 = Level2Capability(name= 'c.2.2', 
                         description= "standardization",
                         hasDimensions= [
                             d_2_2_p,
                             d_2_2_o,
                             d_2_2_i,
                             d_2_2_r
                         ])


## compliancce testing
d_2_3_p = Dimension(name= '2.3.p', description= 'process')
d_2_3_o = Dimension(name= '2.3.o', description= 'people and organization')
d_2_3_i = Dimension(name= '2.3.i', description= 'information')
d_2_3_r = Dimension(name= '2.3.r', description= 'resources')

c_2_3 = Level2Capability(name= 'c.2.3', 
                         description= "compliance testing",
                         hasDimensions= [
                             d_2_3_p,
                             d_2_3_o,
                             d_2_3_i,
                             d_2_3_r
                         ])

## technical agreements
c_2 = Level1Capability(
    name='c.2',
    description= 'technical agreements',
    hasSubCapability= [
        c_2_1,
        c_2_2,
        c_2_3
    ]
    )


# Facilitating implementation
## user base growth
d_3_1_p = Dimension(name= '3.1.p', description= 'process')
d_3_1_o = Dimension(name= '3.1.o', description= 'people and organization')
d_3_1_i = Dimension(name= '3.1.i', description= 'information')
d_3_1_r = Dimension(name= '3.1.r', description= 'resources')

c_3_1 = Level2Capability(name= 'c.3.1', 
                         description= "user base growth",
                         hasDimensions= [
                             d_3_1_p,
                             d_3_1_o,
                             d_3_1_i,
                             d_3_1_r
                         ])

## Operational Allignment
d_3_2_p = Dimension(name= '3.2.p', description= 'process')
d_3_2_o = Dimension(name= '3.2.o', description= 'people and organization')
d_3_2_i = Dimension(name= '3.2.i', description= 'information')
d_3_2_r = Dimension(name= '3.2.r', description= 'resources')

c_3_2 = Level2Capability(name= 'c.3.2', 
                         description= "operational allignment",
                         hasDimensions= [
                             d_3_2_p,
                             d_3_2_o,
                             d_3_2_i,
                             d_3_2_r
                         ])

## Tool, product and reference implementation development
d_3_3_p = Dimension(name= '3.3.p', description= 'process')
d_3_3_o = Dimension(name= '3.3.o', description= 'people and organization')
d_3_3_i = Dimension(name= '3.3.i', description= 'information')
d_3_3_r = Dimension(name= '3.3.r', description= 'resources')

c_3_3 = Level2Capability(name= 'c.3.3', 
                         description= "tool, product and reference implementation development",
                         hasDimensions= [
                             d_3_3_p,
                             d_3_3_o,
                             d_3_3_i,
                             d_3_3_r
                         ])

## market creation
d_3_4_p = Dimension(name= '3.4.p', description= 'process')
d_3_4_o = Dimension(name= '3.4.o', description= 'people and organization')
d_3_4_i = Dimension(name= '3.4.i', description= 'information')
d_3_4_r = Dimension(name= '3.4.r', description= 'resources')

c_3_4 = Level2Capability(name= 'c.3.4', 
                         description= "market creation",
                         hasDimensions= [
                             d_3_4_p,
                             d_3_4_o,
                             d_3_4_i,
                             d_3_4_r
                         ])


## facilitating implementation
c_3 = Level1Capability(
    name='c.2',
    description= 'facilitating implementation',
    hasSubCapability= [
        c_3_1,
        c_3_2,
        c_3_3,
        c_3_4
    ]
    )




# Whole Capability Model

c_0 = Level0Capability(
    name= 'c.0',
    description= 'interoperability',
    hasSubCapability= [
        c_1,
        c_2,
        c_3
    ]
    )