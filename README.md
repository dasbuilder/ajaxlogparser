# WP Engine Admin-AJAX Log Parser

A Python program for parsing Admin-AJAX log files that are generated as part of a troubleshooting process. You can read more about enabling the Admin-AJAX log from WP Engine's [Support guide](https://wpengine.com/support/admin-ajax/#Admin_AJAX_Log).

Before running this program, you'll need to download the file locally.

## Installation

These instructions assume you already have Python version 3 installed and access to GitHub and access to clone repositories.

1. Use git clone to download the repo

```bash
git clone https://github.com/dasbuilder/ajaxlogparser.git
```

2. In the repo directory that's created from **Step 1**, create the virtual environment

```bash
python -m venv ajaxparser
source ajaxparser/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

That's it! You should now be ready to use this program!

## Example usage

```bash
python main.py -f ajax.log
```

-----

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Maintainer

This SDK is maintained by Spencer Anderson (spencer.anderson@wpengine.com). For any questions, issues, or contributions, please reach out directly.