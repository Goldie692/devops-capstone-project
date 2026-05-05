import sys
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS
from service import config
from service.common import log_handlers

# 1. Create Flask application
app = Flask(__name__)
app.config.from_object(config)

# 2. Initialize Security Headers (Talisman) and CORS
talisman = Talisman(app)
CORS(app)

# 3. Import routes and models (to avoid circular imports)
# pylint: disable=wrong-import-position, cyclic-import, wrong-import-order
from service import routes, models  # noqa: F401 E402
from service.common import error_handlers, cli_commands  # noqa: F401 E402

# 4. Set up logging
log_handlers.init_logging(app, "gunicorn.error")
app.logger.info("Service initialized!")