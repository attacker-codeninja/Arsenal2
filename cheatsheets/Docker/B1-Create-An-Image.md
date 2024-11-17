
# Kali Linux Docker Cheatsheet

This cheatsheet guides you through creating, customizing, and using a **Kali Linux Docker image** for penetration testing.

---

## 1. Pull the Official Kali Linux Docker Image
Download the prebuilt official Kali Linux image from Docker Hub:
```
docker pull kalilinux/kali-rolling
```

---

## 2. Verify the Image
Check if the image was successfully downloaded:
```
docker images
```
You should see `kalilinux/kali-rolling` in the list.

---

## 3. Run the Kali Linux Container
Start a container interactively:
```
docker run -it --name kali-container kalilinux/kali-rolling /bin/bash
```
- `-it`: Interactive mode with a terminal.
- `--name kali-container`: Assigns a custom name to the container.

---

## 4. Install Kali Linux Tools
Once inside the container, install desired tools:

### Update and Upgrade Packages
```
apt update && apt upgrade -y
```

### Install Common Tools
```
apt install -y kali-tools-top10 kali-linux-headless net-tools
```

---

## 5. Save Changes to a New Image
To persist the changes made in the container:

1. Exit the container:
   ```
   exit
   ```
2. Commit the changes:
   ```
   docker commit kali-container custom-kali-image
   ```

---

## 6. Run the Customized Kali Image
Launch a container using the customized image:
```
docker run -it --name custom-kali-container custom-kali-image /bin/bash
```

---

## 7. Add Persistent Storage
To ensure files persist between container runs, mount a volume:
```
docker run -it --name kali-with-storage -v /path/to/local/dir:/mnt/shared custom-kali-image /bin/bash
```
- **Example**: Mount `/home/user/kali-data` on your local machine to `/mnt/shared` in the container.

---

## 8. Export and Share the Image
If you want to share the customized image:

1. Save the image as a `.tar` file:
   ```
   docker save -o custom-kali-image.tar custom-kali-image
   ```
2. Transfer the `.tar` file.
3. Import the image on another machine:
   ```
   docker load -i custom-kali-image.tar
   ```

---

## 9. Automate with a Dockerfile (Optional)
To automate the creation of a custom Kali image, use a `Dockerfile`:

### Example `Dockerfile`
```dockerfile
FROM kalilinux/kali-rolling

RUN apt update && apt upgrade -y && \
    apt install -y kali-tools-top10 kali-linux-headless net-tools

CMD ["/bin/bash"]
```

### Build the Image
```
docker build -t custom-kali-image .
```

---

## 10. Manage Containers and Images
- **List all containers**:
  ```
  docker ps -a
  ```
- **Remove a container**:
  ```
  docker rm <container_id_or_name>
  ```
- **Remove an image**:
  ```
  docker rmi <image_id_or_name>
  ```

---

## 11. Useful Docker Commands for Kali
- **Restart a stopped container**:
  ```
  docker start -ai kali-container
  ```
- **Access a running container**:
  ```
  docker exec -it kali-container /bin/bash
  ```
- **Stop a running container**:
  ```
  docker stop kali-container
  ```

---

## 12. Troubleshooting

### Fix apt-key Warnings
```
apt install gnupg -y
apt-key adv --recv-keys --keyserver keyserver.ubuntu.com ED444FF07D8D0BF6
```

### Rebuild a Broken Image
```
docker build --no-cache -t custom-kali-image .
```

---