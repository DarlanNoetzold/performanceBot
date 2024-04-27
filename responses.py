from random import choice, randint
import psutil
from discord import Intents, Client, Message

async def send_large_message(destination, text, chunk_size=2000):
    """Enviar mensagens grandes divididas em múltiplas partes se necessário."""
    for start in range(0, len(text), chunk_size):
        end = min(start + chunk_size, len(text))
        await destination.send(text[start:end])

def get_cpu_usage():
    return f"CPU usage is: {psutil.cpu_percent(interval=1)*10}%"

def get_memory_usage():
    memory = psutil.virtual_memory()
    return f"Memory usage is: {memory.percent}% (Used: {memory.used / (1024 ** 3):.2f} GB, Total: {memory.total / (1024 ** 3):.2f} GB)"

def get_running_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            pid = proc.info['pid']
            name = proc.info['name']
            processes.append(f"PID: {pid}, Name: {name}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass  # Ignorar processos que não podem ser acessados
    return "\n".join(processes)

def get_response(user_input: str) -> str:
    lowered = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'Good, thanks!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    elif 'cpu usage' in lowered:
        return get_cpu_usage()
    elif 'memory usage' in lowered:
        return get_memory_usage()
    elif 'running processes' in lowered:
        return get_running_processes()
    else:
        return choice(['I do not understand...',
                       'What are you talking about?',
                       'Do you mind rephrasing that?'])
