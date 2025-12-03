from fastapi import FastAPI

app = FastAPI()

@app.put("/vectorize_markdown/{file_name}")
def vectorize_markdown(file_name: str):
    pass

@app.put("/vectorize_source/{source_name}")
def vectorize_source(source_name: str):
    pass

@app.put("/vectorize_notebook/{notebook_name}")
def vectorize_notebook(notebook_name: str):
    pass



