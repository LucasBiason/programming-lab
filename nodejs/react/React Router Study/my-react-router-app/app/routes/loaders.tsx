import type { Route } from "./+types/loaders";
import { Link } from "react-router";

interface Brewery {
  id: string;
  name: string;
  brewery_type: string;
  address_1: string | null;
  address_2: string | null;
  address_3: string | null;
  city: string;
  state_province: string;
  postal_code: string;
  country: string;
  longitude: number | null;
  latitude: number | null;
  phone: string | null;
  website_url: string | null;
  state: string;
  street: string | null;
}

export async function loader() {
  const response = await fetch("https://api.openbrewerydb.org/v1/breweries");
  const breweries = (await response.json()) as Brewery[];
  return {
    message: "Hello from loader!",
    breweries
  };
}

export function meta({}: Route.MetaArgs) {
  return [
    { title: "Loaders - React Router App" },
    { name: "description", content: "Página de exemplo para demonstrar Loaders no React Router" },
  ];
}

export default function ({loaderData}: Route.ComponentProps) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 via-white to-emerald-50 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900">
      {/* Header Básico */}
      <header className="bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm border-b border-gray-200 dark:border-gray-700">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center space-x-3">
              <div className="w-8 h-8 bg-gradient-to-r from-green-600 to-emerald-600 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-sm">L</span>
              </div>
              <h1 className="text-xl font-bold text-gray-900 dark:text-white">Loaders</h1>
            </div>
            <nav className="flex space-x-4">
              <Link 
                to="/" 
                className="text-gray-700 dark:text-gray-300 hover:text-green-600 dark:hover:text-green-400 transition-colors"
              >
                ← Voltar para Home
              </Link>
            </nav>
          </div>
        </div>
      </header>

      {/* Conteúdo Principal */}
      <main className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="text-center mb-16">
          {/* Título Principal */}
          <h1 className="text-4xl md:text-6xl font-bold text-gray-900 dark:text-white mb-6">
            Página de{' '}
            <span className="bg-gradient-to-r from-green-600 to-emerald-600 bg-clip-text text-transparent">
              Loaders
            </span>
          </h1>
          
          {/* Descrição */}
          <p className="text-xl text-gray-600 dark:text-gray-400 max-w-3xl mx-auto mb-8 leading-relaxed">
            Esta página demonstra como funcionam os Loaders no React Router. 
            Os Loaders são funções que executam antes da renderização de uma rota.
            <br />
            <span className="text-green-600 font-semibold">{loaderData.message}</span>
          </p>

          {/* Lista de Cervejarias */}
          <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8 mb-8">
            <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
              Cervejarias Carregadas ({loaderData.breweries.length})
            </h2>
            <div className="max-h-96 overflow-y-auto">
              <div className="grid gap-4">
                {loaderData.breweries.slice(0, 10).map((brewery, index) => (
                  <div key={brewery.id} className="bg-gray-50 dark:bg-gray-700 rounded-lg p-4 text-left">
                    <h3 className="font-semibold text-gray-900 dark:text-white mb-2">
                      {brewery.name}
                    </h3>
                    <div className="grid grid-cols-2 gap-2 text-sm text-gray-600 dark:text-gray-400">
                      <div><span className="font-medium">Tipo:</span> {brewery.brewery_type}</div>
                      <div><span className="font-medium">Cidade:</span> {brewery.city}</div>
                      <div><span className="font-medium">Estado:</span> {brewery.state}</div>
                      <div><span className="font-medium">País:</span> {brewery.country}</div>
                    </div>
                  </div>
                ))}
              </div>
              {loaderData.breweries.length > 10 && (
                <p className="text-gray-500 text-sm mt-4">
                  ... e mais {loaderData.breweries.length - 10} cervejarias
                </p>
              )}
            </div>
          </div>
        </div>

        {/* Botões de Navegação */}
        <div className="text-center space-y-4">
          <Link 
            to="/" 
            className="inline-block bg-gray-600 hover:bg-gray-700 text-white font-medium py-3 px-8 rounded-lg transition-colors duration-200 text-lg shadow-lg hover:shadow-xl mr-4"
          >
            ← Voltar para Home
          </Link>
          
          <button 
            className="inline-block bg-green-600 hover:bg-green-700 text-white font-medium py-3 px-8 rounded-lg transition-colors duration-200 text-lg shadow-lg hover:shadow-xl"
            onClick={() => {
              console.log("Dados do loader:", loaderData);
              alert(`Dados carregados: ${loaderData.breweries.length} cervejarias! 🍺`);
            }}
          >
            Ver Dados no Console
          </button>
        </div>
      </main>
    </div>
  );
}