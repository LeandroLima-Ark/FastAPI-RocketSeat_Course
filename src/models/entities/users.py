from sqlalchemy import Table, Column, Integer, String
from src.models.settings.metadata import metadata

Users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nome", String, nullable=True),
    Column("idade", Integer)
)