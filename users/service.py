from users.models import User

JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 84600

class UserService():
    userModel = User()
    
    def getUser(self):
        return User.objects.all()