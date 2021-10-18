from app import create_app

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return dict()


if __name__ == "__main__":
    app.run()