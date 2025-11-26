import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import './App.css';

function ImageGrid({ refresh }) {
  const [images, setImages] = useState([]);

  useEffect(() => {
    const fetchImages = async () => {
      try {
        const response = await axios.get('http://localhost:3008/images');
        setImages(response.data);
      } catch (error) {
        console.error('Erro ao buscar imagens:', error);
      }
    };

    fetchImages();
  }, [refresh]);

  return (
    <div className="image-grid">
      {images.map((image, index) => (
        <div key={index} className="image-item">
          <img src={`http://localhost:3008/${image.path}`} alt={`Imagem ${index}`} />
        </div>
      ))}
    </div>
  );
}

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [refresh, setRefresh] = useState(false);
  const fileInputRef = useRef(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
    setPreview(URL.createObjectURL(file));
  };

  const handleUpload = async () => {
    if (!selectedFile) return;

    const formData = new FormData();
    formData.append('image', selectedFile);

    try {
      const response = await axios.post('http://localhost:3008/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      console.log('Upload bem-sucedido:', response.data);
      setRefresh(!refresh); // Atualiza o estado para forçar a atualização do ImageGrid
      setSelectedFile(null); // Limpa o arquivo selecionado
      setPreview(null); // Limpa a pré-visualização
      if (fileInputRef.current) {
        fileInputRef.current.value = ''; // Limpa o valor do input de arquivo
      }
    } catch (error) {
      console.error('Erro no upload:', error);
    }
  };

  return (
    <div className="App">
      <h1>Upload de Imagem</h1>
      <input type="file" onChange={handleFileChange} ref={fileInputRef} />
      {preview && <img src={preview} alt="Preview" width="100" />}
      <button onClick={handleUpload}>Upload</button>
      <ImageGrid refresh={refresh} />
    </div>
  );
}

export default App;
