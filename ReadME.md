**New commands in docker-compose.yml:**

"healthcheck":does a health check for the 'minio' service 
       -test: uses curl command to check the Minio health endpoint 
       -interval: each 30 seconds we perform the health check
       -timeout: max time to wait for the health check to complete in this case 20 seconds
       -retries: number of failures required to mark the service as unhealthy

"networks": app-network with bridge type of network, this creates an isolated network where services communicate with eachother

**Usage:**
1. clone the repository 
2. run the command: docker compose up --build 
3. An image file is uploaded to the minio port 9001 (since port 9000 is busy): docker3.jpeg
4. Add an image or a text file to the repository and in the upload.py python file include the name and the path
5. Run the python file upload.py 
6. Navigate to the Browser and go to http://localhost/9001 and login  to minio account :
   username:minioadmin
   password:minioadmin
7. You should see the file you added stored after clicking on mybucket 
8. Under Myactions:click preview to see the image or download to download it.
