import subprocess
import os

def download_mega_folder(mega_link, download_path):
    try:
        # Ensure the download path exists
        os.makedirs(download_path, exist_ok=True)

        # Command to download the entire Mega folder
        command = f"megadl {mega_link} --path={download_path}"
        print(f"Running command: {command}")

        # Execute the command using subprocess
        subprocess.run(command, shell=True, check=True)

        print(f"Download completed successfully to {download_path}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while downloading: {e}")
    except Exception as e:
        print(f"Error: {e}")

if name == "main":
    # Prompt the user for the Mega folder link
    mega_link = input("Enter the Mega.nz folder link: ")

    # Specify the download path (e.g., Download folder)
    download_path = "/storage/emulated/0/Download"  # Update path as needed
    download_mega_folder(mega_link, download_path)
