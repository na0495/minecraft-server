# Minecraft Server with Docker

This project sets up a Minecraft server using Docker and PaperMC. It includes a `Dockerfile` and a `docker-compose.yml` file, along with support for plugins. The server runs the PaperMC version 1.20.6 with customizable settings for performance and gameplay.

## Prerequisites

- Docker installed on your machine
- Docker Compose installed on your machine

## Project Structure

- **plugins/**: A folder to hold the Minecraft plugins (JAR files) to enhance your server functionality.
- **Dockerfile**: Used to build a custom Docker image for the Minecraft server with PaperMC and plugins.
- **docker-compose.yml**: Defines the services, environment variables, ports, and volumes for the Minecraft server container.

## Usage

### 1. Clone the Repository
Clone the repository to get started:

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Prepare the Plugins
Place any desired plugins inside the `plugins/` directory. These will be automatically copied into the server when you build the Docker image.

Example plugin filenames:
```
plugins/
  ├── EssentialsX.jar
  ├── WorldEdit.jar
```

### 3. Configure the `docker-compose.yml`

The `docker-compose.yml` file contains the configuration for running the Minecraft server using Docker Compose. It defines the server environment variables such as version, memory allocation, and game rules.

```yaml
services:
  mc:
    build: .
    container_name: paper
    environment:
      EULA: "true"
      TYPE: PAPER
      VIEW_DISTANCE: 20
      MEMORY: 10G
      VERSION: 1.20.6
      PAPER_CHANNEL: experimental
      SPIGET_RESOURCES: 31585,64139
      DIFFICULTY: normal
      MAX_PLAYERS: 10
      SNOOPER_ENABLED: FALSE
      SPAWN_PROTECTION: 0
      ONLINE_MODE: FALSE
      ALLOW_FLIGHT: TRUE
      SERVER_NAME: "Potato land"
      OPS:
        na0495
    ports:
      - "32165:25565"
      - "8080:8080"
      - "8123:8123"
    volumes:
      - ./data:/data
    restart: unless-stopped
```

- **EULA**: Accepts the Minecraft End User License Agreement.
- **TYPE**: Specifies PaperMC as the server type.
- **VERSION**: The Minecraft server version (1.20.6).
- **PAPER_CHANNEL**: Specifies the PaperMC channel (`experimental`).
- **SPIGET_RESOURCES**: Resource IDs for automatic downloading of plugins from Spiget.
- **MAX_PLAYERS**: Maximum number of players allowed on the server.
- **MEMORY**: Allocates 10GB of RAM to the server.
- **OPS**: Adds an operator with the username `na0495`.

### 4. Build and Run the Server

To start the Minecraft server, follow these steps:

1. Build the Docker image using the provided `Dockerfile`:

```bash
docker-compose build
```

2. Start the Minecraft server in detached mode:

```bash
docker-compose up -d
```

This will start the Minecraft server in the background. You can view the logs using:

```bash
docker-compose logs -f
```

### 5. Access the Server

- **Minecraft Server**: The server will be accessible at `localhost:32165` (or replace `localhost` with your server's IP address if running remotely).
- **Web Ports**: Additional ports like `8080` and `8123` can be used for web-based plugins or services like Dynmap.

### 6. Stopping the Server

To stop the server, run:

```bash
docker-compose down
```

This will stop and remove the container, but the data (like world files) will remain in the `data/` directory.

### 7. Persistent Data

By default, the server data (world files, settings, logs) are saved in the `./data` folder on your host machine. This ensures that even after restarting the container, your Minecraft world and server settings will persist.

### Customization

- **Plugins**: Add any additional plugins by placing the corresponding `.jar` files inside the `plugins/` folder.
- **Server Settings**: You can further customize settings like difficulty, flight, view distance, etc., through environment variables defined in `docker-compose.yml`.
- **Memory Management**: Adjust the `MEMORY` environment variable to allocate more or less RAM to the server, depending on your system's resources.

### Plugin Management

This setup also supports downloading plugins directly from Spiget using the `SPIGET_RESOURCES` environment variable. Just add the resource IDs to download specific plugins automatically when starting the server.

### Troubleshooting

- **Firewall/Port Forwarding**: Ensure that port `32165` is open for external access and that your firewall is configured correctly.
- **Memory Issues**: If the server runs out of memory, increase the value of the `MEMORY` environment variable in the `docker-compose.yml`.

## License

This project is open-source and available under the MIT License. Feel free to modify and extend it to suit your needs.

Enjoy playing Minecraft with your custom server setup!
