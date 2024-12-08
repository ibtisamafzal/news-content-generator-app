# AI News Content Generator

## About the Hackathon
This project was developed as part of the BuildwithAI Hackathon, which challenges participants to leverage cutting-edge AI tools and technologies to create innovative solutions. The hackathon focuses on solving real-world problems using AI, emphasizing creativity, technical execution, and impact.

## Project Overview
The **AI News Content Generator** is a web-based application designed to streamline the process of creating engaging content for various social media platforms. Leveraging state-of-the-art AI technologies, the app autonomously fetches news articles, summarizes them, and generates visuals based on user-defined inputs such as tone and target platform. This enables individuals and organizations to save time and effort while maintaining high-quality, platform-specific content.

## Features
- **News Retrieval**: Fetch the latest relevant news articles using the Bing News Search API.
- **Text Summarization**: Generate concise summaries tailored to a specific tone (e.g., humorous, professional) using Hugging Face Transformers.
- **Image Generation**: Create custom images based on the summarized content using Hugging Face Diffusers.
- **Customizable Outputs**: Optimize content for platforms like Instagram, Facebook, and LinkedIn with user-selected options.

## How It Works
1. **User Input**: Enter a news topic, select a tone, and choose a target platform.
2. **News Fetching**: The app retrieves the most relevant news article for the provided topic using Bing News Search.
3. **Summarization**: The app summarizes the article content to match the selected tone.
4. **Image Generation**: A corresponding image is generated using AI-powered models.
5. **Output Display**: The app displays the article, summary, and generated image, ready for use.

## Technologies Used
- **Frontend**: Built with [Streamlit](https://streamlit.io/) for an interactive user interface.
- **APIs**:
  - Bing News Search API for fetching articles.
  - Hugging Face Transformers for summarization.
  - Hugging Face Diffusers for image generation.
- **Backend**: Python-based integration of AI pipelines and APIs.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository-url/news-content-generator-app.git
   cd news-content-generator-app
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up API keys:
   - Add your API keys to a `secrets.env` file in the root directory:
     ```env
     BING_API_KEY=your_bing_api_key
     HUGGINGFACE_API_TOKEN=your_huggingface_api_token
     ```
   - Ensure the `secrets.env` file is listed in `.gitignore` to prevent accidental exposure.
4. Run the app:
   ```bash
   streamlit run src/main.py
   ```

## Usage
1. Open the app in your browser (the link will be provided by Streamlit upon running).
2. Enter a news topic in the prompt field.
3. Choose a tone (e.g., neutral, humorous, professional).
4. Select the target platform (Instagram, Facebook, or LinkedIn).
5. View the generated summary and image. You can download the content or use it directly.

## Contributions
Contributions are welcome! Please fork the repository, make changes, and submit a pull request. Ensure that your code adheres to the project's coding standards and includes appropriate documentation.

## Acknowledgments
We extend our gratitude to the BuildwithAI Hackathon organizers for providing an excellent platform to explore AI's potential and drive innovation. Special thanks to Hugging Face and Microsoft Azure for offering their APIs and tools, enabling us to develop this project.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

