# MCP-GroundX RAG Integration: AI-Powered Document Search Server

A Model Context Protocol (MCP) server that integrates with GroundX RAG platform to enable AI assistants to search and retrieve information from document collections.

## 🚀 Features

- **RAG Integration**: Seamless integration with GroundX's document search capabilities
- **MCP Protocol**: Standard protocol for AI tool integration
- **Semantic Search**: Advanced document retrieval using vector embeddings
- **Real-time Queries**: Fast, responsive document search
- **Secure API Management**: Environment-based configuration

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **FastMCP** - MCP server framework
- **GroundX SDK** - Document search and RAG platform
- **python-dotenv** - Environment variable management

## 📋 Prerequisites

- Python 3.7+
- GroundX account and API key
- Git

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd MCP
   ```

2. **Install dependencies**
   ```bash
   pip install mcp-server-fastmcp groundx python-dotenv
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` file and add your GroundX API key:
   ```
   GROUNDX_API_KEY=your_groundx_api_key_here
   ```

## 🚀 Usage

1. **Start the MCP server**
   ```bash
   python3 server.py
   ```

2. **Connect with MCP clients**
   The server provides a tool called `search_doc_for_rag_context` that accepts query strings and returns relevant document excerpts.

## 📁 Project Structure

```
MCP/
├── server.py          # Main MCP server implementation
├── .env               # Environment variables (not in repo)
├── .env.example       # Example environment file
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## 🔧 Configuration

### Environment Variables

- `GROUNDX_API_KEY`: Your GroundX API key (required)

### GroundX Database

The server is configured to search GroundX database ID `19859`. To use a different database:

1. Update the `id` parameter in `server.py`:
   ```python
   response = client.search.content(
       id=YOUR_DATABASE_ID,  # Change this
       query=query,
       n=10,
   )
   ```

## 🛠️ API Reference

### MCP Tool: `search_doc_for_rag_context`

**Parameters:**
- `query` (string): Search query for document retrieval

**Returns:**
- `string`: Relevant document excerpts from GroundX database

**Example:**
```python
# Query for aircraft specifications
result = search_doc_for_rag_context("MIG 29 aircraft dimensions")
```

## 🔒 Security

- API keys are stored in environment variables (not in code)
- `.env` file is excluded from version control
- Use `.env.example` as a template for configuration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [GroundX](https://groundx.ai/) for the RAG platform
- [Model Context Protocol](https://modelcontextprotocol.io/) for the integration standard
- [FastMCP](https://github.com/microsoft/mcp) for the server framework

## 📞 Support

For issues and questions:
- Create an issue in this repository
- Check the [GroundX documentation](https://docs.groundx.ai/)
- Review [MCP documentation](https://modelcontextprotocol.io/) 