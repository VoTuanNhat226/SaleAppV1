from sqlalchemy import Column, Integer, String, ForeignKey, Float
from app import db
from sqlalchemy.orm import relationship
class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(200))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__ == "__main__":
    from app import  app
    with app.app_context():
        # c1 = Category(name = 'Mobile')
        # c2 = Category(name = 'Tablet')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()
        p1 = Product(name='iPad Pro 2021', price=24000000, image="https://bom.so/K1brIv", category_id=1)
        p2 = Product(name='iPad Pro 2022', price=24000000, image="https://bom.so/K1brIv", category_id=1)
        p3 = Product(name='iPad Pro 2023', price=24000000, image="https://bom.so/K1brIv", category_id=2)
        p4 = Product(name='iPad Pro 2024', price=24000000, image="https://bom.so/K1brIv", category_id=2)
        p5 = Product(name='iPad Pro 2025', price=24000000, image="https://bom.so/K1brIv", category_id=2)
        db.session.add_all([p1,p2,p3,p4,p5])
        db.session.commit()
        # db.create_all()