from django.db import models
from django.utils import timezone
import datetime

class Breast(models.Model):
    patientid = models.UUIDField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    ethnicity = models.TextField(blank=True, null=True)
    deceaseddate = models.DateField(blank=True, null=True)
    isdeceased = models.BooleanField(blank=True, null=True)
    vitalstatus = models.TextField(blank=True, null=True)
    race = models.TextField(blank=True, null=True)
    sex = models.TextField(blank=True, null=True)
    sourcename = models.CharField(max_length=64, blank=True, null=True)
    tumor_diagnosisdate = models.DateField(blank=True, null=True)
    tumor_type = models.CharField(max_length=1024, blank=True, null=True)
    tumor_histology = models.TextField(blank=True, null=True)
    stage_m = models.TextField(blank=True, null=True)
    stage_stagegroup = models.TextField(blank=True, null=True)
    metastasis_bodysite = models.CharField(max_length=4096, blank=True, null=True)
    metastasis_metastasisdate = models.DateField(blank=True, null=True)
    hasmetastasis = models.BooleanField(blank=True, null=True)
    procedure_proceduretype = models.CharField(max_length=4096, blank=True, null=True)
    recurrence_recurrencetype = models.CharField(max_length=4096, blank=True, null=True)
    familyhistory_condition = models.CharField(max_length=4096, blank=True, null=True)
    familyhistory_relationship = models.TextField(blank=True, null=True)
    riskfactor_menopausalvalue = models.TextField(blank=True, null=True)
    riskfactor_ashkenazivalue = models.TextField(blank=True, null=True)
    diagnostic_status_flag = models.IntegerField(blank=True, null=True)
    molecularreport_id = models.UUIDField(blank=True, null=True)
    molecularreport_labname = models.CharField(max_length=256, blank=True, null=True)
    molecularreport_reportdate = models.DateField(blank=True, null=True)
    molecularreport_testname = models.CharField(max_length=256, blank=True, null=True)
    molecularbiomarker_platformtechnology = models.CharField(max_length=4096, blank=True, null=True)
    molecularbiomarker_biomarkername = models.CharField(max_length=4096, blank=True, null=True)
    molecularbiomarker_biomarkertype = models.CharField(max_length=4096, blank=True, null=True)
    molecularbiomarker_call = models.CharField(max_length=4096, blank=True, null=True)
    molecularbiomarker_clinicalsignificance_flag = models.IntegerField(blank=True, null=True)
    molecularbiomarker_gene = models.TextField(blank=True, null=True)
    molecularbiomarker_genomicsource = models.CharField(max_length=4096, blank=True, null=True)
    further_testing_genomic_source = models.TextField(blank=True, null=True)
    hasbiomarkerreport = models.BooleanField(blank=True, null=True)
    hr_positive = models.BooleanField(blank=True, null=True)
    hr_negative = models.BooleanField(blank=True, null=True)
    erbb2_positive = models.BooleanField(blank=True, null=True)
    erbb2_negative = models.BooleanField(blank=True, null=True)
    molecularbiomarker_clinicalsignificance = models.TextField(blank=True, null=True)
    germline_somatic_patient_level = models.TextField(blank=True, null=True)
    germline_somatic_gene_level = models.TextField(blank=True, null=True)
    molecular_subtype = models.TextField(blank=True, null=True)
    diagnostic_status = models.TextField(blank=True, null=True)
    molecularbiomarker_genes = models.TextField(blank=True, null=True)  # This field type is a guess.
    targetedtherapy = models.TextField(blank=True, null=True)
    lineoftherapy = models.IntegerField(blank=True, null=True)
    actionable = models.BooleanField(blank=True, null=True)
    genecount = models.IntegerField(blank=True, null=True)
    sizecategory = models.CharField(max_length=4096, blank=True, null=True)
    specificity = models.CharField(max_length=4096, blank=True, null=True)
    biomarkerclass = models.CharField(max_length=4096, blank=True, null=True)
    drugclass = models.TextField(blank=True, null=True)
    hasactionabletargetedtherapy = models.BooleanField(blank=True, null=True)
    nottargetedtherapytested = models.BooleanField(blank=True, null=True)
    targeted_therapy_genes = models.TextField(blank=True, null=True)  # This field type is a guess.
    actionable_genes = models.TextField(blank=True, null=True)  # This field type is a guess.
    genes_tested = models.TextField(blank=True, null=True)  # This field type is a guess.
    carecategory = models.TextField(blank=True, null=True)
    molecularbiomarker_biomarkertested = models.TextField(blank=True, null=True)
    targetedtherapymolecularindicator = models.TextField(blank=True, null=True)
    targeted_therapy_gene = models.TextField(blank=True, null=True)
    riskfactor_oncotypedxdate = models.DateField(blank=True, null=True)
    riskfactor_oncotypedxvalue = models.TextField(blank=True, null=True)
    riskfactor_oncotypedxinterpretation = models.TextField(blank=True, null=True)
    riskfactor_oncotypedxname = models.TextField(blank=True, null=True)
    suborg = models.CharField(max_length=64, blank=True, null=True)
    haschemotherapy = models.BooleanField(blank=True, null=True)
    chemotherapydrug = models.TextField(blank=True, null=True)
    source_schema = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"bti"."breast"'
