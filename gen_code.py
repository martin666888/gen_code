import subprocess

result = subprocess.run(['pip', 'list'], capture_output=True, check=True, text=True)

print(result.stdout)