# README Creator

A streamlined command-line utility designed to automate the generation of professional, standardized `README.md` files for software repositories.

## Description

**README Creator** simplifies the documentation process by providing a structured workflow for generating high-quality project documentation. It ensures that essential sections—such as installation instructions, usage guides, and licensing—are consistently formatted, allowing developers to focus on code while maintaining high documentation standards.

## Features

- **Interactive CLI:** Guided prompts to capture project-specific metadata.
- **Template-Based Generation:** Uses standardized Markdown templates for consistency.
- **Dynamic Sectioning:** Automatically generates core sections including Description, Features, Installation, and Usage.
- **Developer Friendly:** Lightweight, fast, and easy to integrate into existing workflows.

## Installation

To set up the project locally, clone the repository and install the necessary dependencies.

```bash
# Clone the repository
git clone git@github.com:maksymrusanov/readme_creator.git

# Navigate into the project directory
cd readme_creator

# Install dependencies (assuming a Python-based environment)
pip install -r requirements.txt
```

## Usage

Run the main script to start the interactive generation process:

```bash
python main.py
```

Follow the on-screen prompts to input your project details. Once completed, the tool will output a `README.md` file in the target directory.

### Example

```text
Project Name: My Awesome App
Description: A web-based task manager...
License: MIT
...
[File Generated Successfully]
```

## Contributing

Contributions are welcome to improve the templates or add new features.

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

Distributed under the MIT License. See `LICENSE` for more information.