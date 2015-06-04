#!/usr/bin/env python

#
# Generated Wed Jun  3 16:51:11 2015 by generateDS.py version 2.16a.
#
# Command line options:
#   ('-o', 'clinvar_api.py')
#   ('-s', 'clinvar_sub.py')
#   ('--super', 'clinvar_api')
#
# Command line arguments:
#   clinvar_public.xsd
#
# Command line:
#   ../../generateDS.py -o "clinvar_api.py" -s "clinvar_sub.py" --super="clinvar_api" clinvar_public.xsd
#
# Current working directory (os.getcwd()):
#   Code
#

import sys
from lxml import etree as etree_

import clinvar_api as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

# ExternalEncoding = 'ascii'
ExternalEncoding = 'utf-8'

#
# Data representation classes
#


class XrefTypeSub(supermod.XrefType):
    def __init__(self, URL=None, Type=None, DB=None, ID=None, Status='current'):
        super(XrefTypeSub, self).__init__(URL, Type, DB, ID, Status, )
supermod.XrefType.subclass = XrefTypeSub
# end class XrefTypeSub


class CitationTypeSub(supermod.CitationType):
    def __init__(self, Abbrev=None, Type=None, ID=None, URL=None, CitationText=None):
        super(CitationTypeSub, self).__init__(Abbrev, Type, ID, URL, CitationText, )
supermod.CitationType.subclass = CitationTypeSub
# end class CitationTypeSub


class CommentTypeSub(supermod.CommentType):
    def __init__(self, Type=None, DataSource=None, valueOf_=None):
        super(CommentTypeSub, self).__init__(Type, DataSource, valueOf_, )
supermod.CommentType.subclass = CommentTypeSub
# end class CommentTypeSub


class DataSourceTypeSub(supermod.DataSourceType):
    def __init__(self, SourceType=None, DataSource=None, ID=None):
        super(DataSourceTypeSub, self).__init__(SourceType, DataSource, ID, )
supermod.DataSourceType.subclass = DataSourceTypeSub
# end class DataSourceTypeSub


class PublicSetTypeSub(supermod.PublicSetType):
    def __init__(self, ID=None, DateLastUpdated=None, RecordStatus='current', ReplacedBy=None, Replaces=None, Title=None, ReferenceClinVarAssertion=None, ClinVarAssertion=None):
        super(PublicSetTypeSub, self).__init__(ID, DateLastUpdated, RecordStatus, ReplacedBy, Replaces, Title, ReferenceClinVarAssertion, ClinVarAssertion, )
supermod.PublicSetType.subclass = PublicSetTypeSub
# end class PublicSetTypeSub


class ReleaseTypeSub(supermod.ReleaseType):
    def __init__(self, Type=None, Dated=None, ClinVarSet=None):
        super(ReleaseTypeSub, self).__init__(Type, Dated, ClinVarSet, )
supermod.ReleaseType.subclass = ReleaseTypeSub
# end class ReleaseTypeSub


class MeasureTraitTypeSub(supermod.MeasureTraitType):
    def __init__(self, ID=None, SubmissionName=None, SubmissionDate=None, DateLastUpdated=None, DateCreated=None, ClinVarSubmissionID=None, ClinVarAccession=None, AdditionalSubmitters=None, RecordStatus='current', ClinicalSignificance=None, CustomAssertionScore=None, Assertion=None, ExternalID=None, AttributeSet=None, ObservedIn=None, MeasureSet=None, TraitSet=None, Citation=None, StudyName=None, StudyDescription=None, Comment=None):
        super(MeasureTraitTypeSub, self).__init__(ID, SubmissionName, SubmissionDate, DateLastUpdated, DateCreated, ClinVarSubmissionID, ClinVarAccession, AdditionalSubmitters, RecordStatus, ClinicalSignificance, CustomAssertionScore, Assertion, ExternalID, AttributeSet, ObservedIn, MeasureSet, TraitSet, Citation, StudyName, StudyDescription, Comment, )
