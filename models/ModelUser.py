from .entities.User import User
from werkzeug.security import generate_password_hash

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            conn = db.connect()
            cursor=conn.cursor()
            sql = """SELECT id, username,email,password FROM user 
                    WHERE email = '{}'""".format(user.email)
            cursor.execute(sql)
            conn.commit()
            conn.close()
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], row[2],User.check_password(row[3], user.password))
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def registro(self,db,user):
        try:
            conn=db.connect()
            cursor=conn.cursor()
            password=generate_password_hash(user.password)
            sql="INSERT INTO user (id,username,email,password) VALUES(NULL,%s,%s,%s)"
            datos=(user.username,user.email,password,)
            cursor.execute(sql,datos)
            conn.commit()
            conn.close()
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_by_id(self, db, id):
        try:
            conn=db.connect()
            cursor=conn.cursor()
            sql = "SELECT id, username,email,password FROM user WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1],row[2],row[3])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
