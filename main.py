# import subprocess
# import sys

# # Lista de scripts na ordem desejada
# scripts = ["ETL.py", "tratamento_base_externa.py", "integracao.py"]

# for script in scripts:
#     try:
#         print(f"Executando {script}...")
#         # Executa o script e aguarda terminar
#         result = subprocess.run(
#             ["python", script],
#             check=True,  # Lança exceção se o script retornar erro
#             capture_output=True,
#             text=True
#         )
#         print(f"{script} finalizado com sucesso.")
#         print("Saída:", result.stdout.strip())

#     except subprocess.CalledProcessError as e:
#         print(f"Erro ao executar {script}.")
#         print("Saída de erro:", e.stderr.strip())
#         sys.exit(1)  # Interrompe a sequência se houver falha

from pathlib import Path
import subprocess
import sys

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

scripts_folder = Path("scripts")
script_names = ["ETL.py", "tratamento_base_externa.py", "integracao.py"]

for script_name in script_names:
    run_script(scripts_folder / script_name)