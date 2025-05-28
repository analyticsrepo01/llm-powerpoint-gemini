# PowerPoint Generation with LLM

This repository contains a Jupyter notebook that demonstrates how to generate PowerPoint presentations programmatically using a Large Language Model (LLM). The notebook provides step-by-step instructions on how to interact with the LLM, structure your data, and generate a fully functional PowerPoint presentation.

## Features

- **Automated PowerPoint generation**: Create slides with titles, bullet points, images, and other content dynamically.
- **Large Language Model Integration**: Utilize LLMs to assist in structuring and enhancing your presentation content.
- **Customizable Templates**: Modify the look and feel of your slides to match your presentation style.

## Prerequisites

To run the notebook, you'll need the following dependencies installed in your Python environment:

```bash
pip install from google  pptx jupyter pandas
pip install vertexai langchain_google_vertexai
```

## Usage

1. **Clone the repository:**
```bash
git clone git@github.com:userID/llm-powerpoint.git
cd llm-powerpoint.git
```

2. **Run the Jupyter Notebook:**
Launch Jupyter notebook and open the provided notebook:
```bash
jupyter notebook ppt-gen.ipynb
```

3.	Generate PowerPoint:
    * Follow the instructions within the notebook to provide your input text.
    * Customize the slide structure as needed (titles, bullet points, images, etc.).
    * Run the notebook cells to generate the presentation.

4.	Save the Presentation:
Once generated, the PowerPoint presentation will be saved as a .pptx file in the specified directory.

### Customization

You can customize the slides by modifying the cell responsible for defining slide content. For instance, you can adjust the number of slides, their order, and the content style.

### Contribution
If you’d like to contribute to the development of this project, please feel free to submit a pull request or open an issue

## License

This project is licensed under the MIT License.
