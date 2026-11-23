# Becoming Her — YouTube Audience Analysis

## Project Overview

This is a Python-based data analytics project designed to research YouTube audiences, understand content trends, analyze competing channels, and identify opportunities for the **Mia Deita | Becoming Her** YouTube channel.

The project combines data collection, data cleaning, exploratory analysis, and visualization to support evidence-based content decisions.

## Project Objectives

- Understand the interests and needs of women in their 20s who want to build a better and more independent life.
- Identify popular topics within personal growth and self-development.
- Analyze relevant YouTube channels and their publicly available performance metrics.
- Explore audience comments to identify recurring questions, challenges, and interests.
- Discover content gaps and opportunities for the Becoming Her channel.
- Translate research findings into actionable content recommendations.

## Research Questions

1. What personal growth topics attract attention on YouTube?
2. What challenges and questions do viewers frequently discuss?
3. Which videos and content formats perform well among relevant channels?
4. What audience needs are not adequately addressed by existing content?
5. What content opportunities could help position Becoming Her?

## Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Data collection and analysis |
| YouTube Data API v3 | Access publicly available YouTube data |
| Pandas | Data cleaning and manipulation |
| OpenPyXL | Excel file creation and processing |
| Google API Python Client | Connect Python to YouTube Data API |
| python-dotenv | Secure API key management |
| Git and GitHub | Version control and portfolio documentation |
| VS Code | Development environment |

## Planned Project Workflow

1. **Environment Setup** — Configure Python, install dependencies, and prepare the project.
2. **API Integration** — Connect to YouTube Data API v3.
3. **Data Collection** — Gather public channel, video, and comment data.
4. **Data Cleaning** — Prepare collected data for analysis.
5. **Audience Analysis** — Identify recurring interests, questions, and challenges.
6. **Competitor Analysis** — Examine relevant channels and their public performance.
7. **Exploratory Data Analysis** — Identify patterns, trends, and content opportunities.
8. **Visualization and Reporting** — Present findings through charts and reports.
9. **Content Strategy** — Develop evidence-based recommendations for Becoming Her.

## Current Project Status

**Completed**
- Python virtual environment created.
- Required Python libraries installed.
- Google Cloud project created.
- YouTube Data API v3 enabled.
- API key configured using an environment variable.
- Successful test connection to YouTube Data API v3.
- Git repository initialized.
- First commit created and pushed to GitHub.

**Planned**
- Build automated YouTube data collection scripts.
- Collect relevant channel and video information.
- Analyze audience comments and recurring themes.
- Develop competitor and content opportunity analyses.
- Create visualizations and research reports.

## Project Structure

```text
becoming-her-research/
│
├── .gitignore
├── .env                  # Private API credentials (not uploaded)
├── README.md
├── test_youtube_api.py
│
└── .venv/                # Python virtual environment (not uploaded)
```

Additional folders and scripts will be added as the project develops.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/deitamia/becoming-her-youtube-audience-analysis.git
cd becoming-her-youtube-audience-analysis
```

### 2. Create and activate a virtual environment

For Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install the required libraries

```powershell
python -m pip install google-api-python-client pandas openpyxl python-dotenv
```

### 4. Configure your API key

Create a `.env` file in the project root and add:

```text
YOUTUBE_API_KEY=your_api_key_here
```

Replace the placeholder with your own YouTube Data API key.

**Security note:** Never publish your API key or upload your `.env` file to GitHub.

### 5. Test the API connection

```powershell
python test_youtube_api.py
```

## Data and Research Limitations

This project uses publicly accessible information through the YouTube Data API v3.

It does not provide access to private competitor analytics such as:
- Click-through rate (CTR)
- Audience retention
- Watch time
- Private audience demographics
- Revenue and monetization data

All findings will be interpreted within the limitations of publicly available data and YouTube API quota restrictions.

## Intended Deliverables

- Cleaned YouTube research datasets
- Channel and video performance analysis
- Audience comment and topic analysis
- Competitor benchmarking
- Data visualizations
- Content opportunity recommendations
- YouTube channel positioning and content strategy

## Project Owner

**Mia Deita**

Digital Creator | Aspiring Data Analyst

YouTube Channel: Mia Deita | Becoming Her

GitHub: [@deitamia](https://github.com/deitamia)

---

*This project is an ongoing research and portfolio initiative. Its findings will evolve as more data is collected and analyzed.*