supermod.MeasureTraitType.subclass = MeasureTraitTypeSub
# end class MeasureTraitTypeSub


class ReferenceAssertionTypeSub(supermod.ReferenceAssertionType):
    def __init__(self, ID=None, SubmissionDate=None, DateLastUpdated=None, DateCreated=None, ClinVarAccession=None, RecordStatus='current', ClinicalSignificance=None, Assertion=None, ExternalID=None, AttributeSet=None, ObservedIn=None, MeasureSet=None, TraitSet=None, Citation=None, Comment=None):
        super(ReferenceAssertionTypeSub, self).__init__(ID, SubmissionDate, DateLastUpdated, DateCreated, ClinVarAccession, RecordStatus, ClinicalSignificance, Assertion, ExternalID, AttributeSet, ObservedIn, MeasureSet, TraitSet, Citation, Comment, )
supermod.ReferenceAssertionType.subclass = ReferenceAssertionTypeSub
# end class ReferenceAssertionTypeSub


class MeasureSetTypeSub(supermod.MeasureSetType):
    def __init__(self, Type=None, ID=None, Measure=None, Name=None, Symbol=None, AttributeSet=None, Citation=None, XRef=None, Comment=None):
        super(MeasureSetTypeSub, self).__init__(Type, ID, Measure, Name, Symbol, AttributeSet, Citation, XRef, Comment, )
supermod.MeasureSetType.subclass = MeasureSetTypeSub
# end class MeasureSetTypeSub


class TraitSetTypeSub(supermod.TraitSetType):
    def __init__(self, Type=None, ID=None, Trait=None, Name=None, Symbol=None, AttributeSet=None, Citation=None, XRef=None, Comment=None):
        super(TraitSetTypeSub, self).__init__(Type, ID, Trait, Name, Symbol, AttributeSet, Citation, XRef, Comment, )
supermod.TraitSetType.subclass = TraitSetTypeSub
# end class TraitSetTypeSub


class TraitTypeSub(supermod.TraitType):
    def __init__(self, Type=None, ID=None, Name=None, Symbol=None, AttributeSet=None, TraitRelationship=None, Citation=None, XRef=None, Comment=None, Source=None):
        super(TraitTypeSub, self).__init__(Type, ID, Name, Symbol, AttributeSet, TraitRelationship, Citation, XRef, Comment, Source, )
supermod.TraitType.subclass = TraitTypeSub
# end class TraitTypeSub


class AttributeTypeSub(supermod.AttributeType):
    def __init__(self, integerValue=None, dateValue=None, valueOf_=None, extensiontype_=None):
        super(AttributeTypeSub, self).__init__(integerValue, dateValue, valueOf_, extensiontype_, )
supermod.AttributeType.subclass = AttributeTypeSub
# end class AttributeTypeSub


class SetElementSetTypeSub(supermod.SetElementSetType):
    def __init__(self, ElementValue=None, Citation=None, XRef=None, Comment=None):
        super(SetElementSetTypeSub, self).__init__(ElementValue, Citation, XRef, Comment, )
supermod.SetElementSetType.subclass = SetElementSetTypeSub
# end class SetElementSetTypeSub


class SoftwareSetSub(supermod.SoftwareSet):
    def __init__(self, version=None, name=None, purpose=None):
        super(SoftwareSetSub, self).__init__(version, name, purpose, )
supermod.SoftwareSet.subclass = SoftwareSetSub
# end class SoftwareSetSub


class SubmitterTypeSub(supermod.SubmitterType):
    def __init__(self, category=None, OrgID=None, SubmitterName=None, primary=None, valueOf_=None):
        super(SubmitterTypeSub, self).__init__(category, OrgID, SubmitterName, primary, valueOf_, )
supermod.SubmitterType.subclass = SubmitterTypeSub
# end class SubmitterTypeSub


