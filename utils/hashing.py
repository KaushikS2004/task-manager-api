from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str) -> str:
    # bcrypt max length = 72 bytes
    return pwd_context.hash(password.encode("utf-8")[:72])

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain.encode("utf-8")[:72], hashed)
