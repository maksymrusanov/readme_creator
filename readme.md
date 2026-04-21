# Readme Creator

A streamlined command-line interface (CLI) tool designed to help developers generate professional, standardized, and high-quality `README.md` files for their projects in seconds.

## Description

**Readme Creator** automates the tedious process of writing project documentation. By providing an interactive prompt-based workflow, it ensures that your repositories include essential sections required for open-source best practices, helping other developers understand, install, and contribute to your work effectively.

## Features

- **Interactive Prompts:** Step-by-step guidance to gather project details.
- **Pre-defined Templates:** Built-in structures following industry standards.
- **Dynamic Content Generation:** Automatically populates sections like Installation, Usage, and License.
- **Lightweight:** Minimal dependencies for fast execution.
- **Markdown Optimized:** Generates clean, valid Markdown syntax ready for GitHub/GitLab.

## Installation

To install the project locally, ensure you have [Python](https://python.org/) installed, then follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/maksymrusanov/readme_creator.git
   ```

2. **Navigate to the directory:**
   ```bash
   cd readme_creator
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the interactive generator, run the following command in your terminal:

```bash
python src/main.py
```

Follow the on-screen prompts to enter your github url. Once completed, a `README.md` file will be generated in your current working directory.

## Contributing

Contributions are welcome! To contribute to this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a Pull Request.

Please ensure your code adheres to the existing style and includes appropriate tests where applicable.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
