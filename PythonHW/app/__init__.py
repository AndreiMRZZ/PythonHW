from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.routes.healthcheck_route import healthcheck_bp
    app.register_blueprint(healthcheck_bp)
    from app.routes.pow_route import pow_bp
    app.register_blueprint(pow_bp)
    from app.routes.factorial_route import factorial_bp
    app.register_blueprint(factorial_bp)
    from app.routes.fibonacci_route import fibonacci_bp
    app.register_blueprint(fibonacci_bp)
    from app.routes.history_route import history_bp
    app.register_blueprint(history_bp)

    return app
