from flask_wtf import Form
from wtforms import SubmitField, StringField, SelectField, FileField, IntegerField
from wtforms.validators import Required

class DbBlastForm(Form):
    pass

class BlastForm(Form):
    fasta = FileField('Fastafile') #,validators=[Required()])
    outfmt = StringField('Outfmt.', default='6')
    block_size = StringField('Size of blocks to split file into.', default='100k')
    blastAlgorithm = StringField('blastn or blastp', default='blastn', validators=[Required()])
    evalue = StringField('Evalue', default='1e-06')
    # cloud_provider = SelectField('Run job on:', choices=[('AWS','Amazon Web Services'), \
                                                            # ('GCE', 'Google Cloud Engine'), \
                                                            # ('Azure', 'Microsoft Azure')])
    submit = SubmitField('Submit job.')

class CawForm(Form):
    zipfile = FileField('Zip with the fasta files')
    submit = SubmitField('Submit.')

class UploadForm(Form):
    filehandle = FileField('File to upload')
    submit = SubmitField('Upload file.')
