from models import School  

def query_example():
    """
    Returns a list of all schools from the database.
    Each row is a School object.
    """
    schools = School.query.all()  # fetch all records
    return schools