class MethodTypeSub(supermod.MethodType):
    def __init__(self, NamePlatform=None, TypePlatform=None, Purpose=None, ResultType=None, MinReported=None, MaxReported=None, ReferenceStandard=None, Citation=None, XRef=None, Description=None, Software=None, SourceType=None, MethodType_member=None, MethodAttribute=None, MethodResult=None, extensiontype_=None):
        super(MethodTypeSub, self).__init__(NamePlatform, TypePlatform, Purpose, ResultType, MinReported, MaxReported, ReferenceStandard, Citation, XRef, Description, Software, SourceType, MethodType_member, MethodAttribute, MethodResult, extensiontype_, )
supermod.MethodType.subclass = MethodTypeSub
# end class MethodTypeSub


class ObservationSetSub(supermod.ObservationSet):
    def __init__(self, Sample=None, Method=None, ObservedData=None, Co_occurrenceSet=None, TraitSet=None, Citation=None, XRef=None, Comment=None):
        super(ObservationSetSub, self).__init__(Sample, Method, ObservedData, Co_occurrenceSet, TraitSet, Citation, XRef, Comment, )
supermod.ObservationSet.subclass = ObservationSetSub
# end class ObservationSetSub


class FamilyInfoSub(supermod.FamilyInfo):
    def __init__(self, PedigreeID=None, NumFamiliesWithVariant=None, NumFamiliesWithSegregationObserved=None, NumFamilies=None, FamilyHistory=None):
        super(FamilyInfoSub, self).__init__(PedigreeID, NumFamiliesWithVariant, NumFamiliesWithSegregationObserved, NumFamilies, FamilyHistory, )
supermod.FamilyInfo.subclass = FamilyInfoSub
# end class FamilyInfoSub


class SampleTypeSub(supermod.SampleType):
    def __init__(self, SampleDescription=None, Origin=None, Ethnicity=None, GeographicOrigin=None, Tissue=None, CellLine=None, Species=None, Age=None, Strain=None, AffectedStatus=None, NumberTested=None, NumberMales=None, NumberFemales=None, NumberChrTested=None, Gender=None, FamilyData=None, Proband=None, Indication=None, Citation=None, XRef=None, Comment=None, SourceType=None):
        super(SampleTypeSub, self).__init__(SampleDescription, Origin, Ethnicity, GeographicOrigin, Tissue, CellLine, Species, Age, Strain, AffectedStatus, NumberTested, NumberMales, NumberFemales, NumberChrTested, Gender, FamilyData, Proband, Indication, Citation, XRef, Comment, SourceType, )
supermod.SampleType.subclass = SampleTypeSub
# end class SampleTypeSub


class Co_occurrenceTypeSub(supermod.Co_occurrenceType):
    def __init__(self, Zygosity=None, AlleleDescSet=None, Count=None):
        super(Co_occurrenceTypeSub, self).__init__(Zygosity, AlleleDescSet, Count, )
supermod.Co_occurrenceType.subclass = Co_occurrenceTypeSub
# end class Co_occurrenceTypeSub


class ClinicalSignificanceTypeSub(supermod.ClinicalSignificanceType):
    def __init__(self, DateLastEvaluated=None, ReviewStatus=None, Description=None, Explanation=None, XRef=None, Citation=None, Comment=None):
        super(ClinicalSignificanceTypeSub, self).__init__(DateLastEvaluated, ReviewStatus, Description, Explanation, XRef, Citation, Comment, )
supermod.ClinicalSignificanceType.subclass = ClinicalSignificanceTypeSub
# end class ClinicalSignificanceTypeSub


class ClinicalSignificanceTypeSCVSub(supermod.ClinicalSignificanceTypeSCV):
    def __init__(self, DateLastEvaluated=None, ReviewStatus=None, Description=None, Explanation=None, XRef=None, Citation=None, Comment=None):
        super(ClinicalSignificanceTypeSCVSub, self).__init__(DateLastEvaluated, ReviewStatus, Description, Explanation, XRef, Citation, Comment, )
