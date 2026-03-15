from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cod-mf")
def cod_mf():
    return render_template("COD-MF/COD-MF.html")

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory("games", filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)