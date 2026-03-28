from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Text, ForeignKey, Float, Column, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

# one to one


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(100), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(80), nullable=True, unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean(), default=False)
    password: Mapped[str] = mapped_column(String(180), nullable=False)

    profile: Mapped["Profile"] = relationship(
        "Profile", back_populates="user", uselist=False)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "is_active": self.is_active,
            # password no debe ser serializado
        }


class Profile(db.Model):
    __tablename__ = "profile"

    id: Mapped[int] = mapped_column(primary_key=True)
    bio: Mapped[str] = mapped_column(Text(), nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    user: Mapped["User"] = relationship(
        "User", back_populates="profile", uselist=False)

    def serialize(self):
        return {
            "id": self.id,
            "biografía": self.bio
        }

# one to many


class Parent(db.Model):
    __tablename__ = "parents"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)

    children: Mapped[list["Child"]] = relationship(
        "Child",
        back_populates="parent",
        uselist=True
    )


class Child(db.Model):
    __tablename__ = "children"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)

    parent_id: Mapped[int] = mapped_column(
        ForeignKey("parents.id"), nullable=False)

    parent: Mapped["Parent"] = relationship(
        "Parent",
        back_populates="children",
    )


# many to many

customer_product = Table(
    'customer_product',
    db.Model.metadata,
    Column("customer_id", ForeignKey("customers.id"), primary_key=True),
    Column("product_id", ForeignKey("products.id"), primary_key=True)
)


class Customer(db.Model):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    email: Mapped[str] = mapped_column(String(80), nullable=True, unique=True)

    products: Mapped[list["Product"]] = relationship(
        "Product",
        secondary=customer_product,
        back_populates="customers"
    )


class Product(db.Model):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    price: Mapped[float] = mapped_column(Float(), nullable=False)

    customers: Mapped[list["Customer"]] = relationship(
        "Customer",
        secondary=customer_product,
        back_populates="products"
    )
