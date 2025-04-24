import os
import subprocess
import sys

def get_folder_size(path):
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.isfile(fp):
                total += os.path.getsize(fp)
    return total

def format_size(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.1f}{unit}"
        size /= 1024
    return f"{size:.1f}PB"

def get_package_size(pkg_name):
    try:
        result = subprocess.run(['pip', 'show', pkg_name], capture_output=True, text=True)
        location = None
        for line in result.stdout.splitlines():
            if line.startswith('Location:'):
                location = line.split(':', 1)[1].strip()
                break
        if not location:
            return None
        pkg_path = os.path.join(location, pkg_name.lower())
        if not os.path.exists(pkg_path):
            return None
        size = get_folder_size(pkg_path)
        return format_size(size)
    except Exception:
        return None

def main():
    if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help'):
        print("Usage: pip-size")
        sys.exit(0)

    result = subprocess.run(['pip', 'list', '--format=freeze'], capture_output=True, text=True)
    packages = [line.split('==')[0] for line in result.stdout.splitlines()]

    for pkg in packages:
        size = get_package_size(pkg)
        if size:
            print(f"{pkg}: {size}")
        else:
            print(f"Cannot get size for {pkg}")

if __name__ == '__main__':
    main()
