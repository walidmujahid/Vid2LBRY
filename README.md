# Vid2LBRY - YouTube to LBRY Video Uploader
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Free Imam Jamil](https://i.imgur.com/x0LVzeZ.png)](https://www.imamjamilactionnetwork.org/)

Vid2LBRY is a Python script that allows you to process YouTube videos and upload them to the LBRY network. It automates the process of downloading YouTube videos, converting them to MP4 format (if necessary), and uploading them to LBRY for decentralized video hosting.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Command-line Options](#command-line-options)
- [Web App Integration](#web-app-integration)
- [Future Plans](#future-plans)
- [Contributing](#contributing)
- [License](#license)

## Installation

To use Vid2LBRY, you need to have Python and the required dependencies installed. Start by cloning this repository:

```bash
git clone https://github.com/yourusername/vid2lbry.git
cd vid2lbry
```

Next, install the required Python packages by running:

```bash
pip install -r requirements.txt
```

### PyBRY

Vid2LBRY uses [PyBRY](https://github.com/osilkin98/PyBRY). The wrapper has been pre-generated and included in the Vid2LBRY package.


## Configuration

Vid2LBRY uses a configuration file (`config.ini`) to specify various settings, including database connection details, LBRY channel ID, and downloader options. You can customize these settings according to your needs.

The `config.ini` file has sections for each configuration category:

- **Database**: Contains database connection details for storing video information.
- **LBRY**: Contains the LBRY channel ID for uploading videos to a specific channel.
- **Downloader**: Contains options for the YouTube video downloader, including download archive directory, format, and post-processing options.

You can modify the `config.ini` file to suit your requirements.

Rename `copy-config.ini` to `config.ini` and add your LBRY `channel_id`.

## Usage

Vid2LBRY can be used both as a command-line tool and integrated into a web app. 

### Command-line Usage

To process and upload a YouTube video, use the following command:

```bash
python main.py [YouTube URL]
```

Replace `[YouTube URL]` with the URL of the YouTube video you want to upload to LBRY.

### Web App Integration

If you plan to integrate Vid2LBRY into a web app, you can use the `main.py` script as a backend service. You can submit the YouTube URL from your web app to the backend, and Vid2LBRY will process and upload the video to LBRY in the background. Make sure to handle any errors or responses from the backend accordingly in your web app.

## Command-line Options

The command-line tool supports the following options:

- `[YouTube URL]`: The URL of the YouTube video to process and upload to LBRY.

## Future Plans

- [] Video Metadata Customization: Enable users to customize the metadata of their uploaded videos on LBRY, including options to edit video titles, descriptions, and thumbnail images. This will enhance the discoverability and presentation of content.

- [] Batch Processing: Add support for batch processing, allowing users to upload multiple videos at once. This feature will be beneficial for content creators with a large collection of videos.

- [] YouTube Channels: Ability to transfer entire youtube Channels to LBRY.

- [] YouTube Playlists: Ability to transfer YouTube playlists to LBRY.

- [] YouTube authentication

- [] Batch Processing: Add support for batch processing, allowing users to upload multiple videos at once. This feature will be beneficial for content creators with a large collection of videos.

- [] Multi-Platform Support: Extend support for other video platforms (e.g., Vimeo, Dailymotion) to enable users to upload videos from different sources to LBRY seamlessly. 

## Contributing

Contributions to Vid2LBRY are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

When contributing to this repository, please follow the existing coding style and ensure that your changes do not break any existing functionality. Include clear commit messages and documentation for your changes.

## License

Vid2LBRY is released under the MIT License. See [LICENSE](LICENSE) for more information.

---

Vid2LBRY simplifies the process of uploading YouTube videos to LBRY, allowing users to host their videos on the decentralized LBRY network. It can be used as a standalone command-line tool or integrated into a web app to enable seamless video uploading and sharing on LBRY. Feel free to explore and modify the code to suit your specific use case. Happy video uploading!
