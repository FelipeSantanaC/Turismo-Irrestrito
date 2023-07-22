from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models

class MyUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('O endereço de email deve ser fornecido.')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(email=email, name=name, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    name = models.CharField(max_length=45)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = MyUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

      
    def has_perm(self, perm, obj=None):
        return True

class Local(models.Model):
    nome = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    recursos = models.TextField()
    cep = models.CharField(max_length=10)
    foto_url = models.CharField(max_length=255)
    nota = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    relevancia = models.IntegerField(default=0)
    tipo = models.CharField(max_length=100, default='')


#Esses modelos irão armazenar um id e o tipo do local/DAM/recurso, ex. museu, muleta, rampa,  respectivamente.
class TiposLocais(models.Model):
    title = models.CharField(max_length=40)
class ListaRecursos(models.Model):
    title = models.CharField(max_length=80)
class ListaDispositivos(models.Model):
    title = models.CharField(max_length=40)



#Esses modelos ligam MyUser de modo OneToMany a LocaldeInteresse, Recursos, e DAM, através do id do MyUser e o id do local/DAM/recurso.
class LocaisInteresse(models.Model):
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    recurso_id = models.ForeignKey(TiposLocais, on_delete=models.CASCADE)

class RecursosAcessibilidade(models.Model):
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    tipo_local_id = models.ForeignKey(ListaRecursos, on_delete=models.CASCADE)

class DispositivoAuxiliarMarcha(models.Model):
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    dispositivo_id = models.ForeignKey(ListaDispositivos, on_delete=models.CASCADE)


#Esse modelo armazena os dados exibidos no perfil do usuário.
class UserProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    data_nascimento = models.DateField(null=True, blank=True)
    foto_perfil = models.URLField(blank=True)
    acompanhamento = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')], default='nao')
    DURACAO_CONDICAO_CHOICES = [
        ('progressiva', 'Progressiva/Degenerativa'),
        ('temporaria', 'Temporária'),
        ('estavel', 'Estável ou Permanente'),
    ]
    duracao_condicao = models.CharField(max_length=40, choices= DURACAO_CONDICAO_CHOICES, default='temporaria')
    TIPO_USUARIO_CHOICES = [
        ('acompanhantes','Acompanhante'),
        ('pmlr','Pessoa com mobilidade de locomoção reduzida'),
        ('outro','Outro')
    ]
    tipo_usuario = models.CharField(max_length=50, choices= TIPO_USUARIO_CHOICES, default='temporaria')