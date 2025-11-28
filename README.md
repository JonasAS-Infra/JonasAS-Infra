# 👋 Olá, eu sou o Jonas!

Sou Analista de Infraestrutura com experiência em ambientes Cloud, On Premise e Hibridos, atuando na admnistração de servidores Linux e Windows, virtualização, redes e automação de tarefas.  
Atualmente estou aprimorando minhas habilidades em Python e Shell Script aplicado à administração de sistemas e criando uma base sólida de projetos práticos para evoluir na carreira de Cloud e SysAdmin.

---

## 🚀 Projetos

### 🔹 1. Monitoramento via SSH (Python + Linux + Windows) 
**Status:** Finalizado  
**Descrição:**  
Criado um ambiente virtual com 3 máquinas (2 servidores e 1 host Linux) conectadas em rede NAT com IPs fixos.  
Desenvolvido um script em Python que se conecta via SSH nos servidores Linux e Windows para coletar:

- Uso de CPU  
- Uso de Memória  
- Processamento e formatação da saída  
- Exportação dos dados para arquivo `.txt`

> **Tecnologias:** Python, Paramiko, Linux (CentOS), Windows Server, SSH, VMware

Repositório do projeto: https://github.com/JonasAS-Infra/Monitoramento-ssh

---

### 🔹 2. Inventário Automático de Servidores (Python + Linux + Windows)
**Status:** Finalizado  
**Descrição:**  
Criado um ambiente com 1 host Linux responsável por coletar informações de inventário de 4 servidores Linux e 1 Windows Server.
Foi desenvolvido um script em Python que:

Lê automaticamente listas de hosts através de arquivos externos (hosts_linux.txt e hosts_win.txt)

Conecta via SSH (Linux) e WinRM (Windows)

Coleta informações como:

- Nome do host

- Versão do sistema

- Tempo de atividade (uptime)

- Trata e formata a saída

- Gera um arquivo .txt com o inventário completo e datado

> **Tecnologias:** Python, Paramiko, WinRM, Linux (CentOS/Ubuntu), Windows Server, SSH, WinRM, VMware

Repositório do projeto: https://github.com/JonasAS-Infra/Automa-o-de-Invent-rio-de-Servidores-Python-

---

### 🔹 3. Coleta de falhas de login (Python + Linux + Windows)
**Status:** Finalizado  
**Descrição:**  
Criado um ambiente com múltiplos servidores (Linux e Windows) para coletar e registrar os últimos eventos de falhas de autenticação.
O script em Python se conecta via SSH (Linux) e WinRM (Windows) para consultar:

- Falhas de login em /var/log/secure (CentOS/RHEL)

- Falhas de login no auth.log (Ubuntu/Debian)

- Eventos de falha de autenticação no Windows (EventID 4625)

- Exportação dos resultados para arquivos .txt dentro da pasta log/

- Tratamento para servidores sem eventos recentes

- Suporte a múltiplos hosts usando arquivos externos (hosts_linux.txt e hosts_win.txt)

> **Tecnologias:** Python, Paramiko, WinRM, Linux (CentOS/Ubuntu), Windows Server, SSH, WinRM, VMware

Repositório do projeto: https://github.com/JonasAS-Infra/Coleta-de-falhas-de-login-Python-Linux-Windows-

---

## 🛠️ Tecnologias & Ferramentas

- **Linux (RHEL / CentOS / Debian)**
- **Windows Server / Active Directory**
- **Firewall Fortgate / Sophos**
- **Backup - VEEAM / Acronis**
- **Python** (Automação, SSH, Scripts)
- **Shell Script**
- **VMware /Citrix/ Hiper-V / Virtualização**
- **Redes (DNS, DHCP, NAT)**
- **Azure & AWS Cloud**  
  - AWS Cloud Practitioner  
  - Azure AZ-900  
  - Em estudo: AWS SysOps / AWS Solutions Architect Associate

---


## 🎯 Objetivo do Portfólio
Este repositório centraliza meus estudos e projetos aplicados ao mundo real, sempre voltados para:

- Automação  
- Infraestrutura  
- Cloud  
- Troubleshooting  
- Aprendizado contínuo

---

## 📫 Contato
Caso queira trocar ideias sobre infraestrutura, cloud ou automação:

**LinkedIn:** https://www.linkedin.com/in/jonas-araújo-de-sousa-299220170/
**E-mail:** jonasaraujodesousa@gmail.com

---

⭐ *Obrigado por visitar meu portfólio! Novos projetos serão adicionados em breve.*

