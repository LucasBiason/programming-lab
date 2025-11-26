import { Sequelize, DataTypes } from 'sequelize';

// Endpoint para upload de imagem
// Configuração do Sequelize
const sequelize = new Sequelize('postgres', 'postgres', 'postgres', {
    host: 'localhost',
    dialect: 'postgres',
    port: 5432
});


// Definição do modelo de Imagem
const Imagem = sequelize.define('Imagem', {
    filename: {
        type: DataTypes.STRING,
        allowNull: false
    },
    path: {
        type: DataTypes.STRING,
        allowNull: false
    }
});

// Sincronizar o modelo com o banco de dados
sequelize.sync();

export { sequelize, Imagem };