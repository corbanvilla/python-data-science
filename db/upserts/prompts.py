"""A script to upsert a CSV into the database."""

from db import *
from analysis import *

# Locate the file to import, add to path
dataset = "baseline"
import_file = "datasets/prompts/baseline/en"
table = Prompts

prompts = []
with open(import_file, "r") as f:
    for line in f:
        prompts.append(
            {
                "prompt": line.strip(),
                "dataset": dataset,
            }
        )

# Iterate over DataFrame rows
updates = 0
inserts = 0
for idx, row in enumerate(prompts):
    # Check if record already exists
    result = session.query(table).filter(table.prompt == row["prompt"]).first()

    # If record exists, update it
    if result is not None:
        for column, value in row.items():
            setattr(result, column, value)
        updates += 1
    # If record does not exist, create it
    else:
        new_record = table(**row)
        session.add(new_record)
        inserts += 1

# Commit the changes
session.commit()
print(
    f"Inserted {inserts} records, updated {updates} records into {table.__tablename__}."
)