supermod.ClinicalSignificanceTypeSCV.subclass = ClinicalSignificanceTypeSCVSub
# end class ClinicalSignificanceTypeSCVSub


class AlleleDescTypeSub(supermod.AlleleDescType):
    def __init__(self, Name=None, RelativeOrientation=None, Zygosity=None, ClinicalSignificance=None):
        super(AlleleDescTypeSub, self).__init__(Name, RelativeOrientation, Zygosity, ClinicalSignificance, )
supermod.AlleleDescType.subclass = AlleleDescTypeSub
# end class AlleleDescTypeSub


class IndicationTypeSub(supermod.IndicationType):
    def __init__(self, Type=None, ID=None, Trait=None, Name=None, Symbol=None, AttributeSet=None, Citation=None, XRef=None, Comment=None):
        super(IndicationTypeSub, self).__init__(Type, ID, Trait, Name, Symbol, AttributeSet, Citation, XRef, Comment, )
supermod.IndicationType.subclass = IndicationTypeSub
# end class IndicationTypeSub


class AssertionTypeRCVSub(supermod.AssertionTypeRCV):
    def __init__(self, Type=None):
        super(AssertionTypeRCVSub, self).__init__(Type, )
supermod.AssertionTypeRCV.subclass = AssertionTypeRCVSub
# end class AssertionTypeRCVSub


class AssertionTypeSCVSub(supermod.AssertionTypeSCV):
    def __init__(self, Type=None):
        super(AssertionTypeSCVSub, self).__init__(Type, )
supermod.AssertionTypeSCV.subclass = AssertionTypeSCVSub
# end class AssertionTypeSCVSub


class SequenceLocationTypeSub(supermod.SequenceLocationType):
    def __init__(self, outerStart=None, Assembly=None, display_stop=None, start=None, stop=None, AssemblyAccessionVersion=None, Accession=None, innerStart=None, outerStop=None, innerStop=None, Chr=None, variantLength=None, display_start=None, AssemblyStatus=None, referenceAllele=None, alternateAllele=None, Strand=None):
        super(SequenceLocationTypeSub, self).__init__(outerStart, Assembly, display_stop, start, stop, AssemblyAccessionVersion, Accession, innerStart, outerStop, innerStop, Chr, variantLength, display_start, AssemblyStatus, referenceAllele, alternateAllele, Strand, )
supermod.SequenceLocationType.subclass = SequenceLocationTypeSub
# end class SequenceLocationTypeSub


class IDTypeSub(supermod.IDType):
    def __init__(self, Source=None, valueOf_=None):
        super(IDTypeSub, self).__init__(Source, valueOf_, )
supermod.IDType.subclass = IDTypeSub
# end class IDTypeSub


class ClinVarSubmissionIDTypeSub(supermod.ClinVarSubmissionIDType):
    def __init__(self, submitter=None, submitterDate=None, localKeyIsSubmitted=None, localKey=None, title=None):
        super(ClinVarSubmissionIDTypeSub, self).__init__(submitter, submitterDate, localKeyIsSubmitted, localKey, title, )
supermod.ClinVarSubmissionIDType.subclass = ClinVarSubmissionIDTypeSub
# end class ClinVarSubmissionIDTypeSub


class ClinVarAccessionTypeSub(supermod.ClinVarAccessionType):
    def __init__(self, Acc=None, OrgID=None, DateUpdated=None, Version=None, Type=None):
        super(ClinVarAccessionTypeSub, self).__init__(Acc, OrgID, DateUpdated, Version, Type, )
supermod.ClinVarAccessionType.subclass = ClinVarAccessionTypeSub
# end class ClinVarAccessionTypeSub


class AdditionalSubmittersTypeSub(supermod.AdditionalSubmittersType):
    def __init__(self, SubmitterDescription=None):
        super(AdditionalSubmittersTypeSub, self).__init__(SubmitterDescription, )
supermod.AdditionalSubmittersType.subclass = AdditionalSubmittersTypeSub
# end class AdditionalSubmittersTypeSub


