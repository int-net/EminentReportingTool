from datetime import date, datetime, time, timedelta
from typing import List, Optional
from pydantic import BaseModel
from typing import Union

# define data objects

# FocusArea uses the layers, domains and zones of the SGAM 
# framework to indcate the area of expertise of an individual 
# or the area of operation of an organization

class FocusArea(BaseModel) :
    inZone : List[str]
    inDomain : List[str]
    onLayer : List[str]

#     

class Organization(BaseModel) :
   size: str
   description : str # either q5 or q6
   AreaOfExpertise : Optional[FocusArea] = None

class Person(BaseModel) :
    AreaOfExpertise : FocusArea
    actedOnBehalfOf : Organization

class Question(BaseModel) : 
   phrasing : str
   questionID : Optional[str] = None

class Answer(BaseModel) :
   hasSimpleAnswer : Union[int, str]
   usedProcedure : Question

class Answerset(BaseModel) :
    id : str
    resultTime: Optional[datetime] = None
    wasQuotedFrom : Person
    hasPart : List[Answer]


class Study(BaseModel) :
    studyID : str 
    hasPart : List[Answerset] = []

#################################################################################################
### the part below is semantically ugly. It combines the notion of capabilities with          ###
### the notions of measurements of those capabilities  into single objects. this requires     ###
### careful evaluation when we start to trace maturity scores over time                       ###
#################################################################################################

class MaturityScore(BaseModel) :
    resultTime : Optional[datetime] = None
    raw_data : List[Union[str, int]]= []
    averageScore : Union[str, float]
    standardDeviation : Union[str, float]
    medianScore : Union[str, float]
    modeScore : Union[str, float]
    totalAnswers : int
    numberOfUnsure : int
    # unknown means the answer that was given was not recognized as one of the multiple choice answers, 
    # this indicates a problem with the data collection process or the data interpretation process 
    # in the sense that they are not alligned
    numberOfUnknown : int 


class Dimension(BaseModel) : # this is a dimension in the context of a capability
    name : str # for simplicity and navigability, this str matches the questionID
    description : str
    hasMaturityScore : Optional[MaturityScore] = None


class Level2Capability(BaseModel) :
    name : str
    description : str
    hasDimensions : List[Dimension] = []
    hasMaturityScore : Optional[MaturityScore] = None

class Level1Capability(BaseModel) :
    name : str
    description : str
    hasSubCapability : List[Level2Capability] = []
    hasMaturityScore : Optional[MaturityScore] = None

class Level0Capability(BaseModel) :
    name : str
    description : str
    hasSubCapability : List [Level1Capability] = []
    hasMaturityScore : Optional[MaturityScore] = None