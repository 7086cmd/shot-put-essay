import polars
from os import path

df = polars.read_csv(path.join(path.dirname(__file__), "data.csv"))
