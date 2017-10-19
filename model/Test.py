from sqlalchemy import create_engine

class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    
    def __repr__(self):
        return "<User(name='%s')>" % (
            self.name,
        )

if __name__ == "__main__";
    print("OK")

