from flask import Flask, request, render_template
from func import check_seq

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        seq = request.form['seq']
        seq = seq.strip()
        desc, transcriptie, translatie, soort = check_seq(seq)
        if soort == 1:
            type = 'DNA'
        elif soort == 2:
            type = 'RNA'
        elif soort == 3:
            type = 'Eiwit'
        else:
            type = 'Onbekend'
        return render_template("index.html", desc=desc,
                               transcriptie=transcriptie,
                               translatie=translatie, type=type)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run()
