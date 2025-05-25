import subprocess

def run_migrations():
    subprocess.run(["alembic", "upgrade", "head"], check=True)

if __name__ == "__main__":
    run_migrations()

// execute with `python src/migrate.py` to run the migrations