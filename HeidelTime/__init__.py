import jpype

# start the JVM
if not jpype.isJVMStarted() :
	jar = "HeidelTime/de.unihd.dbs.heideltime.standalone.jar"
	jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % jar)

# get the Java classes we want to use
heideltime_resources = jpype.JPackage("de.unihd.dbs.uima.annotator.heideltime.resources")
heideltime_standalone = jpype.JPackage("de.unihd.dbs.heideltime.standalone")

# constants
LANGUAGES = {
	'english':heideltime_resources.Language.ENGLISH,
	'german':heideltime_resources.Language.GERMAN,
	'dutch':heideltime_resources.Language.DUTCH,
	'italian':heideltime_resources.Language.ITALIAN,
	'spanish':heideltime_resources.Language.SPANISH,
	'arabic':heideltime_resources.Language.ARABIC,
	'french':heideltime_resources.Language.FRENCH,
	'chinese':heideltime_resources.Language.CHINESE,
	'russian':heideltime_resources.Language.RUSSIAN,
	'portuguese':heideltime_resources.Language.PORTUGUESE
}

DOCUMENTS = {
	'narratives':heideltime_standalone.DocumentType.NARRATIVES,
	'news':heideltime_standalone.DocumentType.NEWS,
	'colloquial':heideltime_standalone.DocumentType.COLLOQUIAL,
	'scientific':heideltime_standalone.DocumentType.SCIENTIFIC
}

OUTPUTS = {
	'timeml':heideltime_standalone.OutputType.TIMEML,
	'xmi':heideltime_standalone.OutputType.XMI
}

CONFIG = 'config.props'


class HeidelTimeWrapper():

	def __init__(self, lang, doc=None, output=None):
		self.language = LANGUAGES[lang]
		if (doc is None):
			self.doc_type = DOCUMENTS['news']
		else:
			self.doc_type = DOCUMENTS[doc]
		if (output is None):
			self.output_type = OUTPUTS['timeml']
		else:
			self.output_type = OUTPUTS[output]
		print(jpype.JPackage("de.unihd.dbs.uima.annotator.heideltime.resources").Language.ENGLISH)
		self.heideltime = heideltime_standalone.HeidelTimeStandalone(self.language, self.doc_type, self.output_type, CONFIG)

	def convert_date(slef, day, month, year):
		sdf = jpype.java.text.SimpleDateFormat('dd-M-yyyy hh:mm:ss')
		str_date = str(day)+'-'+str(month)+'-'+str(year)+' 00:00:00'
		return sdf.parse(str_date)

	def parse(self, text, date_ref=None):
		if (date_ref is None):
			document_creation_date = jpype.java.util.Date()
		else:
			# convert to Java.util.Date
			document_creation_date = self.convert_date(date_ref.day, date_ref.month, date_ref.year)
		return self.heideltime.process(text, document_creation_date)
