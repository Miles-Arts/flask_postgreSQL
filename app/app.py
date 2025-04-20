from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
      #return ("<h1>Hola mi gente Python 🤖</h1>")
      cursos=['Python','Java','JavaScript','C#','Cobol','Go']
      data={
            'titulo':'Index123 📚',
            'bienvenida':'Hola Python 💻',
            'cursos': cursos,
            'numero_cursos':len(cursos)
            #'numero_cursos':0
      }
      return render_template('index.html', data=data)

@app.route('/contacto/<nombre>')
def contacto(nombre):
      data={
            'titulo': 'Contacto 📞',
            'nombre': nombre      
      }
      return render_template('contacto.html',data=data)


if __name__ == '__main__':
      app.run(debug=True,port=5050)
      
      