class CustomAssertionScoreTypeSub(supermod.CustomAssertionScoreType):
    def __init__(self, Type=None, Value=None, Citation=None, XRef=None):
        super(CustomAssertionScoreTypeSub, self).__init__(Type, Value, Citation, XRef, )
supermod.CustomAssertionScoreType.subclass = CustomAssertionScoreTypeSub
# end class CustomAssertionScoreTypeSub


class AttributeSetTypeSub(supermod.AttributeSetType):
    def __init__(self, Attribute=None, Citation=None, XRef=None, Comment=None):
        super(AttributeSetTypeSub, self).__init__(Attribute, Citation, XRef, Comment, )
supermod.AttributeSetType.subclass = AttributeSetTypeSub
# end class AttributeSetTypeSub


class AttributeType2Sub(supermod.AttributeType2):
    def __init__(self, integerValue=None, dateValue=None, Type=None, valueOf_=None):
        super(AttributeType2Sub, self).__init__(integerValue, dateValue, Type, valueOf_, )
supermod.AttributeType2.subclass = AttributeType2Sub
# end class AttributeType2Sub


class ClinVarAccessionType3Sub(supermod.ClinVarAccessionType3):
    def __init__(self, Acc=None, DateUpdated=None, Version=None, Type=None):
        super(ClinVarAccessionType3Sub, self).__init__(Acc, DateUpdated, Version, Type, )
supermod.ClinVarAccessionType3.subclass = ClinVarAccessionType3Sub
# end class ClinVarAccessionType3Sub


class AttributeSetType5Sub(supermod.AttributeSetType5):
    def __init__(self, Attribute=None, Citation=None, XRef=None, Comment=None):
        super(AttributeSetType5Sub, self).__init__(Attribute, Citation, XRef, Comment, )
supermod.AttributeSetType5.subclass = AttributeSetType5Sub
# end class AttributeSetType5Sub


class AttributeType6Sub(supermod.AttributeType6):
    def __init__(self, integerValue=None, dateValue=None, Type=None, valueOf_=None):
        super(AttributeType6Sub, self).__init__(integerValue, dateValue, Type, valueOf_, )
supermod.AttributeType6.subclass = AttributeType6Sub
# end class AttributeType6Sub


class MeasureTypeSub(supermod.MeasureType):
    def __init__(self, Type=None, ID=None, Name=None, Symbol=None, AttributeSet=None, CytogeneticLocation=None, SequenceLocation=None, MeasureRelationship=None, Citation=None, XRef=None, Comment=None, Source=None):
        super(MeasureTypeSub, self).__init__(Type, ID, Name, Symbol, AttributeSet, CytogeneticLocation, SequenceLocation, MeasureRelationship, Citation, XRef, Comment, Source, )
supermod.MeasureType.subclass = MeasureTypeSub
# end class MeasureTypeSub


class AttributeSetType7Sub(supermod.AttributeSetType7):
    def __init__(self, Attribute=None, Citation=None, XRef=None, Comment=None):
        super(AttributeSetType7Sub, self).__init__(Attribute, Citation, XRef, Comment, )
supermod.AttributeSetType7.subclass = AttributeSetType7Sub
# end class AttributeSetType7Sub


class AttributeType8Sub(supermod.AttributeType8):
    def __init__(self, integerValue=None, dateValue=None, Type=None, Change=None, valueOf_=None):
        super(AttributeType8Sub, self).__init__(integerValue, dateValue, Type, Change, valueOf_, )
supermod.AttributeType8.subclass = AttributeType8Sub
# end class AttributeType8Sub


class MeasureRelationshipTypeSub(supermod.MeasureRelationshipType):
    def __init__(self, Type=None, ID=None, Name=None, Symbol=None, AttributeSet=None, SequenceLocation=None, Citation=None, XRef=None, Comment=None):
        super(MeasureRelationshipTypeSub, self).__init__(Type, ID, Name, Symbol, AttributeSet, SequenceLocation, Citation, XRef, Comment, )
