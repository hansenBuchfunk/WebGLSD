from django.db import models
from multiselectfield import MultiSelectField
from multiselectfield.validators import MaxValueMultiFieldValidator

# Geschlecht
geschlecht_choices = [
	('M', 'M'),
	('W', 'W'),
	('D', 'D'),
]
# PoC
poc_choices = [
	('Ja', 'Ja'),
]

# Stimmlagen
stimmlage_choices = [
    ('Hoch', 'Hoch'),
    ('Mittel', 'Mittel'),
    ('Tief', 'Tief'),
]
# Genre
genre_choices = [
	('Sachbuch','Sachbuch'),
	('Belletristik','Belletristik'),
	('Krimi/Thriller','Krimi/Thriller'),
	('Erotik','Erotik'),
]
# Charakter
charakter_choices = [
	('sonor','sonor'),
	('klar','klar'),
	('rauh','rauh'),
	('weich','weich'),
]
# Honorarkategorie
honorar_choices = [
	('1','1'),
	('2','2'),
	('3','3'),
	('4','4'),
]
# Sprachkenntnisse
sprachkenntnisse_choices = [
	('keine','keine'),
	('Vorkenntnisse','Vorkenntnisse'),
	('Gut','Gut'),
	('Fliessend','Fliessend'),
	('Muttersprache','Muttersprache')
]

# Stimmlagen
stimmalter_choices = [
    ('Kind', 'Kind'),
    ('Teenager', 'Teenager'),
    ('junge Erwachsene', 'junge Erwachsene'),
    ('beste Jahre', 'beste Jahre'),
    ('Senior:in', 'Senior:in'),
]

# Dialekte
dialekte_choices = [
	('Bayerisch','Bayerisch'),
	('Berlinerisch','Berlinerisch'),
	('Fränkisch','Fränkisch'),
	('Hessisch','Hessisch'),
	('Norddeutsch','Norddeutsch'),
	('Rheinisch','Rheinisch'),
	('Sächsisch','Sächsisch'),
	('Schwäbisch','Schwäbisch'),
	('Badisch','Badisch'),
	('Schweizerdeutsch','Schweizerdeutsch'),
	('Westfälisch','Westfälisch'),
	('Wienerisch','Wienerisch'),
]

stimmlage_validators = [
    MaxValueMultiFieldValidator(3)  # hier 3 ist die maximale Anzahl der ausgewählten Stimmlagen
]

genre_validators = [
    MaxValueMultiFieldValidator(4)  # hier 3 ist die maximale Anzahl der ausgewählten Stimmlagen
]

charakter_validators = [
    MaxValueMultiFieldValidator(4)  # hier 3 ist die maximale Anzahl der ausgewählten Stimmlagen
]

honorar_validators = [
    MaxValueMultiFieldValidator(1)  # hier 1 ist die maximale Anzahl der ausgewählten Honorarkategri
]

stimmalter_validators = [
    MaxValueMultiFieldValidator(5)  # hier 1 ist die maximale Anzahl der ausgewählten Honorarkategri
]

dialekte_validators = [
    MaxValueMultiFieldValidator(12)  # hier 1 ist die maximale Anzahl der ausgewählten Honorarkategri
]
poc_validators = [
    MaxValueMultiFieldValidator(1)  # hier 1 ist die maximale Anzahl der ausgewählten Honorarkategri
]


class Mitarbeiter(models.Model):
	name = models.CharField('Mitarbeiter Name', max_length=120)
	telefonma = models.CharField('Mitarbeiter Telefon', max_length=20)
	emailma = models.EmailField('Mitarbeiter Email')

	def __str__(self):
		return self.name

class Sprecherinnen(models.Model):
	nachname = models.CharField(max_length=30)
	vorname = models.CharField(max_length=30)
	geschlecht = models.CharField(max_length=1, choices=geschlecht_choices, default='', blank=True)
	poC = models.CharField(max_length=2, choices=poc_choices, default='', blank=True)
	telefon = models.CharField(max_length=30, blank=True)
	emailadresse = models.EmailField('Sprecher:in Mail', blank=True)
	geburtsjahr = models.CharField(max_length=30, blank=True)
	stimmlage = MultiSelectField(choices=stimmlage_choices, default=None, blank=True, validators=stimmlage_validators)
	genre = MultiSelectField(choices=genre_choices, default=None, blank=True, validators=genre_validators)
	stimmcharakter = MultiSelectField(choices=charakter_choices, default=None, blank=True, validators=charakter_validators)
	stimmalter = MultiSelectField(choices=stimmalter_choices, default=None, blank=True, validators=stimmalter_validators)
	honorarkategorie = models.CharField(max_length=10, choices=honorar_choices, default='', blank=True)
	mindesthonorar = models.CharField(max_length=30, blank=True)

	# Sprachkenntnisse

	deutsch = models.CharField('Deutsch', max_length=13, choices=sprachkenntnisse_choices, default='', blank=True)
	englisch = models.CharField('Englisch (GB)', max_length=13, choices=sprachkenntnisse_choices, default='', blank=True)
	englischus = models.CharField('Englisch (US)', max_length=13, choices=sprachkenntnisse_choices, default='', blank=True)
	französisch = models.CharField('Französisch', max_length=13, choices=sprachkenntnisse_choices, default='', blank=True)
	italienisch = models.CharField('Italienisch', max_length=13, choices=sprachkenntnisse_choices, default='', blank=True)
	niederländisch = models.CharField('Niederländisch', max_length=13, choices=sprachkenntnisse_choices, default='', blank=True)
	polnisch = models.CharField('Polnisch', max_length=13, choices=sprachkenntnisse_choices, default='', blank=True)
	portugiesisch = models.CharField('Portugiesisch', max_length=13, choices=sprachkenntnisse_choices, default='', blank=True)
	russisch = models.CharField('Russisch', max_length=13, choices=sprachkenntnisse_choices, default='', blank=True)
	spanisch = models.CharField('Spanisch', max_length=13, choices=sprachkenntnisse_choices, default='', blank=True)
	türkisch = models.CharField('Türkisch', max_length=13, choices=sprachkenntnisse_choices, default='', blank=True)

	# Dialekte
	dialekte = MultiSelectField(choices=dialekte_choices, default=None, blank=True, validators=dialekte_validators)


	def __str__(self):
		return self.vorname + ' ' + self.nachname

class Angebot(models.Model):
	titel = models.CharField('Angebot Titel', max_length=120)
	datum = models.DateTimeField('Angebot Datum') 
	apbuchfunk = models.ForeignKey(Mitarbeiter, blank=True, null=True, on_delete=models.CASCADE)
	beschreibung = models.TextField(blank=True)
	sprecheriAngebot = models.ManyToManyField(Sprecherinnen, blank=True)
	
	def __str__(self):
		return self.titel