# DermaCare-AI

---
#### **Streamlit URL**
[Vis-RAG](https://dermacare-ai.streamlit.app)
[TxT-RAG](https://pdiddy-ifq52ac4nzsss9k4t4n93o.streamlit.app/)

#### **Project Overview**
The Multi-Modal Medical Assistant (MMA) is a cutting-edge tool designed to enhance healthcare diagnostics by integrating visual and textual data analysis. It employs Visual Retrieval-Augmented Generation (VIS-RAG) and Text Retrieval-Augmented Generation (Text-RAG) pipelines to process multi-modal medical data, providing efficient and accurate classification tasks. The system is augmented with LangSmith for evaluation, monitoring, and debugging, ensuring transparency and robust performance.

---

#### **Key Components**

##### **VIS-RAG: Visual Data Pipeline**
- **Input:** Image of the skin disease.
- **Embedding Model:** Encodes image features into vector embeddings for similarity analysis.
- **Image Index:** Stores embeddings for efficient retrieval.
- **Metadata Annotations:** Adds labels and contextual information to the embeddings.
- **Generator:** Produces outputs like diagnostic insights or annotated images.
- **Output:** Image-based diagnostic results or features aiding clinical decision-making.

##### **Text-RAG: Text Data Pipeline**
- **Input:** Textual data such as symptoms or medical reports.
- **Text Database:** Retrieves relevant medical knowledge using embeddings.
- **Conversational Augmentation:** Dynamically queries users to refine inputs for better context.
- **Generator:** Processes inputs and retrieved data to generate detailed diagnostic insights.
- **Output:** Text-based results providing comprehensive diagnostic details.

##### **Integration Workflow**
1. VIS-RAG and Text-RAG independently process visual and textual inputs.
2. Outputs are combined using a Decision Model to produce a unified result.
3. LangSmith tools monitor and trace data flow, ensuring debugging ease and operational transparency.

---

#### **Features & Benefits**
- **Multi-Modal Retrieval:** Enriches analysis by combining visual and textual embeddings.
- **Dynamic Input Augmentation:** Iteratively refines inputs for higher diagnostic accuracy.
- **LangSmith Monitoring:** Tracks workflows, ensuring transparency and debugging efficiency.
- **Efficient Storage:** Employs vector indexing for scalable and fast data retrieval.
- **Comprehensive Insights:** Generates actionable diagnostic results through integrated data analysis.

---

#### **Applications**
1. **Healthcare Diagnostics:** Supports correlating medical images (e.g., radiology, dermatology, pathology) with textual data (e.g., patient records).
2. **Enhanced Decision-Making:** Processes images and text to deliver precise and actionable insights.
3. **Use in Dermatology:** VIS-RAG efficiently analyzes skin disease images, aiding accurate diagnoses.
4. **Textual Insights:** Text-RAG evaluates symptoms and histories, offering valuable support for healthcare professionals.

---

#### **Snowflake Integration**
The project leverages **Snowflake** as a scalable and efficient data storage and analytics solution. Snowflake supports:
- Centralized storage for large datasets, including images and textual data.
- High-performance querying for retrieving patient data and embedding vectors.
- Seamless integration with multi-modal pipelines, enabling efficient data management.

---

#### **Conclusion**
The Multi-Modal Medical Assistant bridges the gap between visual and textual diagnostics, advancing healthcare through innovative AI-driven solutions. By integrating VIS-RAG and Text-RAG pipelines with dynamic retrieval and Snowflake's robust data capabilities, this tool provides personalized care and supports advanced medical research, ensuring improved patient outcomes.
