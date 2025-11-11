import os
import sys
import subprocess
from datetime import datetime

def connect_to_shared_folder(shared_folder_path, username, password):
    """Menghubungkan ke shared folder dengan authentikasi"""
    try:
        # Ekstrak server name dari path (contoh: \\10.10.0.113\bahan berita)
        parts = shared_folder_path.split('\\')
        server = parts[2]
        share = parts[3]
        
        # Format: \\server\share
        network_path = f"\\\\{server}\\{share}"
        
        print(f"Mencoba menghubungkan ke: {network_path}")
        
        # Command untuk Windows: net use
        cmd = f'net use "{network_path}" "{password}" /user:{username} /persistent:yes'
        
        # Jalankan command
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✓ Berhasil terhubung ke shared folder")
            return True
        else:
            print(f"❌ Gagal terhubung: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error koneksi: {e}")
        return False


def disconnect_shared_folder(shared_folder_path):
    """Memutuskan koneksi dari shared folder"""
    try:
        parts = shared_folder_path.split('\\')
        server = parts[2]
        share = parts[3]
        network_path = f"\\\\{server}\\{share}"
        
        cmd = f'net use "{network_path}" /delete /yes'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✓ Berhasil memutuskan koneksi")
            return True
        else:
            print(f"❌ Gagal memutuskan koneksi: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def clear_output_folder(folder_path):
    """Menghapus semua file dalam folder output"""
    try:
        if os.path.exists(folder_path):
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                        print(f"🗑️  Menghapus: {filename}")
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f"❌ Gagal menghapus {file_path}: {e}")
            print("✓ Folder output berhasil dibersihkan")
        else:
            print("✓ Folder output belum ada, akan dibuat")
    except Exception as e:
        print(f"❌ Error membersihkan folder: {e}")


def detect_encoding(file_path):
    """Mendeteksi encoding file secara otomatis"""
    encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252', 'windows-1252']
    
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                file.read()
            return encoding
        except UnicodeDecodeError:
            continue
    
    return 'latin-1'


def read_split_and_export(shared_folder_path, result_folder_path, filename, split_char='@_@'):
    try:
         
        file_path = os.path.join(shared_folder_path, filename) 
        print(f"Mendeteksi encoding file...")
        encoding = detect_encoding(file_path)
        print(f"Encoding terdeteksi: {encoding}")
         
        with open(file_path, 'r', encoding=encoding) as file:
            content = file.read()
         
        items = [item.strip() for item in content.split(split_char) if item.strip()]
        
        if not items:
            print("Tidak ada item yang ditemukan.")
            return []
        
        print(f"File: {filename}")
        print(f"Item ditemukan: {len(items)}")
          
        output_folder = result_folder_path

        print("\nMembersihkan folder output...")
        clear_output_folder(output_folder)

        os.makedirs(output_folder, exist_ok=True)
        created_files = []
        for i, item in enumerate(items, 1): 
            number = str(i).zfill(2)
            output_filename = f"{number}.txt"
            output_path = os.path.join(output_folder, output_filename)
            
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(item)
            
            created_files.append(output_path)
            print(f"✓ {output_filename}")
         
        return created_files
        
    except FileNotFoundError:
        print(f"❌ File {filename} tidak ditemukan!")
        return []
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

if __name__ == "__main__": 
    sekarang = datetime.now() 
    bulan_sekarang = sekarang.strftime("%B").upper()
    tanggal_sekarang = sekarang.strftime("%d") 
    shared_folder = f"\\\\10.10.0.113\\bahan berita\\2025\\RUNNING TEXT\\RUNNING TEXT HEADLINE BERITA\\{bulan_sekarang}"
    result_folder = r"C:\CPNS\RUNNING TEXT TERBARU NOVEMBER 2025"
    file_name = f"{tanggal_sekarang}.txt"
    
    # Username dan Password untuk shared folder
    username = "admin"              # Ganti dengan username yang Anda ketahui
    password = "password_anda"      # Ganti dengan password shared folder
  
    print("Memproses file...")
    print("=" * 50)
    print(f"Shared Folder: {shared_folder}")
    print(f"Result Folder: {result_folder}")
    print(f"File Name: {file_name}")
    print("=" * 50)
    
    # Hubungkan ke shared folder terlebih dahulu
    print("\n🔐 Menghubungkan ke shared folder...")
    if not connect_to_shared_folder(shared_folder, username, password):
        print("Gagal menghubungkan ke shared folder. Program dihentikan.")
        sys.exit(1)
    
    print()
    results = read_split_and_export(
        shared_folder_path=shared_folder,
        result_folder_path=result_folder,
        filename=file_name,
        split_char='@_@', 
    )
    
    if results:
        print(f"\n🎉 Proses selesai! {len(results)} file telah dibuat.")
        print(f"File hasil disimpan di: {result_folder}")
    else:
        print("\n😞 Gagal memproses file.")
    
    # Opsional: Putuskan koneksi setelah selesai
    # disconnect_shared_folder(shared_folder)