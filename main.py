from pathlib import Path
import subprocess
import sys

def main():
    scripts_folder = Path("scripts")
    script_names = ["ETL.py", "tratamento_base_externa.py", "integracao.py"]

    def run_script(script_path):
        try:
            print(f"Executando {script_path}...")
            result = subprocess.run(["python", str(script_path)], check=True, capture_output=True, text=True)
            print(f"{script_path} finalizado com sucesso.")
            print("Saída:", result.stdout.strip())
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar {script_path}.")
            print("Saída de erro:", e.stderr.strip())
            sys.exit(1)
    for script_name in script_names:
        run_script(scripts_folder / script_name)

if __name__ == "__main__":
    main()