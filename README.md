# My Building of AI Warehouse Manager

Warehousing Meets AI: A No-Nonsense Guide to Smarter Inventory Management

TL;DR

WealthSense AI represents a sophisticated approach to stock market analysis by combining multiple AI agents, each specialized in different aspects of financial analysis. The system leverages CrewAI and Ollama models to process market data, conduct technical and fundamental analysis, assess risks, and evaluate market sentiment. Through a Streamlit dashboard, it delivers comprehensive investment insights in real-time, demonstrating how AI can transform traditional financial analysis into an automated, intelligent process.

Full Article : [https://medium.com/@learn-simplified/building-wealthsense-ai-the-intelligent-agent-for-advanced-stock-analysis-f50da1eef918


Tech stack
# AI Warehouse Manager Technical Stack

## Frontend Technologies
| Technology | Purpose | Implementation Details |
|------------|---------|------------------------|
| Streamlit | Web Framework | Powers the interactive web interface with built-in components and state management |
| Custom CSS | Styling | Dark theme implementation with professional color schemes and responsive design |
| Session State | User Management | UUID-based session tracking and state persistence |
| Wide Layout | UI/UX | Responsive design with collapsible sidebar and multi-column layout |

## AI and Machine Learning
| Technology | Purpose | Implementation Details |
|------------|---------|------------------------|
| Llama 3.2 (3B) | Language Model | Processes natural language queries and generates contextual responses |
| BAAI/bge-large | Embeddings | Creates document embeddings for semantic search capabilities |
| Vector Store Index | Search Engine | Indexes document content for efficient query processing |
| Markdown Node Parser | Content Processing | Structures document content for AI processing |

## Data Processing
| Technology | Purpose | Implementation Details |
|------------|---------|------------------------|
| Pandas | Data Manipulation | Handles Excel file processing and data transformations |
| DoclingReader | Excel Processing | Specialized reader for extracting structured data from Excel files |
| SimpleDirectoryReader | File Management | Manages document loading and processing pipelines |
| Garbage Collection | Memory Management | Optimizes memory usage during long-running sessions |

## Configuration Management
| Technology | Purpose | Implementation Details |
|------------|---------|------------------------|
| YAML | Settings Storage | Stores application configuration in human-readable format |
| Python Constants | System Values | Defines system-wide constants and configuration values |
| JSON | Model Settings | Manages AI model configurations and parameters |
| Config Loader | Integration | Centralizes configuration management across the application |

## Core Dependencies
| Technology | Purpose | Implementation Details |
|------------|---------|------------------------|
| Asyncio | Async Operations | Enables non-blocking operations for better performance |
| TempFile | File Handling | Manages temporary file operations during document processing |
| NumPy | Numerical Operations | Supports data processing and mathematical operations |
| UUID4 | Unique Identifiers | Generates unique identifiers for session and document tracking |

## Development Tools
| Technology | Purpose | Implementation Details |
|------------|---------|------------------------|
| Python 3.x | Core Language | Primary development language for the entire application |
| Git | Version Control | Manages source code versioning and collaboration |
| Virtual Environment | Dependency Management | Isolates project dependencies and ensures consistency |

## Security Features
| Technology | Purpose | Implementation Details |
|------------|---------|------------------------|
| Session Management | User Isolation | Ensures user data and queries remain isolated |
| File Validation | Upload Security | Validates file types and content before processing |
| Memory Cleanup | Resource Management | Automatically cleans up temporary files and resources |



## Introduction
In today’s fast-paced financial markets, making informed investment decisions requires processing vast amounts of data in real-time — a task that’s becoming increasingly challenging for human analysts alone. Enter WealthSense AI, an innovative platform that brings together artificial intelligence and traditional financial expertise to create a powerful tool for stock market analysis. Imagine having a team of tireless financial experts who can analyze markets 24/7, spot patterns in milliseconds, and process years of historical data in moments — that’s the power of WealthSense AI.
   
## What's This Project About

This article takes you on a journey through building a sophisticated AI-powered stock analysis system. At its core, WealthSense AI utilizes a multi-agent architecture where different AI specialists work together, much like a team of financial experts. The technical analyst agent scrutinizes price patterns and technical indicators, while the fundamental analyst digs deep into company financials. A sentiment analyst monitors market mood through news and social media, and a risk assessment specialist evaluates potential dangers.

The system integrates various modern technologies: the CrewAI framework orchestrates the AI agents, yfinance provides real-time market data, technical analysis tools process market patterns, and Plotly creates interactive visualizations. All of this comes together in a user-friendly Streamlit interface that makes complex financial analysis accessible to both professionals and retail investors.

## Why Work on It?

The integration of AI in business isn’t just a trend — it’s becoming a necessity for survival and growth in modern markets. This article demonstrates how businesses can practically implement AI solutions through WealthSense AI’s example. Here’s why this matters:

Financial Analysis Evolution:

- Traditional analysis methods can’t keep up with the volume and speed of modern markets
- AI can process massive amounts of data and identify patterns humans might miss
- Real-time analysis becomes possible across multiple markets simultaneously

Business Implementation:

- Shows how to break down complex problems into manageable AI tasks
- Demonstrates practical integration of multiple AI agents for better decision-making
- Provides a blueprint for scaling analysis capabilities without proportional cost increase

Competitive Advantage:

- Helps businesses understand how to leverage AI for market intelligence
- Shows how to combine different data sources for more accurate insights
- Demonstrates building user-friendly interfaces for complex AI systems

## Architecture

### My Building of AI Warehouse Manager


![Design Diagram](design_docs/design.jpg)


# Tutorial: My Building of AI Warehouse Manager

## Prerequisites
- Python installed on your system.
- A basic understanding of virtual environments and command-line tools.

## Steps

1. **Virtual Environment Setup:**
   - Create a dedicated virtual environment for our project:
   
     ```bash
     python -m venv My-Building-of-AI-warehouse-manager
     ```
   - Activate the environment:
   
     - Windows:
       ```bash
       My-Building-of-AI-warehouse-manager\Scripts\activate       
       ```
     - Unix/macOS:
       ```bash
       source My-Building-of-AI-warehouse-manager/bin/activate
       ```
   

# Installation and Setup Guide

**Install Project Dependencies:**

Follow these steps to set up and run the  "My Building of AI Warehouse Manager"

1. Navigate to your project directory:
   ```
   cd path/to/your/project
   ```
   This ensures you're in the correct location for the subsequent steps.

2. Install the required dependencies:
   ```
   pip install -r requirements.txt   
   ```
   This command installs all the necessary Python packages listed in the requirements.txt file.


## Run - Hands-On Guide: My Building of AI Warehouse Manager

   ```bash 
     
      # Run 
      streamlit run app.py
      
   ```