supermod.MeasureRelationshipType.subclass = MeasureRelationshipTypeSub
# end class MeasureRelationshipTypeSub


class AttributeSetType9Sub(supermod.AttributeSetType9):
    def __init__(self, Attribute=None, Citation=None):
        super(AttributeSetType9Sub, self).__init__(Attribute, Citation, )
supermod.AttributeSetType9.subclass = AttributeSetType9Sub
# end class AttributeSetType9Sub


class AttributeType10Sub(supermod.AttributeType10):
    def __init__(self, integerValue=None, dateValue=None, Type=None, valueOf_=None):
        super(AttributeType10Sub, self).__init__(integerValue, dateValue, Type, valueOf_, )
supermod.AttributeType10.subclass = AttributeType10Sub
# end class AttributeType10Sub


class AttributeSetType11Sub(supermod.AttributeSetType11):
    def __init__(self, Attribute=None, Citation=None, XRef=None, Comment=None):
        super(AttributeSetType11Sub, self).__init__(Attribute, Citation, XRef, Comment, )
supermod.AttributeSetType11.subclass = AttributeSetType11Sub
# end class AttributeSetType11Sub


class AttributeType12Sub(supermod.AttributeType12):
    def __init__(self, integerValue=None, dateValue=None, Type=None, Change=None, valueOf_=None):
        super(AttributeType12Sub, self).__init__(integerValue, dateValue, Type, Change, valueOf_, )
supermod.AttributeType12.subclass = AttributeType12Sub
# end class AttributeType12Sub


class AttributeSetType13Sub(supermod.AttributeSetType13):
    def __init__(self, Attribute=None, Citation=None, XRef=None, Comment=None):
        super(AttributeSetType13Sub, self).__init__(Attribute, Citation, XRef, Comment, )
supermod.AttributeSetType13.subclass = AttributeSetType13Sub
# end class AttributeSetType13Sub


class AttributeType14Sub(supermod.AttributeType14):
    def __init__(self, integerValue=None, dateValue=None, Type=None, valueOf_=None):
        super(AttributeType14Sub, self).__init__(integerValue, dateValue, Type, valueOf_, )
supermod.AttributeType14.subclass = AttributeType14Sub
# end class AttributeType14Sub


class AttributeSetType15Sub(supermod.AttributeSetType15):
    def __init__(self, Attribute=None, Citation=None, XRef=None, Comment=None):
        super(AttributeSetType15Sub, self).__init__(Attribute, Citation, XRef, Comment, )
supermod.AttributeSetType15.subclass = AttributeSetType15Sub
# end class AttributeSetType15Sub


class AttributeType16Sub(supermod.AttributeType16):
    def __init__(self, integerValue=None, dateValue=None, Type=None, valueOf_=None):
        super(AttributeType16Sub, self).__init__(integerValue, dateValue, Type, valueOf_, )
supermod.AttributeType16.subclass = AttributeType16Sub
# end class AttributeType16Sub


class TraitRelationshipTypeSub(supermod.TraitRelationshipType):
    def __init__(self, Type=None, ID=None, Name=None, Symbol=None, AttributeSet=None, Citation=None, XRef=None, Source=None):
        super(TraitRelationshipTypeSub, self).__init__(Type, ID, Name, Symbol, AttributeSet, Citation, XRef, Source, )
supermod.TraitRelationshipType.subclass = TraitRelationshipTypeSub
# end class TraitRelationshipTypeSub


class AttributeSetType17Sub(supermod.AttributeSetType17):
    def __init__(self, Attribute=None, Citation=None, XRef=None, Comment=None):
        super(AttributeSetType17Sub, self).__init__(Attribute, Citation, XRef, Comment, )
supermod.AttributeSetType17.subclass = AttributeSetType17Sub
# end class AttributeSetType17Sub


