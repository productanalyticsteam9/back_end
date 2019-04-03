import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"~/backend/project")

from project import app as application
