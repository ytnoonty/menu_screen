from menuscreen import create_app

app = create_app()
# print(app)

if __name__ == '__main__':
    app.run(debug=True)
