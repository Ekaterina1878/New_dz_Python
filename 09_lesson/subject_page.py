from sqlalchemy import text


class SubjectPage:
    def __init__(self, session):
        self.session = session

    def insert_subject(self, title, subject_id):
        sql = text("INSERT INTO subject("
                   "subject_title, subject_id) VALUES (:new_title, :new_id)")
        self.session.execute(sql, {'new_title': title, 'new_id': subject_id})
        self.session.commit()

    def update_subject(self, subject_id, new_title):
        sql = text("UPDATE subject SET "
                   "subject_title = :new_title WHERE subject_id = :new_id")
        self.session.execute(
            sql, {'new_title': new_title, 'new_id': subject_id})
        self.session.commit()

    def delete_subject(self, title):
        sql = text("DELETE FROM subject WHERE subject_title = :title")
        self.session.execute(sql, {'title': title})
        self.session.commit()

    def get_subject(self, title):
        sql = text("SELECT * FROM subject WHERE subject_title = :title")
        return self.session.execute(sql, {'title': title}).fetchone()

    def get_subject_by_id(self, subject_id):
        sql = text("SELECT * FROM subject WHERE subject_id = :new_id")
        return self.session.execute(sql, {'new_id': subject_id}).fetchone()
