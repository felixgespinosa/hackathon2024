from flask import Flask

app = Flask(__name__)

@app.route('/ejecutar-script')
def ejecutar_script():
    # Lógica para ejecutar el script de Python aquí
    # Por ejemplo, puedes usar subprocess para ejecutar el script
    import subprocess
    subprocess.run(["python", "ruta/al/script.py"])
    
    return 'Script ejecutado correctamente'

if __name__ == '__main__':
    app.run()
