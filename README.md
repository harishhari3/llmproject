# Advanced LLM Project

A comprehensive Large Language Model project built with LangChain, featuring multiple AI providers, RAG capabilities, document processing, and web interfaces.

## Features

### 🤖 Multi-Provider LLM Support
- OpenAI GPT models (GPT-4, GPT-3.5)
- Anthropic Claude
- Local models via Ollama
- Hugging Face transformers

### 📚 RAG (Retrieval Augmented Generation)
- Document ingestion and processing
- Vector embeddings with ChromaDB
- Semantic search and retrieval
- Context-aware responses

### 💬 Interactive Interfaces
- Command-line chat interface
- Web-based chat UI
- RESTful API endpoints
- WebSocket streaming

### 🧠 Advanced Features
- Conversation memory and context
- Document Q&A system
- Code generation and analysis
- Multi-modal support (text, images)

### 🔧 Developer Tools
- Comprehensive testing suite
- Code formatting and linting
- Type checking with mypy
- Docker support

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Environment Variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. **Run the Application**
   ```bash
   # CLI Interface
   python -m src.cli.chat

   # Web Interface
   python -m src.web.app

   # API Server
   python -m src.api.server
   ```

## Project Structure

```
src/
├── core/           # Core LLM interfaces and providers
├── rag/           # RAG system components
├── memory/        # Conversation memory
├── processing/    # Document processing
├── api/           # REST API and WebSocket
├── web/           # Web interface
├── cli/           # Command-line interface
├── config/        # Configuration management
└── tests/         # Test suite

docs/              # Documentation
data/              # Data storage
models/            # Saved models
```

## Configuration

The application uses environment variables for configuration. See `.env.example` for all available options.

## API Documentation

Once running, visit `http://localhost:8000/docs` for interactive API documentation.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

MIT License - see LICENSE file for details.
