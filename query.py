"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
car_eight = Brand.query.get(8)
# <Brand id=8 name=Austin founded=1905 headquarters=Longbridge, England discontinued=1987>

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
cars = Model.query.filter(Model.name=='Corvette', Model.brand_name=='Chevrolet').all()

# Get all models that are older than 1960.
car_models = Model.query.filter(Model.year>1960).all()


# Get all brands that were founded after 1920.
car = Brand.query.filter(Brand.founded>1920).all()


# Get all models with names that begin with "Cor".
# sqlite> SELECT name FROM Models WHERE name LIKE "Cor%"; --- SQLalchemy and I are having disagreement so I decided to put the sql version for now.

cor_car = Model.query.filter(Model.name.like('Cor%')).all() 
#yay! SQLalchemy and I are friends again!

# Get all brands with that were founded in 1903 and that are not yet discontinued.

classic = Brand.query.filter((Brand.founded==1903) & (Brand.discontinued==None)).all()

# Get all brands with that are either discontinued or founded before 1950.
og_cars = Brand.query.filter((Brand.discontinued==None) | (Brand.founded<1950)).all()

# Get any model whose brand_name is not Chevrolet.
chevy_hater = Model.query.filter(Model.name != "Chevrolet").all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    year = db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand).filter(Model.year == year).all()
    return year
    print year
    
	

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

     #get all the brand name from Brands 
     #print the car models attached to Brand name
    brand_and_model = db.session.query(Brand.name, Model.name).join(Model).filter(Brand.name == Model.brand_name).all()
    return brand_and_model
    print brand_and_model

    

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# <flask_sqlalchemy.BaseQuery object at 0x1058cabd0>
# It returns an object. The query is not complete unless you include query method like .all(), .one()

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
#Association table is how tables are connected. 
#The association between tables is by using model of many-to-many, many-to-one or one-to-one relationship. Which
#is using foreing key(s) to refer a parent table to a child table. 
#
