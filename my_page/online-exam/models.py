import datetime as dt
from ..database import Column, Model, SurrogatePK, reference_col, relationship

class Question(Model, SurrogatePK):
    __tablename__ = 'question'

    id = Column(db.Integer, primary_key=True)
    examid = Column(db.Integer, db.ForeignKey('exam.id'))
    question = Column(db.String(250), nullable=False)
    image = Column(db.String(250))
    option = relationship('Option', backref='question')
    answer = relationship('Answer', backref='question')
    
    def __repr__(self):
        return f"Question('{self.question}')"

class Option(Model, SurrogatePK):
    __tablename__ = 'option'

    id = Column(Integer, primary_key=True)
    question_id = Column(db.Integer, db.ForeignKey('question.id'))
    option = Column(db.String(250))
    isright = Column(db.Boolean)


    def __repr__(self):
        return f"Option('{self.question_id}', '{self.option}', '{self.isright}')"

class Answer(Model, SurrogatePK):
    __tablename__ = 'answers'

    id = Column(db.Integer, primary_key=True)
    question_id = Column(db.Integer, db.ForeignKey('question.id'))
    answer = Column(db.String(250))

    def __repr__(self):
        return f"Answer('{self.question_id}', '{self.answer}')"

class Exam(Model, SurrogatePK):
    __tablename__='exam'

    id = Column(db.Integer, primary_key=True)
    title = Column(db.String(350))
    description = Column(db.String(350))
    long_description = Column(db.String(350))
    question = relationship('Question', backref='exam')
    contributor_id = reference_col('account', nullable=False)
    contributor = relationship('Account', backref='exam')

    def __repr__(self):
        return f"Exam('{self.title}', '{self.description}', '{self.long_description}')"
