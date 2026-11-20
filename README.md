# CityPulse

CityPulse is a Linux and Windows Subsystem for Linux (WSL) practice repository. It documents hands-on exercises covering directory management, file operations, system monitoring, shell scripts, permissions, and basic environment commands.

The repository is primarily a learning artifact: it contains text files and command screenshots rather than an application or executable service.

## Repository Overview

| Item | Description |
| --- | --- |
| `README.md` | Project documentation |
| `script.sh` | Shell script placeholder; currently empty |
| `data/` | Text files used in Linux file-management exercises |
| `linux/` | Duplicate/organized Linux exercise files |
| `task1.png`, `task1.1.png` | WSL and directory setup screenshots |
| `task 2.png`, `task2.1.png` | Directory/file move and cleanup screenshots |
| `task 3.png` | Disk usage and system filesystem screenshot |
| `task 4.png` | Shell script, permission, and process screenshots |
| `task 5.png` | Environment and user identity command screenshot |
| `wsl installed.png` | WSL installation screenshot |
| `1.png`, `22.png` | Initial Linux exercise screenshots |

## Completed Exercises

### 1. WSL and Directory Setup

- Installed and verified WSL.
- Opened Ubuntu through WSL.
- Created a working directory with `mkdir`.
- Listed repository and directory contents with `ls`.
- Practiced moving files into new directories.

Relevant evidence: `wsl installed.png`, `task1.png`, and `task1.1.png`.

### 2. File and Directory Operations

The exercises demonstrate common Linux file-management commands:

```bash
mkdir temp-dir
mkdir data linux
ls
mv README.md temp-dir
mv temp-dir/README.md .
rm -r linux
```

Other operations include:

- Creating text files and directories.
- Moving files between folders.
- Listing directory contents.
- Removing directories.
- Organizing exercise data into `data/` and `linux/`.

Relevant evidence: `task 2.png` and `task2.1.png`.

### 3. Filesystem and System Information

The system-information exercise uses commands to inspect mounted storage and the runtime environment.

```bash
ls
df
df -h
mount
```

The completed screenshot shows filesystem sizes, available space, mount points, and WSL-mounted Windows drives.

Relevant evidence: `task 3.png`.

### 4. Shell Scripts, Permissions, and Processes

The exercises cover shell script creation and Linux permissions.

```bash
touch script.sh
ls
ls -l script.sh
chmod +x script.sh
chmod 644 script.sh
ps aux
```

Key concepts demonstrated:

- Creating an empty shell script with `touch`.
- Viewing file permissions with `ls -l`.
- Making a script executable with `chmod +x`.
- Restoring standard read/write permissions with `chmod 644`.
- Inspecting running processes with `ps aux`.

The repository's `script.sh` is currently empty and can be used as the starting point for future script work.

Relevant evidence: `task 4.png`.

### 5. Environment and User Commands

The final exercise demonstrates Linux identity and environment commands:

```bash
whoami
id
id -run
echo "$USER"
echo "$SUSER"
logname
hostname
uname
uname -a
who
w
id -un
```

These commands show:

- The current user name.
- User and process IDs.
- Login and hostname information.
- Kernel and system details.
- Active logged-in users and system uptime.

Environment variables such as `$USER` and system values are displayed directly in the terminal.

Relevant evidence: `task 5.png`.

## Data Files

The `data/` and `linux/` directories contain simple text data used while practicing copy and move operations.

Example contents:

```text
students
hello
Hello Students
```

Additional files include:

- `data/data3.txt`
- `data/data4.txt`
- `linux/data1.txt`
- `linux/data3.txt`
- `linux/data5.txt`
- `linux/data6.txt`

## Getting Started

### Prerequisites

- Windows 10 or Windows 11
- WSL enabled
- An installed Linux distribution, such as Ubuntu
- Git

### Clone the Repository

```bash
git clone https://github.com/sup6-ai/CityPulse.git
cd CityPulse
```

### Open the Exercises in WSL

```bash
wsl
cd /mnt/c/Users/<your-user>/Desktop/CityPulse_Supriya/CityPulse
ls
```

Replace the path with the location of the repository on your system.

## Suggested Git Workflow

```bash
git status
git add .
git commit -m "Complete Linux exercise"
git push origin main
```

## Learning Outcomes

This repository demonstrates practical familiarity with:

- Installing and using WSL.
- Working in the Linux terminal.
- Creating and organizing directories.
- Creating, moving, copying, and removing files.
- Inspecting disk and filesystem usage.
- Managing file permissions.
- Viewing running processes.
- Reading environment variables.
- Identifying the logged-in user and system.
- Adding command evidence and documentation to Git.

## Screenshots

The PNG files provide visual evidence of the commands executed during each exercise. Open them directly in GitHub or a local image viewer to review the terminal output.
