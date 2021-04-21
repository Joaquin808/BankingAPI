from flask import Flask
from controllers import main_controller as mc
import logger

app = Flask(__name__)

mc.route(app)

if __name__ == '__main__':
    logger.log_info("Application start")
    app.run(debug=True)


