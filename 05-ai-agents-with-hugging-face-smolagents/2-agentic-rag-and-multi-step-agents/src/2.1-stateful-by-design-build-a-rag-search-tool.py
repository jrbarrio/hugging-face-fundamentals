from smolagents import Tool 

class ApplianceSearchTool(Tool):
    name = "appliance_manual_search"
    description = "Search appliance manuals for maintenance and usage information"
    inputs = {"query": {"type": "string", "description": "Question about appliance operation"}}
    output_type = "string"

    # Pass the vector store into the constructor
    def __init__(self, vector_store, k=3):
        super().__init__()
        self.vector_store = vector_store
        self.k = k

    # Accept the query string as input to the forward method
    def forward(self, query):
        # Use self.k here to specify how many chunks to return
        docs = self.vector_store.similarity_search(query, k=self.k)
        return "\n\n".join(doc.page_content for doc in docs) or "No relevant manual sections found."