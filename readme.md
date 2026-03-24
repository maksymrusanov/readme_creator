# README Creator

A streamlined CLI tool designed to automate the generation of professional, high-quality `README.md` files for software projects. This tool ensures consistency across repositories by following industry standards and technical writing best practices.

## Description

**README Creator** simplifies the documentation process by providing a structured framework for project metadata. It helps developers move from a bare repository to a fully documented project in minutes, ensuring that essential information like installation steps, usage instructions, and licensing are never overlooked.

## Features

- **Automated Scaffolding**: Generates a standard Markdown structure instantly.
- **Interactive CLI**: Prompts the user for project-specific details to ensure accuracy.
- **Consistency**: Maintains a uniform look and feel across all your GitHub repositories.
- **Markdown Optimized**: Produces clean, lint-friendly Markdown syntax.

## Installation

To install and set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone git@github.com:maksymrusanov/readme_creator.git
   cd readme_creator
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To generate a new README file, run the main script from your terminal:

```bash
python main.py
```

Follow the on-screen prompts to enter your project name, description, features, and other relevant details. Once completed, a `README.md` file will be generated in your current working directory.

### Example
```text
? Project Title: My Awesome App
? Description: A brief summary of the application...
? License: MIT
...
[SUCCESS] README.md has been generated successfully!
```

## Contributing

Contributions are welcome! To contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a Pull Request.

Please ensure your code adheres to the existing style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.