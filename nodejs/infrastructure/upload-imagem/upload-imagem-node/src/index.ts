import express from 'express';
import multer from 'multer';
import path from 'path';
import cors from 'cors';
import { Imagem } from './repository';

const app = express();
const port = 3008;

// Configuração do CORS
app.use(cors({
    origin: 'http://localhost:3000'
}));

// Configuração do Multer
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/');
  },
  filename: (req, file, cb) => {
    cb(null, `${Date.now()}-${file.originalname}`);
  }
});

const upload = multer({ storage });


// Endpoint para upload de imagem
app.post('/upload', upload.single('image'), async (req, res): Promise<void> => {
    if (!req.file) {
        res.status(400).send('Nenhum arquivo enviado.');
        return;
    }

    try {
        // Salvar informações da imagem no banco de dados
        const imagem = await Imagem.create({
            filename: req.file.filename,
            path: req.file.path
        });

        res.send(`Arquivo enviado com sucesso: ${req.file.filename}`);
    } catch (error) {
        res.status(500).send('Erro ao salvar a imagem no banco de dados.');
    }
});

// Endpoint para obter todas as imagens salvas
app.get('/images', async (req, res): Promise<void> => {
    try {
        const imagens = await Imagem.findAll();
        res.json(imagens);
    } catch (error) {
        res.status(500).send('Erro ao buscar as imagens no banco de dados.');
    }
});

// Servir arquivos estáticos da pasta uploads
app.use('/uploads', express.static(path.join(__dirname, '../uploads')));

app.listen(port, () => {
  console.log(`Servidor rodando em http://localhost:${port}`);
});