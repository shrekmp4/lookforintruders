# @/srkdev - https://github.com/shrekmp4
import psutil
import socket

def listar_conexiones():
    conexiones = psutil.net_connections(kind='inet')
    print(f"{'PROTOCOLO':<10}{'LOCAL':<25}{'REMOTO':<25}{'ESTADO':<15}{'PROCESO':<30}{'RUTA':<50}")
    print("=" * 130)
    
    for conn in conexiones:
        laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "-"
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "-"
        estado = conn.status
        
        try:
            proceso = psutil.Process(conn.pid)
            nombre = proceso.name()
            ruta = proceso.exe()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            nombre = "Desconocido"
            ruta = "-"
        
        protocolo = "TCP" if conn.type == socket.SOCK_STREAM else "UDP"
        print(f"{protocolo:<10}{laddr:<25}{raddr:<25}{estado:<15}{nombre:<30}{ruta:<50}")

if __name__ == "__main__":
    listar_conexiones()
