import pandas as pd
csv = 'C:/Users/jongk/Desktop/data_images/restaurants-database.csv'
df = pd.read_csv('C:/Users/jongk/Desktop/data_images/restaurants-database.csv')

def capitalizecity(df):
    
    df['CITY']=df['CITY'].map(lambda x: x.capitalize())
    return df[['CITY']]

def insertintocontact(df):
    df['CONTACTNAME'].fillna('Not Available', inplace = True)
    return df[['CONTACTNAME']]

def capitalizename(df):
    df['name']=df['name'].map(lambda x: x.capitalize)
    return df[['name']]

def insertintostate(df):
    df['STATE'].fillna('N/A', inplace = True)
    return df[['STATE']]
def insertintophone(df):
    df['PHONE'].fillna('N/A',inplace= True)
    return df[['PHONE']]
import unittest
from pandas.testing import assert_frame_equal
class TestColumnMunging(unittest.TestCase):
    #must name all functions with test at the beginning of the clause
    def test_capitalize_city(self):
       
        df=pd.DataFrame({
          'CITY': ['wayne','new york city','los angeles']  
        })
        expected = pd.DataFrame({
            'CITY': ['Wayne', 'New york city', 'Los angeles1']
        })
        actual = capitalizecity(df)
        assert_frame_equal(expected, actual)
    def test_capitalize_name(self):
        df1 = pd.DataFrame({
          'name' : ['wendys', 'grasshopper too','tofu house']

        })

        expected_1 = pd.DataFrame({
            'name' : ['Wendys','Grasshopper too', 'Tofu house']
        })

        actual_1 = capitalizename(df)
        assert_frame_equal(expected_1,actual_1)
    def test_insert_into_contact(self):
        df2 = pd.DataFrame({
            'CONTACTNAME':['','Jonathan Moyers', '']
        })

        expected_2 = pd.DataFrame({
            'CONTACTNAME':['Not Available', 'Jonathan Moyers', 'Not Available']
        })
        actual_2 = insertintocontact(df2)
        assert_frame_equal(expected_2,actual_2)
    def test_insert_into_state(self):
        df3 = pd.DataFrame({
            'STATE': ['NJ','','']
        })

        expected_3 = pd.DataFrame({
            'STATE' : ['NJ','N/A','N/A']
        })
        actual_3 = insertintostate(df3)
        assert_frame_equal(expected_3,actual_3)
    def test_insert_into_contact(self):
        df4 = pd.DataFrame({
            'PHONE':['(973)766-3929','','']

        })
        expected_4 = pd.DataFrame({
            'PHONE' : ['(973)766-3929','N/A','N/A']
        })
        actual_4 = insertintophone(df4)
        assert_frame_equal(expected_4,actual_4)