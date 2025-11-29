# 🐦‍🔥 Phoenix AI Tutor

   **Phoenix AI Buddy** is an intelligent multi-agent system that provides personalized programming assistance through specialized AI agents. It helps learners and developers get instant help with programming concepts, code review, debugging, practice exercises, and code generation through a professional chat interface.

The project demonstrates advanced multi-agent workflows, intelligent query routing, session management, and real-time AI-powered assistance using Google's Gemini models.

---

## 🚀 Features

- **🤖 Multi-Agent System** - Six specialized AI agents working in coordination  
- **💬 Professional Chat Interface** - Clean, dark-themed Streamlit UI  
- **🎯 Intelligent Query Routing** - Automatic agent selection based on user needs  
- **📊 Session Management** - Track learning progress and concepts covered  
- **🔍 Observability** - Monitor agent usage and system performance  
- **🚀 Real-time Processing** - Instant responses with parallel agent execution  
- **🎨 Custom Branding** - Professional UI with custom logo support  

---

## 🧠 How It Works

1. **User Input** → Message sent through the chat interface  
2. **Intelligent Routing** → Orchestrator analyzes query and selects appropriate agents  
3. **Parallel Processing** → Multiple specialized agents work simultaneously  
4. **Response Synthesis** → Orchestrator combines agent outputs into coherent response  
5. **Progress Tracking** → Session updated with concepts and exercises completed  

---

## 🤖 Agent System

| Agent                  | Role                  | Specialization                               |
|------------------------|-----------------------|----------------------------------------------|
| **General Chat**       | Casual conversation   | Friendly interaction and general questions   |
| **Concept Explainer**  | Educational content   | Clear explanations with examples & analogies |
| **Code Reviewer**      | Code analysis         | Quality improvements and best practices      |
| **Debugging Agent**    | Error fixing          | Problem identification and resolution        |
| **Practice Generator** | Exercise creation     | Custom learning challenges                   |
| **Code Generator**     | Code creation         | Complete solution building                   |

---

## 🏗 Architecture

```
User Input → Orchestrator Agent
                |
        ┌───────┼───────┼────────────────┐
        ▼       ▼       ▼                ▼
General Chat  Concept   Code          Debugging
   Agent     Explainer Reviewer        Agent
                    |      |              |
                    ▼      ▼              ▼
              Practice   Code          Session
             Generator  Generator     Management
               Agent     Agent
```

---

## 🔁 Workflow

1. **Query Analysis** - Orchestrator analyzes user input and context  
2. **Agent Selection** - Routes to appropriate specialized agents  
3. **Parallel Execution** - Agents process query simultaneously  
4. **Response Integration** - Unified response synthesis  
5. **Progress Tracking** - Session updates with learning metrics  

---

## 📦 Project Structure

```
phoenix-multi-agent-tutor/
│
├── src/
│   ├── agents/
│   │   ├── base_agent.py
│   │   ├── concept_explainer.py
│   │   ├── code_reviewer.py
│   │   ├── debugging_agent.py
│   │   ├── practice_generator.py
│   │   ├── code_generator.py
│   │   └── general_chat.py
│   │
│   ├── core/
│   │   ├── orchestrator.py
│   │   ├── session_manager.py
│   │   └── observability.py
│   │
│   ├── utils/
│   │   └── helpers.py
│   │
│   └── main.py
│
├── requirements.txt
├── .gitignore
├── README.md
└── phoenix.py
```

---

## 🛠 Tech Stack

- **Python** - Core programming language  
- **Streamlit** - Web interface and chat UI  
- **Google Gemini AI** - LLM powering all AI agents  
- **Custom CSS** - Professional dark-themed styling  
- **Session Management** - Progress tracking and analytics  

---

---

## ⚙️ Setup

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Lloyd-Hansen/phoenix-ai-buddy.git
   cd phoenix-ai-buddy
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variable**
   
   **Windows (Command Prompt):**
   ```cmd
   set GOOGLE_API_KEY=your_actual_api_key_here
   ```
   
   **Windows (PowerShell):**
   ```powershell
   $env:GOOGLE_API_KEY="your_actual_api_key_here"
   ```
   
   **macOS/Linux:**
   ```bash
   export GOOGLE_API_KEY=your_actual_api_key_here
   ```

   **For permanent setup**, add the environment variable to your system:
   - **Windows**: System Properties → Environment Variables
   - **macOS/Linux**: Add to `~/.bashrc` or `~/.zshrc`

4. **Run the application**
   ```bash
   streamlit run run.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501`

---

## 🎯 Usage Examples

- **💬 General Questions**: "Hello! How are you today?"  
- **📚 Concept Explanations**: "Explain Python decorators with examples"  
- **🔍 Code Review**: Paste your code and ask for improvements  
- **🐛 Debugging Help**: "My function returns None unexpectedly"  
- **💪 Practice**: "Give me a Python list comprehension exercise"  
- **💻 Code Generation**: "Create a Flask REST API endpoint"  

---

## 🔧 Configuration

### Environment Variables

- `GOOGLE_API_KEY` - Your Google Gemini API key (required)
- `APP_ENV` - Application environment (development/production)
- `DEBUG` - Enable debug mode (true/false)
- `LOG_LEVEL` - Logging level (DEBUG/INFO/WARNING/ERROR)

### Customization

- Modify agent prompts in `src/agents/`
- Adjust UI styling in `src/main.py`
- Extend session management in `src/core/session_manager.py`

---

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure `GOOGLE_API_KEY` is set as environment variable
   - Verify the key is valid and has Gemini access
   - Restart your terminal/IDE after setting the environment variable

2. **Import Errors**
   - Check all dependencies are installed: `pip install -r requirements.txt`
   - Verify Python version is 3.8+

3. **Streamlit Connection Issues**
   - Check if port 8501 is available
   - Try: `streamlit run run.py --server.port 8502`

4. **Environment Variable Not Found**
   - Verify the environment variable is set in the same terminal session
   - Check for typos in the variable name
   - Restart the application after setting the variable

---

## 📌 Limitations

- Requires Google Gemini API key as environment variable
- Internet connection required for AI model access
- Response quality depends on model capabilities
- Session data is stored in memory (resets on restart)

---

## 🎯 Future Enhancements

- **Persistent Sessions** - Database integration for long-term progress tracking
- **Multi-language Support** - Expand beyond Python programming
- **Advanced Analytics** - Detailed learning progress insights
- **Export Capabilities** - Save conversations and exercises
- **Plugin System** - Custom agent development framework
- **Mobile App** - Native mobile application

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support

- Create an [Issue](https://github.com/Lloyd-Hansen/phoenix-ai-buddy/issues)
- Email: kevinlevin2385@gmail.com

---

<div align="center">

**Built with 🧠 using python, Streamlit and Google Gemini AI**

[Report Bug](https://github.com/Lloyd-Hansen/phoenix-ai-buddy/issues) · [Request Feature](https://github.com/Lloyd-Hansen/phoenix-ai-buddy/issues)

</div>
