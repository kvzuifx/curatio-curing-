import django
from django.db import connections
import os
import taipy
# Configure Django settings
django.setup()
# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "curesys.settings")

try:
    # Use the default database connection
    connection = connections['default']

    # Execute a test query
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")

    # Check if the query was successful
    result = cursor.fetchone()
    if result == (1,):
        print("Database connection successful!")
    else:
        print("Database connection test failed.")
except Exception as e:
    print(f"Error: {e}")

