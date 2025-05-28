import os

from dotenv import load_dotenv

load_dotenv()

_basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Configuration class for storing environment variables and API keys.
    """
    # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GOOGLE_CLOUD_PROJECT='my-project-0004-346516'
    GOOGLE_CLOUD_LOCATION='us-central1'
    # Configuration for google-genai to use Vertex AI
    # Set to "True" if you are using Vertex AI, otherwise you might use an API_KEY for other Gemini services
    GOOGLE_GENAI_USE_VERTEXAI=True
    # PATHS
    BASEDIR = _basedir

    TEMPLATES_PATH = os.path.join(_basedir, "templates")
    POWERPOINTS_PATH = os.path.join(_basedir, "powerpoints")