class AttributeType18Sub(supermod.AttributeType18):
    def __init__(self, integerValue=None, dateValue=None, Type=None, valueOf_=None):
        super(AttributeType18Sub, self).__init__(integerValue, dateValue, Type, valueOf_, )
supermod.AttributeType18.subclass = AttributeType18Sub
# end class AttributeType18Sub


class ElementValueTypeSub(supermod.ElementValueType):
    def __init__(self, Type=None, valueOf_=None):
        super(ElementValueTypeSub, self).__init__(Type, valueOf_, )
supermod.ElementValueType.subclass = ElementValueTypeSub
# end class ElementValueTypeSub


class MethodAttributeTypeSub(supermod.MethodAttributeType):
    def __init__(self, Attribute=None):
        super(MethodAttributeTypeSub, self).__init__(Attribute, )
supermod.MethodAttributeType.subclass = MethodAttributeTypeSub
# end class MethodAttributeTypeSub


class AttributeType19Sub(supermod.AttributeType19):
    def __init__(self, integerValue=None, dateValue=None, Type=None, valueOf_=None):
        super(AttributeType19Sub, self).__init__(integerValue, dateValue, Type, valueOf_, )
supermod.AttributeType19.subclass = AttributeType19Sub
# end class AttributeType19Sub


class MethodType20Sub(supermod.MethodType20):
    def __init__(self, NamePlatform=None, TypePlatform=None, Purpose=None, ResultType=None, MinReported=None, MaxReported=None, ReferenceStandard=None, Citation=None, XRef=None, Description=None, Software=None, SourceType=None, MethodType_member=None, MethodAttribute=None, MethodResult=None, Type=None):
        super(MethodType20Sub, self).__init__(NamePlatform, TypePlatform, Purpose, ResultType, MinReported, MaxReported, ReferenceStandard, Citation, XRef, Description, Software, SourceType, MethodType_member, MethodAttribute, MethodResult, Type, )
supermod.MethodType20.subclass = MethodType20Sub
# end class MethodType20Sub


class ObservedDataTypeSub(supermod.ObservedDataType):
    def __init__(self, ID=None, Attribute=None, Severity=None, Citation=None, XRef=None, Comment=None):
        super(ObservedDataTypeSub, self).__init__(ID, Attribute, Severity, Citation, XRef, Comment, )
supermod.ObservedDataType.subclass = ObservedDataTypeSub
# end class ObservedDataTypeSub


class AttributeType21Sub(supermod.AttributeType21):
    def __init__(self, integerValue=None, dateValue=None, Type=None, valueOf_=None):
        super(AttributeType21Sub, self).__init__(integerValue, dateValue, Type, valueOf_, )
supermod.AttributeType21.subclass = AttributeType21Sub
# end class AttributeType21Sub


class SampleDescriptionTypeSub(supermod.SampleDescriptionType):
    def __init__(self, Description=None, Citation=None):
        super(SampleDescriptionTypeSub, self).__init__(Description, Citation, )
supermod.SampleDescriptionType.subclass = SampleDescriptionTypeSub
# end class SampleDescriptionTypeSub


class SpeciesTypeSub(supermod.SpeciesType):
    def __init__(self, TaxonomyId=None, valueOf_=None):
        super(SpeciesTypeSub, self).__init__(TaxonomyId, valueOf_, )
supermod.SpeciesType.subclass = SpeciesTypeSub
# end class SpeciesTypeSub


class AgeTypeSub(supermod.AgeType):
    def __init__(self, Type=None, age_unit=None, valueOf_=None):
        super(AgeTypeSub, self).__init__(Type, age_unit, valueOf_, )
supermod.AgeType.subclass = AgeTypeSub
# end class AgeTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ReleaseType'
        rootClass = supermod.ReleaseType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ReleaseType'
        rootClass = supermod.ReleaseType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ReleaseType'
        rootClass = supermod.ReleaseType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ReleaseType'
        rootClass = supermod.ReleaseType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from clinvar_api import *\n\n')
        sys.stdout.write('import clinvar_api as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
