# GoogleSerp

GoogleSerp is a Python class that provides methods for performing Google searches and retrieving search results, including web pages and images.

## Features

- Web search functionality
- Image search functionality
- Uses both direct Google searches and the Serper API as a fallback
- Proxy support for making requests

## Installation

To use GoogleSerp, you need to have Python installed on your system. You also need to install the following dependencies:

```
pip install requests beautifulsoup4
```

## Usage

Here's a basic example of how to use the GoogleSerp class:

```python
from google_serp import GoogleSerp

# Initialize the GoogleSerp object
google_serp = GoogleSerp()

# Perform a web search
web_results = google_serp.webSearch("Python programming", {}, 0)

# Perform an image search
image_results = google_serp.imageSearch("cute cats", {}, 0)

# Use the Serper API for web search
serper_results = google_serp.serper("Machine learning")

# Use the Serper API for image search
serper_img_results = google_serp.serperImg("Beautiful landscapes")
```

## Configuration

The class uses a proxy by default. You can modify the proxy settings in the `__init__` method of the GoogleSerp class.

## API Key

This code uses the Serper API as a fallback. Make sure to replace the API key in the `serper` and `serperImg` methods with your own Serper API key.

## Note

This code is for educational purposes only. Make sure to comply with Google's Terms of Service and the terms of any third-party services used.
