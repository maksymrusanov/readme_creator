# README Creator

![License](https://img.shields.io/github/license/maksymrusanov/readme_creator)
![Version](https://img.shields.io/github/v/release/maksymrusanov/readme_creator?include_prereleases)
![Build Status](https://img.shields.io/github/actions/workflow/status/maksymrusanov/readme_creator/main.yml)

## Description
README Creator is a specialized utility designed to automate the generation of professional, standardized `README.md` files for software repositories. It streamlines the documentation process by providing a structured framework that ensures all critical project information is captured clearly and concisely.

## Features
*   **Standardized Templates**: Automatically generates essential sections including Installation, Usage, and Configuration.
*   **Badge Integration**: Built-in support for shields.io badges to display build status, licenses, and versions.
*   **Markdown Optimized**: Outputs clean, high-quality Markdown compatible with GitHub, GitLab, and Bitbucket.
*   **CLI Support**: Intuitive command-line interface for rapid documentation generation.
*   **Technical Writing Standards**: Follows industry best practices for technical documentation clarity and accessibility.

## Installation

Clone the repository and install the necessary dependencies:

```bash
# Clone the repository
git clone git@github.com:maksymrusanov/readme_creator.git

# Navigate to the project directory
cd readme_creator

# Install dependencies (example for Python-based tool)
pip install -r requirements.txt
```

## Usage

To generate a new README file, run the creator script and follow the interactive prompts:

```bash
# Basic usage
python main.py --init

# Generate a README from a specific config file
python main.py --config project_details.json --output README.md
```

### Common Example
```python
from readme_creator import Generator

gen = Generator(project_name="My Awesome Project")
gen.add_section("Features", ["Fast", "Reliable", "Scalable"])
gen.render()
```

## Configuration

The project can be configured using environment variables or a local `.env` file:

| Variable | Description | Default |
|----------|-------------|---------|
| `TEMPLATE_PATH` | Path to custom Markdown templates | `./templates` |
| `DEFAULT_LICENSE` | License identifier for new projects | `MIT` |
| `OUTPUT_DIR` | Directory where files are saved | `./output` |

## Contributing

Contributions are welcome to improve the templates and functionality. 
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

Distributed under the [MIT](https://opensource.org/licenses/MIT) License. See `LICENSE` for more information.