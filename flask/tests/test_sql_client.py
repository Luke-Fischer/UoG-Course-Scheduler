import sys
sys.path.append('../flask')

from clients.sql_client import SQLClient

#Test for the number of course sections = 2112
def test_all_courses():
    sql_client = SQLClient()
    class_list = str(sql_client.get_all_courses())
    num_courses = class_list.count(" [") + 1
    assert num_courses == 2112
