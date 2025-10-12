import pandas as pd
from sqlalchemy import create_engine
import pyscopg2

# Create database connection
engine = create_engine('postgresql://postgres:admin@localhost:5432/library_db')
