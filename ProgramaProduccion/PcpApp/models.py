from django.db import models

# Create your models here.	

class Cliente(models.Model):
	idCliente = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=60)

class MateriaPrima(models.Model):
	idMateriaPrima = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=60)
	ancho = models.IntegerField()#mm
	espesor = models.IntegerField()
	largo = models.IntegerField()#metros
	peso = models.IntegerField()#kg
	zonaTratada = models.IntegerField() #zona de impresión del material
	margenA = models.IntegerField() #zona sin impresion o margen
	margenB = models.IntegerField() #zona sin impresion o margen
	fechaAlta = models.DateTimeField(auto_now_add=True,blank=True)#None e ingresa la fecha del servidor automaticamente
	fechaBaja = models.DateTimeField(blank=True,null=True) #Coloco fechaBaja=None para que quede en null en Base de datos

class Setup(models.Model):
	idSetup = models.AutoField(primary_key=True)
	desarrollo = models.IntegerField()
	repeticiones= models.IntegerField() #Repeticiones por vuelta Desarrollo/distancia
	offset= models.IntegerField() #mm
	tipoDeMaterial= models.CharField(max_length=20) #elastico, etc.
	tiroDesbobinador = models.IntegerField() #Kilos
	tensionCalandras = models.IntegerField() #Kilos
	tensionRebobinador = models.IntegerField() #Kilos
	taperTension = models.IntegerField() #Kilos
	temperaturaColores = models.IntegerField() #Centigrados
	temperaturaTunel = models.IntegerField() #Centigrados
	temperaturaTambor = models.IntegerField() #Centigrados
	temperaturaCalandras = models.IntegerField() #Centigrados
	velocidadImpresion = models.IntegerField() #Metros por minuto
	SUBFAMILIA_CHOICES = (
		('TOALLITA', 'Toallita'),
       	('TERMOCONTRAIBLE', 'Termocontraible'),
      	('YOGUR', 'Yogur'),
     	('LAMINADO','Laminado'),
       	('LACTEO','Lacteo'),
      	('FILM','Film')
	)

	subFamilia_choice = models.CharField(max_length=20,choices=SUBFAMILIA_CHOICES,default='FILM')
    #models.CharField(max_length=70) # Toallitas / Termocontraible / Yogures / Lacteos 
	observaciones = models.TextField()
	color1 = models.CharField(max_length=20)
	color2 = models.CharField(max_length=20)
	color3 = models.CharField(max_length=20)
	color4 = models.CharField(max_length=20)
	color5 = models.CharField(max_length=20)
	color6 = models.CharField(max_length=20)
	color7 = models.CharField(max_length=20)
	color8 = models.CharField(max_length=20)
	bcmAnilox1 = models.IntegerField()
	bcmAnilox2 = models.IntegerField()
	bcmAnilox3 = models.IntegerField()
	bcmAnilox4 = models.IntegerField()
	bcmAnilox5 = models.IntegerField()
	bcmAnilox6 = models.IntegerField()
	bcmAnilox7 = models.IntegerField()
	bcmAnilox8 = models.IntegerField()
	lPulgAnilox1 = models.CharField(max_length=10,null=True)
	lPulgAnilox2 = models.CharField(max_length=10,null=True)
	lPulgAnilox3 = models.CharField(max_length=10,null=True)
	lPulgAnilox4 = models.CharField(max_length=10,null=True)
	lPulgAnilox5 = models.CharField(max_length=10,null=True)
	lPulgAnilox6 = models.CharField(max_length=10,null=True)
	lPulgAnilox7 = models.CharField(max_length=10,null=True)
	lPulgAnilox8 = models.CharField(max_length=10,null=True)
	viscosidad1 = models.IntegerField() #Segundos
	viscosidad2 = models.IntegerField() #Segundos
	viscosidad3 = models.IntegerField() #Segundos
	viscosidad4 = models.IntegerField() #Segundos
	viscosidad5 = models.IntegerField() #Segundos
	viscosidad6 = models.IntegerField() #Segundos
	viscosidad7 = models.IntegerField() #Segundos
	viscosidad8 = models.IntegerField() #Segundos
	temperaruta1 = models.IntegerField()#Centigrados
	temperaruta2 = models.IntegerField()#Centigrados
	temperaruta3 = models.IntegerField()#Centigrados
	temperaruta4 = models.IntegerField()#Centigrados
	temperaruta5 = models.IntegerField()#Centigrados
	temperaruta6 = models.IntegerField()#Centigrados
	temperaruta7 = models.IntegerField()#Centigrados
	temperaruta8 = models.IntegerField()#Centigrados
	ajusteDeColor = models.CharField(max_length=50,null=True)
	fechaAlta = models.DateTimeField(auto_now_add=True,blank=True)
	fechaModificacion = models.DateTimeField(blank=True,null=True)
	fechaBaja = models.DateTimeField(blank=True,null=True)# null por defecto cuando esta activa 
	
	def is_upperclass(self):
        #Aunque puede definir una lista de opciones fuera de una clase de modelo y luego consultarla, 
		# definiendo las opciones y los nombres para cada opción dentro de la clase de modelo mantiene
		# toda esa información con la clase que la usa y ayuda a hacer referencia a opciones 
		# (por ejemplo, Setup.TERMOCONTRAIBLE funcionará en cualquier lugar donde se haya importado el modelo de Setup)'''

		return self.subfamilia_choices(self.TOALLITA,self.TERMOCONTRAIBLE,self.YOGUR,self.LAMINADO,self.LACTEO,self.FILM)

class FichaTecnica(models.Model):
	idFichaTecnica = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=60)
	anchoBanda=models.IntegerField()
	distanciaTac = models.IntegerField() # distancia de repeticion nos sirve para calcular la cantidad de impresiones por vuelta
	cliente = models.ForeignKey(Cliente,null=True,blank=True, on_delete=models.CASCADE)
	setup = models.ForeignKey(Setup,null=True,blank=True, on_delete=models.CASCADE)
	materiaPrima = models.ForeignKey(MateriaPrima,null=True,blank=True, on_delete=models.CASCADE)
	fechaAlta = models.DateTimeField(auto_now_add=True,blank=True)
	fechaBaja = models.DateTimeField(blank=True,null=True)
	observaciones = models.TextField()