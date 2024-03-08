from typing import *
from PyPDF2 import PdfReader
from gentopia.tools.basetool import *

class PDF_Reader_Args(BaseModel):
    file_path: str = Field(..., description="Path to the PDF file to be read")

class PDF_Reader_Tool(BaseTool):

    name = "PDF_Reader_Resu"
    description = "Reads and extracts info from PDF files."
    args_schema: Optional[Type[BaseModel]] = PDF_Reader_Args

    def _run(self, file_path: str) -> str:
        print(file_path)
        text = ''
        try:
            reader = PdfReader(file_path)
            for page in reader.pages:
                text += page.extract_text() + '\n\n'
            return text
        except Exception as e:
            return f"Failed to read PDF: {str(e)}"

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        # Async implementation can be similar but would need an async library for PDF reading
        raise NotImplementedError

if __name__ == "__main__":
    # Example usage
    ans = PDF_Reader_Tool()._run("Attention for transformer")
