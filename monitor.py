import paramiko

def ssh_connect(host, user, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=user, password=password)
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode()
    client.close()
    return output

# ------ Linux ------

linux_host = "192.168.145.x"
linux_user = "user1"
linux_pass = "teste.1"

cpu_linux = ssh_connect(linux_host, linux_user, linux_pass, "top -bn1 | grep 'Cpu(s)'")
mem_linux = ssh_connect(linux_host, linux_user, linux_pass, "free -h")

print("--- Linux ---")
print(cpu_linux)
print(mem_linux)

# ---- Windows ----

windows_host = "192.168.145.x"
windows_user = "user1"
windows_pass = "teste.1"

command_windows_cpu = "powershell -Command \"(Get-CimInstance Win32_Processor).LoadPercentage\""
command_windows_mem = "powershell -Command \"Get-CimInstance Win32_OperatingSystem | Select-Object FreePhysicalMemory,TotalVisibleMemorySize\""

cpu_win = ssh_connect(windows_host, windows_user, windows_pass, command_windows_cpu)
mem_win = ssh_connect(windows_host, windows_user, windows_pass, command_windows_mem)

print("--- Windows ---")
print(cpu_win)
print(mem_win)

with open("status.txt", "w") as f:
    f.write("====== STATUS DAS MÁQUINAS ======\n\n")

    f.write("----- Linux -----\n")
    f.write(f"CPU: {cpu_linux}%\n")
    f.write(f"Memória: {mem_linux}\n\n")

    f.write("----- Windows -----\n")
    f.write(f"CPU: {cpu_win}%\n")
    f.write(f"Memória: {mem_win}\n")


