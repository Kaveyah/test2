"""
SQL-Connector and all things DB go in here
"""
import mysql.connector
from config import USER, PASSWORD, HOST, DATABASE

class DbConnectionError(Exception):
    """Raised when the DB connection or query fails."""
    pass

def _connect_to_db():
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=DATABASE
    )
    return cnx

# EXAMPLE 1
def get_all_pets_db():
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = """SELECT * FROM pets WHERE adopted = FALSE"""
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple

        cur.close()

        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


if __name__ == "__main__":
    print("TESTING DB CONNECTION")
    print(get_all_pets_db())


# Apply to adopt a pet
def apply_to_adopt_db(pet_id, applicant_name):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        insert_application = """
        INSERT INTO applications (pet_id, applicant_name)
        VALUES (%s, %s)
        """
        update_pet = """
        UPDATE pets SET adopted = TRUE WHERE id = %s
        """

        cur.execute(insert_application, (pet_id, applicant_name))
        cur.execute(update_pet, (pet_id,))
        db_connection.commit()

        cur.close()
        return {"message": "Application submitted."}

    except Exception:
        raise DbConnectionError("Failed to apply for adoption")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# Cancel an adoption application
def cancel_application_db(pet_id):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        delete_application = """
        DELETE FROM applications WHERE pet_id = %s
        """
        update_pet = """
        UPDATE pets SET adopted = FALSE WHERE id = %s
        """

        cur.execute(delete_application, (pet_id,))
        cur.execute(update_pet, (pet_id,))
        db_connection.commit()

        cur.close()
        return {"message": "Application cancelled."}

    except Exception:
        raise DbConnectionError("Failed to cancel adoption")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


if __name__ == "__main__":
    print("TESTING DB CONNECTION")
    print(get_all_pets_db())