import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Base de datos simulada
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

class UserManager:
    def __init__(self, session):
        self.session = session

    def create_user(self, username, email):
        # Verifica si el usuario o el correo ya existen
        if self.session.query(User).filter_by(username=username).first() or \
           self.session.query(User).filter_by(email=email).first():
            raise ValueError("El nombre de usuario o correo ya están en uso.")

        user = User(username=username, email=email)
        self.session.add(user)
        self.session.commit()
        return user

    def authenticate_user(self, username, email):
        # Verifica si el usuario existe con el nombre de usuario y correo proporcionados
        user = self.session.query(User).filter_by(username=username, email=email).first()
        return user is not None

# Configuración de la base de datos en memoria
@pytest.fixture
def db_session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

# Pruebas de integración
def test_user_management_integration(db_session):
    user_manager = UserManager(db_session)

    # Registro de usuario
    user = user_manager.create_user("testuser", "test@example.com")
    assert user is not None
    assert user.username == "testuser"
    assert user.email == "test@example.com"

    # Autenticación exitosa
    authenticated = user_manager.authenticate_user("testuser", "test@example.com")
    assert authenticated is True

    # Autenticación fallida (usuario incorrecto)
    authenticated = user_manager.authenticate_user("wronguser", "test@example.com")
    assert authenticated is False

    # Autenticación fallida (correo incorrecto)
    authenticated = user_manager.authenticate_user("testuser", "wrong@example.com")
    assert authenticated is False

def test_user_creation_duplicate(db_session):
    user_manager = UserManager(db_session)

    # Crear un usuario
    user_manager.create_user("testuser", "test@example.com")

    # Intentar crear un usuario con el mismo nombre de usuario o correo
    with pytest.raises(ValueError):
        user_manager.create_user("testuser", "different@example.com")
    with pytest.raises(ValueError):
        user_manager.create_user("differentuser", "test@example.com")
