import type { Route } from "./+types/home";
import { Link } from "react-router";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "My First React Router App" },
    { name: "description", content: "Welcome to my first React Router App!" },
  ];
}

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-indigo-50 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900">
      {/* Header */}
      <header className="bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm border-b border-gray-200 dark:border-gray-700">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center space-x-3">
              <div className="w-8 h-8 bg-gradient-to-r from-blue-600 to-indigo-600 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-sm">R</span>
              </div>
              <h1 className="text-xl font-bold text-gray-900 dark:text-white">React Router App</h1>
            </div>
            <nav className="flex space-x-4">
              <Link 
                to="/login" 
                className="text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
              >
                Login
              </Link>
            </nav>
          </div>
        </div>
      </header>

      {/* Conteúdo Principal */}
      <main className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="text-center">
          {/* Título de Boas-vindas */}
          <h1 className="text-4xl md:text-6xl font-bold text-gray-900 dark:text-white mb-6">
            Bem-vindo ao{' '}
            <span className="bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
              React Router
            </span>
          </h1>
          
          {/* Texto de Boas-vindas */}
          <p className="text-xl text-gray-600 dark:text-gray-400 max-w-2xl mx-auto mb-12 leading-relaxed">
            Esta é uma aplicação de exemplo criada para demonstrar as funcionalidades do React Router. 
            Aqui você pode explorar diferentes conceitos como roteamento, loaders e muito mais.
          </p>
          
          {/* Botões de Navegação */}
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link 
              to="/loaders" 
              className="inline-block bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 px-8 rounded-lg transition-colors duration-200 text-lg shadow-lg hover:shadow-xl"
            >
              Ir para Loaders
            </Link>
            
            <Link 
              to="/login" 
              className="inline-block bg-purple-600 hover:bg-purple-700 text-white font-medium py-3 px-8 rounded-lg transition-colors duration-200 text-lg shadow-lg hover:shadow-xl"
            >
              Fazer Login
            </Link>
          </div>
        </div>
      </main>
    </div>
  );
}
