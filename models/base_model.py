
import peewee

db = peewee.SqliteDatabase('tasks.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db