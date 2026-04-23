import subprocess
import sys

# Lista de scripts na ordem desejada
scripts = ["ETL.py", "tratamento_base_externa.py", "integracao.py"]

for script in scripts:
    try:
        print(f"🔹 Executando {script}...")
        # Executa o script e aguarda terminar
        result = subprocess.run(
            ["python", script],
            check=True,  # Lança exceção se o script retornar erro
            capture_output=True,
            text=True
        )
        print(f"✅ {script} finalizado com sucesso.")
        print("Saída:", result.stdout.strip())

    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar {script}.")
        print("Saída de erro:", e.stderr.strip())
        sys.exit(1)  # Interrompe a sequência se houver falha
